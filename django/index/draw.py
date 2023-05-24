from .img_generate import img_gen
from .get_result import get_res
from .super_res import super_res

from urllib.request import urlretrieve

import cv2
import json
import time


# 找最接近的预设尺寸
def find_best_size(page_size):
    draw_size = [(1280, 720), (1024, 768), (1024, 1024), (768, 1024), (720, 1280)]
    page_scale = page_size[0] / page_size[1]
    draw_scale = []
    for s in draw_size:
        draw_scale.append(s[0] / s[1])
    scale = []
    for s in draw_scale:
        scale.append(abs(page_scale - s))
    best_size = draw_size[scale.index(min(scale))]
    return f"{best_size[0]}*{best_size[1]}"


# 轮询获取图片url
def polling_get_res(id, task):
    while True:
        status_res, response_res = get_res(id)
        if status_res == 200:
            if response_res.data.status != "PROCESSING":
                break
            else:
                time.sleep(1)
        else:
            print("Error code:", status_res)
            break
    if task == "gen":
        url = json.loads(response_res.data.result)["imageUrls"][0]
    elif task == "sup":
        url = json.loads(response_res.data.result)["resultUrl"]
    return url


def high_res(url_init):
    status_sup, response_sup = super_res(url_init, 2)
    if status_sup == 200:
        id = response_sup.request_id
        print("processing...")
        url_sup = polling_get_res(id, "sup")
        return url_sup
    else:
        print("Error code:", status_sup)
        return url_init


def ai_draw(prompt, page_size, need_highres=False):
    # 获取当前日期和时间
    now = time.strftime("%Y%m%d%H%M", time.localtime())
    # 找最接近的预设尺寸
    size = find_best_size(page_size)
    # 设置图片保存路径
    bg_origin_path = 'media/bg_' + now + '_origin.png'
    bg_resize_path = 'media/bg_' + now + '_resize.png'
    # 调用img_gen函数生成图片
    status_gen, response_gen = img_gen(prompt, size, 1)
    if status_gen == 200:
        id = response_gen.request_id
        print("generating...")
        url_init = polling_get_res(id, "gen")
        if need_highres == True:
            url_download = high_res(url_init)
        else:
            url_download = url_init
        urlretrieve(url_download, bg_origin_path)
        bg_origin = cv2.imread(bg_origin_path)
        bg_resize = cv2.resize(bg_origin, page_size)
        cv2.imwrite(bg_resize_path, bg_resize)
        return bg_resize_path
    else:
        print("Error code:", status_gen)
        return "Error"

# 【调试使用】从控制台输入参数
# prompt = input("请输入prompt：")
# prompt += ", wallpaper, masterpiece, 8k, best quality, highres, ultra detailed"
# page_size = (1920, 1080)
# ai_draw(prompt, page_size, False)

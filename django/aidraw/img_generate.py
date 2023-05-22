# pip install alibabacloud_imageenhan20190930

from alibabacloud_imageenhan20190930.client import Client
from alibabacloud_imageenhan20190930.models import GenerateImageWithTextRequest
from alibabacloud_tea_openapi.models import Config
from alibabacloud_tea_util.models import RuntimeOptions

config = Config(
    access_key_id='LTAI5tMoHxHFbaagPdg3EHKH',
    access_key_secret='zptiQ4FB2rsOwqNyxWkr5tEFT6Bj2W',
    endpoint='imageenhan.cn-shanghai.aliyuncs.com',
    region_id='cn-shanghai'
)

def img_gen(prompt, size, num):
    generate_image_with_text_request = GenerateImageWithTextRequest(
            text=prompt,
            resolution=size,
            number=num
    )
    runtime = RuntimeOptions()
    try:
        client = Client(config)
        response = client.generate_image_with_text_with_options(
                generate_image_with_text_request, runtime)
        return response.status_code, response.body
    except Exception as error:
        return error.code, error.message

from django.http import JsonResponse
from aidraw import ai_draw
import os
import base64

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
}

def aidraw_view(request):
    prompt = request.GET.get('prompt')
    page_size = request.GET.get('page_size')
    need_highres = request.GET.get('need_highres')
    bg_path = ai_draw(prompt, page_size, need_highres)
    result = {'bg': ''}
    if os.path.exists(bg_path):
        with open(bg_path, 'rb') as f:
            data = f.read()
            result['bg'] = bytes.decode(base64.b64encode(data))
    return JsonResponse(result)

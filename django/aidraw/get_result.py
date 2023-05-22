# pip install alibabacloud_viapi20230117

from alibabacloud_tea_openapi.models import Config
from alibabacloud_tea_util.models import RuntimeOptions
from alibabacloud_viapi20230117.client import Client
from alibabacloud_viapi20230117.models import GetAsyncJobResultRequest

config = Config(
    access_key_id='LTAI5tMoHxHFbaagPdg3EHKH',
    access_key_secret='zptiQ4FB2rsOwqNyxWkr5tEFT6Bj2W',
    endpoint='viapi.cn-shanghai.aliyuncs.com',
    region_id='cn-shanghai'
)

def get_res(id):
    get_async_job_result_request = GetAsyncJobResultRequest(
            job_id=id
    )
    runtime = RuntimeOptions()
    try:
        client = Client(config)
        response = client.get_async_job_result_with_options(
                get_async_job_result_request, runtime)
        return response.status_code, response.body
    except Exception as error:
        return error.code, error.message

from django.http import HttpResponseRedirect
from sjtuers.oauth import jaccount
from sjtuers.settings import JACCOUNT_CLIENT_ID
from django.shortcuts import redirect
from authlib.jose import jwt
from authlib.oidc.core import CodeIDToken
from urllib.parse import urlencode


def index_view(request):
    return HttpResponseRedirect('/index/')


def login(request):
    redirect_uri = request.build_absolute_uri('/authorize')
    return jaccount.authorize_redirect(request, redirect_uri)


def authorize(request):
    token: dict = jaccount.authorize_access_token(request)
    claims = jwt.decode(token.pop('id_token'),
                        jaccount.client_secret, claims_cls=CodeIDToken)
    claims.validate()
    request.session['token'] = token
    request.session['user'] = claims
    redir_uri = request.build_absolute_uri('/index')
    return redirect(redir_uri)


def logout(request):
    response = HttpResponseRedirect(
        'https://jaccount.sjtu.edu.cn/oauth2/logout?' +
        urlencode({
            'client_id': JACCOUNT_CLIENT_ID,
            'post_logout_redirect_uri': request.build_absolute_uri('/logged_out'),
            # 'state': '' # jAccount后台对该参数的处理疑似存在 bug，会在 state 前错误添加 ? 和 &，遂弃用
        })
    )
    response.delete_cookie('sessionid')  # 指示客户端清除 cookie 会话
    return response


def logged_out(request):
    redir_uri = request.build_absolute_uri('/index')
    return HttpResponseRedirect(redir_uri)

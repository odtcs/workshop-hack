from django.contrib.auth.views import redirect_to_login
from django.urls import resolve

from hackut import settings
from main.models import Session


class AuthenticationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        res = resolve(request.path)
        if not res.url_name == 'check':
            urlname = '%s:%s' % (res.namespace, res.url_name)
            session = Session.objects.filter(pk=request.session.get('sid'))
            if not session.exists() and res.app_name not in settings.EXTERNAL_APPS and urlname not in settings.AUTHENTICATION_BLACKLIST:
                if 'sid' in request.session:
                    request.session.pop('sid')
                return redirect_to_login(request.get_full_path(), settings.LOGIN_URL)
            else:
                request.s = None
                if session.exists():
                    request.s = session.first()
                    request.challenges = settings.CHALLENGES
                    total = 0
                    finished = 0
                    for challenge in request.challenges:
                        c = request.s.has_completed(challenge['id'])
                        challenge['completed'] = c
                        if c:
                            finished = finished + 1
                        total = total + 1
                        request.finished = finished
                        request.total = total
        response = self.get_response(request)
        return response
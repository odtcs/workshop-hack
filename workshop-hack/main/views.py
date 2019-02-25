from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, RedirectView
from django.urls import reverse_lazy

from .models import *


class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        session = Session.objects.filter(pk=request.session.get('sid'))
        if session.exists():
            return HttpResponseRedirect(reverse('home'))
        return super(LoginView, self).get(request)

    def post(self, request, *args, **kwargs):
        session = Session()
        session.save()
        request.session['sid'] = session.pk
        return HttpResponseRedirect(reverse('home'))


class LogoutView(RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        session = Session.objects.filter(pk=request.session.get('sid'))
        if session.exists():
            session.first().delete()
        del request.session['sid']
        return super(LogoutView, self).get(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = 'home.html'


class CheckView(View):
    def get(self, request, **kwargs):
        return JsonResponse({
            'status': Session.objects.filter(pk=request.session.get('sid')).exists()
        })
from django.shortcuts import redirect

from hackut import settings
from django.views.generic import TemplateView


def get_challenge_by_id(id):
    for i in settings.CHALLENGES:
        if i['id'] == id:
            return i
    return None


class Challenge01View(TemplateView):
    template_name = 'challenges/01.html'
    challenge = get_challenge_by_id(1)

    def get_context_data(self, **kwargs):
        context = super(Challenge01View, self).get_context_data(**kwargs)
        context['currentchallenge'] = self.challenge
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('code') == 'easypeasy':
            request.s.complete(request, self.challenge)
            return redirect('1')
        return super(Challenge01View, self).get(request, *args, **kwargs)


class Challenge02View(TemplateView):
    template_name = 'challenges/02.html'
    challenge = get_challenge_by_id(2)

    def get_context_data(self, **kwargs):
        context = super(Challenge02View, self).get_context_data(**kwargs)
        context['currentchallenge'] = self.challenge
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('code') == 'lemonsqueezy':
            request.s.complete(request, self.challenge)
            return redirect('2')
        return super(Challenge02View, self).get(request, *args, **kwargs)


class Challenge03View(TemplateView):
    template_name = 'challenges/03.html'
    challenge = get_challenge_by_id(3)

    def get_context_data(self, **kwargs):
        context = super(Challenge03View, self).get_context_data(**kwargs)
        context['currentchallenge'] = self.challenge
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('code') == 'var x = \'x\';':
            request.s.complete(request, self.challenge)
            return redirect('3')
        return super(Challenge03View, self).get(request, *args, **kwargs)


class Challenge04View(TemplateView):
    template_name = 'challenges/04.html'
    challenge = get_challenge_by_id(4)

    def get_context_data(self, **kwargs):
        context = super(Challenge04View, self).get_context_data(**kwargs)
        context['currentchallenge'] = self.challenge
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('code') == 'yougotit':
            request.s.complete(request, self.challenge)
            return redirect('4')
        return super(Challenge04View, self).get(request, *args, **kwargs)


class Challenge05View(TemplateView):
    template_name = 'challenges/05.html'
    challenge = get_challenge_by_id(5)
    decoded = None

    def get_context_data(self, **kwargs):
        context = super(Challenge05View, self).get_context_data(**kwargs)
        context['currentchallenge'] = self.challenge
        context['decoded'] = self.decoded
        return context

    def post(self, request, *args, **kwargs):
        if 'decipher' in request.POST:
            encoded = request.POST.get('decipher')
            decoded = ""
            for encodedLetter in encoded:
                encodedNumber = ord(encodedLetter) - 33
                decodedLetter = chr(((encodedNumber - 7) % (122- 33)) + 33)
                decoded = decoded + decodedLetter
            self.decoded = decoded
        elif 'code' in request.POST:
            if request.POST.get('code') == 'KnifeInTheBack':
                request.s.complete(request, self.challenge)
                return redirect('5')
        return super(Challenge05View, self).get(request, *args, **kwargs)

class Challenge06View(TemplateView):
    template_name = 'challenges/06.html'
    challenge = get_challenge_by_id(6)
    decoded = None

    def get_context_data(self, **kwargs):
        context = super(Challenge06View, self).get_context_data(**kwargs)
        context['currentchallenge'] = self.challenge
        context['decoded'] = self.decoded
        return context

    def post(self, request, *args, **kwargs):
        if 'decipher' in request.POST:
            encoded = request.POST.get('decipher')
            decoded = ""
            key = "UTTCS"
            keyindex = 0
            for encodedLetter in encoded:
                if (ord(encodedLetter.upper()) > 64) and (ord(encodedLetter.upper()) < 91):
                    encodedNumber = ord(encodedLetter.upper()) - 65
                    decodedLetter = chr(((encodedNumber + ord(key[keyindex]) - 65) % 26) + 65)
                    if encodedLetter.islower():
                        decoded = decoded + decodedLetter.lower()
                    else:
                        decoded = decoded + decodedLetter
                    keyindex += 1
                    if keyindex == len(key):
                        keyindex = 0
                else:
                    decoded = decoded + encodedLetter
            self.decoded = decoded
        elif 'code' in request.POST:
            if request.POST.get('code') == 'B4guette_Au-Fr0mage!':
                request.s.complete(request, self.challenge)
                return redirect('6')
        return super(Challenge06View, self).get(request, *args, **kwargs)

class Challenge07View(TemplateView):
    template_name = 'challenges/07.html'
    challenge = get_challenge_by_id(7)

    def get_context_data(self, **kwargs):
        context = super(Challenge07View, self).get_context_data(**kwargs)
        context['currentchallenge'] = self.challenge
        return context

    def post(self, request, *args, **kwargs):
        if request.COOKIES.get('level_completed') == 'true':
            request.s.complete(request, self.challenge)
            return redirect('7')
        return super(Challenge07View, self).get(request, *args, **kwargs)
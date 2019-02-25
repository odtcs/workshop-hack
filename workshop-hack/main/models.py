from django.db import models
from django.contrib import messages
from hackut.settings import CHALLENGES


class ChallengeCompleted(models.Model):
    challenge_id = models.IntegerField(unique=True)

    def __str__(self):
        return "Completed {}".format(self.challenge_id)


class Session(models.Model):
    completed = models.ManyToManyField(ChallengeCompleted)

    def complete(self, request, challenge):
        if not self.has_completed(challenge['id']):
            if not ChallengeCompleted.objects.filter(challenge_id=challenge['id']).exists():
                cp = ChallengeCompleted(challenge_id=challenge['id'])
                cp.save()
            else:
                cp = ChallengeCompleted.objects.get(challenge_id=challenge['id'])
            self.completed.add(cp)
            self.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Great! You finished {} challenge {}: {}'.format(challenge['category'],
                                                                                  challenge['id'], challenge['name']))
        else:
            messages.add_message(request, messages.SUCCESS,
                                 'You already finished finished {} challenge {}: {}'.format(challenge['category'],
                                                                                  challenge['id'], challenge['name']))

    def has_completed(self, id):
        for cp in self.completed.all():
            if cp.challenge_id == id:
                return True
        return False

    def __str__(self):
        total = 0
        finished = 0
        for challenge in CHALLENGES:
            c = self.has_completed(challenge['id'])
            challenge['completed'] = c
            if c:
                finished = finished + 1
            total = total + 1
        return "Session with {}/{} challenges completed.".format(finished, total)

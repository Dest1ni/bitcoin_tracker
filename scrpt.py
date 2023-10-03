import requests
import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'bitcoin_tracker.settings'
django.setup()
from graph.models import X,Y

answer = requests.get('https://blockchain.info/ticker')

if answer.status_code == 200:
    answer = answer.json()
    x = X(x=answer["USD"]["last"])
    x.save()
    y = Y(y=X.objects.count())
    y.save()
    clear_x = X.objects.first()
    clear_x.delete()

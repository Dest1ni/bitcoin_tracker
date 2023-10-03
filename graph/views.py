from django.views.generic import TemplateView
import matplotlib.pyplot as plt
from .models import *
import requests

class Graph(TemplateView):
    template_name = 'graph/graph.html'

    def get_context_data(self, **kwargs):
        response = requests.get('https://blockchain.info/ticker')
        context  = super().get_context_data(**kwargs)
        if response.status_code == 200:
            response = response.json()
            plt.switch_backend('agg')
            x = [x.x for x in X.objects.all()]
            y = [y for y in range(1,25)]
            print(x,y)
            plt.clf()
            plt.plot(y,x)
            plt.savefig('static/graphic.png', format='png',dpi=115)
            response['rate'] = round(response['RUB']['last']/response['USD']['last'],2)
            context['response'] = response
        return context



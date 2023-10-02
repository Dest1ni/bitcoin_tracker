from typing import Any
from django.views.generic import TemplateView
import matplotlib.pyplot as plt
from .models import *

class Graph(TemplateView):
    template_name = 'graph/graph.html'

    def get_context_data(self, **kwargs):
        context  = super().get_context_data(**kwargs)
        plt.switch_backend('agg')
        x = [x.x for x in X.objects.all()]
        y = [y.y for y in Y.objects.all()]
        print(x,y)
        plt.plot(y,x)
        plt.savefig('static/graphic.png', format='png',dpi=115)


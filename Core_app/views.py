from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

class HomeTemplateView(View):
  def get(self, *args, **kwargs):
    template_name = 'Core_app/index.html'
    context:dict = dict()
    return render(self.request,template_name=template_name,context=context)
  
class ListarPessoasView(View):
  def get(self, request, *args):
    template_name = 'Core_app'

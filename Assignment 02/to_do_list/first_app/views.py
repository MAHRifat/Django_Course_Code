from django.shortcuts import render,redirect
from first_app.forms import To_Do_Form
from first_app.models import TO_Do_Model
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.views.generic import TemplateView,ListView,DetailView
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, 'home.html')

class Store_info(CreateView):
    model = TO_Do_Model
    template_name = 'store_info.html'
    form_class = To_Do_Form
    success_url = reverse_lazy('show_page')

class show_info(ListView):
    model = TO_Do_Model
    template_name = 'show_info.html'
    context_object_name = 'info'

class InfoUpdate(UpdateView):
    model = TO_Do_Model
    template_name = 'store_info.html'
    form_class = To_Do_Form
    success_url = reverse_lazy('show_page')

class DeleteInfo(DeleteView):
    model = TO_Do_Model
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('show_page')

class Complete(DeleteView):
    model = TO_Do_Model
    template_name = 'complete_confirmation.html'
    success_url = reverse_lazy('show_page')
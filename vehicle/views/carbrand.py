from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from vehicle.models import CarBrand
from vehicle.forms.carbrand import CarBrandForm

# Create your views here.
class CarBrandlist(ListView):    
    model = CarBrand
    paginate_by = 2

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CarBrandlist, self).dispatch(*args, **kwargs)

class CarBrandCreate(SuccessMessageMixin, CreateView):
    model = CarBrand
    form_class = CarBrandForm
    success_url = reverse_lazy('vehicle:carbrand_list')
    success_message = "%(code)s was created successfully"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CarBrandCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        return super().form_valid(form)


class CarBrandDelete(DeleteView):
    model = CarBrand
    success_url = reverse_lazy('vehicle:carbrand_list')
    success_message = "%(code)s was deleted"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CarBrandDelete, self).dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(CarBrandDelete, self).delete(request, *args, **kwargs)

class CarBrandUpdate(SuccessMessageMixin, UpdateView):
    model = CarBrand
    form_class = CarBrandForm
    success_url = reverse_lazy('vehicle:carbrand_list')
    success_message = "%(code)s was updated successfully"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CarBrandUpdate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.updated_by = self.request.user
        obj.save()
        return super().form_valid(form)

class CarBrandDetail(DetailView):
    model = CarBrand

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CarBrandDetail, self).dispatch(*args, **kwargs)








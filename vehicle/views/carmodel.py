from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from vehicle.models import CarModel
from vehicle.forms.carmodel import CarModelForm


class CarModellist(ListView):    
    model = CarModel
    paginate_by = 2

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CarModellist, self).dispatch(*args, **kwargs)

class CarModelCreate(SuccessMessageMixin, CreateView):
    model = CarModel
    form_class = CarModelForm
    success_url = reverse_lazy('vehicle:carmodel_list')
    success_message = "%(code)s was created successfully"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CarModelCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        return super().form_valid(form)

class CarModelDelete(DeleteView):
    model = CarModel
    success_url = reverse_lazy('vehicle:carmodel_list')
    success_message = "%(code)s was deleted"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CarModelDelete, self).dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(CarModelDelete, self).delete(request, *args, **kwargs)

class CarModelUpdate(SuccessMessageMixin, UpdateView):
    model = CarModel
    form_class = CarModelForm
    success_url = reverse_lazy('vehicle:carmodel_list')
    success_message = "%(code)s was updated successfully"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CarModelUpdate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.updated_by = self.request.user
        obj.save()
        return super().form_valid(form)

class CarModelDetail(DetailView):
    model = CarModel

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CarModelDetail, self).dispatch(*args, **kwargs)
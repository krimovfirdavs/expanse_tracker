import django.views.generic as cbv
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

import src.core.models as models
import src.template_views.forms as forms


class BaseQuerysetMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(added_by=self.request.user)


class BaseListView(LoginRequiredMixin, BaseQuerysetMixin, cbv.ListView):
    ...


class BaseCreateView(LoginRequiredMixin, SuccessMessageMixin, cbv.CreateView):
    template_name = "form.html"
    success_message = "Muaffaqiyatli qo'shildi :)!"

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)


class BaseUpdateView(LoginRequiredMixin, SuccessMessageMixin, cbv.UpdateView):
    template_name = "form.html"
    success_message = "Muaffaqiyatli yangilandi :)!"


class BaseDeleteView(LoginRequiredMixin, cbv.View):
    model = None
    fields = None
    success_url = None

    def get(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        obj.delete()
        messages.info(request, f"'{obj}' o'chirildi!")
        return redirect(self.success_url)

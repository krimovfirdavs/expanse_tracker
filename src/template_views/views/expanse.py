from src.bases.base_view import *


class ExpanseSuperView:
    model = models.Expanse


class ExpanseBaseView(ExpanseSuperView):
    success_url = "/expanse/list"
    fields = ("amount", "category", "note")


class ExpanseListView(ExpanseSuperView, BaseListView):
    template_name = "expanse/list.html"


class ExpanseCreateView(ExpanseBaseView, BaseCreateView):
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["category"].queryset = models.Category.objects.filter(
            added_by=self.request.user)
        return form


class ExpanseUpdateView(ExpanseBaseView, BaseUpdateView):
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["category"].queryset = models.Category.objects.filter(
            added_by=self.request.user)
        return form


class ExpanseDeleteView(ExpanseBaseView, BaseDeleteView):
    ...

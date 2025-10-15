from src.bases.base_view import *


class IncomeSuperView:
    model = models.Income


class IncomeBaseView(IncomeSuperView):
    success_url = "/income/list"
    fields = ("amount", "type", "note")


class IncomeListView(IncomeSuperView, BaseListView):
    template_name = "income/list.html"


class IncomeCreateView(IncomeBaseView, BaseCreateView):
    ...


class IncomeUpdateView(IncomeBaseView, BaseUpdateView):
    ...


class IncomeDeleteView(IncomeBaseView, BaseDeleteView):
    ...

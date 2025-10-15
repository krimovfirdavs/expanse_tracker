from datetime import timedelta

from django.db.models import Sum
from django.utils import timezone
from django.views.generic import TemplateView
from django.db.models.functions import ExtractMonth
from django.contrib.auth.mixins import LoginRequiredMixin

import src.core.models as models


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data(**kwargs)
        user = self.request.user
        today = timezone.now().date()  # 2025-10-3
        start_week = today - timedelta(days=today.weekday())

        context["this_year_expanse"] = models.Expanse.objects.filter(
            added_at__date__year=today.year, added_by=user
        ).aggregate(
            total=Sum("amount"))["total"] or 0

        context["this_month_expanse"] = models.Expanse.objects.filter(
            added_at__date__year=today.year,
            added_at__date__month=today.month,
            added_by=user
        ).aggregate(
            total=Sum("amount"))["total"] or 0

        context["this_day_expanse"] = models.Expanse.objects.filter(
            added_at__date=today,  # 2025-10-06
            added_by=user
        ).aggregate(
            total=Sum("amount"))["total"] or 0

        context["this_week_expanse"] = models.Expanse.objects.filter(
            added_at__date__gte=start_week,
            added_by=user
        ).aggregate(
            total=Sum("amount"))["total"] or 0

        # Income

        context["this_month_income"] = models.Income.objects.filter(
            added_by=user,
            added_at__date__year=today.year,
            added_at__date__month=today.month
        ).aggregate(total=Sum("amount"))["total"] or 0

        context["this_year_income"] = models.Income.objects.filter(
            added_by=user,
            added_at__date__year=today.year
        ).aggregate(total=Sum("amount"))["total"] or 0

        context["top_income_type"] = models.Income.objects.filter(
            added_by=user, added_at__date__month=today.month
        ).values("type").annotate(total=Sum("amount")).order_by("-total").first()

        context["balance"] = context["this_month_income"] - context["this_month_expanse"]

        category_pie = models.Expanse.objects.filter(
            added_by=user, added_at__date__month=today.month
        ).values("category__name").annotate(total=Sum("amount")).order_by("-total")

        expanse_bar_chart = (models.Expanse.objects
                             .filter(added_by=user, added_at__date__year=today.year)
                             .annotate(month=ExtractMonth("added_at"))
                             .values("month")
                             .annotate(total=Sum("amount"))
                             .order_by("month"))

        context["category_pie_labels"] = [i.get("category__name") for i in category_pie]
        context["category_pie_totals"] = [i.get("total") for i in category_pie]

        context["expanse_bar_labels"] = [i.get("month") for i in expanse_bar_chart]
        context["expanse_bar_totals"] = [i.get("total") for i in expanse_bar_chart]

        try:
            context["object_list"] = models.Expanse.objects.filter(
                added_by=user, added_at__date__month=today.month
            ).order_by("-amount")[:10]
        except IndexError:
            context["object_list"] = models.Expanse.objects.filter(
                added_by=user, added_at__date__month=today.month
            ).order_by("-amount")

        return context

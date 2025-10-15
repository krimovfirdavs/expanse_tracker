from django.contrib import admin

import src.core.models as models


# Register your models here.

@admin.register(models.Income)
class IncomeAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Expanse)
class ExpanseAdmin(admin.ModelAdmin):
    ...

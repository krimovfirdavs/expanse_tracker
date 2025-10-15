from src.bases.base_view import *


class CategorySuperView:
    model = models.Category


class CategoryBaseView(CategorySuperView):
    fields = ("name",)
    success_url = "/category/list"


class CategoryListView(CategorySuperView, BaseListView):
    template_name = "category/list.html"


class CategoryCreateView(CategoryBaseView, BaseCreateView):
    ...


class CategoryUpdateView(CategoryBaseView, BaseUpdateView):
    ...


class CategoryDeleteView(CategoryBaseView, BaseDeleteView):
    ...

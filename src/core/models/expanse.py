from src.bases.base_model import *


class Expanse(BaseModel):
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL,
        null=True, blank=True, related_name="expanses"
    )
    amount = models.BigIntegerField()
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.amount} {self.category.name} {self.added_at.strftime('%Y-%m-%d')}"

    class Meta:
        ordering = ("-id",)

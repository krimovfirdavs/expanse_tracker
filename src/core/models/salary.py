from src.bases.base_model import *

INCOME_TYPE = (
    ("salary", "Oylik maosh"),
    ("extra_income", "Qo'shimcha daromad"),
    ("other", "Boshqa"),
)


class Income(BaseModel):
    amount = models.BigIntegerField()
    type = models.CharField(max_length=50, choices=INCOME_TYPE)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.amount} - {self.added_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ("-added_at",)

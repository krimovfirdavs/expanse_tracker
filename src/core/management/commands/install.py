from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

import json
import src.core.models as models


class Command(BaseCommand):
    resource = "src/core/management/resource"

    def handle(self, *args, **options):
        user_object = User.objects

        if not user_object.filter(username="admin").exists():
            user = user_object.create_superuser(username="admin", password="123")
            self.stdout.write(self.style.SUCCESS("✅ Admin user qo'shildi!"))
        else:
            user = user_object.get(username="admin")
            self.stdout.write(self.style.WARNING("⚠️ Admin user allaqachon mavjud"))

        with open(f"{self.resource}/category.json", "r", encoding="utf8") as file:
            data: list[dict] = json.load(file)
            for i in data:
                fields: dict = i.get("fields")
                if not models.Category.objects.filter(name=fields.get("name")).exists():
                    models.Category.objects.create(
                        added_by=user,
                        name=fields.get("name"),
                        added_at=fields.get("added_at"),
                        updated_at=fields.get("updated_at"),
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f"✅ {fields.get('name')} categoryasi qo'shildi")
                    )
                else:
                    self.stdout.write(self.style.WARNING(
                        f"⚠️ {fields.get('name')} allaqachon mavjud")
                    )

        with open(f"{self.resource}/income.json", "r", encoding="utf8") as file:
            data: list[dict] = json.load(file)
            for i in data:
                fields: dict = i.get("fields")
                amount = fields.get("amount")
                if not models.Income.objects.filter(amount=amount).exists():
                    models.Income.objects.create(
                        added_by=user,
                        amount=amount,
                        type=fields.get('type'),
                        note=fields.get('note'),
                        added_at=fields.get("added_at"),
                        updated_at=fields.get("updated_at"),
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f"✅ {amount} so'mlik income qo'shildi")
                    )
                else:
                    self.stdout.write(self.style.WARNING(
                        f"⚠️ {amount} so'mlik income allaqachon mavjud")
                    )

        with open(f"{self.resource}/expanse.json", "r", encoding="utf8") as file:
            data: list[dict] = json.load(file)
            for i in data:
                pk = i.get("pk")
                fields: dict = i.get("fields")
                amount = fields.get("amount")
                if not models.Expanse.objects.filter(pk=pk).exists():
                    models.Expanse.objects.create(
                        added_by=user,
                        amount=amount,
                        note=fields.get('note'),
                        added_at=fields.get("added_at"),
                        category_id=fields.get('category'),
                        updated_at=fields.get("updated_at"),
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f"✅ {amount} so'mlik expanse qo'shildi")
                    )
                else:
                    self.stdout.write(self.style.WARNING(
                        f"⚠️ {amount} so'mlik expanse allaqachon mavjud")
                    )

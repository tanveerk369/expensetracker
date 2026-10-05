from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ("Food", "Food"),
        ("Transport", "Transport"),
        ("Shopping", "Shopping"),
        ("Bills", "Bills"),
        ("Entertainment", "Entertainment"),
        ("Other", "Other"),
    ]

    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

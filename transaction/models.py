from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User 모델과 연결
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=0)
    date = models.DateField()
    memo = models.TextField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.title} - {self.amount}"
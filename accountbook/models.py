from django.db import models

class Record(models.Model):
    TYPE_CHOICES = (
        ('income', '수입'),
        ('expense', '지출'),
    )

    CATEGORY_CHOICES = (
        ('식비', '식비'),
        ('교통', '교통'),
        ('쇼핑', '쇼핑'),
        ('생활', '생활'),
        ('월급', '월급'),
        ('기타', '기타'),
    )

    title = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    record_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.amount}원"
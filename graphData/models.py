from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    title = models.CharField('カテゴリ', max_length=20)

    def __str__(self):
        return self.title


class GraphData(models.Model):
    title = models.CharField('タイトル', max_length=50, help_text='勉強タイトル')
    studyDay = models.DateField('勉強日', help_text='勉強日')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, help_text='学習した勉強のカテゴリ')
    details = models.CharField(
        '詳細', max_length=400, help_text='勉強の詳細')
    studyTime = models.FloatField('学習時間', help_text='学習時間', validators=[
                                  MinValueValidator(0.0, '時間を入力してください！'),
                                  MaxValueValidator(24.0, '24時間以内で記入してください！')])
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

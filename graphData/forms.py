from django.forms import ModelForm
from django import forms
from .models import Category, GraphData


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']


class GraphDataForm(ModelForm):
    class Meta:
        model = GraphData
        fields = ['title', 'studyDay', 'category', 'details', 'studyTime']
        widgets = {  # プルダウン選択
            'studyDay': forms.SelectDateWidget
        }

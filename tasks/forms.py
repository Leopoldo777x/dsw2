from django import forms

from .models import Task


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description')

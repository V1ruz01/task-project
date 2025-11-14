from django import forms
from .models import TaskStatus, CommentModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskStatus
        fields = ('title', 'desc', 'status')

# add an ability to add images to the tasks

class FiltrationForm(forms.Form):
    status_filtr = forms.ChoiceField(
        choices=[('', 'All')] + list(TaskStatus.Status.choices),
        required=False,
        label='Status'
    )

    def __init__(self, *args, **kwargs): #hmmmmmm
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['content', 'media_content']
        widget = {
            'media': forms.FileInput()
        }
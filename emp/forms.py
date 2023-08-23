from django.forms import ModelForm
from .models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model=Feedback
        fields=['name','email','feedback']
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
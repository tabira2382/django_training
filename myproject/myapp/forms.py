from django import forms

from .models import Post_comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Post_comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'textarea'})
        }
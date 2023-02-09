from django import forms
from notice.models import Notice


class NoticeForm(forms.ModelForm):
    title = forms.CharField(label='標題', max_length=128)
    content = forms.CharField(label='內容', widget=forms.Textarea)
    
    class Meta:
        model = Notice
        fields = ['title', 'content']
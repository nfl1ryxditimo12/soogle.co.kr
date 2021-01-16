from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해 주세요.'
        },
        max_length=64, label='title'
    )

    contents = forms.CharField(
        error_messages={
            'requires': '내용을 입력해 주세요.'
        },
        label='contents'
    )

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        contents = cleaned_data.get('contents')


        if title and contents:

            reg = Post(
                title=title,
                contents=contents
            )
            reg.save()

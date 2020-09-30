from .models import *
from django import forms
from tinymce.widgets import TinyMCE
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from captcha.fields import ReCaptchaField

class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows':50,'class': 'form-control'}))

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Post Title'}),
            # 'content':forms.TextField(attrs={'class':'form-control', 'placeholder':'Post Content'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            # 'tag':forms.TextInput(attrs={'class':'form-control', 'placeholder':'#post_tags'}),
        }
        fields = [
            'title',
            'category',
            'content',
            'image',
        ]


class PostUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.field_class = 'mt-10'
        self.helper.layout = Layout(
            Field('title', css_class='single-input', placeholder='Title'),
            Field('category', css_class='single-input'),
            Field('content', css_class='single-input', placeholder='Whats\'s on your mind?'),
            Field('image', css_class='file'),
            Field('tag', css_class='single-input', placeholder='Post Tags. Seperate with a comma ","', value=self.instance.post_tag()),

        )
        self.helper.add_input(Submit('submit', 'Update', css_class='btn btn-outline-success'))

    tag = forms.CharField()

    class Meta:
        model = Post
        fields = [
            'title',
            'category',
            'content',
            'image',
        ]


class CreateCommentForm(forms.ModelForm):

    captcha = ReCaptchaField()
    def __init__(self, *args, **kwargs):
        super(CreateCommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('name', css_class='form-control'),
            Field('content', css_class='form-control mb-10'),
            Field('captcha'),

        )

        self.helper.add_input(Submit('submit', 'Post Comment', css_class="btn btn-primary"))

    class Meta:
        model = Comment
        fields = [
            'name',
            'content',

        ]

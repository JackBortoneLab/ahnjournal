from django import forms
from django.forms import widgets
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from comms import models

class CommentForm(forms.ModelForm):
    #author = forms.CharField(required=False)
    body = SummernoteTextField()

    class Meta:
        model = models.Comment
        exclude = ('date_time', 'views', 'news_item')
        widgets = {
            'body': SummernoteWidget()
        }


class NewsItemForm(forms.ModelForm):
    body = SummernoteTextField()

    image_file = forms.FileField(required=False)
    tags = forms.CharField(required=False)


    def save(self, commit=True):
        news_item = super(NewsItemForm, self).save()
        posted_tags = self.cleaned_data['tags'].split(',')
        news_item.set_tags(posted_tags=posted_tags)
        news_item.save()

        return news_item

    class Meta:
        model = models.NewsItem
        exclude = ('content_type', 'object_id', 'posted', 'posted_by', 'large_image_file', 'tags')

        widgets = {
          'body': SummernoteWidget(),
        }

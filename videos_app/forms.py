from dataclasses import fields
from fileinput import FileInput
from django_countries.fields import CountryField
from django.forms import ModelForm
from django import forms
from .models import Category, Country, Fixture, LiveVideo, Player, Video, Review, News, Standing, LiveComments


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video', 'category', 'country']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'description-input'}),
            # 'video': forms.FileInput(attrs={'class': 'file-input'}),
            'Category': forms.SelectMultiple(attrs={'class': 'tag-input'}),
        }
        # fields = '__all__'


class LiveVideoForm(ModelForm):
    class Meta:
        model = LiveVideo
        fields = ['title', 'description', 'url',
                  'category', 'country', 'venue']
        widgets = {
            'url': forms.Textarea(attrs={'class': 'description-input'}),
            'description': forms.Textarea(attrs={'class': 'description-input'}),
            'category': forms.SelectMultiple(attrs={'class': 'tag-input'}),
        }


class ReviewForm (ModelForm):
    class Meta:
        model = Review
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'comment-input', 'placeholder': 'Add a comment'}),
        }


class LiveCommentsForm(ModelForm):
    class Meta:
        model = LiveComments
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'comment-input', 'placeholder': 'Add a comment'}),
        }


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ['country']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class NewsForm (ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'image',
                  'photo_caption', 'author', 'imageBy']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'description-input'}),
        }


class FixtureForm(ModelForm):
    date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Fixture
        fields = ['fixture', 'date', 'thumbnail']


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'image', 'gold', 'silver', 'bronze', 'total']


class StandingForm(ModelForm):
    class Meta:
        model = Standing
        fields = ['country', 'gold', 'silver', 'bronze', 'total']

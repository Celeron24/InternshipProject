from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class NewsArticle(Page):
    published_date = models.DateField()
    news_title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField()
    image_url = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.CharField(max_length=50, choices=[
        ('business', 'Business'),
        ('world', 'World'),
        ('Health', 'Health'),
        ('England', 'England'),
        ('Asia', 'Asia'),
        ('Africa', 'Africa'),
        ('entertainment', 'entertainment'),
        ('Europe', 'Europe'),
        ('LatinAmerica', 'LatinAmerica'),
        ('MiddleEast', 'MiddleEast'),
        ('NorthernIreland', 'NorthernIreland'),
        ('Politics', 'Politics'),
        ('Scotland', 'Scotland'),
        ('Sports', 'Sports'),
        ('Technology', 'Technology'),
        ('UsCanada', 'UsCanada'),
        ('Wales', 'Wales'),
        ('general', 'General'),
    ], default='general')

    content_panels = Page.content_panels + [
        FieldPanel('published_date'),
        FieldPanel('news_title'),
        FieldPanel('description'),
        FieldPanel('link'),
        FieldPanel('image_url'),
        FieldPanel('category'),
    ]

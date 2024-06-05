from django.db import models
from wagtail.fields import RichTextField
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
        ('health', 'Health'),
        ('england', 'England'),
        ('asia', 'Asia'),
        ('africa', 'Africa'),
        ('entertainment', 'entertainment'),
        ('europe', 'Europe'),
        ('latinAmerica', 'LatinAmerica'),
        ('middleEast', 'MiddleEast'),
        ('northernIreland', 'NorthernIreland'),
        ('politics', 'Politics'),
        ('scotland', 'Scotland'),
        ('sports', 'Sports'),
        ('technology', 'Technology'),
        ('usCanada', 'UsCanada'),
        ('wales', 'Wales'),
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



class ContactDetailsPage(Page):
    query = models.CharField(max_length=255,default="")
    email = models.EmailField(null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('query'),
        FieldPanel('email'),
        FieldPanel('username'),
        FieldPanel('phone_number'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
    ]



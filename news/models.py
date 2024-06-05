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


class NewsRequest(models.Model):
    query = models.CharField(max_length=255)
    email = models.EmailField(blank=False, default=None)
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}'s query: {self.query}"


class ContactDetailsPage(Page):
    # intro = RichTextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.IntegerField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('email'),
        FieldPanel('username'),
        FieldPanel('phone_number'),
    ]

    # def get_context(self, request):
    #     context = super().get_context(request)
    #     context['news_requests'] = NewsRequest.objects.all()
    #     return context



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


class SearchQuery(models.Model):
    query = models.CharField(max_length=255)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}'s query: {self.query}"


class ContactDetailsPage(Page):

    search_query = models.ForeignKey(
        SearchQuery,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='save_contact_details'
    )

    content_panels = Page.content_panels + [
        # Define panels for additional fields if needed
    ]

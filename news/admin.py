from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import NewsArticle, NewsRequest, ContactDetailsPage


class NewsArticleModelAdmin(ModelAdmin):
    model = NewsArticle
    menu_label = 'News Articles'
    menu_icon = 'doc-full-inverse'  # Change this to the appropriate icon
    list_display = ('news_title', 'published_date', 'category')
    search_fields = ('news_title', 'description')
    list_filter = ('category',)


modeladmin_register(NewsArticleModelAdmin)


class ContactDetailsPageAdmin(ModelAdmin):
    model = ContactDetailsPage
    menu_label = 'ContactDetailsPage'
    menu_icon = 'doc-full-inverse'  # change as needed
    list_display = ('username', 'phone_number', 'email')
    search_fields = ('username', 'email')


modeladmin_register(ContactDetailsPageAdmin)

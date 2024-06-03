from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import NewsArticle, ContactDetailsPage


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
    menu_label = 'Requests for News'
    menu_icon = 'doc-full-inverse'
    list_display = ('query', 'username', 'email', 'phone_number', 'created_at')


modeladmin_register(ContactDetailsPageAdmin)

#from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import NewsArticle

class NewsArticleModelAdmin(ModelAdmin):
    model = NewsArticle
    menu_label = 'News Articles'
    menu_icon = 'doc-full-inverse'  # Change this to the appropriate icon
    list_display = ('news_title', 'published_date', 'category')
    search_fields = ('news_title', 'description')
    list_filter = ('category',)

modeladmin_register(NewsArticleModelAdmin)

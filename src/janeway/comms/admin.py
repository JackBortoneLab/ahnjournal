from django.contrib import admin
from comms import models


class TagAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'object', 'posted', 'posted_by', 'start_display', 'end_display')
    list_filter = ('posted_by', 'content_type')
    search_fields = ('title', 'posted_by')


admin_list = [
    (models.NewsItem, NewsItemAdmin),
    (models.Tag, TagAdmin),
]

[admin.site.register(*t) for t in admin_list]

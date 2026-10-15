from django.contrib import admin
from .models import Posts

class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "body",
)

admin.site.register(Posts)
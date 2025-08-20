from django.contrib import admin

from apps.kun_uz.models import KunPost,KunAuthor,Category

admin.site.register(KunPost)
admin.site.register(KunAuthor)
admin.site.register(Category)

from django.contrib import admin
from mini_url.models import MiniURL


class MiniURLAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'longURL', 'code', 'dateCreation', 'nbAcces')
    ordering = ('dateCreation',)
    search_fields = ('longURL', )

admin.site.register(MiniURL, MiniURLAdmin)



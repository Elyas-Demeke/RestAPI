from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('note_subject', 'note_body', 'pub_date', 'author')
    search_fields = ['note_subject', 'note_body']
    readonly_fields = ('pub_date',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# admin.site.register(Note)
admin.site.register(Note, NoteAdmin)

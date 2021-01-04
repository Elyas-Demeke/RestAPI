from django.urls import path

from memo_app.api.views import (
    api_detail_note_view,
    api_create_note_view,
    api_delete_note_view,
    api_update_note_view,
    api_list_note_view,

)

app_name = 'memo_app'

urlpatterns = [
    path('<slug>/', api_detail_note_view, name='detail'),
    path('<slug>/update', api_update_note_view, name='update'),
    path('<slug>/delete', api_delete_note_view, name='delete'),
    path('create', api_create_note_view, name='create'),
    path('', api_list_note_view, name='list')
]

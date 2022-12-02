from django.urls import path
from .views import ItemList, ItemAddView, ItemEditView, ItemShowView


app_name = 'shoppinglist'
urlpatterns = [
    path('list/',ItemList.as_view(),name='list'),
    path('add', ItemAddView.as_view(), name='add'),
    path('edit', ItemEditView.as_view(),name='edit'),
    path('show', ItemShowView.as_view(), name='show'),
    ]
from django.urls import path

from blackbox.cms.views.pages.page_views import PageListView, PageDetailsView

urlpatterns = [
    path('pages/', PageListView.as_view(), name='page-list'),
    path('pages/<str:slug>/', PageDetailsView.as_view(), name='page-details'),
]

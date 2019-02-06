from django.urls import path
from .views import (
	IGPListView,  
	IGPCreateView,
	IGPDeleteView,
	IGPUpdateView,
	
	ORGListView,
	ORGDetailView,
	ORGCreateView,
	ORGUpdateView,
	ORGDeleteView
	)
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('igps/', IGPListView.as_view(), name='app-igps'),
    path('orgs/', ORGListView.as_view(), name='app-orgs'),
    path('orgs/<int:pk>/', ORGDetailView.as_view(), name='orgigps_detail'),
    path('igps/new/', IGPCreateView.as_view(), name='igp-create'),
    path('igps/<int:pk>/delete/', IGPDeleteView.as_view(), name='igp-delete'),
    path('igps/<int:pk>/update/', IGPUpdateView.as_view(), name='igp-update'),
    path('orgs/new/', ORGCreateView.as_view(), name='org-create'),
    path('orgs/<int:pk>/delete/', ORGDeleteView.as_view(), name='org-delete'),
    path('orgs/<int:pk>/update/', ORGUpdateView.as_view(), name='org-update')
]
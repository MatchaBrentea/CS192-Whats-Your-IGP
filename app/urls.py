# MIT License

# Copyright (c) Justin James Gonzales, Thomas Martin Saliba, Brent Zaguirre

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# “This is a course requirement for CS 192 Software Engineering II under the supervision of 
# Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, 
# University of the Philippines, Diliman for the AY 2015-2016”.

# ---------------------------------------------------------------------------------------------

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
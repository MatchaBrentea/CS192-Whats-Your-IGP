from django.shortcuts import render
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)
from .models import IGP, ORG
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
	context = {
		'page': ''
	}
	return render(request, 'app/home.html', context)
 
def orgs(request):
	context = {
		'orgs': ORG.objects.all(),
		'page': 'ORGS'
	}
	return render(request, 'app/org.html', context)

def orgigps(request):
	context = {
		'orgs': ORG.objects.all(),
		'igps': IGP.objects.all(),
		'page': org.name
	}
	return render(request, 'app/orgigps.html', context)

	
class IGPListView(ListView):
	model = IGP
	template_name = 'app/igp.html'
	context_object_name = 'igp'
	ordering = ['-date_posted']

class IGPCreateView(LoginRequiredMixin, CreateView):
	model = IGP
	fields = ['item', 'org', 'itype', 'price']

class IGPDeleteView(LoginRequiredMixin, DeleteView):
	model = IGP
	success_url ='/app/igps/'

class IGPUpdateView(LoginRequiredMixin, UpdateView):
	model = IGP
	fields = ['item', 'org', 'itype', 'price']

class ORGListView(ListView):
	model = ORG
	template_name = 'app/org.html'
	context_object_name = 'orgs'
	ordering = ['name']

class ORGDetailView(DetailView):
	model = ORG
	orgId = model.id
	template_name = 'app/orgigps_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['org_igps']=IGP.objects.filter(org_id=self.object.id)

		return context

class ORGCreateView(LoginRequiredMixin, CreateView):
	model = ORG
	fields = ['name', 'desc']

class ORGUpdateView(LoginRequiredMixin, UpdateView):
	model = ORG
	fields = ['name', 'desc']

class ORGDeleteView(LoginRequiredMixin, DeleteView):
	model = ORG
	success_url ='/app/orgs/'

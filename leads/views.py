from multiprocessing import context
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, FormView
from leads.filters import LeadFilter

from .models import Prospect, Event
from .forms import EventFormAdmin, LeadModelForm, LeadModelAdminForm, EventForm, LeadUpdateForm, LeadUpdateFormUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render


class LeadCreateViewForUser(LoginRequiredMixin,CreateView):
    template_name = "leads/lead_create.html"
    
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_list")

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.Agent = self.request.user
        
        form.save()
        
        messages.success(self.request, "You have successfully created a lead")
        return super(LeadCreateViewForUser, self).form_valid(form)



class LeadCreateViewForAdmin(LoginRequiredMixin,CreateView):
    template_name = "leads/lead_create.html"
    
    form_class = LeadModelAdminForm

    def get_success_url(self):
        return reverse("leads:lead_list")

    def form_valid(self, form):
        form.save()
        
        messages.success(self.request, "You have successfully created a lead")
        return super(LeadCreateViewForAdmin, self).form_valid(form)



@login_required
def lead_update_admin(request, pk,*args):
    lead = Prospect.objects.get(id=pk)
    form = LeadUpdateForm(instance=lead)
    if request.method == "POST":
        form = LeadUpdateForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('leads:lead_detail', args=[lead.id]))

    
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html", context)

@login_required
def lead_update_user(request, pk):
    lead = Prospect.objects.get(id=pk)
    form = LeadUpdateFormUser(instance=lead)
    if request.method == "POST":
        form = LeadUpdateFormUser(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html", context)

class LeadDeleteView(LoginRequiredMixin,DeleteView):
    model = Prospect
    template_name = "leads/lead_confirm_delete.html"

    def get_success_url(self):
        return reverse("leads:lead_list")

@login_required
def detail_view(request, pk):
    lead = get_object_or_404(Prospect, id=pk)

    events = Event.objects.filter(Prospect = lead)
    last_events = Event.objects.filter(Prospect =  lead).last()


    context = {
        "lead": lead,
        "events": events,
        "last_events": last_events

    }
                 
    return render(request, "leads/detail.html", context)



def last_c(request,pk):
    lead = get_object_or_404(Prospect, id=pk)
    last_events = Event.objects.filter(Prospect =  lead).last()
    return last_events



        


@login_required
def lead_list(request):
    if request.user.is_agent:
       leads = Prospect.objects.filter(Agent=request.user)
    else: leads = Prospect.objects.all()
    

    myFilter = LeadFilter(request.GET, queryset= leads)
    leads = myFilter.qs
    
    context = {
        "leads": leads,
        "myFilter": myFilter,
    }
    return render(request, "leads/lead_list.html", context)











class EventCreateForAdmin(LoginRequiredMixin,CreateView):
    template_name = "leads/event_create.html"
    
    form_class = EventFormAdmin

    def get_success_url(self):
        return reverse("leads:lead_list")

    def form_valid(self, form):
        form.save()
        
        messages.success(self.request, "You have successfully created an event")
        return super(EventCreateForAdmin, self).form_valid(form)



class EventCreateForUser(LoginRequiredMixin,FormView):
    template_name = "leads/event_create.html"
    
    form_class = EventForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['Agent'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse("leads:lead_list")

    def form_valid(self, form):
        event = form.save(commit=False)
        
        event.Prospect.Agent = self.request.user
        
        form.save()
        
        messages.success(self.request, "You have successfully created a lead")
        return super(EventCreateForUser, self).form_valid(form)



@login_required
def events_list(request):
    if request.user.is_agent:
        events = Event.objects.filter(Agent=request.user)
    else: events = Event.objects.all()
    context = {
        "events": events
    }
    return render(request, "leads/events_list.html", context)



   







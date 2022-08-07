from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .forms import UserForm
from .models import User
# Create your views here.



class HomeView(TemplateView):
    template_name = 'home.html'

def register(request):
    form = SignUpForm(request.POST)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'

    return render(request,'register.html', {'form': form, 'messages': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('dashboard')
            elif user is not None and user.is_agent:
                login(request, user)
                return redirect('profile')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'messages': msg})



class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = reverse_lazy('home')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    template_name = 'profile-update.html'

    def post(self, request):

        post_data = request.POST or None

        user_form = UserForm(post_data, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



def agents_list(request):
    agents = User.objects.filter(is_agent= True)
    context = {
        "agents": agents
    }
    return render(request, "agents_list.html", context)









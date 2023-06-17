from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import default_storage
import folium
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.

def landing(request):

    return render(request, 'core/landing.html')

def home(request):
    # Create a Folium map instance
    my_map = folium.Map(location=[6.918658, 122.077802], zoom_start=14, control_scale=True, max_zoom=20, min_zoom=2, max_bounds=True)

    # Retrieve job data from the database
    jobs = Job.objects.all()

    for job in jobs:
        lat = job.latitude
        lon = job.longitude
        job_name = job.name

        marker = folium.Marker(location=[lat, lon], popup=job_name)
        marker.add_to(my_map)

    # Render the map to HTML
    context = {
        'map': my_map._repr_html_(),
        'jobs': jobs
    }

    return render(request, 'core/home.html', context)

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

@login_required
def update_profile(request):
    user = request.user
    form = ProfileUpdateForm(instance=user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            user = form.save(commit=False)
            mobile = form.cleaned_data['mobile']
            if mobile == '':
                user.mobile = None
            else:
                user.mobile = mobile
            user.save()
            form.save_m2m()
            return redirect('profile')

    return render(request, 'profile_update.html', {'form': form})

def available(request):

    my_map = folium.Map(location=[6.918658, 122.077802], zoom_start=14, control_scale=True, max_zoom=20, min_zoom=2, max_bounds=True)

    # Retrieve job data from the database
    jobs = Job.objects.all()

    for job in jobs:
        lat = job.latitude
        lon = job.longitude
        job_name = job.name

        marker = folium.Marker(location=[lat, lon], popup=job_name)
        marker.add_to(my_map)

    # Render the map to HTML
    context = {
        'map': my_map._repr_html_(),
        'jobs': jobs
    }

    return render(request, 'available-jobs.html', context)

def faq(request):

    return render(request, 'faq.html')

def about(request):

    return render(request, 'about.html')

def match(request):

    user = request.user
    matching_jobs = Job.objects.filter(job_type__in=user.skills.all()).distinct()
    my_map = folium.Map(location=[6.918658, 122.077802], zoom_start=14, control_scale=True, max_zoom=20, min_zoom=2, max_bounds=True)

    # Add markers, polygons, or other layers to the map using Folium methods
    for job in matching_jobs:
        lat = job.latitude
        lon = job.longitude
        job_name = job.name

        marker = folium.Marker(location=[lat, lon], popup=job_name)
        marker.add_to(my_map)

    # Render the map to HTML
    context = {
         'map': my_map._repr_html_(),
         'matching_jobs':matching_jobs
    }

    return render (request, 'match.html', context)

def dashboard(request):

    return render (request, 'dashboard.html')

def userdash(request):

    users = User.objects.all

    return render (request, 'user-dash.html', {'users':users})

def jobdash(request):

    jobs = Job.objects.all

    return render (request, 'job-dash.html', {'jobs':jobs})


def addjob(request):

    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.save()
            form.save_m2m()
            return redirect('jobdashboard')

    return render(request, 'addjob.html', {'form': form})

@staff_member_required(login_url='/login')
def deletejob(request, pk):
    job = get_object_or_404(Job, id=pk)
    try:
        job.delete()
        messages.success(request, 'Organization deleted successfully')
    except Exception as e:
        messages.error(request, f'Error deleting Organization: {str(e)}')
    return redirect('jobdashboard')

class updatejob(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    fields = '__all__'
    success_url = reverse_lazy('jobdashboard')
    template_name = 'addjob.html'

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser
    
    def post(self, request, *args, **kwargs):
        # Get the existing object
        self.object = self.get_object()

        # Delete previous image if it exists
        previous_image = self.object.thumbnail
        if previous_image:
            default_storage.delete(previous_image.path)

        return super().post(request, *args, **kwargs)
    
def job(request, name):

    jobs = Job.objects.all()
    job = Job.objects.get(name=name)
    
    my_map = folium.Map(location=[job.latitude, job.longitude], zoom_start = 16, control_scale=True, max_zoom=20, min_zoom=2, max_bounds=True)

    for job in jobs:
        lat = job.latitude
        lon = job.longitude
        job_name = job.name

        marker = folium.Marker(location=[lat, lon], popup=job_name)
        marker.add_to(my_map)

    # Render the map to HTML
    context = {
        'map': my_map._repr_html_(),
        'jobs': jobs,
        'job': job
    }

    return render(request, 'active-job.html', context)
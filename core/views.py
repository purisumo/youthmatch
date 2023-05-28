from django.shortcuts import render
import folium
# Create your views here.

def home(request):
    # Create a Folium map instance
    my_map = folium.Map(location=[6.918658, 122.077802], zoom_start=14, control_scale=True,)

    # Add markers, polygons, or other layers to the map using Folium methods
    lat = 6.913787
    lon = 122.079292
    lat2 = 6.916772
    lon2 = 122.064755
    marker1 = folium.Marker(location=[lat, lon], popup='Job 1')
    marker2 = folium.Marker(location=[lat2, lon2], popup='Job 2')

    marker1.add_to(my_map)
    marker2.add_to(my_map)
    # Render the map to HTML
    context = {
         'map': my_map._repr_html_()
    }

    return render(request, 'core/home.html', context)

def profile(request):

    return render(request, 'profile.html')

def available(request):

    my_map = folium.Map(location=[6.918658, 122.077802], zoom_start=14, control_scale=True,)

    # Add markers, polygons, or other layers to the map using Folium methods

    # Render the map to HTML
    context = {
         'map': my_map._repr_html_()
    }

    return render(request, 'available-jobs.html', context)

def faq(request):

    return render(request, 'faq.html')

def about(request):

    return render(request, 'about.html')

def match(request):
    my_map = folium.Map(location=[6.918658, 122.077802], zoom_start=14, control_scale=True,)

    # Add markers, polygons, or other layers to the map using Folium methods

    # Render the map to HTML
    context = {
         'map': my_map._repr_html_()
    }

    return render (request, 'match.html', context)

def dashboard(request):

    return render (request, 'dashboard.html')
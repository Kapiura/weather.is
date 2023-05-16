from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    context = {

    }
    return render(request, "home.html", context)

def weather_view(request, *args, **kwargs):
    context = {

    }
    return render(request, "weather.html", context)

def about_me_view(request, *args, **kwargs):
    context = {

    }
    return render(request, "about_me.html", context)

def contact_view(request, *args, **kwargs):
    context = {

    }
    return render(request, "contact.html", context)

def graphs_view(request, *args, **kwargs):
    context = {

    }
    return render(request, "graphs.html", context)

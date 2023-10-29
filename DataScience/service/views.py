from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Service , ServiceRequest


# Create your views here.

add_Service = lambda request: redirect("users:login_view") if not request.user.is_staff else (
    redirect("service:all_services_view") if request.method == "POST" else render(request, 'service/add_Service.html')
)

all_services_view = lambda request: render(request, "service/services.html", context={"services": Service.objects.all()})

service_detail = lambda request, service_id: render(request, "service/service_detail.html", {"service": Service.objects.get(id=service_id)})

def service_update_view(request:HttpRequest, service_id):
    
    service = Service.objects.get(id=service_id)

    #updating a post
    if request.method == "POST":
       service.title=request.POST["title"]
       service.description=request.POST["description"]
       service.image=request.FILES["image"]
        
       service.save()

       return redirect("service:service_detail", service_id=service_id)

    return render(request, "service/update_service.html", {"service": service})


def service_delete_view(request: HttpRequest, service_id):
    #deleting an entry from database
    
    service = Service.objects.get(id=service_id)
    service.delete()
    return redirect ("service:all_services_view")


def add_request(request: HttpRequest,service_id):
    
     if not request.user.is_authenticated:
        return redirect("users:login_view")
     
     service=Service.objects.get(id=service_id)
     if not ServiceRequest.objects.filter(user=request.user, service=service).exists():
        new_request = ServiceRequest(user=request.user, service=service,)
        
        new_request.save()
    
     return redirect("service:service_detail", service_id=service_id)

def user_service_request(request: HttpRequest):
    requests=ServiceRequest.objects.filter(user=request.user)
    return render(request, 'service/requests.html',{"requests":requests})


def users_request(request: HttpRequest):
    requests=ServiceRequest.objects.all()
  
    return render(request, 'service/users_request.html',{"requests":requests})


def users_request_update(request: HttpRequest, request_id):
    service_request=ServiceRequest.objects.get(id=request_id)
    
    if request.method == "POST":
        service_request.status =request.POST['status']
        service_request.save()
    
        return redirect("service:users_request")


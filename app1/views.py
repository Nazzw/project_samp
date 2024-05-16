from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,get_object_or_404
from . models import pets
from .forms import petsForm
# Create your views here.
def hello(request):
    return HttpResponse("HELLO WORLD")
def home(request):
    inst=pets.objects.all()
    return render(request,'index.html',{"inst":inst})
    
def pet(request):
    form = petsForm()
    if request.method == 'POST':
        form = petsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
    'form': form,
    }

    return render(request, 'pets_in.html', context)
def update_view(request, id):
    context ={}
    obj = get_object_or_404(pets, id = id)
    form = petsForm(request.POST or None,request.FILES or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context["form"] = form
 
    return render(request, "update_view.html", context)
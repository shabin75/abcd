from django.shortcuts import render, redirect
from .models import ServiceData


def test(request):
    try:
        obj = ServiceData.objects.all()
        print(obj)
        return render(request, 'index.html', {'object': obj})
    except:
        return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        a = request.POST['form_head']
        b = request.POST['form_des']
        c = request.FILES['form_file']
        ServiceData.objects.create(head=a, des=b, img=c)

        return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def search(request):
    data = request.GET['search']
    objects = ServiceData.objects.filter(head=data)
    print(objects)
    return render(request, 'search.html', {'obj': objects})


def delete(request, pk):
    ServiceData.objects.get(id=pk).delete()
    return redirect('services')


def detail(request, pk):
    obj = ServiceData.objects.get(id=pk)
    return render(request, 'detail.html', {'obj': obj})


def update(request, pk):
    if request.method == 'POST':
        a = request.POST['form_head']
        b = request.POST['form_des']
        c = request.POST['form_price']
        ServiceData.objects.filter(id=pk).update(head=a, des=b, price=c)
        return redirect('detail',pk=pk)
    else:
        obj = ServiceData.objects.get(id=pk)
        return render(request, 'update.html', {'obj': obj})

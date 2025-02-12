import json
from django.http import JsonResponse
from django.shortcuts import render
from cv.forms import contactmeForm
from cv.models import AboutMe, Education, Service


def cv_view(request):

    academics= Education.objects.all()
    aboutme= AboutMe.objects.all()
    service =Service.objects.filter(fetured=True).order_by('-created_at')[:4]



    context = {

        'educations': academics,
        'aboutme': aboutme,
        'service': service

    }

    return render(request, 'index.html', context)


def submit_form(request):
    if request.method=='POST':
        data = json.loads(request.body)
        form = contactmeForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({ 'status':"success",'message':'Form submiited sucessfully!'})
        else:
            return JsonResponse({ 'status':'error'}, status=400)
        
    return JsonResponse({'status':'error', 'message':'Method Not Allowed!'}, status=405)










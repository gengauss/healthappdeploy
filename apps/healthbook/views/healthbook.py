from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models import MentalInfo, PhysicalInfo, Contact, Feedback


def index(request):
    return render(request, '../templates/healthbook/index.html', {})


def physical_health(request):
    physicaldiseases = PhysicalInfo.objects.all()
    data_dict = {'physicaldiseases': physicaldiseases}
    return render(request, '../templates/healthbook/physicalhealth.html', data_dict)


def mental_health(request):
    mentaldiseases = MentalInfo.objects.all()
    data_dict = {'mentaldiseases': mentaldiseases}
    return render(request, '../templates/healthbook/mentalhealth.html', data_dict)


def physical_detail(request, physicalinfo_id):
    physicaldiseases = PhysicalInfo.objects.get(pk=physicalinfo_id)
    data_dict = {'physicaldiseases': physicaldiseases}
    return render(request, '../templates/healthbook/physicaldetail.html', data_dict)


def mental_detail(request, mentalinfo_id):
    mentaldiseases = MentalInfo.objects.get(pk=mentalinfo_id)
    data_dict = {'mentaldiseases': mentaldiseases}
    return render(request, '../templates/healthbook/mentaldetail.html', data_dict)


def physical_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        physicaldiseases = PhysicalInfo.objects.filter(name__icontains=q)
        return render(request, '../templates/healthbook/physicalsearch.html',
                      {'physicaldiseases': physicaldiseases, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


def mental_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        mentaldiseases = MentalInfo.objects.filter(name__icontains=q)
        return render(request, '../templates/healthbook/mentalsearch.html',
                      {'mentaldiseases': mentaldiseases, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


def contact(request):
    if request.method == 'POST':
        contact_form = Contact(name=request.POST['name'], email=request.POST['email'], feedback=request.POST['feedback'])
        contact_form.save()
    return render(request, '../templates/home/contact.html', {})


def feedback(request):
    if request.method == 'POST':
        feedback_form = Feedback(hb_content=request.POST.get('hb_content', False),
                                 hb_design=request.POST.get('hb_design', False),
                                 hb_change=request.POST.get('hb_change', False),
                                 hb_feedback=request.POST.get('hb_feedback', False),
                                 vs_content=request.POST.get('vs_content', False),
                                 vs_design=request.POST.get('vs_design', False),
                                 vs_change=request.POST.get('vs_change', False),
                                 vs_feedback=request.POST.get('vs_feedback', False),
                                 fr_design=request.POST.get('fr_design', False),
                                 fr_use=request.POST.get('fr_use', False),
                                 fr_opinion=request.POST.get('fr_opinion', False),
                                 fr_change=request.POST.get('fr_change', False),
                                 fr_feedback=request.POST.get('fr_feedback', False),
                                 ct_design=request.POST.get('ct_design', False),
                                 ct_use=request.POST.get('ct_use', False),
                                 ct_opinion=request.POST.get('ct_opinion', False),
                                 ct_change=request.POST.get('ct_change', False),
                                 ct_feedback=request.POST.get('ct_feedback', False),
                                 hg_design=request.POST.get('hg_design', False),
                                 hg_use=request.POST.get('hg_use', False),
                                 hg_opinion=request.POST.get('hg_opinion', False),
                                 hg_change=request.POST.get('hg_change', False),
                                 hg_feedback=request.POST.get('hg_feedback', False)
                                 )
        feedback_form.save()
    return render(request, '../templates/home/feedback.html', {})

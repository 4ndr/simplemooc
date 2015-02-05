from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response

from .models import Course
from .form import ContactCourse

def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context = {'courses': courses}
    return render(request, template_name, context)


# def details(request, pk): #se usa quando for numeros na url
#     course = get_object_or_404(Course, pk=pk)
#     context = {'course': course}
#     template_name = 'courses/details.html'
#     return render(request, template_name, context)

def details(request, slug): #usa quando a url for slug
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            # print(form.cleaned_data['name'])#pega valores do formulario
            # print(form.cleaned_data['message'])
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['form'] = form
    context['course'] = course
    template_name = 'courses/details.html'
    return render(request, template_name, context)
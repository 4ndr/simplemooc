#executar no shell do django

from courses.models import Course

django = Course(name='Python com Django', slug='django')
django.save()
# django.pk

python_dev = Course(name='Python para alguma coisa', slug='python-dev')
python_dev.save()
# python_dev.pk

courses = Course.objects.all()
for course in courses:
    print(course.name)

# courses[0].name
courses = Course.objects.filter(slug='django')
# courses

# courses[0]
courses = Course.objects.filter(slug='django').filter(name='Python')
# courses
courses = Course.objects.filter(slug='django', name='Python')
# courses
courses = Course.objects.filter(name__icontains='Python')
type('Course.db.models.manager.manager')
type(courses)
# Course.objects.get_queryset()
# courses.delete()


#parte2

from courses.models import Course

Course.objects.create(name='Python com django', slug='django')
Course.objects.create(name='Python para devs', slug='python')
Course.objects.create(name='Python para logica', slug='logica')

Course.objects.search('python')

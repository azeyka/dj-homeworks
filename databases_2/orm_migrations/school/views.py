from django.views.generic import ListView

from .models import Student


class StudentListView(ListView):
    model = Student
    ordering = 'group'

    def get_context_data(self, *, object_list=None, **kwargs):
        students = Student.objects.all().prefetch_related('teacher')
        return {
            'object_list': students
        }

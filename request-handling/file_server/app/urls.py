from django.urls import path

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
from app.views import file_list, file_content

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', file_list, name='file_list'),
    path('<date>/', file_list, name='file_list'),
    path('filecontent/<name>', file_content, name='file_content'),
]

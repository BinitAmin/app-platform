from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage


class Home(TemplateView):
    template_name = 'home.html'


def upload_file(request):
    document_details = {"url" : []}
    if request.method == "POST":
        uploaded_files = request.FILES.getlist("document")
        for file_obj in uploaded_files:
            file = FileSystemStorage()
            saved_name = file.save(file_obj.name, file_obj)
            document_details['url'].append(file.url(saved_name))
    return render(request, 'upload.html', document_details)

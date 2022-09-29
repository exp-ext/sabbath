from django.shortcuts import redirect, render

from .forms import PhotoForm
from .models import Photo


def photo_list(request):
    photos = Photo.objects.all()

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:photo_list')
    else:
        form = PhotoForm()

    context = {
        'form': form,
        'photos': photos
    }
    template = 'core/photo_list.html'
    return render(request, template, context)

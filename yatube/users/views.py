from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm, ProfileForm

User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)

    if user != request.user:
        redirect('posts:index')

    form = ProfileForm(
        request.POST or None,
        files=request.FILES or None,
        instance=user
    )

    if request.method == "POST" and form.is_valid():
        user = form.save()
        return redirect('posts:profile', username=username)

    context = {
        'user': user,
        'form': form,
    }
    template = 'users/user_profile.html'
    return render(request, template, context)

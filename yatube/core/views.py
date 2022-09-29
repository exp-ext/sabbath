from django.core.paginator import Paginator
from django.shortcuts import render


def page_not_found(request, exception):
    return render(request, 'core/404.html', {'path': request.path}, status=404)


def server_error(request):
    return render(request, 'core/500.html', status=500)


def permission_denied(request, exception):
    return render(request, 'core/403.html', status=403)


def csrf_failure(request, reason=''):
    return render(request, 'core/403csrf.html')


def paginator_handler(request, query):
    paginator = Paginator(query, 10)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)

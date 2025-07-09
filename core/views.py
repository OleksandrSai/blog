from django.shortcuts import render
import logging

logger = logging.getLogger("django")


def permission_denied_view(request, exception):
    logger.error(f"403 Forbidden: Path {request.path}")
    return render(request, "403.html", status=403)


def page_not_found_view(request, exception):
    logger.error(f"404 Not Found: Path {request.path}")
    return render(request, "404.html", status=404)


def server_error_view(request):
    logger.error(f"500 Server Error at Path {request.path}")
    return render(request, "500.html", status=500)

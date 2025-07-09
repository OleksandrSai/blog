from ckeditor_uploader import views
from django.views.decorators.csrf import csrf_exempt

upload = csrf_exempt(views.upload)
browse = views.browse

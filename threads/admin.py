from django.contrib import admin
from .models import Subject, Thread, Posts

admin.site.register(Posts)
admin.site.register(Thread)
admin.site.register(Subject)

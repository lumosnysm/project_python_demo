from django.contrib import admin

from .models import Question, Choice, Feedback, GenDoc

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Feedback)
admin.site.register(GenDoc)

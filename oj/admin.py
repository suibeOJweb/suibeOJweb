from django.contrib import admin
from .models import Question, Suiber, Example

# Register your models here.
admin.site.register(Question)
admin.site.register(Suiber)
admin.site.register(Example)
from django.contrib import admin

from .models import Question,Choice, Acount_Login


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields' : ['question_text']}),
        ('Data info',   {'fields' : ['pub_date']})
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question)
admin.site.register(Acount_Login)


# Register your models here.

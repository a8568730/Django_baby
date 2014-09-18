from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.

# 時間欄位上方有標題
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 	{'fields':['question_text']}),
		('Date information', {'fields':['pub_date']})
	]

admin.site.register(Question, QuestionAdmin)	
admin.site.register(Choice)

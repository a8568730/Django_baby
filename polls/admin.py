from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.
# 新增問題時，一次出現三個選項
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3
# 時間欄位上方有標題
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 	{'fields':['question_text']}),
		('Date information', {'fields':['pub_date']})
	]
	inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)	
admin.site.register(Choice)

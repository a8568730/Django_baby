from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
	# 新增問題時，一次出現三個選項
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	# 時間欄位上方有標題
	fieldsets = [
		(None, 	{'fields':['question_text']}),
		('Date information', {'fields':['pub_date']})
	]
	# 水平顯示每個選項和投票數
	inlines = [ChoiceInline]
	# 搜尋問題清單
	search_fields = ['question_text']
	# 問題清單的資訊
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	# 可以按照過濾器，挑出要看的問題表
	list_filter = ['pub_date']
admin.site.register(Question, QuestionAdmin)	
admin.site.register(Choice)

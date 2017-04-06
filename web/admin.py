from django.contrib import admin
from .models import Expense, Income, Token, News
# Register your models here.
class Menubar(admin.ModelAdmin):
    list_display =["user","date","amount"]
    
admin.site.register(Expense,Menubar)
admin.site.register(Income,Menubar)
admin.site.register(Token)
admin.site.register(News)

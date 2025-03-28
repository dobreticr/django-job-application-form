from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email") # Prikazuje sve navedeno bez da se stisne na ime
    search_fields = ("first_name", "last_name", "email")  # Dodaje search opciju za brzinsko pretrazivanje
    list_filter = ("date", "occupation")  #Filtriraj ovisno o datumu ili zaposlenju
    ordering = ("first_name", ) # Organizira se po prvom slovu imena
    readonly_fields = ("occupation", ) #Samo se moze procitati nemoze se promjeniti

admin.site.register(Form, FormAdmin)

from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title') #Lien pour pouvoir accéder au détails d'une annonce
    list_filter = ('realtor',)  #appliquer les filtres sur une colonne
    list_editable = ('is_published',) #Permettre la modification d'une colone directement sans aller dans les détails.
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price') #définir des champs sur lesquels on peut effectuer une recherche.
    list_per_page = 25 #définir la pagination sur la page d'admiistration

admin.site.register(Listing, ListingAdmin)
from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')  # Fields to display in the list view
    search_fields = ('question',)  # Add a search bar for the question field

admin.site.register(FAQ, FAQAdmin)
from django.contrib import admin

# Register your models here.
from .models import GamePlatform, Game, PriceList

admin.autodiscover()

admin.site.register(GamePlatform)
admin.site.register(Game)
admin.site.register(PriceList)

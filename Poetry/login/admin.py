from django.contrib import admin
from models import *

# Register your models here.
class loginAdmin(admin.ModelAdmin):
    admin.site.register(user_data)


class OtpAdmin(admin.ModelAdmin):
    admin.site.register(otp_data)
    
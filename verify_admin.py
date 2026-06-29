import os
import sys
import urllib.request

os.chdir(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'holiday_site.settings')

import django
django.setup()
from django.contrib.auth import get_user_model

User = get_user_model()
username = '3Dholidays666'
password = '3dholidays4452'

try:
    user = User.objects.get(username=username)
    print('user_exists', True)
    if not user.has_usable_password():
        print('password_usable', False)
        user.set_password(password)
        user.save()
        print('password_set', True)
    else:
        print('password_usable', True)
except User.DoesNotExist:
    print('user_exists', False)
    user = User.objects.create_superuser(username=username, email='holidaysat3d@gmail.com', password=password)
    print('superuser_created', True)

try:
    response = urllib.request.urlopen('http://127.0.0.1:8000/admin/', timeout=5)
    print('admin_status', response.getcode())
except Exception as exc:
    print('admin_status_error', repr(exc))

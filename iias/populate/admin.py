from populate import base
from django.contrib.auth.models import User

def populate():
    print('Creating admin account ...', end='')
    User.objects.all().delete()
    User.objects.create_superuser(username='admin', email=None, password='admin12345')
    print('done')
    
if __name__ == '__main__':
    populate()
#my_settings.py
DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'test', #2
        'USER': 'root', #3
        'PASSWORD': 'Hello@9709', #4
        'HOST': 'localhost', #5
        'PORT': '3306', #6
    }

}
SECRET_KEY = 'django-insecure-^%s68-y$e6v_@r+uimgxey#d7g&#rqq+r30@ybi%%ls043j_0n'
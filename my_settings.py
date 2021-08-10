SECRET_KEY = 'django-insecure-ebbnqpf8won$d97n2hql@5@$-mr9beyflfh+x#b&0_8!!q^seh'
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cicd2',
        'USER': 'root',
        'PASSWORD': '1q2w3e4r',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS' : {
            'charset' : 'utf8mb4'
        }
    }
}

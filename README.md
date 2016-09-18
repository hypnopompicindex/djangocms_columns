#djangocms_columns

DjangoCMS plugin for creation of entries in Bootstrap columns

## Dependencies
[django-cms](https://github.com/divio/django-cms)
[bootstrap 3](http://getbootstrap.com/)
[django-filebrowser-no-grappelli](https://github.com/smacker/django-filebrowser-no-grappelli)
[django-tinymce](https://github.com/aljosa/django-tinymce)
[django-orderedmodel](https://github.com/MagicSolutions/django-orderedmodel)


## Setup
add djangocms_columns to project

in settings.py

```
INSTALLED_APPS = (
    'cms'
    'tinymce'
    'filebrowser'
    .....
    'orderedmodel',
    'django_account_starter',
)
```

and run the migrations
```
python manage.py migrate cmsplugin_carousel
```



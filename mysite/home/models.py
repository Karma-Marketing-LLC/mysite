import os
from django.db import models, utils
from django.utils.encoding import force_str

# local vars


theme_root = 'home/static/home/themes'

# models here


def update_themes():
    """ This function adds new themes that were added to the themes directory.

    Check if the theme is 'complete' or not, then add it as a new Theme object.
    The folder name must be 'theme_name' and it must contain 'bg.jpg' and
    '/main.css' and... """
    if Theme.objects.all() is True:
        theme_query = Theme.objects.all()
    else:
        theme_query = []

    actual_list = os.listdir(theme_root)
    print(actual_list)

    # for item in actual_list:
    #     item = str(item)
    #     if item not in theme_query:
    #         if os.path.isfile(item + '/bg.jpg') and os.path.isfile(item + '/theme.css'):
    #         TODO: its not currently worth the hassle to check that these files are included
    #         due to explanation above, indent is temporarily decreased one level to ensure it works
    #         new_theme = Theme(item)
    #         new_theme.save()
    #         print(new_theme)
    #     else:
    #         raise Exception('No Themes to Add')
    #         return Theme(item)

# THIS IS A MESS RN


class Theme(models.Model):

    theme_name = models.CharField(max_length=255)
    bg_label = models.CharField(max_length=255, default='/bg.jpg')
    css_label = models.CharField(max_length=255, default='/theme.css')

    # IN PROGRESS

    def _get_theme_name_display(self, field):
        value = getattr(self, field.theme_name)
        # force_str() to coerce lazy strings.
        force_str(dict(field.flatchoices).get(value, value), strings_only=True)


    @staticmethod
    def get_random_theme():
        try:
            return Theme.objects.order_by("?").first()
        except utils.OperationalError:
            theme = Theme('default_theme')
            print('crap')
            return theme

from typing import Set, Any, Union
from .models import update_themes, Theme
from django.shortcuts import render, get_object_or_404
from django.db import utils

from django.views import View

# Create your views here.

def get_random_theme():
    try:
        return Theme.objects.order_by("?").first()
    except utils.OperationalError:
        theme = Theme('default_theme')
        return theme


class IndexView(View):
    """ Steps to building a home-page:
    Create unique user experience (TIP: reduce, reuse, recycle)

        - Identify user-source
            - Where did they come from?
            - relevant keywords?
            - if the user has not been here before:
                - Create a new object for them
                - Base it on something stable & automatically obtainable (cookies, ip-address)
                - Create a default theme based on source
        - Identify repeat-users
            - If an object matches a user-profile (must be indexed)
                - Return their customizations (created in models)
        - Create an interactive experience (WILL IT RETURN: RAW-DATA or ANALYZED DATA)
            ### REFER TO ANALYSIS APP [INPUT = DATA(TRACKERS, ETC.), OUTPUT = ANTICIPATION CALCULATION(ATTRS?)]
            - Nothing should be static that doesn't have to be
            - Simplicity is worth its weight in gold
            - React to details updated in real-time

       """

    # TODO: finish outline for homepage

    try:
        update_themes()
    except Exception:
        raise Exception("Ya Themes Don't work")
    template_name = 'home/base_home.html'

    def get(self, request):
        return render(request, self.template_name, self.)


from django.apps import AppConfig


class RserveConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Reserve'
    default_user_model='Reserve.CoustomUser'

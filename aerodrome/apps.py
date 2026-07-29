from django.apps import AppConfig


class AerodromeConfig(AppConfig):
    name = 'aerodrome'
    verbose_name = 'Aerodromes'

    def ready(self):
        import event_handlers.aerodrome_handlers  # noqa: F401

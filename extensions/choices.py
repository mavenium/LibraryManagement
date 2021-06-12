from django.utils.translation import ugettext_lazy as _


class GenderChoices:
    MAN = 0
    FEMALE = 1

    @classmethod
    def generate_choices(cls):
        return [
            (cls.MAN, _('Man')),
            (cls.FEMALE, _('Female'))
        ]

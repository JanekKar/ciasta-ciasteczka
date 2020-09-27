import os
import uuid
from django.utils.deconstruct import deconstructible


@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        extension = os.path.splitext(filename)[1]
        return self.path % (uuid.uuid4(), extension)


@deconstructible
def convert_to_ASCI_characters(word):
    pl_to_ang = {
        'ą': 'a',
        'ć': 'c',
        'ę': 'e',
        'ł': 'l',
        'ń': 'n',
        'ó': 'o',
        'ś': 's',
        'ź': 'z',
        'ż': 'z',
    }

    out = ""
    for letter in word:
        if letter in pl_to_ang:
            out += pl_to_ang[letter]
        else:
            out += letter
    return str(out)

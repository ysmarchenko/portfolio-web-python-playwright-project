from enum import Enum

class DropdownTypes(Enum):
    FROM = 'From'
    TO = 'To'

class Languages(Enum):
    ENGLISH = 'English'
    UKRAINIAN = 'Ukrainian'
    LINGALA = 'Lingala'
    SPANISH = 'Spanish'
    DETECT_LANGUAGE = 'Detect language'

class Tabs(Enum):
    TEXT = 'Text'
    DOCUMENT = 'Document'
    WEBSITE = 'Website'
    IMAGE = 'Image'
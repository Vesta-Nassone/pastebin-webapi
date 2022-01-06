from django.db import models
from pygments.lexer import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICE = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


    



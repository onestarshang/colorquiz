from django.db import models
import random

# Create your models here.

class LanguageColor(models.Model):
    language_code = models.IntegerField()
    language_color = models.CharField(max_length=128)
    language_str = models.CharField(max_length=128)
    
    @staticmethod
    def get_color_by_language_id(languageid):
        res = LanguageColor.objects.get(language_code=languageid)
        return res.language_color

    @staticmethod
    def generate_quiz(limit=10):
        quiz_list = []
        unique_c = []
        for i in range(int(limit)):
            while True:
                choice_res = list(random.sample(LanguageColor.objects.all(), 4))
                rr = random.randint(0,3)
                color_obj = choice_res[rr]
                _color = color_obj.language_color
                if _color not in unique_c:
                    unique_c.append(_color)
                    quiz_list.append({'choice_list':choice_res, 'langcolor':color_obj})
                    break
        answer_str = ','.join(unique_c)
        return quiz_list, answer_str
    
    @staticmethod
    def all_colornum_list():
        res = LanguageColor.objects.all()
        return [item.language_color for item in res]

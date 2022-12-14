from django.db import models

class Person(models.Model):
    person_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.person_text
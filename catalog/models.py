from django.db.models import Model, IntegerField, CharField, Choices


# Create your models here.
class Brick(Model):
    """This class is meant for individual LEGO brick pieces"""

    id = IntegerField(primary_key=True)
    name = CharField(max_length=200, verbose_name='catalog name')
    color = CharField(max_length=7, verbose_name='color')
    type = CharField(max_length=8, choices=[(1, 'standard'), (2, 'special')])

    def __str__(self):
        return f'{self.name} [{self.id}] is {self.type} type, of {self.color} color'

    class Meta:
        ordering = ['name']

from django.core.validators import MinValueValidator
from django.db.models import Model, IntegerField, CharField, ImageField, OneToOneField, \
    CASCADE, FloatField, ManyToManyField


def image_path(instance, filename):
    return str(type(instance).__name__) + '/' + str(instance.id) + filename


# Create your models here.
class Set(Model):
    """Entire class for LEGO set"""

    id = IntegerField(primary_key=True)
    name = CharField(max_length=200, verbose_name='set name')
    year = IntegerField(verbose_name='release year')
    number_of_pieces = IntegerField(null=True, default=100, validators=[MinValueValidator(0)])
    # price in $(USD)
    price = FloatField(verbose_name='price', null=True, default=0.0, validators=[MinValueValidator(0.0)])
    image = ImageField(upload_to=image_path, null=True, blank=True)

    def __str__(self):
        return f'{self.name} [{self.id}] releasd in year: {self.year}, has {self.number_of_pieces} pieces!'


class Manual(Model):
    """Every LEGO sets have manual that describes how to built it"""

    id = IntegerField(primary_key=True)
    name = CharField(max_length=200, verbose_name='manual name')
    number_of_pages = IntegerField(null=True, default=0, validators=[MinValueValidator(0)])
    image = ImageField(upload_to=image_path, null=True)
    set = OneToOneField(Set, on_delete=CASCADE)

    def __str__(self):
        return f'{self.name} [{self.id}] has {self.number_of_pages} pages'


class Brick(Model):
    """This class is meant for individual LEGO brick pieces"""

    id = IntegerField(primary_key=True)
    name = CharField(max_length=200, verbose_name='catalog name')
    color = CharField(max_length=7, verbose_name='color')
    type = CharField(max_length=8, choices=[('standard', 'standard'), ('special', 'special')])
    image = ImageField(upload_to=image_path, null=True)

    sets = ManyToManyField(Set)

    def __str__(self):
        return f'{self.name} [{self.id}] is {self.type} type, of {self.color} color'

    class Meta:
        ordering = ['name']

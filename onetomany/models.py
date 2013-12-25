from django.db import models

# Create your models here.
class OneToManyField(models.ManyToManyField):
    """A forgein key field that behaves just like djangos ManyToMany field,
    the only difference is that an instance of the other side can only be 
    related to one instance of your side. Also see the test cases.
    """
    def contribute_to_class(self, cls, name):
        # Check if the intermediate model will be auto created.
        # The intermediate m2m model is not auto created if:
        #  1) There is a manually specified intermediate, or
        #  2) The class owning the m2m field is abstract.
        #  3) The class owning the m2m field has been swapped out.
        auto_intermediate = False
        if not self.rel.through and not cls._meta.abstract and not cls._meta.swapped:
            auto_intermediate = True
        
        #One call super contribute_to_class and have django create the intermediate model.
        super(OneToManyField, self).contribute_to_class(cls, name)

        if auto_intermediate == True:
            #Set unique_together to the 'to' relationship, this ensures a OneToMany relationship.
            self.rel.through._meta.unique_together = ((self.rel.through._meta.unique_together[0][1],),)
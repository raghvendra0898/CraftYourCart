from django.db import models


from django.urls import reverse


class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=250, unique=True)


    class Meta:
        #By default Django creates model of the form Categorys
        # so here we used verbose to define the name manually
        verbose_name_plural = 'categories'


    def __str__(self):
        #By default when its object is created it is of the form Category(1)
        # by using this function we return the name of the object created as its title
        return self.name


    def get_absolute_url(self):

        return reverse('list-category', args=[self.slug])



class Product(models.Model):

    #FK 

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)


    title = models.CharField(max_length=250)

    brand = models.CharField(max_length=250, default='un-branded')

    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=255)

    price = models.DecimalField(max_digits=4, decimal_places=2)

    image = models.ImageField(upload_to='images/')


    class Meta:

        verbose_name_plural = 'products'


    def __str__(self):

        return self.title



    def get_absolute_url(self):

        return reverse('product-info', args=[self.slug])





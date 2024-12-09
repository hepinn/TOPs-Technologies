# from django.db import models

# class Product(models.Model):
# 	name=models.CharField(max_length=50)
# 	price=models.IntegerField(default=0)
# 	description=models.CharField(max_length=200, default="")
# 	image=models.ImageField(upload_to='products/')


# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     image=models.ImageField(upload_to='products/')

#     @staticmethod
#     def get_all_product():
#     	return Product.objects.all()




from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Other fields as needed
    
    def __str__(self):
        return self.name



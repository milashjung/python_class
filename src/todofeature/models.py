from django.db import models
class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)#you don't have 
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True



class Category(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Priority(models.TextChoices):
    LOWEST ="lowest", "Lowest"
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"
    HIGHEST = "highest","Highest"


class Task(TimestampModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="todoimage",blank=True, null=True)
    task_date = models.DateField(blank=True, null=True)  
    priority = models.CharField(
        max_length=100,
        choices=Priority.choices,
        default=Priority.LOWEST
    )    

    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank=True, 
        null=True
        
    )
    Label = models.ManyToManyField(Label, blank=True)

    def __str__(self):
        return self.name 

from django.db import models

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = ''
        managed = True
        verbose_name_plural = 'Posts'

    def __str__(self) -> str:
        return (f"{self.title} by {self.author}").__str__()
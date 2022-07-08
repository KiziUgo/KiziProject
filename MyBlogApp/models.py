from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from django.contrib.contenttypes.fields import GenericRelation
from PIL import Image
from users.models import Profile
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils.timezone import utc



class PostWelcome(models.Model):
      title = models.CharField(max_length=100)
      img = models.ImageField(null=True, blank=True, upload_to='pics')
      content = RichTextField(blank=True, null=True)
      date_posted = models.DateTimeField(auto_now_add=True)
      author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
      likes = models.ManyToManyField(User, related_name='blog_posts')
      unlikes = models.ManyToManyField(User, related_name='blog_unlike_posts')

      def total_likes(self):
            return self.likes.count()

      def total_unlikes(self):
            return self.unlikes.count()

      def __str__(self):
            return self.title



class PostCars(models.Model):
      topic = models.CharField(max_length=100, null=True)
      imge = models.ImageField(null=True, blank=True, upload_to='pics')
      content = RichTextField(blank=True, null=True)
      body = RichTextField(blank=True, null=True)
      date = models.DateTimeField(auto_now_add=True)
      name = models.CharField(max_length=200, null=True)
      by = models.ForeignKey(User, on_delete=models.CASCADE)
      likescars = models.ManyToManyField(User, related_name='blog_postscars')
      unlikescars = models.ManyToManyField(User, related_name='blog_unlike_postscars')
      access_code = models.IntegerField(null=True, blank=True)

      now = datetime.now()
      hour = int(now.strftime("%H"))
      min = int(now.strftime("%M"))


      def total_likescars(self):
            return self.likescars.count()

      def total_unlikescars(self):
            return self.unlikescars.count()

      def __str__(self):
            return self.topic

      def save(self, *args, **kwargs):
               refresh = 0
               durationToWait = datetime.now()
               durationHour = int(durationToWait.strftime("%H"))
               durationMin = int(durationToWait.strftime("%M"))
               numOfPost = PostCars.objects.filter(by=self.by).count()
               totalPost = int(numOfPost)
               timeInHour = durationHour
               timeInMin = durationMin


               if totalPost < 1:

                        return super(PostCars, self).save(*args, **kwargs)

               elif timeInHour == 2 and timeInMin >= 10:
                        return super(PostCars, self).save(*args, **kwargs)
               else:
                        raise ValidationError("please re-subscribe ")





      def get_absolute_url(self):
            return reverse('MyBlogApp:carpost-postcars_detail', kwargs={'pk': self.pk})


class PostTech(models.Model):
      title = models.CharField(max_length=100)
      img = models.ImageField(null=True, blank=True, upload_to='pics')
      content = RichTextField(blank=True, null=True)
      date = models.DateTimeField(auto_now_add = True)
      author = models.ForeignKey(User, on_delete = models.CASCADE)
      likestech = models.ManyToManyField(User, related_name='blog_poststech')
      unlikestech = models.ManyToManyField(User, related_name='blog_unlike_poststech')

      def total_likestech(self):
            return self.likestech.count()

      def total_unlikestech(self):
            return self.unlikestech.count()

      def __str__(self):
            return self.title

      def get_absolute_url(self):
            return reverse('MyBlogApp:techpost-posttech_detail', kwargs={'pk': self.pk})




@property
def commentsCars(self):
      return self.commentsCars.all()

class CommentCarPosts(models.Model):
      postcars = models.ForeignKey(PostCars, related_name='commentsCar', on_delete=models.CASCADE, default=None, blank=True ,null=True,)
      name = models.CharField(max_length=255)
      content = models.TextField()
      timestampCars = models.DateTimeField(auto_now_add = True)
      parentCars = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='repliesCars')

      class Meta:
            ordering = ['-timestampCars']

      def __str__(self):
            return 'CommentCars {} by {}' .format(self.content, self.name)





@property
def commentsTech(self):
      return self.commentsTech.all()

class CommentTechPosts(models.Model):
      posttech = models.ForeignKey(PostTech, related_name='commentsTech', on_delete=models.CASCADE, default=None, blank=True ,null=True,)
      name = models.CharField(max_length=255)
      content = models.TextField()
      timestampTech = models.DateTimeField(auto_now_add = True)
      parentTech = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='repliesTech')

      class Meta:
            ordering = ['-timestampTech']

      def __str__(self):
            return 'CommentTech {} by {}' .format(self.content, self.name)













































from django.contrib import admin
from .models import PostCars, CommentCarPosts, PostTech, CommentTechPosts,PostWelcome

admin.site.register(PostCars)
admin.site.register(CommentCarPosts)
admin.site.register(CommentTechPosts)
admin.site.register(PostTech)
admin.site.register(PostWelcome)






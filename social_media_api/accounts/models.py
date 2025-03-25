# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.conf import settings

# class CustomUser(AbstractUser):
#     bio = models.TextField(max_length=500, blank=True)
#     profile_picture = models.ImageField(
#         upload_to='profile_pics/', 
#         null=True, 
#         blank=True
#     )
    
#     followers = models.ManyToManyField(
#         'self', 
#         symmetrical=False, 
#         related_name='following_users', 
#         blank=True
#     )

#     def follow(self, user):
#         """
#         Follow another user
#         """
#         if user != self:
#             self.following_users.add(user)

#     def unfollow(self, user):
#         """
#         Unfollow a user
#         """
#         self.following_users.remove(user)

#     def is_following(self, user):
#         """
#         Check if the current user is following another user
#         """
#         return self.following_users.filter(pk=user.pk).exists()

#     def get_followers_count(self):
#         """
#         Get the number of followers
#         """
#         return self.followers.count()

#     def get_following_count(self):
#         """
#         Get the number of users this user is following
#         """
#         return self.following_users.count()

#     def __str__(self):
#         return self.username

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', 
        null=True, 
        blank=True
    )
    
    followers = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='following',  
        blank=True
    )

    def follow(self, user):
        """
        Follow another user
        """
        if user != self:
            self.following.add(user) 

    def unfollow(self, user):
        """
        Unfollow a user
        """
        self.following.remove(user)  

    def is_following(self, user):
        """
        Check if the current user is following another user
        """
        return self.following.filter(pk=user.pk).exists() 

    def get_followers_count(self):
        """
        Get the number of followers
        """
        return self.followers.count()

    def get_following_count(self):
        """
        Get the number of users this user is following
        """
        return self.following.count()  

    def __str__(self):
        return self.username
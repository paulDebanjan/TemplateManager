from django.db import models
from PIL import Image as ImageTool

class HomeDesign(models.Model):
    webSiteName = models.CharField(max_length=75 ,null=False, blank=False)
    webSiteNameSize = models.IntegerField(null=True)
    webSiteCommit = models.CharField(max_length=75 ,null=True)
    webSiteCommitSize = models.IntegerField(null=True)
    backbroundImage = models.ImageField(upload_to='homePageImage/',max_length=250, null=True, default=None, blank=True)
    logoColor = models.CharField(max_length=6, default="004500", null=True)

    def __str__(self):
        return str(self.webSiteName)
    
class About(models.Model):
    title = models.CharField(max_length=75 ,null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.title)


class NavbarOption(models.Model):
    name = models.CharField(max_length=75 ,null=False, blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    menu = models.ForeignKey(NavbarOption, on_delete=models.CASCADE)
    title = models.CharField(max_length=250 ,null=False, blank=False, unique=False)
    pragraphOne = models.TextField(blank=True)
    main_image = models.ImageField(upload_to='postsImages/',max_length=250, null=True, default=None, blank=True)
    pragraphTwo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.title)

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
    photo = models.ImageField(upload_to ='postsImages/')

    def save(self, *args, **kwargs): 
       super(Image, self).save(*args, **kwargs)
       img = ImageTool.open(self.photo.path)
       if img.height > 1125 or img.width > 1125:
           img.thumbnail((1125,1125))
       img.save(self.photo.path,quality=70,optimize=True)
       
    
    # def get_posts_extra_photo(self, *args, **kwargs):
    #     return self.post.navbar_option == *args
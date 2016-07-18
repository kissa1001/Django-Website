from django.db import models

class Album(models.Model):
	artist = models.Charfield(max_length = 250)
	album_title = models.Charfield(max_length = 500)
	genre = models.Charfield(max_length = 100)
	album_logo = models.Charfield(max_length = 1000)

class Song(models.Model):
	album - models.ForeignKey(Album, on_delete = models.CASCADE)
	file_type = models.Charfield(max_length = 10)
	song_title = models.Charfield(max_length = 250)
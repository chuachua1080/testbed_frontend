from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    attrs = models.CharField(max_length=300)
    start_time = models.CharField(max_length=30)
    end_time = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name
class Topology(models.Model):
    name = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    project = models.ForeignKey(Project)
    attrs = models.CharField(max_length=300)
    def __unicode__(self):
        return self.name

class Device(models.Model):
    name=models.CharField(max_length=30)
    topology= models.ForeignKey(Topology)
    type=models.CharField(max_length=30)
    pos= models.CharField(max_length=60)
    def __unicode__(self):
        return self.name
class OVS(models.Model):
    name=models.CharField(max_length=30)
    topology= models.ForeignKey(Topology)
    type=models.CharField(max_length=30)
    pos= models.CharField(max_length=60)
    def __unicode__(self):
        return self.name
class Connection(models.Model):
    source=models.CharField(max_length=30)
    target=models.CharField(max_length=30)
    bandwidth=models.CharField(max_length=30)
    delay=models.CharField(max_length=30)
    note=models.CharField(max_length=600)
    topology=models.ForeignKey(Topology)
    def __unicode__(self):
        return self.source

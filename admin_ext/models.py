from django.db import models
from django.contrib.auth.models import User
import datetime

"""
This is a task to assign tasks to users on the admin panel
"""
class Task( models.Model ) :
    
    name = models.CharField( max_length = 500, default = "", blank = False )
    description = models.CharField( max_length = 500, default = "", blank = True )
    date_end = models.DateTimeField( blank = False )
    
    value = models.IntegerField( default = 0, blank = True )
    state = models.IntegerField( default = 1, blank = True )
    
    user = models.ForeignKey( User, related_name="master" )
    user_assigned = models.ForeignKey( User, related_name="assigned_user" )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        """ this returns a string that represents the model """
        return self.name
        
    def  get_tasks_not_done_by_duedate( self, user ) :
        """ this will return the tsask created by user not done by due time """
        return Task.objects.filter( user = user.id, date_end__gte = datetime.datetime.now() )
from django.db import models

import datetime
from django.utils import timezone

''' Status Choices for change control '''
STATUS_CHOICES = (
    ('a', 'Active'),
    ('p', 'Pending'),
    ('d', 'Delete'),
    ('u', 'Unverified'),
)


class ProductionTable(models.Model):
    """Build abstract class to inherit production table information for viewing and editing
    """


class TempTable(ProductionTable):
    """This will build the temp production table for change control. Users will approve and write into this table.
       Admin will then have the opportunity to approve or deny change to push to production
    """
    
    #Replicate production table columns


    TempItemID = models.AutoField(primary_key = True)
    Status = models.CharField(max_length = 1, choices=STATUS_CHOICES)
    Comment = models.TextField()

    class Meta:
        "Allow for scalability. Overwrite and dynamically create new table name according to application name.
        db_table = '{0}_{1}'.format() 

    def change_attributes(self):
        "Returns the attributes of change request by looking at ChangeControl status"

    def save(self):
        "Add additional actions when saving results within scope"
        do_something #Like movving data to production and emailing BI
        super(ChangeControl, self).save()   #Call the real save method
        do_something_else


class ChangeControl(models.Model):
    """This will build change control tracking table. Every new change instance will be written into this table
       for review. Once approved, Temp table will be updated
    """

    ChangeID = models.AutoField(primary_key = True)
    TempItemID =  models.ForeignKey(TempTable)
    InitiatorFirstName = models.CharField(max_length = 25)
    InitiatorLastName = models.CharField(max_length = 25)
    GroupName = models.CharField(max_length = 25)
    InitiateTime = DateTimeField()

    ##Need to bring in table option
    #TableItems_Old
    #TableItems_New
    Status = models.CharField(max_length = 1, choices=STATUS_CHOICES)

    class Meta:
        db_table = '{0}_{1}'.format()

    def change_status(self):
        "Returns the status of change request by looking at Committees status"

    def save(self):
        "Add additional actions when saving results within scope"
        do_something #Like movving data to temp enviornment and emailing Admin
        super(ChangeControl, self).save()   #Call the real save method
        do_something_else



class ChangeControlCommittee(models.Model):
    """This will keep track of relevant decision makers of a committee along with the admin. Once proper approval is
       passed, change control items will be sent to temp table for admin review. Admin will be reviewing both steps of
       process to ensure data is accurate.
    """

    ID = models.AutoField(primary_key = True)
    ChangeID =  models.ForeignKey(ChangeControl)
    GroupName = models.CharField(max_length = 25)
    MemberFirstName = models.CharField(max_length = 25)
    MemberLastName =models.CharField(max_length = 25)
    isAdmin = NullBooleanField()
    RespondTime = DateTimeField()
    Status = models.CharField(max_length = 1, choices=STATUS_CHOICES)
    Comment = models.TextField()

    class Meta:
        db_table = '{0}_{1}'.format()


    def save(self):
        "Add additional actions when saving results within scope"
        do_something #Like movving data to temp enviornment and emailing Admin
        super(ChangeControlCommittee, self).save()   #Call the real save method
        do_something_else
    
    
    

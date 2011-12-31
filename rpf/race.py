from django.db import models

class race( models.Model ):
    id = models.AutoField( primary_key = True )
    create_dtm = models.DateTimeField(verbose_name="Date created",
                                      db_index=False)
    name = models.CharField( max_length = 30,
                             db_index=False)

    def __unicode__( self ):
        return self.name

    class Meta:
        db_table = 'rpf_race'
        app_label= 'rpf'

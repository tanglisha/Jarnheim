from django.db import models

class guild( models.Model ):
    id = models.AutoField( primary_key = True )
    guild_leader_character = models.ForeignKey( 'character' )
    create_dtm = models.DateTimeField(verbose_name="Date created",
                                      db_index=False)
    name = models.CharField( max_length = 30 )
    

    def __unicode__( self ):
        return self.name

    class Meta:
        db_table = 'rpf_guild'
        app_label= 'rpf'

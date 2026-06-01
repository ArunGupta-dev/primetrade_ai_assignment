from CoreUtils.Logger import Logger
from trade_notes.utils.serializer import trade_notes_serializer
from trade_notes.models import trade_notes

class Trading_notes_handler():

    def __init__(self, user):
        self.user = user
        self.createLog = Logger()




    def create_note(self, data):

        try:
            serializer = trade_notes_serializer(data = data)

            if serializer.is_valid():
                serializer.save(author=self.user)
                return "created"
            else:
                self.createLog.Log_Debug('created_note_serializer_invalid', serializer.errors)
                return "not-created"

        except Exception as e:
            self.createLog.Log_Error('Trade_note_handler_Exception', e)
            return "error"




    def update_note(self, data):
        try:
            note_instance = trade_notes.objects.get(note_id = data['note_id'])

            if note_instance.author != self.user and not self.user.is_staff:
                return "no-permission"

            serializer = trade_notes_serializer(note_instance, data = data, partial= True)

            if serializer.is_valid():
                serializer.save(author=self.user)
                return "updated"
            
            else:
                return "not-updated"

        except Exception as e:
            self.createLog.Log_Error('Trade_notes_handler_Exception', e)
            return "error"


    def delete_note(self, data):
        try:
            note_instance = trade_notes.objects.get(note_id=data['note_id'])
            if note_instance.author != self.user and not self.user.is_staff:
                return "no-permission"

            note_instance.delete()
            return "deleted"
        
        except Exception as e:
            self.createLog.Log_Error('Trade_notes_handler_delete_note_Exception', e)
            return "error"





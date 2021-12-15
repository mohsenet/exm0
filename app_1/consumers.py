from channels.generic.websocket import WebsocketConsumer
from django.utils.safestring import mark_safe


def get_list(path, this_section):
    state = 2
    list_data = []
    with open(path, "r") as filehandler:
         for i in filehandler:
             if state <= 1:
                 if i == '\n':
                     break
                 cur = i[:-1]
                 list_data.append(cur)
             if i == this_section:
                 state = state - 1
    return list_data


class EchoInfo(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        data = get_list('/home/mohsen/Dropbox/_2021/core.txt', ('[' + text_data + ']' + '\n'))

        d = ''
        for i in data:
            d += i + '\n'

        self.send(text_data=d)


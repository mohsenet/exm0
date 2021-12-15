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

        selected_data = ''
        index = text_data.find('/')
        if index != -1:
            # selected data
            selected_data = '#' + text_data[index + 1:]
            # subject
            text_data = text_data[:text_data.find('/')]

        data = get_list('/home/mohsen/Dropbox/_2021/core.txt', ('[' + text_data + ']' + '\n'))

        if selected_data != '':
            selected_d = ''
            read_status = '1'
            for i in data:
                if i == selected_data:
                    read_status = '0'
                if read_status == '0':
                    selected_d += i + '\n'
                    if i == '#':
                        break
            self.send(text_data=selected_d)
        else:
            d = ''
            for i in data:
                d += i + '\n'

            self.send(text_data=d)


# To run this code:

# Connect to internet
# Create virtual environment
# Activate virtual environment

# After that, then
# Just pip install sentence-transformers scikit-learn, kivy
# Run interface.py (python interface.py)

# U can make your own dataset, that it's format should look like the dialogs.txt or the self.data variable
# U can contact me 0981254727 on whatsApp if, U want to understand a little bit more.


from kivy.uix.accordion import BooleanProperty
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from wargebot import WargeBot
from kivy.clock import Clock

class ChatBubble(BoxLayout):
    text = StringProperty("")
    is_user = BooleanProperty(False)

class ChatScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(ChatScreen, self).__init__(**kwargs)
        self.bot = WargeBot()
        self.bot.load_dataset()

        self.add_message("Hello, am WargeBot,  jakwsjdas aijsjcx ascnasc ascjas casicas casijjc ascaisc ascaisc ascaisca scodcnsc asdc I answer basic health questions, am still learning, so please go easy on me", False)

    def send_message(self):
        user_text = self.ids.user_input.text.strip()
        if not user_text:
            return

        self.add_message(user_text, True)
        self.ids.user_input.text = ""

        response = self.bot.get_response(user_text)
        self.type_message(response, False)

    def add_message(self, message, is_user=False):
        bubble = ChatBubble(text=message, is_user=is_user)
        self.ids.chat_box.add_widget(bubble)

        

    def type_message(self, message, is_user=False):
        self.current_text = ""
        self.full_text = message
        self.bubble = ChatBubble(text="", is_user=is_user)

        self.ids.chat_box.add_widget(self.bubble)

        self.index = 0
        Clock.schedule_interval(self.update_text, 0.03)

        self.ids.scroll.scroll_y = 0

    def update_text(self, dt):
        if self.index < len(self.full_text):
            self.current_text += self.full_text[self.index]
            self.bubble.text = self.current_text
            self.index += 1
        else:
            return False 


class ChatApp(App):
    def build(self):
        self.title = "WargeBot"
        self.icon = "logoEdt.jpg"
        return ChatScreen()


if __name__ == "__main__":
    ChatApp().run()
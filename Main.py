from kivy.app import App
from kivy.uix.label import Label

class VoiceAssistantApp(App):
    def build(self):
        return Label(text="Hello! My Voice Assistant.")

if __name__ == '__main__':
    VoiceAssistantApp().run()
  

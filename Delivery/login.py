from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton

class Login(MDApp):
    def background(self): # Background 
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.5
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

if __name__=="__main__":
    Login().run()
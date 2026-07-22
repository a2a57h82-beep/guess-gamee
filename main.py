from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Game(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.secret = ""
        self.attempts = 0
        self.setting_secret = True

    def check(self):
        text = self.ids.guess.text

        if len(text) != 4:
            self.ids.result.text = "أدخل رقم من 4 خانات"
            return

        # أول مرة: حفظ الرقم السري
        if self.setting_secret:
            self.secret = text
            self.setting_secret = False
            self.ids.guess.text = ""
            self.ids.result.text = "تم حفظ الرقم السري، الآن ابدأ التخمين"
            return

        # التخمين
        self.attempts += 1

        if text == self.secret:
            self.ids.result.text = f"🎉 مبروك!\nعدد المحاولات: {self.attempts}"
            self.setting_secret = True
            self.attempts = 0
            self.ids.guess.text = ""
            return

        result = ""

        for i in range(4):
            if text[i] == self.secret[i]:
                result += f"الخانة {i+1}: ✅ صحيح\n"
            else:
                result += f"الخانة {i+1}: ❌ خطأ\n"

        self.ids.result.text = result
        self.ids.guess.text = ""


class GuessApp(App):
    def build(self):
        return Game()


if __name__ == "__main__":
    GuessApp().run()
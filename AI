import pyttsx3
import speech_recognition as sr

class AI():
    __name = ""
    __skills = []

    def __init__(self, name=None):
        self.engine = pyttsx3.init("sapi5")
        cs_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_csCZ_Jakub"
        self.engine.setProperty('voice', cs_voice_id)
        voicespeed = 180
        self.engine.setProperty('rate', voicespeed)
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        if name is not None:
            self.__name = name

        print("Poslouchám")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        sentence = "Ahoj, jmenuji se" + self.__name
        self.engine.say(sentence)
        self.engine.runAndWait()

    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()

    def listen(self):
        print("Řekni něco")
        with self.m as source:
            audio = self.r.listen(source)
        print("Mám to.")
        try:
            phrase = self.r.recognize_google(audio, show_all=False, language="cs-CZ")
            sententce = "Řekl jsi" + phrase
            self.engine.say(sententce)
            self.engine.runAndWait()
        except:
            print("Omlouvám se, nestihl jsem to.")
            self.engine.say("Omlouvám se, nestihl jsem to.")
            self.engine.runAndWait()


#parte 1 - importar bibliotecas
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib
# import pyaudio

#parte 2 -configuracao geral
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def cuprimento ():
    hora = int(datetime.datetime.now().hour)
    if hora>5 and hora<12:
        speak("Bom dia")
    elif hora>=12 and hora<18:
        speak("Boa tarde")
    else:
        speak("Boa noite")
    
    speak("Eu me chamo Jarvis, como posso lhe ajudar?")

cuprimento()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt-in')
        print(f"voce disse: {query}\n")

    except Exception as e:
        print("Repita novamente, por favor...")
        return "None"

    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
    
        if 'abrir google' in query:
            #webbrowser.open("google.com") 
            url = "google.com"
            webbrowser.register('chrome',
            None,
            # webbrowser.BackgroundBrowser("D://launcher.exe"))
            webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open_new(url)
        
        elif 'abrir spotify' in query:
            url = "open.spotify.com"
            webbrowser.register('spotify',
            None,
            # webbrowser.BackgroundBrowser("D://launcher.exe"))
            webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('spotify').open_new(url)

        elif 'fechar programa' in query:
            speak("Até a próxima, tchau")
            break
        
        elif 'horas por favor' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"São exatamente {strTime}")

        elif 'abrir documento' in query:
            diretorio_documento = "D://documentos"
            os.startfile(diretorio_documento)
        
        elif 'abrir mapa' in query:
            speak("Que local você deseja olhar no mapa?")
            query = takeCommand().lower()
            location = query
            speak("Aguarde um instante, estou abrindo o google maps com a localização de"+location)
            webbrowser.open("https://www.google.com.br/maps/place/"+location)
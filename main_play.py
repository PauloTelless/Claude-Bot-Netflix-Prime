from command_open_netflix import abrir_netflix_login
from command_open_amazon_prime import abrir_amazon_prime
import speech_recognition as sr


while True:
    rec = sr.Recognizer()
    with sr.Microphone(2) as mic:
        rec.adjust_for_ambient_noise(mic)
        print('Fala permitida')
        try:
            audio = rec.listen(mic)   
            texto = str(rec.recognize_google(audio, language='pt-BR')).lower()    
        
            if texto == 'abrir netflix':
                abrir_netflix_login()
                
            elif texto == 'abrir prime':
                abrir_amazon_prime()
        
        except sr.UnknownValueError:
            print('Bot: Não entendi, fale novamente.')
    
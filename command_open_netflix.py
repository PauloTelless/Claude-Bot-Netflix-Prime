from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
import speech_recognition as sr
import time
from commands import passar_proximo_episodio, pausar_episodio, pular_abertura, pular_resumo, mutar_episodio, desmutar_episodio, despausar_episodio,sair_episodio, sair_tela_cheia, colocar_tela_cheia, avancar_dez_segundos, voltar_dez_segundos, email, senha


def abrir_netflix_login():
    try:
        service = Service(ChromeDriverManager().install())

        navegador = webdriver.Chrome(service=service)

        navegador.get('https://www.netflix.com/br/login')
        time.sleep(1)
        navegador.find_element(By.ID, 'id_userLoginId').send_keys(email)

        navegador.find_element(By.ID, 'id_password').send_keys(senha)

        navegador.find_element(By.CSS_SELECTOR, 'button.btn.login-button.btn-submit.btn-small').click()

        time.sleep(1)
        navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a').click()
        time.sleep(1)
        navegador.find_element(By.CSS_SELECTOR, '[data-uia="pin-number-0"]').send_keys('1')
        navegador.find_element(By.CSS_SELECTOR, '[data-uia="pin-number-1"]').send_keys('9')
        navegador.find_element(By.CSS_SELECTOR, '[data-uia="pin-number-2"]').send_keys('6')
        navegador.find_element(By.CSS_SELECTOR, '[data-uia="pin-number-3"]').send_keys('1')    
        
        while True:
            rec = sr.Recognizer()
            with sr.Microphone(2) as mic:
                rec.adjust_for_ambient_noise(mic)
                print('Bot: Fala permitida.')
                try:
                    audio = rec.listen(mic)   
                    texto = str(rec.recognize_google(audio, language='pt-BR')).lower()
                     
                    if texto == 'próximo episódio':
                        passar_proximo_episodio(navegador=navegador)
                        
                    elif texto == 'pular abertura':
                        pular_abertura(navegador=navegador)
                        
                    elif texto == 'pular resumo':
                        pular_resumo(navegador=navegador)
                        
                    elif texto == 'pause':
                        pausar_episodio(navegador=navegador)
                        
                    elif texto == 'continuar':
                        despausar_episodio(navegador=navegador)
                    
                    elif texto == 'mudo':
                        mutar_episodio(navegador=navegador)
                    
                    elif texto == 'áudio':
                        desmutar_episodio(navegador=navegador)
                    
                    elif texto == 'tela cheia':
                        colocar_tela_cheia(navegador=navegador)
                    
                    elif texto == 'tela normal':
                        sair_tela_cheia(navegador=navegador)
                    
                    elif texto == 'avançar':
                        avancar_dez_segundos(navegador=navegador)
                    
                    elif texto == 'voltar':
                        voltar_dez_segundos(navegador=navegador)
                    
                    elif texto == 'saia':
                        sair_episodio(navegador=navegador)
                    
                    elif texto == 'sair netflix':
                        navegador.quit()
                        
                except sr.UnknownValueError:
                    print('Bot: Não entendi, fale novamente.')
            
    except KeyboardInterrupt:
        # Se o usuário pressionar Ctrl+C (KeyboardInterrupt), encerrar o programa
        print("Programa encerrado pelo usuário.")
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        
    finally:
        # Fechar o navegador ao encerrar o programa
        navegador.quit()
        
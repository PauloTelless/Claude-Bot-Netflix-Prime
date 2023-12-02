from selenium.webdriver.common.by import By
import time
email = ''
senha = ''

def passar_proximo_episodio(navegador):
    #passa para o próximo episódio
    navegador.find_element(By.CLASS_NAME, 'watch-video').click()
    time.sleep(1)
    navegador.find_element(By.CSS_SELECTOR, '[data-uia="control-next"]').click()
      
        
def pular_abertura(navegador):
    #pular abertura
    navegador.find_element(By.CSS_SELECTOR, '[data-uia="player-skip-intro"]').click()
    
    
def pausar_episodio(navegador):
    #pausa o episódio
    navegador.find_element(By.CSS_SELECTOR, '[data-uia="watch-video"]').click()
    
            
def despausar_episodio(navegador):
    #tira o pause do episódio
    navegador.find_element(By.CSS_SELECTOR, '[data-uia="watch-video"]').click()
    time.sleep(1)
    navegador.find_element(By.CSS_SELECTOR, '[data-name="Play"]').click()
    

def mutar_episodio(navegador):
    #tira o áudio do episódio em reprodução
    navegador.find_element(By.CLASS_NAME, 'watch-video').click()
    time.sleep(1)
    navegador.find_element(By.CSS_SELECTOR, '[data-name="VolumeHigh"]').click()


def sair_episodio(navegador):
    #sai do episódio  
    navegador.find_element(By.CLASS_NAME, 'watch-video').click()
    time.sleep(1)
    navegador.find_element(By.CSS_SELECTOR, '[data-name="ArrowLeft"]').click()
    
    
def desmutar_episodio(navegador):
    #retorna o áudio da reprodução
    navegador.find_element(By.CLASS_NAME, 'watch-video').click()
    time.sleep(1.2)
    navegador.find_element(By.CSS_SELECTOR, '[data-name="VolumeOff"]').click()
    
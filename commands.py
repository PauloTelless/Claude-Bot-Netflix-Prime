from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
email = 'tellespedro257@gmail.com'
senha = 'Paulinhogostoso12'


def passar_proximo_episodio(navegador):
    try:
        #passa para o próximo episódio
        navegador.find_element(By.CLASS_NAME, 'watch-video').click()
        time.sleep(1)
        navegador.find_element(By.CSS_SELECTOR, '[data-uia="control-next"]').click()
    except NoSuchElementException:
        print('Elemento não encontrado')    
      
        
def pular_abertura(navegador):
    try:
        #pular abertura
        navegador.find_element(By.CSS_SELECTOR, '[data-uia="player-skip-intro"]').click()
    except (NoSuchElementException, StaleElementReferenceException) as e:
        print(f'Elemento não encontrado. Excessão: {e}')    
    
    
def pular_resumo(navegador):
    try:
        #pula resumo do episódio anterior, se houver
        navegador.find_element(By.CSS_SELECTOR, '[data-uia="player-skip-recap"]').click()
    except (NoSuchElementException, StaleElementReferenceException) as e:
        print(f'Elemento não encontrado. Excessão: {e}')
    

def pausar_episodio(navegador):
    try:
        #pausa o episódio
        navegador.find_element(By.CSS_SELECTOR, '[data-uia="watch-video"]').click()
    except (NoSuchElementException, StaleElementReferenceException) as e:
        print(f'Elemento não encontrado. Excessão: {e}')    
            
def despausar_episodio(navegador):
    try:
        #tira o pause do episódio
        navegador.find_element(By.CSS_SELECTOR, '[data-uia="watch-video"]').click()
        time.sleep(1)
        navegador.find_element(By.CSS_SELECTOR, '[data-name="Play"]').click()
    except (NoSuchElementException, StaleElementReferenceException) as e:
        print(f'Elemento não encontrado. Excessão: {e}')    


def mutar_episodio(navegador):
    try:
        #tira o áudio do episódio em reprodução
        navegador.find_element(By.CLASS_NAME, 'watch-video').click()
        time.sleep(1)
        navegador.find_element(By.CSS_SELECTOR, '[data-name="VolumeHigh"]').click()
        navegador.find_element(By.CSS_SELECTOR, '[data-name="Play"]').click()
    except (NoSuchElementException, StaleElementReferenceException) as e:
        print(f'Elemento não encontrado. Excessão: {e}')


def sair_episodio(navegador):
    try:
        #sai do episódio  
        navegador.find_element(By.CLASS_NAME, 'watch-video').click()
        time.sleep(1)
        navegador.find_element(By.CSS_SELECTOR, '[data-name="ArrowLeft"]').click()
    except (NoSuchElementException, StaleElementReferenceException) as e:
        print(f'Elemento não encontrado. Excessão: {e}')    
    
    
def desmutar_episodio(navegador):
    try:
        #retorna o áudio da reprodução
        navegador.find_element(By.CLASS_NAME, 'watch-video').click()
        time.sleep(1.2)
        navegador.find_element(By.CSS_SELECTOR, '[data-name="VolumeOff"]').click()
        navegador.find_element(By.CSS_SELECTOR, '[data-name="Play"]').click()
    except (NoSuchElementException, StaleElementReferenceException) as e:
        print(f'Elemento não encontrado. Excessão: {e}') 
           
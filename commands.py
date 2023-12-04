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
        navegador.find_element(By.CSS_SELECTOR, '[data-uia="watch-video"]').click()
        #pular abertura
        navegador.find_element(By.CSS_SELECTOR, '[data-uia="player-skip-intro"]').click()
        navegador.find_element(By.CSS_SELECTOR, '[data-name="Play"]').click()
        
        
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
        

def colocar_tela_cheia(navegador):
    try:
        #coloca o episódio em reprodução em tela cheia
        navegador.find_element(By.CLASS_NAME, 'watch-video').click()
        navegador.find_element(By.CSS_SELECTOR, '[data-uia="control-fullscreen-enter"]').click()
        time.sleep(0.5)
        navegador.find_element(By.CSS_SELECTOR, '[data-name="Play"]').click()
        
    except (NoSuchElementException, StaleElementReferenceException) as e:
        print(f'Elemento não encontrado. Excessão: {e}')
    

def sair_tela_cheia(navegador):
    try:
        #sair do modo tela cheia 
        navegador.find_element(By.CLASS_NAME, 'watch-video').click()
        navegador.find_element(By.CSS_SELECTOR, '[data-uia="control-fullscreen-exit"]').click()
        time.sleep(0.5)
        navegador.find_element(By.CSS_SELECTOR, '[data-name="Play"]').click()
        
    except (NoSuchElementException, StaleElementReferenceException) as e:
        print(f'Elemento não encontrado. Excessão: {e}')


def avancar_dez_segundos(navegador):
    try:
        #avança 10 segundo de um episódio/capítulo em reprodução"
        navegador.find_element(By.CLASS_NAME, 'watch-video').click()
        navegador.find_element(By.CSS_SELECTOR, '[data-name="Forward10"]').click()
        navegador.find_element(By.CSS_SELECTOR, '[data-name="Play"]').click()
        
    except (NoSuchElementException, StaleElementReferenceException) as e:
        print(f'Elemento não encontrado. Excessão: {e}') 


def voltar_dez_segundos(navegador):
    try:
        #volta 10 segundos de um episódio/capítulo em um reprodução
        navegador.find_element(By.CLASS_NAME, 'watch-video').click()
        navegador.find_element(By.CSS_SELECTOR, '[data-name="Back10"]').click()
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
           
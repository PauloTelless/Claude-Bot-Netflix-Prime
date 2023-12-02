from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
import speech_recognition as sr
import time

def abrir_amazon_prime():
    service = Service(ChromeDriverManager().install())

    navegador = webdriver.Chrome(service=service)

    navegador.get('https://www.primevideo.com/offers/nonprimehomepage/ref=dv_web_force_root?_encoding=UTF8&language=pt_BR')
    navegador.find_element(By.CLASS_NAME, 'dv-overlay').click()
    navegador.find_element(By.ID, 'ap_email').send_keys('ptelles020@gmail.com') 
    navegador.find_element(By.CLASS_NAME, 'a-button-inner').click()
    navegador.find_element(By.ID, 'ap_password').send_keys('Paulinhogostoso1!')
    navegador.find_element(By.ID, 'signInSubmit').click()

    #passa o episódio
    navegador.find_element(By.CSS_SELECTOR, 'div.ffszj3z.f8hspre.f1icw8u').click()
    navegador.find_element(By.CSS_SELECTOR, 'div.fiqc9rt.f17ept9u').click()

    #passa a abertura 
    navegador.find_element(By.CSS_SELECTOR, 'div.button.fqye4e3.f1ly7q5u.fk9c3ap.fz9ydgy.f1xrlb00.f1hy0e6n.fgbpje3.f1uteees.f1h2a8xb.atvwebplayersdk-skipelement-button.f1cg7427.fiqc9rt.fg426ew.f1ekwadg').click()

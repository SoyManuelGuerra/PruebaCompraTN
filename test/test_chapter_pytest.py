import time
from utils.funciones import *
from config.credentials import *

options = webdriver.ChromeOptions()


service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

utilidades = UtilidadesPruebas(driver)
utilidades.cargar_pagina(login_url)
utilidades.click_btn(Selectores.cookies_btn)
utilidades.click_btn(Selectores.agregar_carrito)
utilidades.click_btn(Selectores.ver_carrito)
utilidades.click_btn(Selectores.iniciar_compra)
utilidades.ingresar_txt(Selectores.email_input, email)
utilidades.ingresar_txt(Selectores.cp_input, codigo_postal)
utilidades.click_btn(Selectores.continuar_1)
utilidades.ingresar_txt(Selectores.first_name, nombre)
utilidades.ingresar_txt(Selectores.last_name, apellido)
utilidades.ingresar_txt(Selectores.address, calle)
utilidades.ingresar_txt(Selectores.number_address, numero)
utilidades.ingresar_txt(Selectores.departament_address, departamento)
utilidades.ingresar_txt(Selectores.localidad, barrio)
utilidades.click_btn(Selectores.continuar_compra)
utilidades.cambiar_a_iframe(Selectores.iframe_transferencia)
utilidades.click_btn(Selectores.transferencia_btn)
utilidades.ingresar_txt(Selectores.documento_comprador, DNI)
#utilidades.scrol(driver.execute_script("window.scrollBy(0, 1000);"))
utilidades.click_btn(Selectores.compra_final_btn)
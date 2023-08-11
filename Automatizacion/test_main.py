from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
 # La variable Nav. es Navegador abreviado.
class Test1(unittest.TestCase):
    def setUp(nav):
       nav.driver = webdriver.Edge() 

    def url (nav):
        url = nav.driver.get("https://www.corotos.com.do")
        return url   
    
    # Historia de usuario 1- inicio de sesion
    def test_01_login_valido(nav):
        
        nav.url()
       
        nav.click = nav.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/div/div[3]/div[2]/div/button').click()
        time.sleep(3)
        nav.inicio_de_sesion = nav.driver.find_element(By.ID, 'g4-taco-signin-button')
        nav.inicio_de_sesion.click()
        nav.inicio_de_sesion = nav.driver.find_element(By.ID, 'app_user_email')
        nav.inicio_de_sesion.send_keys("jonsy5277@gmail.com")
        nav.inicio_de_sesion = nav.driver.find_element(By.ID, 'app_user_password')
        nav.inicio_de_sesion.send_keys("-Jguzman182003")
        # screenshot 1
        screenshots = r"C:\Users\jonsy\Downloads\Automatizacion\capturas"
        test_01_img_1 = "test_01_inicio_de_sesion_valido.png"
        concatenar = screenshots + "/" + test_01_img_1
        nav.driver.save_screenshot(concatenar)
        nav.inicio_de_sesion.submit()
        time.sleep(5)
        # screenshot 2
        test_01_img_2 = "test_01_inicio_de_sesion_valido_2.png"
        concatenar2 = screenshots + "/" + test_01_img_2
        nav.driver.save_screenshot(concatenar2)
    

    # historia de usuario 1.2 - inicio invalidado

    def test_02_inicio_de_sesion_invadilado(nav):

        nav.url()
        nav.click = nav.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/div/div[3]/div[2]/div/button').click()
        nav.inicio_de_sesion = nav.driver.find_element(By.ID, 'g4-taco-signin-button')
        nav.inicio_de_sesion.click()
        nav.inicio_de_sesion = nav.driver.find_element(By.ID, 'app_user_email')
        nav.inicio_de_sesion.send_keys("pruebaInvalida@gmail.com")
        nav.inicio_de_sesion = nav.driver.find_element(By.ID, 'app_user_password')
        nav.inicio_de_sesion.send_keys("123")

        # screenshot 1
        screenshots = r"C:\Users\jonsy\Downloads\Automatizacion\capturas"
        test_02_img_1 = "test_02_inicio_de_sesion_valido.png"
        concatenar = screenshots + "/" + test_02_img_1
        nav.driver.save_screenshot(concatenar)
        nav.inicio_de_sesion.submit()
        time.sleep(5)
        

        # screenshot 2
        screenshots = r"C:\Users\jonsy\Downloads\Automatizacion\capturas"
        test_02_img_1 = "test_02_inicio_de_sesion_valido.png"
        concatenar = screenshots + "/" + test_02_img_1
        nav.driver.save_screenshot(concatenar)
    
    # historia de usuario 2 - Barra de busqueda
    def test_03_busqueda(nav):

        nav.url()
        nav.click = nav.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/div/div[3]/div[2]/div/button').click()
        nav.busqueda = nav.driver.find_element(By.ID, 'search')
        nav.busqueda.send_keys("pc")
        # screenshot 1
        screenshots = r"C:\Users\jonsy\Downloads\Automatizacion\capturas"
        test_03_img_1 = "test_03_busqueda.png"
        concatenar = screenshots + "/" + test_03_img_1
        nav.driver.save_screenshot(concatenar)
        nav.busqueda = nav.driver.find_element(By.CLASS_NAME,'common-search-bar__field__icon')
        nav.busqueda.click()
        time.sleep(3)
       # screenshot 2
        test_03_img_2 = "test_03_busqueda_2.png"
        concatenar2 = screenshots + "/" + test_03_img_2
        nav.driver.save_screenshot(concatenar2)

    # historia de usuario 3 - Utilizar el filtro para tener diferentes categorias
    def test_04_categoria_y_mas(nav):
        
        nav.url()
        nav.click = nav.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/div/div[3]/div[2]/div/button').click()
        nav.filtro = nav.driver.find_element(By.CLASS_NAME, 'navbar-desktop__categories_and_more')
        nav.filtro.click()
        # screenshot 1
        screenshots = r"C:\Users\jonsy\Downloads\Automatizacion\capturas"
        test_04_img_1 = "test_04_categoria_y_mas.png"
        concatenar = screenshots + "/" + test_04_img_1
        nav.driver.save_screenshot(concatenar)
        nav.filtro = nav.driver.find_element(By.ID, 'g4-taco-elements-display-menu-electronics-link')
        nav.filtro.click()
        time.sleep(3)

        # screenshot 2
        test_04_img_2 = "test_04_categoria_y_mas_2.png"
        concatenar2 = screenshots + "/" + test_04_img_2
        nav.driver.save_screenshot(concatenar2)
        time.sleep(3)

    # Historia de usuario 4 - El logo principal lleve al inicio

    def test_05_Home(nav):
        nav.url()
        nav.click = nav.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/div/div[3]/div[2]/div/button').click()
        nav.busqueda = nav.driver.find_element(By.ID, 'search')
        nav.busqueda.send_keys("pc")

        # Screenshot 1
        screenshots = r"C:\Users\jonsy\Downloads\Automatizacion\capturas"
        test_05_img_1 = "test_05_categoria_y_mas.png"
        concatenar = screenshots + "/" + test_05_img_1
        nav.driver.save_screenshot(concatenar)
        time.sleep(3)

        # Home
        nav.home = nav.driver.find_element(By.XPATH, '//*[@id="g4-taco-corotos-logo"]/div')
        nav.home.click()
        # Screenshot 2
        screenshots = r"C:\Users\jonsy\Downloads\Automatizacion\capturas"
        test_05_img_2 = "test_05_categoria_y_mas_2.png"
        concatenar = screenshots + "/" + test_05_img_2
        nav.driver.save_screenshot(concatenar)
        time.sleep(3)

    # Historia de usuario 5 - Establecer un rango de precios mínimo y máximo

    def test_06_min_max_precio (nav):
        
        nav.url()
        nav.click = nav.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/div/div[3]/div[2]/div/button').click()
        nav.min_max = nav.driver.find_element(By.CLASS_NAME, 'navbar-desktop__categories_and_more')
        nav.min_max.click()
        nav.min_max = nav.driver.find_element(By.ID, 'g4-taco-elements-display-menu-electronics-link')
        nav.min_max.click()
        nav.min_max = nav.driver.find_element(By.CLASS_NAME, "common-input-text")
        nav.min_max.send_keys("5000")
        #Primera captura
        screenshots = r"C:\Users\jonsy\Downloads\Automatizacion\capturas"
        test_06_img_1 = "test_06_min_max.png"
        concatenar = screenshots + "/" + test_06_img_1
        nav.driver.save_screenshot(concatenar)
        nav.max = nav.driver.find_element(By.XPATH, "/html/body/div/div/div/main/div/div[2]/div[4]/div[2]/div[1]/div[1]/div[5]/div/div[2]/div[2]/label/div/div/input")
        nav.max.send_keys("27000")
        #Segunda captura
        test_06_img_2 = "test_06_min_max_2.png"
        concatenar2 = screenshots + "/" + test_06_img_2
        nav.driver.save_screenshot(concatenar2)
        nav.min_max = nav.driver.find_element(By.XPATH, "/html/body/div/div/div/main/div/div[2]/div[4]/div[2]/div[1]/div[1]/div[5]/div/button").click()
        time.sleep(3)
        test_06_img_3 = "test_06_min_max_3.png"
        concatenar3 = screenshots + "/" + test_06_img_3
        nav.driver.save_screenshot(concatenar3)

        # para cerrar la instancia del navegador después de cada prueba
        def tearDown(nav):
            nav.driver.close   

        #utiliza unittest.main() para ejecutar las pruebas definidas en la clase cuando el script se ejecuta directamente.
        if __name__ == '__main__' :
            unittest.main()
        
       





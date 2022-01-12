#Version Chrome For 97.
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

import time

#Global Var input
print("Masukkan NISN: ")
nisn      = input()
print("Masukkan NPSN: ")
npsn      = input()
print("Masukkan Tanggal Lahir, Contoh (26022004): ")
tgl_lahir = input()


def task():  
        # Buka link
        link = 'https://reg.ltmpt.ac.id/reg/siswa/'
        print("Opening link : " + link )
        driver.get(link)

        print("Assign input tag..")
        # Assign input tag 
        nisn_input = driver.find_element_by_id("nisn")
        npsn_input = driver.find_element_by_id("npsn")
        tgllahir_input = driver.find_element_by_id("tgl_lahir")

        print("Send keys..")
        # Isi nilai input nya
        nisn_input.send_keys(nisn)
        npsn_input.send_keys(npsn)
        tgllahir_input.send_keys(tgl_lahir)

        #Send Form
        button = driver.find_element_by_id("btn-submit")
        button.click()

        # Cek if failed
        try:                
                cek_response = webdriver.support.wait.WebDriverWait(driver, 5)
                cek_response.until(EC.visibility_of_element_located((By.CLASS_NAME,"alert-heading")))
                # Failed, request back
                print("Request back cause failed..\n\n")
        finally:
                pass
        
        
# =================================== #

driver = webdriver.Chrome()

# Doing task
while True:
        task()

input('Tekan Apa Saja untuk exit dari Browser Chrome!')
driver.close() #Close Chrome
driver.quit()  #Close chromedriver.exe

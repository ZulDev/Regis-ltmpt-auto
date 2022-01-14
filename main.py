from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time

#Global Var input
percobaan_ke = 1
start_time = datetime.now() # Kalkulasi waktu register

print("Masukkan NISN: ", end="")
nisn      = input()
print("Masukkan NPSN: ", end="")
npsn      = input()
print("Masukkan Tanggal Lahir, Contoh (26022004): ", end="")
tgl_lahir = input()

print("\nMemulai Register Otomatis..")
print("******************************")



def task():
        time.sleep(1)
        global percobaan_ke
        # Buka link
        link = 'https://reg.ltmpt.ac.id/reg/siswa/'
        print("Opening link : " + link )
        driver.get(link)

        #Cek Fatal error
        response_fatalerror = driver.find_elements(By.TAG_NAME, 'b')
        for e in response_fatalerror:
                #print("DEBUG: " + e.text)
                if 'Fatal error' == e.text or "Fatal error" == e.text:
                        print("Gagal mengirim, Response Error: Fatal error")
                        percobaan_ke = percobaan_ke + 1
                        print("Mencoba lagi, percobaaan ke " + str(percobaan_ke) + "..")
                        print("******************************\n")
                        return "Fatal error"
        #print("=======")  


        print("Mencari semua tag input..")
        # Assign input tag 
        nisn_input = driver.find_element_by_id("nisn")
        npsn_input = driver.find_element_by_id("npsn")
        tgllahir_input = driver.find_element_by_id("tgl_lahir")

        print("Mengisi data input..")
        # Isi nilai input nya
        nisn_input.send_keys(nisn)
        npsn_input.send_keys(npsn)
        tgllahir_input.send_keys(tgl_lahir)

        print("Mencoba mengirim data..")
        #Send Form
        button = driver.find_element_by_id("btn-submit")
        button.click()

        # Cek if failed
        try:
                
                response_alert = driver.find_elements(By.CLASS_NAME, 'alert-heading')
                for e in response_alert:
                        #print(e.text)
                        print("Gagal Mengirim, Response Error: " + e.text)
                        percobaan_ke = percobaan_ke + 1
                        print("Mencoba lagi, percobaaan ke " + str(percobaan_ke) + "..")
                        print("******************************\n")
                        return e.text
                        #return "Terjadi masalah dengan API Pusdatin Kemdikbud"
                #print("=======")      
                print("Berhasil Mengirim data!!!")
                return "berhasil"
        
        finally:
                pass
        
        
# =================================== #

driver = webdriver.Chrome()

request = task()

# For debuggin only
#request = request + " Test"

while request != "berhasil":
        request = task()

#Berhasil register
print("##############################################")
print("SELAMAT, ANDA BERHASIL MENGIRIM DATA!, Silahkan diisi data sebelum aplikasi dimatikan!")


time_elapsed = datetime.now() - start_time 

print('Waktu lama anda register selama (hh:mm:ss.ms) {}'.format(time_elapsed))

input('\n\nTekan Apa Saja untuk exit dari Browser Chrome!, Pastikan udah diisi datanya!')
input('1x Lagi Enter')
driver.close() #Close Chrome
driver.quit()  #Close chromedriver.exe

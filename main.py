from urdm6300 import Rdm6300
import machine
import time
import _thread

uart = machine.UART(2, baudrate=9600)
rfid_reader = Rdm6300(uart)
cek = ''

# note that this is not blocking and needs to be called as often as possible to check for new card scans
def kosongcek():
    while True:
        time.sleep(50)
        cek= ''
        print('kosongkan cek')
_thread.start_new_thread(kosongcek, ())
    
while True:
    
    card_id = rfid_reader.read_card()
    if card_id == None or cek == str(card_id):
        pass
    else:
        
        #print('tidak sama')
        cek = str(card_id)
        print(cek) 
            
        
    time.sleep(1)
    
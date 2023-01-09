
import machine
import ubinascii


class Rdm6300:
    uart = None

    def __init__(self, uart=None):
        """[Initialise the UART driver]
        Args:
            uart (UART): The UART object to use.
        """
        if uart:
            self.uart = uart
        else:
            self.uart = machine.UART(
                1, baudrate=9600, timeout=2, timeout_char=10, tx=19, rx=18)
            self.uart.init(9600)

        # sometimes there's unwanted data in the buffer when we boot up
        # read it until it's all gone
        while self.uart.any():
            self.uart.read()
            print('cek uart')

    def _parse_packet(self, packet):
        """Attempts to parse a packet from the RFID chip.
        return str(int(card_id, 16))"""
        data = str(packet.decode('utf-8'))
        #print (str(data))
        ID = data.replace('\x02','').split('\x03')[0]
        #print (str(ID))
        return str(ID)

    def read_card(self):
        """Attempts to read a card from the RDM6300 reader.
        Returns:
            string: A string of the card ID as a decimal (normally the value printed on the card)
        """
        # if we have data waiting for us
        if self.uart.any():
            data = self.uart.read()
            print('cekuartbawah')
            if data:
                return self._parse_packet(data)

            return None
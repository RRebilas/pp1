class PHONE:
    def __init__(self, producer, model, imei):
        self.isWifiOn = True
        self.producer = producer
        self.model = model
        self.imei = imei

    def calling(self, number):
        print(f"Callng to {number}")

    def send_sms(self, number, message):
        print(f'Do: {number}')
        print(f'Treść: {message}')


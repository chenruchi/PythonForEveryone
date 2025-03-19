class Theater:
    #Attribute
    theaterName = 'Uncle Engineer Theater'

    #Constructrt
    def __init__(self, title, price):
        self.title = title
        self.price = price

    #Method
    def hello(self):
        print('สวัสดีคุณลูกค้าทุกท่าน')

class Customer(Theater):
    def __init__(self, fullname, age, title, price, seats):
        super().__init__(title, price)
        self.fullname = fullname
        self.age = age
        self.seats = seats
        self.money = 10000
    
    def buyTicket(self):
        #คำนวณค่าตั๋ว
        self.total = self.price * self.seats
        
        #หักเงินจากลูกค้า
        self.money -= self.total

        print(f'ชื่อลูกค้า: {self.fullname}')
        print(f'อายุ: {self.age}')
        print(f'หนังเรื่อง: {self.title}')
        print(f'ซื้อ: {self.seats} ที่นั่ง รวมเงิน {self.total}')
        print(f'เหลือเงิน: {self.money} บาท')

#movie01 = Theater('ธี่หยด',150)
#print(movie01.theaterName)
#print(movie01.title)
#print(movie01.price)
#movie01.hello()

#print('======================')

#movie02 = Theater('สัปปเหร่อ',190)
#print(movie02.theaterName)
#print(movie02.title)
#print(movie02.price)
#movie02.hello()

#print('======================')

#movie03 = Theater('แจ๋วซิ่งทะลุฟ้า',90)
##print(movie03.theaterName)
#print(movie03.title)
#print(f'{movie03.price} บ.')
#movie03.hello()

customer01 = Customer('สมชาย เข็มกลัด', 23, 'ธี่หยด 2', 150, 3)
print(customer01.theaterName)
customer01.hello()
customer01.buyTicket()

print('=============================')

customer02 = Customer('เพชร สว่างเช้า', 33, 'Spiderman', 120, 1)
print(customer02.theaterName)
customer02.hello()
customer02.buyTicket()
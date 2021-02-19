class CoffeeMachine:

    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.machine_input()

    def remaining(self):
        print(f"""
        The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.beans} of coffee beans
        {self.cups} of disposal cups
        ${self.money} of money    
        """)
        self.machine_input()

    def machine_input(self):
        machine = input('Write action (buy, fill, take, remaining, exit): ')
        while machine != 'exit':
            if machine == 'buy':
                self.buy_coffee()
            elif machine == 'fill':
                self.fill_machine()
            elif machine == 'take':
                self.take_money()
            elif machine == 'remaining':
                self.remaining()
            break

    def buy_coffee(self):
        coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')

        if coffee == '1' and min(self.water // 250, self.beans // 16, self.cups // 1) >= 1:
            print('I have enough resources, making you a coffee!')
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
            self.machine_input()
        elif coffee == '2' and min(self.water // 350, self.milk // 75, self.beans // 20, self.cups // 1) >= 1:
            print('I have enough resources, making you a coffee!')
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
            self.machine_input()
        elif coffee == '3' and min(self.water // 200, self.milk // 100, self.beans // 12, self.cups // 1) >= 1:
            print('I have enough resources, making you a coffee!')
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6
            self.machine_input()
        elif coffee == 'back':
            self.machine_input()
        else:
            if self.water < 200:
                print('Sorry, not enough water!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
            elif self.beans < 16:
                print('Sorry not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            self.machine_input()

    def fill_machine(self):
        self.water += int(input('Write how many ml of water do you want to add: '))
        self.milk += int(input('Write how many ml of milk do you want to add: '))
        self.beans += int(input('Write how many grams of coffee beans do you want to add: '))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add: '))
        self.machine_input()

    def take_money(self):
        print(f'I gave you ${self.money}')
        self.money = 0
        self.machine_input()


c = CoffeeMachine()

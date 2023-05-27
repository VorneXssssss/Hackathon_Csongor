class PizzaOrder:
    def __init__(self):
        self.pizzas = []  # A rendelt pizzák tárolása
        self.extra_toppings = []  # A rendelt extra feltétek tárolása
        self.drinks = []  # A rendelt italok tárolása

    def add_pizza(self, pizza, size):
        self.pizzas.append((pizza, size))  # Pizza hozzáadása a rendeléshez

    def add_extra_topping(self, topping):
        self.extra_toppings.append(topping)  # Extra feltét hozzáadása a rendeléshez

    def add_drink(self, drink):
        self.drinks.append(drink)  # Ital hozzáadása a rendeléshez

    def get_total_price(self):
        pizzas_price = self.get_pizzas_price()  # Pizzák árának meghatározása
        toppings_price = self.get_toppings_price()  # Extra feltétek árának meghatározása
        drinks_price = self.get_drinks_price()  # Italok árának meghatározása
        total_price = pizzas_price + toppings_price + drinks_price  # Teljes ár kiszámítása
        return total_price

    def get_pizzas_price(self):
        total_price = 0
        for pizza, size in self.pizzas:
            price = self.get_pizza_price(size)  # Pizzák árának meghatározása méret alapján
            total_price += price
        return total_price

    def get_pizza_price(self, size):
        if size == "kicsi":
            return 2600
        elif size == "közepes":
            return 3300
        elif size == "nagy":
            return 4500

    def get_toppings_price(self):
        return len(self.extra_toppings) * 400  # Extra feltétek árának meghatározása

    def get_drinks_price(self):
        return len(self.drinks) * 600  # Italok árának meghatározása


class PizzaChatbot:
    def __init__(self):
        self.order = PizzaOrder()  # Pizza rendelés példányosítása
        self.order_keywords = {
            "pizza": ["sonkás", "sajtos", "hawaii"],  # Megrendelhető pizzák kulcsszavai
            "size": ["kicsi", "közepes", "nagy"],  # Méretek kulcsszavai
            "topping": ["kukorica", "hagyma", "pepperóni"],  # Extra feltétek kulcsszavai
            "drink": ["kóla", "sprite", "víz"]  # Italok kulcsszavai
        }

    def start(self):
        print("Hello! Üdvözöllek a pizzázóban.")
        print("Mit szeretnél?")
        self.process_order()  # Rendelés feldolgozása

    def process_order(self):
        while True:
            user_input = input("Rendelő: ")
            user_input = user_input.lower()  # Felhasználói bemenet kisbetűssé alakítása

            if any(keyword in user_input for keyword in self.order_keywords["pizza"]):
                pizza = self.extract_pizza(user_input)  # Pizza megszerzése a bemenetből
                self.order.add_pizza(pizza, None)  # Pizza hozzáadása a rendeléshez
                print("Rendelésfelvevő: Tökéletes választás")
                print("Milyen méretű pizzát szeretnél? (kicsi, közepes, nagy)")
            elif any(keyword in user_input for keyword in self.order_keywords["size"]):
                size = self.extract_size(user_input)  # Méret megszerzése a bemenetből
                self.order.pizzas[-1] = (self.order.pizzas[-1][0], size)  # Méret hozzárendelése az utolsó pizzához a rendelésben
                print(f"Rendelésfelvevő: rendben, akkor ez egy {size} {self.order.pizzas[-1][0]} pizza.")
                print("Szeretne még valamit hozzáadni a megrendeléséhez?")
            elif any(keyword in user_input for keyword in self.order_keywords["topping"]):
                topping = self.extract_topping(user_input)  # Extra feltét megszerzése a bemenetből
                self.order.add_extra_topping(topping)  # Extra feltét hozzáadása a rendeléshez
                print(f"Rendelésfelvevő: {topping} extra feltétként hozzáadva.")
                print("Még valamit?")
            elif any(keyword in user_input for keyword in self.order_keywords["drink"]):
                drink = self.extract_drink(user_input)  # Ital megszerzése a bemenetből
                self.order.add_drink(drink)  # Ital hozzáadása a rendeléshez
                print(f"Rendelésfelvevő: {drink} hozzá lett adva a megrendeléséhez.")
                print("Még valamit?")
            elif "nem" in user_input:
                total_price = self.order.get_total_price()  # Teljes ár meghatározása
                print("Rendelésfelvevő: Rendben, itt a végső rendelés:")
                self.print_order_details()  # Rendelés részleteinek kiírása
                print(f"Végső ár: {total_price} Ft")
                break
            else:
                print("Rendelésfelvevő: Sajnálom, nem értettem. Megismételné, kérem?")

    def print_order_details(self):
        for index, (pizza, size) in enumerate(self.order.pizzas):
            print(f"Pizza {index + 1}: {size} {pizza}")
        print(f"Extra feltétek: {', '.join(self.order.extra_toppings)}")
        print(f"Italok: {', '.join(self.order.drinks)}")

    def extract_pizza(self, user_input):
        user_input = user_input.lower()
        pizza_options = ["sonkás", "sajtos", "hawaii"]
        for option in pizza_options:
            if option in user_input:
                return option  # A bemenetben talált pizzát adja vissza

    def extract_size(self, user_input):
        user_input = user_input.lower()
        if "kicsi" in user_input:
            return "kicsi"  # Ha a bemenetben van a "kicsi" szó, akkor "kicsi"-t ad vissza
        elif "közepes" in user_input:
            return "közepes"  # Ha a bemenetben van a "közepes" szó, akkor "közepes"-t ad vissza
        elif "nagy" in user_input:
            return "nagy"  # Ha a bemenetben van a "nagy" szó, akkor "nagy"-t ad vissza

    def extract_topping(self, user_input):
        user_input = user_input.lower()
        toppings = ["kukorica", "hagyma", "pepperóni"]
        for topping in toppings:
            if topping in user_input:
                return topping  # A bemenetben talált extra feltétet adja vissza

    def extract_drink(self, user_input):
        user_input = user_input.lower()
        drinks = ["kóla", "sprite", "víz"]
        for drink in drinks:
            if drink in user_input:
                return drink  # A bemenetben talált italt adja vissza


chatbot = PizzaChatbot()
chatbot.start()

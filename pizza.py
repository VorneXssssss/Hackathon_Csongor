class PizzaOrder:
    def __init__(self):
        self.pizzas = []
        self.extra_toppings = []
        self.drinks = []

    def add_pizza(self, pizza, size):
        self.pizzas.append((pizza, size))

    def add_extra_topping(self, topping):
        self.extra_toppings.append(topping)

    def add_drink(self, drink):
        self.drinks.append(drink)

    def get_total_price(self):
        pizzas_price = self.get_pizzas_price()
        toppings_price = self.get_toppings_price()
        drinks_price = self.get_drinks_price()
        total_price = pizzas_price + toppings_price + drinks_price
        return total_price

    def get_pizzas_price(self):
        total_price = 0
        for pizza, size in self.pizzas:
            price = self.get_pizza_price(size)
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
        return len(self.extra_toppings) * 400

    def get_drinks_price(self):
        return len(self.drinks) * 600


class PizzaChatbot:
    def __init__(self):
        self.order = PizzaOrder()
        self.order_keywords = {
            "pizza": ["sonkás", "sajtos", "hawaii"],
            "size": ["kicsi", "közepes", "nagy"],
            "topping": ["kukorica", "hagyma", "pepperóni"],
            "drink": ["kóla", "sprite", "víz"]
        }

    def start(self):
        print("Hello! Üdvözöllek a pizzázóban.")
        print("Mit szeretnél?")
        self.process_order()

    def process_order(self):
        while True:
            user_input = input("Rendelő: ")
            user_input = user_input.lower()

            if any(keyword in user_input for keyword in self.order_keywords["pizza"]):
                pizza = self.extract_pizza(user_input)
                self.order.add_pizza(pizza, None)
                print("Rendelésfelvevő: Tökéletes választás")
                print("Milyen méretű pizzát szeretnél? (kicsi, közepes, nagy)")
            elif any(keyword in user_input for keyword in self.order_keywords["size"]):
                size = self.extract_size(user_input)
                self.order.pizzas[-1] = (self.order.pizzas[-1][0], size)
                print(f"Rendelésfelvevő: rendben, akkor ez egy {size} {self.order.pizzas[-1][0]} pizza.")
                print("Szeretne még valamit hozzáadni a megrendeléséhez?")
            elif any(keyword in user_input for keyword in self.order_keywords["topping"]):
                topping = self.extract_topping(user_input)
                self.order.add_extra_topping(topping)
                print(f"Rendelésfelvevő: {topping} extra feltétként hozzáadva.")
                print("Még valamit?")
            elif any(keyword in user_input for keyword in self.order_keywords["drink"]):
                drink = self.extract_drink(user_input)
                self.order.add_drink(drink)
                print(f"Rendelésfelvevő: {drink} hozzá lett adva a megrendeléséhez.")
                print("Még valamit?")
            elif "nem" in user_input:
                total_price = self.order.get_total_price()
                print("Rendelésfelvevő: Rendben, itt a végső rendelés:")
                self.print_order_details()
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
                return option

    def extract_size(self, user_input):
        user_input = user_input.lower()
        if "kicsi" in user_input:
            return "kicsi"
        elif "közepes" in user_input:
            return "közepes"
        elif "nagy" in user_input:
            return "nagy"

    def extract_topping(self, user_input):
        user_input = user_input.lower()
        toppings = ["kukorica", "hagyma", "pepperóni"]
        for topping in toppings:
            if topping in user_input:
                return topping

    def extract_drink(self, user_input):
        user_input = user_input.lower()
        drinks = ["kóla", "sprite", "víz"]
        for drink in drinks:
            if drink in user_input:
                return drink


chatbot = PizzaChatbot()
chatbot.start()

#C:\Users\Csongor\PycharmProjects\pythonProject1\pizza.py
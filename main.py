### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients:
            if self.machine_resources[ingredient] < ingredients[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = int(input("how many dollars?: ")) * 1
        half_dollars = int(input("how many half dollars?: ")) * 0.5
        quarters = int(input("how many quarters?: ")) * 0.25
        nickels = int(input("how many nickels?: ")) * 0.05
        return half_dollars + dollars + quarters + nickels
        

        
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            print("Transaction successful")
            change = (coins - cost)
            print(f"Here is your change: ${change:.2f}")
            return True
        else:
            print("Transaction failed: Insufficient funds")
            return False
        
        
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient in order_ingredients:
            self.machine_resources[ingredient] -= order_ingredients[ingredient]
        print(f"{sandwich_size} sandwich is ready!")
            

### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)
    
while True:
    order = input("What would you like? (small/ medium/ large/ off/ report): ")

    if order == "off":
        print("Turning off the machine...")
        break
    elif order == "report":
        print(machine.machine_resources)
    elif order in recipes:
        sandwich = recipes[order]  
        if machine.check_resources(sandwich["ingredients"]):
            inserted_coins = machine.process_coins()
            if machine.transaction_result(inserted_coins, sandwich["cost"]):
                machine.make_sandwich(order, sandwich["ingredients"])  
    else:
        print("Invalid choice, please select again.")

        



        
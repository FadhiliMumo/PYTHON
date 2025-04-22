class GalaxyS24:
    def __init__(self, model="Galaxy S24", storage=128, color="Phantom Black", battery_capacity=5000,processor_type="Exynos 2200"):
        
        self.model = model
        self.storage = storage
        self.color = color
        self.battery_capacity = battery_capacity
        self.processor_type = processor_type

    def make_call(self, number):
        return f"Calling {number} from {self.model}..."

    def send_message(self, number, message):
       return f"Sending message to {number}: {message}"

    def charge_battery(self, amount):
        self.battery_capacity += amount
        return f"Battery charged. Current capacity: {self.battery_capacity}mAh"

    def __str__(self):
        return f"{self.model} - {self.storage}GB, {self.color}, {self.battery_capacity}mAh battery"
    
        
    phone=GalaxyS24(storage=256, color="Cream") # type: ignore
    print(phone)
    print(phone.make_call("123-456-7890"))
    print(phone.send_message("123-456-7890", "Hello!"))
    print(phone.charge_battery(500))


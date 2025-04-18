# This is the blueprint for creating a Smartphone
class Smartphone:
    # When we create a new Smartphone, this special function sets it up
    def __init__(self, phone_brand, phone_model, phone_storage, phone_ram, phone_battery):
        # Let's give our smartphone some features (these are called attributes)
        self.brand = phone_brand     # The brand name (like Apple, Samsung)
        self.model = phone_model     # The specific model (like iPhone 14, Galaxy S22)
        self.storage = phone_storage # How much space it has (in GB)
        self.ram = phone_ram         # How fast it can run apps (in GB)
        self.battery = phone_battery # How long it can last (in mAh)
        self.is_on = False           # Is the phone currently on? (starts as off)
        self.current_app = None      # What app is currently open (starts with nothing)

    # This is something our Smartphone can do (this is called a method)
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"My {self.brand} {self.model} is turning on!")
        else:
            print(f"My {self.brand} {self.model} is already on.")

    # Another thing our Smartphone can do
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"My {self.brand} {self.model} is turning off.")
            self.current_app = None # When it's off, no app is open
        else:
            print(f"My {self.brand} {self.model} is already off.")

    def install_new_app(self, app_name):
        print(f"Installing {app_name} on my {self.brand} {self.model}...")
        print(f"{app_name} is now installed!")

    def open_existing_app(self, app_name):
        if self.is_on:
            self.current_app = app_name
            print(f"Opening {app_name} on my {self.brand} {self.model}.")
        else:
            print(f"Oops! Can't open {app_name} because my {self.brand} {self.model} is off.")

    def close_current_app(self):
        if self.is_on and self.current_app:
            print(f"Closing {self.current_app} on my {self.brand} {self.model}.")
            self.current_app = None
        elif not self.is_on:
            print(f"My {self.brand} {self.model} is off, so no app is open.")
        else:
            print("No app is running right now.")

    def show_specs(self):
        specs = (f"Brand: {self.brand}, Model: {self.model}, "
                 f"Storage: {self.storage}GB, RAM: {self.ram}GB, "
                 f"Battery: {self.battery}mAh")
        return specs

# Let's create some actual smartphones using our blueprint (these are objects)
my_personal_phone = Smartphone("OnePlus", "Nord 2T", 128, 8, 4500)
my_old_phone = Smartphone("Nokia", "3310", 0, 0, 1000) # Old school!

print("My main phone:", my_personal_phone.show_specs())
print("My old phone:", my_old_phone.show_specs())

my_personal_phone.turn_on()
my_personal_phone.install_new_app("Cool Game")
my_personal_phone.open_existing_app("Gallery")
my_personal_phone.close_current_app()
my_old_phone.turn_on() # Even old phones can turn on!
my_old_phone.turn_off()
my_personal_phone.turn_off()

print("\n--- Making a Special Kind of Smartphone ---")

# Let's make a new blueprint that's a special kind of Smartphone - a Gaming Phone!
# It will have all the features of a regular Smartphone, plus some extra.
class GamingPhone(Smartphone):
    def __init__(self, phone_brand, phone_model, phone_storage, phone_ram, phone_battery, cooling_system):
        # First, set up the basic Smartphone features using the parent's setup
        super().__init__(phone_brand, phone_model, phone_storage, phone_ram, phone_battery)
        # Now, add the special feature for GamingPhone
        self.cooling = cooling_system

    def start_gaming(self, game_name):
        if self.is_on:
            print(f"Starting {game_name} on my {self.brand} {self.model} with its {self.cooling} cooling!")
            self.current_app = game_name
        else:
            print("Can't game when the phone is off!")

    # Let's also show the special gaming feature in the specs
    def show_specs(self):
        basic_specs = super().show_specs() # Get the basic specs from the Smartphone blueprint
        return f"{basic_specs}, Cooling: {self.cooling}"

my_gaming_phone = GamingPhone("ROG", "Phone 6", 512, 16, 6000, "Vapor Chamber")
print("My gaming phone:", my_gaming_phone.show_specs())
my_gaming_phone.turn_on()
my_gaming_phone.start_gaming("Awesome Racing Game")
my_gaming_phone.turn_off()
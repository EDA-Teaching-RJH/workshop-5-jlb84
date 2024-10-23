import random 
# Constants 
MISSION_TYPES = ["Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"] 
# Ship systems, resources, and crew 
ship = { 
		"systems": { 
		"shields": 100, 
		"weapons": 100, 
		"engines": 100, 
		"sensors": 100 
		}, 
		"resources": { 
			"energy": 1000, 
			"torpedoes": 10 
		}, 
		"crew": { 
			"Picard": "Command", 
			"Riker": "Command", 
			"Data": "Operations", 
			"Worf": "Operations", 
			"La Forge": "Operations", 
			"Crusher": "Sciences", 
			"Troi": "Sciences" 
		} 
	} 

def main(): 
	print("Welcome to the Star Trek: TNG Mission Simulator!") 
	score = 0 
	turns = 0 

	while True: 
		display_status() 
		action = get_user_action() 

	if action == "1": 
		score += run_mission() 
	elif action == "2": 
		repair_system() 
	elif action == "3": 
		add_crew_member() 
	elif action == "4": 
		print(f"Simulation ended. Final score: {score}") break 
	else: 
		print("Invalid action. Please try again.") 
		
	turns += 1 
	handle_random_event() 

	if turns % 3 == 0: 
		replenish_resources() 

def display_status(): 
	print("Ship Status")
	print(f"Systems: {ship['systems']}")
	print(f"Resources: {ship['resources']}")
	print(f"Crew:{list(ship['crew'].keys())}")
	print()

def get_user_action(): 
	print("Choose an acion: ")
	print("1. Run mission")
	print("2. Repair system") 
	print("3. Add crew member") 
	print("4. End simulation")
	return input ("Choose an action: ")

def run_mission(): 
	mission_type = random.choice(MISSION_TYPES) 
	print(f"\nNew mission: {mission_type}") 
	# TODO: Implement mission logic for different mission types 
	# Return the score earned from the mission 

def repair_system(): 

	print("Which system would you like to repair? ")
	print("1. Shields")
	print("2. Weapons")
	print("3. Engines")
	print("4. Sensors")
	choice = input ("Which system would you like to repair? ")

if choice == "1"
	ship['systems']['shields'] = 100
	print("Shields repaired")
elif choice == "2"
	ship['systems']['weapons'] = 100
	print("Weapons repaired)
elif choice == "3"
	ship['systems']['engines'] = 100
	print("Engines repaired")
elif choice == "4"
	ship['systems']['sensors'] = 100
	print("Sensors repaired")
else
	print("invalid choice")

def add_crew_member(): 
	print("Add new crew member")
 	crew_new = input("Enter the name of the new crew member: ")
  	role_new = input(f"Enter {crew_new}'s role: ")
   if role_new in ["Command", "Operations", "Sciences"]:
   ship["crew"][crew_new] = role_new
   print(f"{crew_new}added to the crew as{role_new}.")
   else 
   print("Invalid role")

def handle_random_event():
# TODO: Implement random events that can occur during the simulation 

def use_resource(resource, amount): 
# TODO: Implement resource usage logic 

def replenish_resources(): 
# TODO: Implement resource replenishment logic 

main()

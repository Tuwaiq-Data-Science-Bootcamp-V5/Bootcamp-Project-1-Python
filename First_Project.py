###Dubai Lists
dubai_hotels=["Movenpik Jumeirah Village Triangle", "Swissotel Almurooj", "Holiday Inn Dubai Al-Maktoum airport"]
dubai_places=["Sky Dubai", "IMG Theme Park", "JBR", "Global Village","Dubai Safari Park"]

###London Lists
london_hotels=["Queen's Gate Hotel","Royal Lancaster","Clayton Hotel London Wall"]
london_places=["London Eye","Leicester Square","Hydepark","Covent Garden","Regent Park"]

###Singapore Lists 
singapore_hotels=["Mondrian Singapore Duxton", "Voco Orchard", "Capri By Fraser China"]
singapore_places=["Marina Bay Sands", "Universal Studios", "Jurong Bird Park", "Trick Eye Museum", "Botanic Gardens"]

###User Inputs
dest=input("Please choose your destination (Dubai, London, Singapore): ").lower()
travelers=int(input("How many travelers?: "))

###While loop to determine the budget
while True:
    days=int(input("How many days?: "))
    budg=float(input("Please enter your budget: "))
    if days>3 and budg<=8000 or days>=budg:
        print("The budget is not enough for the number of days you are planning for")
        repeat = input("Do you want to repeat the process? (yes/no): ")
        if repeat.lower() != "yes":
           break
    else:
        break    


###Assigning lists with if condition to run the next function
if dest=="dubai":
    hotels=dubai_hotels
elif dest=="london":
    hotels=london_hotels
elif dest=="singapore":
    hotels=singapore_hotels


###Function to help the user to choose the hotel 
def userChoice(dest, hotels):
    hotel = ''
    input_message = "\nPick an option:\n"

    for index, item in enumerate(hotels):
        input_message += f'{index+1}) {item}\n'

    input_message += 'Your choice: '
    ###Check if the user choose a hotel that matches one of the option in the list
    while hotel not in map(str, range(1, len(hotels) + 1)):
        hotel = input(input_message)

    print('You picked: ' + hotels[int(hotel) - 1],'\n')
    return (hotel)

userChoice(dest, hotels)


###Assigning lists with if condition to run the next function
if dest== "dubai":
    act=dubai_places
elif dest=="london":
    act=london_places
elif dest=="singapore":
    act=singapore_places
   
###Function to help the user to choose the daily activities
def createSchedule(act, days):
    schedule = {}
    num_act = len(act)
    act_per_day = num_act // days
    extra_acts = num_act % days

    day = 1
    start_index = 0
    for i in range(days):
        end_index = start_index + act_per_day
        if extra_acts > 0:
            end_index += 1
            extra_acts -= 1
        schedule[f"Day {day}"] = act[start_index:end_index]
        start_index = end_index
        day += 1
    return schedule

selected_act = []
for i in act:
    choice = input(f"Do you want to include this activity '{i}'? (y/n): ")
    if choice.lower() == "y":
        selected_act.append(i)
schedule = createSchedule(selected_act,days)
print(schedule)


###Function calculates the expected budget of the designed plan
#based on a percentage calculated for each part of the plan(hotel and schedule)
def budget(budg):
    hotel_budg= budg*0.3
    act_budg=budg*0.2
    total_exp_budg= lambda hotel_budg, act_budg : hotel_budg+act_budg
    return (total_exp_budg(hotel_budg, act_budg))

###Function to display the plan
def plan(dest,days,budg,createSchedule,budget):
    
    print("\n\n\nThis is your plan to\n",dest,"\nfor\n",days," days\n"\
          "Yor daily plan: ",schedule,\
          "\nThe expected budget for this plan: ",budget(budg),"SR. out of ",budg,"SR.")
    
plan(dest,days,budg,createSchedule,budget)
"""
Author:<Daniel Alvarez>
Assignment:#1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton" # String
preferred_weight_kg = 20.5  # Float
highest_reps = 25           # Integer
membership_active = True    # Boolean

# Step c: Create a dictionary named workout_stats
# Dictionary with string keys and tuple(int, int, int) values
workout_stats = {
    "Titas" : (25, 30, 60),
    "Daniel" : (15, 60, 30),
    "Bona" : (10, 120, 10)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
# Loop through person, and activities in the dictionary, and add up all the minutes in (activities) 
for person, activities in list(workout_stats.items()):
    total_minutes = sum(activities)
    workout_stats[f"{person}_Total"] = total_minutes

# Step e: Create a 2D nested list called workout_list
# 2-dimensional list where each row is a friend and each column is an activity represented as integers
workout_list = [
    list(workout_stats["Titas"]),
    list(workout_stats["Daniel"]),  
    list(workout_stats["Bona"])    
]

# Step f: Slice the workout_list
yoga_and_running = [row[:2] for row in workout_list]
print("Yoga and Running minutes for all friends:", yoga_and_running)

weightlifting_two_friends = [row[2] for row in workout_list[1:]] 
print("Weightlifting minutes for last two friends:", weightlifting_two_friends)

# Step g: Check if any friend's total >= 120
friends = ["Titas", "Daniel", "Bona"]
for friend in friends:
    total = workout_stats[f"{friend}_Total"] 
    if total >= 120:
        print(f"Great job staying active, {friend}!")

# Step h: User input to look up a friend
friend_input = input("Enter a friend's name: ").lower() 
if friend_input == "titas".lower():
    friend = "Titas"
elif friend_input == "daniel".lower():
    friend = "Daniel"
elif friend_input == "bona".lower():
    friend = "Bona"
else:
    friend = None
if friend:
    activities = workout_stats[friend]
    total = workout_stats[f"{friend}_Total"]
    print(f"{friend}'s workout minutes for each activity: Yoga: {activities[0]}, Running: {activities[1]}, Weightlifting: {activities[2]}")
    print(f"Total workout minutes: {total}")
else:
    print(f"Friend {friend_input} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
highest_total = -1
lowest_total = float('inf') 
highest_friend = ""
lowest_friend = ""
for friend in ["Titas", "Daniel", "Bona"]:
    total = workout_stats[f"{friend}_Total"]
    
    if total > highest_total:
        highest_total = total
        highest_friend = friend
    
    if total < lowest_total:
        lowest_total = total
        lowest_friend = friend
print(f"Friend with highest total workout minutes: {highest_friend} ({highest_total} minutes)")
print(f"Friend with lowest total workout minutes: {lowest_friend} ({lowest_total} minutes)")


from interface_functions import *

# Build display menu
display_dict = {i + 1: key for i, key in enumerate(functions_drop)}

input("Press ENTER to start...")

choice = "-"

while choice != 0:
    print("\nChoose an option (0 to exit):")
    for idx, title in display_dict.items():
        print(f"{idx}: {title}")

    choice = get_integer(">> ")

    if choice not in display_dict:
        break

    selected_key = display_dict[choice]
    selected_function = functions_drop[selected_key]

    print("-" * 60)
    print(f"{selected_key}:\n")

    result = selected_function()
    print(result)
    print("-" * 60)

print("You have finished editing the college data.")

# Save Process
courses_file = 'college_course.json'
students_file = 'student_details.json'
schedule_file = 'weekly_schedule.json'

save = input("Do you want to save the updated data? [y/n] ").casefold()

if save == 'y':
    dump_data(courses_file, courses_dict)
    dump_data(students_file, students_dict)
    dump_data(schedule_file, schedule)
    print("All data saved successfully!")
else:
    print("Changes were not saved.")

"""Problem:
Clark is conducting an online Quiz competition daily where daily participation for contestants is optional.
Clark want to send specific notifications to following group of participants
- Participants who participated everyday
- Participants who participated only once
- Participants who participated on the first day and never participated again.
Help Clark to write functions in python to get the above information. Sample function definitions are already created.
Participants data will be sent as list of lists. Each row will represent the participants attended on that day.
Sample input:
participants_list = [
    ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
    ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
]
send the solution to cutshort@adnabu.com with the subject line "Solution to Puzzle"
Bonus points for optimising the solution w.r.t. time and space.
"""


def daily_participants(participants_list):
    """Returns the list of all participants who participated everyday
    for the sample input, the right answer is
    ['Desmond', 'Krish', 'Sam']
    expected return object is a list of strings
    """
    result = set(participants_list[0])
    for item in participants_list:
        result = result.intersection(item)
    return list(result)


def one_time_participants(participants_list):
    """Returns the list of all participants who participated only once
    for the sample input, the right answer is
    ['Kapil', 'Ron', 'Ginny', 'Ted', 'Sachin', 'John', 'Joan']
    expected return object is a list of strings
    """
    result = []
    final_list = []
    count_more_than_once = []
    for item in participants_list:
        final_list += item
    final_list.sort()
    i= 0
    while(i< len(final_list)):
        count = 0
        j = i
        while(j<len(final_list) and final_list[i] == final_list[j]):
            count += 1
            j += 1
        if count == 1:
            result.append(final_list[i])
        i = j

    return list(result)


def first_day_only_participants(participants_list):
    """Returns the list of all participants who participated on the first day and never participated again.
    for the sample input, the right answer is
    ['John', 'Joan']
    expected return object is a list of strings
    """
    first_day_participant = set(participants_list[0])
    for item in participants_list[1:]:
        first_day_participant -= set(item)
        print(first_day_participant)
    
    return list(first_day_participant)


participants_list = [['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
    ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']]

print(daily_participants(participants_list))
print(one_time_participants(participants_list))
print(first_day_only_participants(participants_list))


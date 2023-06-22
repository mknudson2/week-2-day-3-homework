# Create a function that given a list which represents street lights given as a parameter(l_street), determine if an outage has occurred. A street with a total number of "F" greater than or equal to 2 returns "Outage", anything below returns "Power"
# Example Input: [ 'T', 'F', 'F', 'F' ]				
# Example Output: "Outage"

lights = ['T', 'F', 'F', 'F']


#MY SOLUTION
def light_status(l_street):
    status = l_street.count('F')
    if status >= 2:
        return('Outage')
    else:
         return('Power')


#DYLAN'S SOLUTION 1
print(light_status(lights))


def determine_outage(lights_list):
    return 'Outage' if lights_list.count('F') >= 2 else 'Power'


#DYLAN'S SOLUTION 2 (need to finish, revisit recording)
def determine_without_count(lights_list):



# MODULE FILE
def printName(name):
    print(f"Hello Mr/Ms {name}...we've been waiting for you!")

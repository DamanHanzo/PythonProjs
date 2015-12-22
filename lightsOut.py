def get_num_buttons():
    """prompt player for the number of buttons
       ensures: return value is a positive int
    """
    prompt = input("Enter the number of buttons: ")
    button_num = "{} {}".format(int(prompt)*("*"), " ")
    
    return button_num   # stub: returns any legal value; replace at the end
    

def get_the_button_number(num_buttons):
    """prompt player for the number of the button to press
       ensures: return value is between 1 and num_buttons
    """
    prompt2 = input("Enter the number of buttons to press: ")
    return prompt2  # stub: returns any legal value; replace at the end
              
def print_game(button_lst):
    """print the state of the button_lst; use '*' for "on" (True), '-' for "off" (False)
       requires: button_lst is iterable (a collection)    
    """
    for i in range(button_list):
        if i==True:
            print("*", end=" ")
        elif i==False:
            print("-", end= " ")
    
    None         # stub 

def button_on(button_lst):
    """check if any button in button_lst is on (True)
       ensures: returns True iff some button is on (True) 
    """
    for i in button_list:
        if i==True:
            print("*", end=" ")
        elif i==False:
            print("-", end= " ")
        
        
    return False   # stub 

def press_button(button_lst, button_num):
    """press the given button in button_list
       requires: 1 <= button <= len(game)
       modifies: button_list, toggling the state of button & its neighbors
    """
    None    # stub
    

def main():
    num_buttons = get_num_buttons()
    game = [True] * num_buttons
    print_game(game)
    while (button_on(game)):
        button_num = get_the_button_number(num_buttons)
        press_button(game, button_num)
        print_game(game)


        
        

    
    
    

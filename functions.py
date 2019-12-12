import string
import random

#functions from is_question to end_chat were taken from A3
def is_question(input_string):
    if "?" in input_string:
        output=True
    else:
        output=False
    return output
    
def remove_punctuation(input_string):
    out_string="" 
    for i in input_string:
        if i not in string.punctuation:
            out_string=out_string+i
    return out_string

def prepare_text(input_string):
    out_list=[]
    temp_string=input_string.lower()
    temp_string=remove_punctuation(temp_string)
    out_list=temp_string.split()
    return out_list

def string_concatenator(string1,string2,seperator):
    output=string1+seperator+string2
    return output

def selector(input_list,check_list,return_list):
    output=None
    for i in input_list:
        if i in check_list:
            output=random.choice(return_list)
            break
    return output

def end_chat(input_list):
    if "quit" in input_list:
        output=True
    else:
        output=False
    return output

def neutral_colors(input_list,check_list,return_list):
    """neutral_colors is a function that if a neutral color is inputted then it 
    returns a statement from the chatbot
    """
    output=None
    for i in input_list:
        if "black" in input_list and check_list:
            output=return_list[0]
            break
        elif "white" in input_list and check_list:
            output=return_list[0]
            break
        elif "grey" in input_list and check_list:
            output=return_list[0]
            break
        elif "gray" in input_list and check_list:
            output=return_list[0]
            break
    return output

def comp_colors(input_list,check_list,return_list):
    """comp_colors is a function that takes in a common color
    it returns its complementary color
    """
    output=None
    for i in input_list:
        if "red" in input_list and check_list:
            output=return_list[1]
            break
        elif "green" in input_list and check_list:
            output=return_list[2]
            break
        elif "orange" in input_list and check_list:
            output=return_list[3]
            break
        elif "blue" in input_list and check_list:
            output=return_list[4]
            break
        elif "yellow" in input_list and check_list:
            output=return_list[5]
            break
        elif "purple" in input_list and check_list:
            output=return_list[6]
            break
    return output

def warm_or_cool(input_list,check_list,return_list):
    """warm_or_cool is a function that takes in warm or cool
    and returns the colors in that category
    """
    output=None
    for i in input_list:
        if "warm" in input_list and check_list:
            output=return_list[0]
            break
        elif "cool" in input_list and check_list:
            output=return_list[1]
            break
    return output
#I declare that my work contains no examples of misconduct,such as plagiarism,or collusion.
#Any code taken from other sources is referenced within my code solution.
# student ID : W1986534
# Date : 19.04.2023


# Part 1 - Main Version A
# student number and credits initiated to zero
total_student = 0
progress_count = 0
module_retriever_count = 0
exclude_count = 0
module_trailer_count = 0

# lists created to store credits
progress_list = []
module_trailer_list = []
module_retriever_list = []
exclude_list = []

# lists created to store student IDs
student_ID_list = []  # common list of the student IDs of all the students
student_ID_list_pro = []  # IDs that progressed
student_ID_list_trail = []  # IDs that got module trailer
student_ID_list_ret = []  # IDs that got module retriever
student_ID_list_ex = []  # IDs that got module  exclude

progression_outcomes_of_students = {}  # a dictionary created to store IDs and progression outcomes

def add_inc(outcome_list,student_id_outcome_list,outcome):
    """
    Prints result of credits entered,appends credits to their respective lists ,
    adds the student ID to the respective list outcome,
    adds studentIDs to the student ID list and increases student count.

    Parameters:
    outcome_list (list): progress_list,module_trailer_list
    student_outcome_list (list): list containing studentIDs specific to their outcome category
    outcome (str) : outcome category such as exclude, progress and module trailer
    
    """
    print(outcome)
    outcome_list.append([student_credits_pass, student_credits_defer, student_credits_fail])
    student_id_outcome_list.append(student_ID)
    student_ID_list.append(student_ID)
    global total_student
    total_student += 1 # increase total student count 
   
                
def student_credit_input(prompt):
    """
    This user defined function validates if credit entered is within the range of 0,20,40,60,80,100,120.

    Parameter:
    prompt (str) : prompt to be displayed to enter credits

    Returns:
    student_credit (int) : returns credits entered
    
    """
    while True:
        try:
            student_credit=int(input(prompt))
            if student_credit not in range(0, 121,20): 
                print("Out of range""\n")
                continue

        except ValueError:
            print("Integer required""\n")
            continue
        return student_credit
            
        
while True:           
    
        student_ID = str(input("\n""Enter your student ID: "))
        if student_ID[0] != 'w' or len(student_ID) != 8:
            print("You have not entered a valid student ID, Please make sure your student ID is in the format w_ _ _ _ _ _ _ ")
            continue
        elif student_ID in student_ID_list:
            print("\n""The student ID you entered already exists,please enter a new student ID" + "\n")
            continue
        
        student_credits_pass = student_credit_input("Please Enter your credit at pass: ") #calling user defined function student_credit_input
    
        student_credits_defer = student_credit_input("Please Enter your credit at defer: ")

        student_credits_fail = student_credit_input("Please Enter your credit at fail: ")

        
        if student_credits_pass + student_credits_defer + student_credits_fail != 120:  # checks if the total sum of credits adds up to 120
            print("Total incorrect")
            student_credits_pass = student_credit_input("Please Enter your credit at pass: ")
            student_credits_defer = student_credit_input("Please Enter your credit at defer: ")
            student_credits_fail = student_credit_input("Please Enter your credit at fail: ")


            
        if student_credits_pass == 120:
               progress_count+=1 #increase number of students whose result is progress
               add_inc(progress_list,student_ID_list_pro,"progress")
               
        elif student_credits_pass == 100:
                add_inc(module_trailer_list,student_ID_list_trail,"Progress (module trailer)")
                module_trailer_count += 1 #increase number of students whose result is module trailer
                
                
        elif student_credits_fail == 80 or student_credits_fail == 100 or student_credits_fail == 120:
                add_inc(exclude_list,student_ID_list_ex,"excluded")
                exclude_count +=1
                #increase number of student whose result is excluded
                
        else:
                add_inc(module_retriever_list,student_ID_list_ret,"module retriever ")
                module_retriever_count += 1 #increase number of student whose result is module retriever
                
                
          
        staff_input = input("\n""Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
        staff_input.lower()
        if staff_input == 'y':
            continue
        if staff_input != 'y' and staff_input != 'q':
                print("Invalid entry.Please enter either 'y' to continue or 'q' to quit the program")
                staff_input = input("\n""Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
                staff_input.lower()
        
        elif staff_input == 'q':
                break
    


def student_progression_list(type_of_list, outcome_type):
   """
   Creates a list of credits with their progression outcome.
   Parameters:
   type_of_list (list):list specific to outcome with lists of credits 
   outcome_type (str) : Outcome category like progress, module trailer etc.

   """
   for x in range(0, len(type_of_list)):
        outcomes = str(type_of_list[x:x + 1]).replace("[", " ").replace("]", " ") #dividing lists   
        if outcomes == "None": #if there is an empty list 
            pass
        else:
            print(outcome_type + " -" + outcomes)
            
# Dictionary
print("\nPart 4")


def id_outcomes(student_id_for_list, outcomes_type, outcome_list):
    """creates a dictionary called progress_outcomes_of_students and assigns the progression outcome of each student with their credits
       to each student.
       
       Parameters:
       student_id_for_list (list) : list of students IDs 
       outcomes_type (str): outcome category
       outcome_list (list) : outcome specific list with credits
     """
    for i in range(len(student_id_for_list)):
        progression_outcomes_of_students[student_id_for_list[i]] = outcomes_type + str(outcome_list[i])


id_outcomes(student_ID_list_pro, "Progress - ", progress_list)
id_outcomes(student_ID_list_trail, "Module trailer - ", module_trailer_list)
id_outcomes(student_ID_list_ret, "Module retriever - ", module_retriever_list)
id_outcomes(student_ID_list_ex, "Exclude - ", exclude_list)

for key, value in progression_outcomes_of_students.items():#prints the dictionary with studentIDs and credits 
    print(str(key) + ":" + str(value).replace("[", " ").replace("]", " "), " ", end='')










# Lewis Muthomi
# 1250 01
# Lab 11
# 7 November 2022
# User greeting
print('This program will let you type in a state name and display that state two letter')
print('abbriviation or abbriviation or type in a state abreviation and display that states name.')
print()
      
# Create list of states
stateName = ['ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 
'CONNECTICUT', 'DELAWARE', 'FLORIDA', 'GEORGIA',
             'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 
'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS',
             'MICHIGAN', 'MINNESOTA', 'MISSISSIPI', 'MISSOURI', 'MONTANA', 
'NEBRASKA', 'NEVADA','NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO',
             'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 
'OREGON', 'PENNSYLVANIA', 'RHODE ISLAND','SOUTH CAROLINA',
             'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 
'WASHINGTON', 'WEST VIRGINIA','WISCONSIN', 'WYOMING']
      
# Create a list of state abbreviation
stateAbbrev = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 
'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME',
                     'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 
'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA',
                     'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 
'WI', 'WY']
                     
# Init run
run = True
      
# Start program loop
while run == True:
   whichWay = input('Please enter "s" to enter a state name or "a" to enter a state abbreviation: ').lower()
   print()
   
   # Error check user input
   while whichWay != 's' and whichWay != 'a':
        whichWay = input('INPUT ERROR: Please type "s" to enter a state name or "a" to enter a state abbreviation: ').lower()
   # Set up input line and list to check
   if whichWay == 's':
      word = 'name: '
      listToCheck = stateName
      
   else:
      word = 'abbreviation: '
      listToCheck = stateAbbrev
      
   # Get user input either a state name or a state abbreviation
   userInput = input('Please enter the state ' + word).upper()
   
   # error check user input
   while userInput not in listToCheck:
      userInput = input('INPUT ERROR: Please enter a correct state ' + word).upper()
      
   # Find and print correct state
   if whichWay == 's':
      for mainIndex in range(len(stateName)):
          if userInput == stateName[mainIndex]:
             print('The state  abbreviation is: ' + stateAbbrev[mainIndex] + '.')
             print()
   
   else:
      for mainIndex in range(len(stateAbbrev)):
          if userInput == stateAbbrev[mainIndex]:
             print('The state  name is: ' + stateName[mainIndex] + '.')
             print()
             
   # Get input for run again loop
   runAgain = input('Would you like to run the program again(y/n): ').lower()
   
   # Error check user input
   print()
   while runAgain != 'y' and runAgain != 'n':
          runAgain = input('INPUT ERROR: Please enter a "y" or "n": ').lower
   if runAgain == 'n':
       run = False
   print()
   
# Exit message
print('Have a nice day!!!!!')

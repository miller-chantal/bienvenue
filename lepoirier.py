# take user input and return quotient


def commute():
    while True:
        fare = int(input('Please enter the fare price '))  # user input will be integer or float
    
        budget = int(input('What is the dollar amount you will be spending? '))

        travel = budget / fare

        rides = round(travel)
        if fare > 0:
            print(rides)
            break
        elif fare < 0:
            print('please re-enter the amount you want to spend')
            continue
        else:
            ('please see a ticket agent')
        
    print('You will be able to make ' + str(rides) + ' trips' )
commute()
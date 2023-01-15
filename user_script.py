"""
Complete the script.
"""
print('Glad you came to the gym today to pump some iron! \n Today you will be doing bench press of 12 reps \n please enter the weights for your sets.')
Set1 = float(input('Enter weight for first set '))
Set2 = float(input('Enter weight for second set '))
Set3 = float(input('Enter weight for third set '))

TotalSet1 = round(Set1 * 12)
TotalSet2 = round(Set2 * 12)
TotalSet3 = round(Set3 * 12)

TotalWeight = TotalSet1 + TotalSet2 + TotalSet3
AverageWeight = round(TotalWeight / 3)
MinWeight = min(TotalSet1, TotalSet2, TotalSet3)
MaxWeight = max(TotalSet1, TotalSet2, TotalSet3)
RangeWeight = MaxWeight - MinWeight

print('Total weight lifted today: ', TotalWeight )
print('Average Weight lifted per set: ', AverageWeight )
print('The lease weight lifted in a set: ', MinWeight )
print('The most weight lifted in a set: ', MaxWeight)
print('The Range of the sets is: ', RangeWeight)

if TotalSet3 == TotalSet1:
    print('Your first set ', TotalSet1, 'is equal to your last set', TotalSet3, ' \n You need to work harder!')
if TotalSet3 <= TotalSet2:
    print('Your first set', TotalSet1, 'Was greater than your last set', TotalSet3, ' \n You need to work harder!')
if TotalSet3 >= TotalSet2:
    print('Your last set', TotalSet3, 'was Greater than you first set', TotalSet1, ' \n Great job! You are going to have insane gains soon!')
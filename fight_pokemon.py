#!/usr/bin/env python
print("Dueling Pokemon")

#define function to calculate any two combinations
def calc_effectiveness(attacker_type,defender_type):
    attacker_type_index= POKEMON_TYPES.index(attacker_type)
    defender_type_index=POKEMON_TYPES.index(defender_type)
    
    effectiveness=MATCHUPS[attacker_type_index][defender_type_index]
    
    return effectiveness

# create types for lookup later
# POKEMON_TYPE[1]='Fire' for example
POKEMON_TYPES= ['Normal','Fire','Water']

# create table or 'matrix'
# find value by using MATCHUPS[r][c]
# where r=row (starts with 0) and c=column (starts with 0)
MATCHUPS = [ [1,1,1], #row 0 or Normal type attacker
    [1,.5,.5],  # row 1 or Fire type
    [1,2,.5]] # row 2 or Water type

# display example attack effectiveness for Water attacking Fire
attacker_type_index= POKEMON_TYPES.index('Water')
defender_type_index=POKEMON_TYPES.index('Fire')

print('Example of Water attacking fire')
print('attacker index=',attacker_type_index)
print('defender index=',defender_type_index)

# calculate how effective attacker is against defender
print('Effectiveness=',MATCHUPS[attacker_type_index][defender_type_index])

# let's try a few different ones
print('Fire attacks Water:',calc_effectiveness('Fire','Water'))
print('Water attacks Fire:',calc_effectiveness('Water','Fire'))
print('Water attacks Water:',calc_effectiveness('Water','Water'))



    
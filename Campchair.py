
# 1) first create the camp_chair class and it's methods;
class CampChair:
    # called when each object is created
    def __init__(self, color, cup_holder, cross_legs, weight_capacity, something_on_the_chair):
        self.color = color
        self.cup_holder = cup_holder
        self.cross_legs = cross_legs
        self.weight_capacity = weight_capacity
        self.something_on_the_chair = something_on_the_chair

    # each method returns its property
    def colour_output(self):
        return self.color

    def cup_holder_output(self):
        return self.cup_holder

    def cross_leg_output(self):
        return self.cross_legs

    def weight_capacity_output(self):
        return self.weight_capacity

    # using some conditional, this method decides if the chair should fold or not
    # notice how it doesn't have a return value, so it's void;
    def chair_folding(self, chair_name):
        if self.something_on_the_chair:
            print(f'don\'t fold it yet, there\'s something on {chair_name}')
        else:
            print(f'since there\'s nothing on the {chair_name}, it will fold now')


# 2) then create the individual chairs/objects (in this case a brown chair and red chair)
chair_one = CampChair(
    color='brown',
    cup_holder=True,
    cross_legs=True,
    weight_capacity=100,
    something_on_the_chair=False
)

chair_two = CampChair(
    color='red',
    cup_holder=False,
    cross_legs=False,
    weight_capacity=80,
    something_on_the_chair=True
)

# 3) then query any of the objects through dot notation;
# (everything above has been going on in memory, not on standard output;

# will show the color of each chair
print(f'chair one\'s colour is {chair_one.color}')
print(f'chair one\'s colour is {chair_two.color}')
print()

# we can assign new values to the attributes
chair_two.color = 'yellow'

# chair one still have everything we said it should have,
# but chair two will now be yellow
print(f'chair one\'s colour is {chair_one.color}')
print(f'chair one\'s colour is now {chair_two.color}')
print()

# and we can also call any of the methods within the class (in this case, assigned to a variable)
chair_one_weight = chair_one.weight_capacity_output()
print(f'chair one can handle {chair_one_weight}kg')

# notice how i just called the 'weight_capacity_output()' method directly within string formatting
print(f'chair two can handle {chair_two.weight_capacity_output()}kg')
print()

# let's try to fold each of the chairs (notice how the void function works)
chair_one.chair_folding(chair_name='chair_one')
chair_two.chair_folding(chair_name='chair_two')

# if we try to call a non-existent chair, e.g. chair_three,
# we'll get an Exception;
# print(chair_three.) <<< this will not work because we don't have this object





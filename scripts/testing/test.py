########################################
#### Test the recommendation system ####
########################################

"""
This script tests the recommendation system.
It runs three tests, one for each of the following cases:
1. An online visitor
2. An online user
3. Multiple offline users
"""

"""
We begin by running the configuration script, if the modules are not loaded to our environment already.
"""
# run the configuration script
exec(configuration)

"""
Next, we create all of the functions.
"""
# run the functions script
exec(functions)

"""
Now we train the algorithm.
This will happen once a day.
"""

# train the algorithm for providing recommendations to visitors 
exec(train_visitors)

# train the algorithm for providing recommendations to users 
exec(train_users)




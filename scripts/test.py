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
This should happen once a day.
There are two training functions, one for visitors and one for users.
The function below is for visitors. It produces a dataframe that is later used by the functions below that recommend items to visitors.
"""
# train the algorithm for providing recommendations to visitors 
exec(train_visitors)
print(df_items_with_betas.info())

"""
If df_items_with_betas was created, then the function was probably successful.
"""

"""
The function below produces a dataframe that is later used by the functions below that recommend items to users.
"""

# train the algorithm for providing recommendations to users 
exec(train_users)
print(df_users_items_with_betas.info())

"""
If df_users_items_with_betas was created, then the function was probably successful.
"""

"""
We are now ready to test providing a recommendation to a visitor.
"""
# run the script for choosing one item for an online visitor
theme = 'all'
mood = 'Reflective'
exec(choose_item_online_visitor)

from choose_item_online_visitor import *

# examine the results
print(df_results)

"""
The output is supposed to be a dataframe that contains:
    a. The modelid (The code randomly chooses one model out of two possibilites, the purpose is to A/B test the recommendation model)
    b. The model name
    c. The itemid of the recommended item

Now let's check whether the item has the theme or mood that the visitor has chosen.
"""

# check item has the chosen theme or mood
check_item_theme_mood(theme, mood)

"""
The recommended item should have the chosen theme or the chosen moood, in case the user chose a theme or a mood.
"""

"""
We now test the script that provides a recommendation to an online visitor.
For the test, we choose a random userid. Note that in production, the userid will be provided by the PWA.
"""
# Randomly choose one userid
df_users_requesting_recommendation = create_users_requesting_recommendation(df_users, 1)
# make sure that it worked properly
print(df_users_requesting_recommendation)

# choose an item for this user
exec(choose_item_online_user)
print(df_results)

"""
The output is supposed to be a dataframe that is similar to the one described above. 
If this is indeed the output, then the test is successful.
"""

"""
The final tests is for mutliple users who chose to receive recommendations
via email or mobile phone. This should run once a day.
Similar to the test above, we choose the userids randomly but in production they will be provided by the PWA.
"""
# Randomly choose multiple userids
df_users_requesting_recommendation = create_users_requesting_recommendation(df_users, 5)
# make sure that it worked properly
print(df_users_requesting_recommendation)

# choose an item for this user
exec(choose_items_many_offline_users)
print(df_results)

"""
The output should be a dataframe that has the same columns as the previous ones,
but mutliple rows (one for each user).
If this is indeed the output, then the test is successful.
"""

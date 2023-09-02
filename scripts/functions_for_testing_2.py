#########################################################
#### Functions for testing the recommendation system ####
#########################################################

##############################################################
### create a dataframe of users requesting recommendations ###
##############################################################

import pandas as pd

def create_users_requesting_recommendation(df_users, n):
    """
    Creates a dataframe with 'n' unique userids from the provided dataframe 'df_users'.

    Parameters:
    - df_users: Dataframe containing user data.
    - n: Number of unique userids to be included in the output dataframe.

    Returns:
    - df_users_requesting_recommendation: Dataframe containing 'n' unique userids.
    """
    
    # Get unique values
    unique_values = df_users['userid'].unique()

    # Create a subset using the first 'n' unique values.
    subset = unique_values[:n]

    # Create new series from subset of unique values
    df_users_requesting_recommendation = pd.Series(subset)

    # Convert the series to a dataframe
    df_users_requesting_recommendation = df_users_requesting_recommendation.to_frame()

    # Change column name to 'userid'
    df_users_requesting_recommendation.columns = ['userid']

    return df_users_requesting_recommendation

###########################################################################################################
### Check whether the online recommendation for a user or for a visitor has the specified theme or mood ###
###########################################################################################################

def check_item_theme_mood(theme, mood):
    """
    Display details of the recommended items based on given theme and mood.

    The function merges `df_results` with `df_items` based on the item ID, 
    and for each recommended item, it displays:
        - Item name
        - Themes associated with the item
        - Moods associated with the item
        - Whether the chosen theme matches any of the item's themes
        - Whether the chosen mood matches any of the item's moods

    Parameters:
        - theme (str): The chosen theme to check against the item's themes. 
                       Use 'all' if no specific theme is chosen.
        - mood (str): The chosen mood to check against the item's moods.
                      Use 'all' if no specific mood is chosen.

    Note:
        - The function assumes the existence of global dataframes `df_results` and `df_items`.
        - 'NaN' values in themes or moods are excluded from the display.
    """
    
    # If both theme and mood are 'all', print the message and exit
    if theme == 'all' and mood == 'all':
        print("No specific theme or mood was chosen.")
        return

    # Merging the dataframes to get item details
    item_details = pd.merge(df_results, df_items, left_on='recommended_item', right_on='itemid')
    
    for _, item in item_details.iterrows():
        # Display the item name (ititle)
        print(f"\nItem Name: {item['ititle']}")
        
        # Extract themes and moods while ensuring they are strings
        themes = item[['itheme1', 'itheme2', 'itheme3', 'itheme4', 'itheme5']].astype(str)
        # Exclude 'nan' from themes for display
        print(f"Themes: {', '.join([th for th in themes if th != 'nan'])}")
        
        moods = item[['imood1', 'imood2', 'imood3']].astype(str)
        # Exclude 'nan' from moods for display
        print(f"Moods: {', '.join([md for md in moods if md != 'nan'])}")
        
        theme_matched = False
        # Check if chosen theme is in the themes of the item
        if theme != 'all':
            for i, th in enumerate(themes, 1):
                if th == theme:
                    print(f"The recommended item has the chosen theme (itheme{i})")
                    theme_matched = True
                    break
            if not theme_matched:
                print(f"The recommended item does not have the chosen theme ({theme}).")
        
        mood_matched = False
        # Check if chosen mood is in the moods of the item
        if mood != 'all':
            for i, md in enumerate(moods, 1):
                if md == mood:
                    print(f"The recommended item has the chosen mood (imood{i})")
                    mood_matched = True
                    break
            if not mood_matched:
                print(f"The recommended item does not have the chosen mood ({mood}).")


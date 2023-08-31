### create df_users_requesting_recommendation ###

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

# Example usage:
df_users_requesting_recommendation = create_users_requesting_recommendation(df_users, 5)
print(result_df)

#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\nikol\OneDrive\Documents\premier_finale.csv")


# # Case when there are no red cards issued for both venues

# In[67]:


#Group matches by their ranks. Each rank corresponds to 2 matches under 2 different perspectives, home team and away team.
red_cards_per_match = df.groupby('MatchRank')['RedCards'].sum()
#Filter only the matches where the sum of their red card columns = 0 and select their indexes
matches_no_red_cards = red_cards_per_match[red_cards_per_match == 0].index
#Filter data frame df by only entries within the indexes selected previously
filtered_data = df[df['MatchRank'].isin(matches_no_red_cards)]


# In[42]:


#Calculate goal average for Away team when there are no red cards involved 
average_away_goals = filtered_data[filtered_data['Venue'] == 'Away']['AwayGoals'].mean()
average_away_goals


# In[44]:


#Calculate goal average for Home team when there are no red cards involved 

average_home_goals = filtered_data[filtered_data['Venue'] == 'Home']['HomeGoals'].mean()
average_home_goals


# In[255]:


# Plotting average goals for both venues


units = ['Average goals for home team', 'Average goals for away team']
values = [1.5483002356109055,1.1868057892965331]

# Plotting the column chart
plt.figure(figsize=(6, 4))  
plt.bar(units, values, color=['skyblue', 'salmon'])  
plt.xlabel('Venues')  
plt.ylabel('Average Goals')  
plt.title('Average goals when red cards were not issued ')  
plt.tight_layout()  
plt.show()  


# In[68]:


# Filter for matches where the home team won

home_wins = filtered_data[(filtered_data['Venue'] == 'Home') & (filtered_data['Match Outcome'] == 'Win')]

# Total number of matches where no red cards were issued for both venues and the home team won
total_home_wins = len(home_wins)

# Total number of matches where no red cards were issued for both venues
total_matches_no_red_cards = len(matches_no_red_cards)

# Calculate the percentage of wins for the home team
percentage_home_wins = (total_home_wins / total_matches_no_red_cards) * 100

percentage_home_wins






# In[70]:


# Filter for matches where the away team won

away_wins = filtered_data[(filtered_data['Venue'] == 'Away') & (filtered_data['Match Outcome'] == 'Win')]

# Total number of matches where no red cards were issued for both venues and the home team won
total_away_wins = len(away_wins)

# Total number of matches where no red cards were issued for both venues
total_matches_no_red_cards = len(matches_no_red_cards)

# Calculate the percentage of wins for the away team
percentage_away_wins = (total_away_wins / total_matches_no_red_cards) * 100

percentage_away_wins


# In[259]:


percentage_tie_wins = 100- percentage_home_wins - percentage_away_wins
percentage_tie_wins


# In[266]:


labels = ['Home team wins', 'Away team wins','Draw']
sizes = [45.77583305284416, 29.38404577583305,24.840121171322785]  # Represents the percentages for Car and Bike

# Plotting the pie chart
plt.figure(figsize=(6, 6))  # Adjust the figure size if needed
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'salmon','yellow'])
plt.title('Percentage of Units')  # Title of the plot
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()  # Adjust layout
plt.show()  # Display the plot


# # Case when one red card is issued for home team solely.

# In[185]:


# Group matches by their 'MatchRank'
grouped_by_match_rank = df.groupby('MatchRank')

# Filter matches for each 'MatchRank' where home team received one red card and away team received zero red cards
home_one_red_matches = pd.DataFrame()  # Initialize an empty DataFrame to store filtered matches

for match_rank,  group_data in grouped_by_match_rank:
    home_one_red = group_data[(group_data['Venue'] == 'Home') & (group_data['RedCards'] == 1)]
    away_zero_red = group_data[(group_data['Venue'] == 'Away') & (group_data['RedCards'] == 1)]
    
    if not home_one_red.empty and away_zero_red.empty:
        home_one_red_matches = pd.concat([home_one_red_matches, group_data])

home_one_red_matches


# In[233]:


#Average goals for home team

home_team_home_one_red_matches = home_one_red_matches[home_one_red_matches['Venue']=='Home']['HomeGoals'].mean()
home_team_home_one_red_matches


# In[234]:


# Average goals for away team

away_team_home_one_red_matches = home_one_red_matches[home_one_red_matches['Venue']=='Away']['AwayGoals'].mean()
away_team_home_one_red_matches


# In[256]:


# Plotting average goals for both venues


units = ['Average goals for home team', 'Average goals for away team']
values = [1.1893491124260356, 1.7041420118343196]

# Plotting the column chart
plt.figure(figsize=(6, 4))  
plt.bar(units, values, color=['skyblue', 'salmon'])  
plt.xlabel('Venues')  
plt.ylabel('Average Goals')  
plt.title('Average goals scored when only one red card was issued to the home team')  
plt.tight_layout()  
plt.show()  




# In[227]:


# Percentage of Matches where home team won 

home_one_red_matches_home_wins = home_one_red_matches[(home_one_red_matches['Venue'] == 'Home') & (home_one_red_matches['Match Outcome'] == 'Win')]

# Total number of matches where no red cards were issued for both venues and the home team won
total_home_one_red_matches_home_wins = len(home_one_red_matches_home_wins)

# Total number of matches where no red cards were issued for both venues
total_matches_home_one_red_matches = len(home_one_red_matches)/2

# Calculate the percentage of wins for the home team
percentage_home_one_home_red_wins = (total_home_one_red_matches_home_wins / total_matches_home_one_red_matches) * 100

percentage_home_one_home_red_wins


# In[230]:


# Percentage of Matches where away team won 

away_one_red_matches_home_wins = home_one_red_matches[(home_one_red_matches['Venue'] == 'Away') & (home_one_red_matches['Match Outcome'] == 'Win')]

# Total number of matches where no red cards were issued for both venues and the home team won
total_away_one_red_matches_home_wins = len(away_one_red_matches_home_wins)

# Total number of matches where no red cards were issued for both venues
total_matches_home_one_red_matches = len(home_one_red_matches)/2

# Calculate the percentage of wins for the home team
percentage_away_one_home_red_wins = (total_away_one_red_matches_home_wins / total_matches_home_one_red_matches) * 100

percentage_away_one_home_red_wins


# In[232]:


# Percentage of Matches with ties 

percentage_ties_one_home_red_wins = 100- percentage_home_one_home_red_wins - percentage_away_one_home_red_wins
percentage_ties_one_home_red_wins


# In[299]:


labels = ['Win','Lose','Draw']
sizes = [26.035502958579883,50.29585798816568,23.668639053254438]  # Represents the percentages for Car and Bike

# Plotting the pie chart
plt.figure(figsize=(5, 5))  
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'salmon','yellow'])
plt.title('Home team match outcome')  
plt.axis('equal')  
plt.tight_layout()  
plt.show()  


# # Case when one red card is issued for away team solely.

# In[207]:


# Group matches by their 'MatchRank'
grouped_by_match_rank = df.groupby('MatchRank')

# Filter matches for each 'MatchRank' where home team received one red card and away team received zero red cards
away_one_red_matches = pd.DataFrame()  # Initialize an empty DataFrame to store filtered matches

for match_rank,  group_data in grouped_by_match_rank:
    home_one_red = group_data[(group_data['Venue'] == 'Away') & (group_data['RedCards'] == 1)]
    away_zero_red = group_data[(group_data['Venue'] == 'Home') & (group_data['RedCards'] == 1)]
    
    if not home_one_red.empty and away_zero_red.empty:
        away_one_red_matches = pd.concat([away_one_red_matches, group_data])

away_one_red_matches


# In[208]:


# Average away goals
away_one_red_matches[away_one_red_matches['Venue']=='Away']['AwayGoals'].mean()


# In[209]:


# Average home goals

away_one_red_matches[away_one_red_matches['Venue']=='Home']['HomeGoals'].mean()


# In[257]:


# Plotting average goals for both venues


units = ['Average goals for home team', 'Average goals for away team']
values = [1.9669421487603307,0.8636363636363636]

# Plotting the column chart
plt.figure(figsize=(6, 4))  
plt.bar(units, values, color=['skyblue', 'salmon'])  
plt.xlabel('Venues')  
plt.ylabel('Average Goals')  
plt.title('Average goals scored when only one red card was issued to the away team')  
plt.tight_layout()  
plt.show()  


# In[220]:


# Percentage of Matches where home team won 

away_one_red_matches_home_wins = away_one_red_matches[(away_one_red_matches['Venue'] == 'Home') & (away_one_red_matches['Match Outcome'] == 'Win')]

# Total number of matches where no red cards were issued for both venues and the home team won
total_away_one_red_matches_home_wins = len(away_one_red_matches_home_wins)

# Total number of matches where no red cards were issued for both venues
total_matches_away_one_red_matches = len(away_one_red_matches)/2

# Calculate the percentage of wins for the home team
percentage_home_one_away_red_wins = (total_away_one_red_matches_home_wins / total_matches_away_one_red_matches) * 100

percentage_home_one_away_red_wins




# In[222]:


# Percentage of Matches where away team won 

away_one_red_matches_away_wins = away_one_red_matches[(away_one_red_matches['Venue'] == 'Away') & (away_one_red_matches['Match Outcome'] == 'Win')]

# Total number of matches where no red cards were issued for both venues and the home team won
total_away_one_red_matches_away_wins = len(away_one_red_matches_away_wins)

# Total number of matches where no red cards were issued for both venues
total_matches_away_one_red_matches = len(away_one_red_matches)/2

# Calculate the percentage of wins for the home team
percentage_away_one_away_red_wins = (total_away_one_red_matches_away_wins / total_matches_away_one_red_matches) * 100

percentage_away_one_away_red_wins



# In[224]:


# Percentage of Matches with ties
percentage_ties_one_away_red_wins = 100 - percentage_home_one_away_red_wins - percentage_away_one_away_red_wins
percentage_ties_one_away_red_wins


# In[280]:


labels = ['Win','Lose','Draw']
sizes = [13.636363636363635, 61.15702479338842, 25.206611570247944]  # Represents the percentages for Car and Bike

# Plotting the pie chart
plt.figure(figsize=(5, 5))  
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'salmon','yellow'])
plt.title('Away team match outcome')  
plt.axis('equal')  
plt.tight_layout()  
plt.show()  


# In[ ]:





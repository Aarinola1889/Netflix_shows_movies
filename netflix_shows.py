import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Step 1: Renaming the dataset
old_file_name = "netflix_data.csv"
new_file_name = "Netflix_shows_movies"

# Unzip the dataset
df = pd.read_csv("old_file_name")

# Load the dataset
netflix_data = pd.read_csv(new_file_name)

 
# Step 2: Data Cleaning
# Addressing missing values
missing_data = netflix_data.isnull().sum()

# Handle missing values by dropping rows with missing values
netflix_cleaned = netflix_data.dropna()

# Verify missing values have been addressed
print(netflix_cleaned.isnull().sum())
netflix_cleaned.head()

# Step 3: Data Exploration
# Data descriptions and statistical analysis
data_description = netflix_cleaned.describe(include="all")
print(data_description)

# Step 4: Data Visualization
# Most watched genres
plt.figure(figsize=(12, 6))
genre_counts = netflix_cleaned["listed_in"].value_counts().head(10)
sns.barplot(x=genre_counts.values, y=genre_counts.index)
plt.title("Top 10 Most Watched Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genres")
plt.xticks(range(0, max(genre_counts) + 50, 50))
plt.tight_layout()
plt.show()

# Calculate frequency of each rating and sort in descending order
rating_counts = netflix_cleaned['rating'].value_counts().sort_values(ascending=False)

# Plot the distribution of ratings
plt.figure(figsize=(10, 6))
sns.barplot(x=rating_counts.index, y=rating_counts.values)
plt.title('Distribution of Ratings on Netflix')
plt.xlabel('Ratings')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.yticks(range(0, max(rating_counts) + 200, 200))
plt.show()

# Step 5: Export to CSV file for R visualization
netflix_cleaned.to_csv("Netflix_cleaned.csv", index=False)
import pandas as pd

# Read data from file
df = pd.read_csv('https://docs.google.com/spreadsheets/d/15e2bJgHcs0qlt2QFq0UvhGHVZE6wfheNJOZL4G_IPSs/export?format=csv')
print(df.head())

def calculate_demographic_data(print_data=True):

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df["race"]).value_counts()
    
    # What is the average age of men?
    average_age_men = df[df["sex"] == 'Male']["age"].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors =(df[df["education"] == "Bachelors"]["education"].count()/df["education"].count()*100).round(1)
    

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    condition = (df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate")
   
    

    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
 
    
    higher_education = df[condition]
    higher_education_count = higher_education.salary.count()
    higher_education_over_50k= higher_education[higher_education.salary == ">50K"].salary.count()

    lower_education = df[~condition]
    lower_education_count = lower_education.salary.count()
    lower_education_over_50k= lower_education[lower_education.salary == ">50K"].salary.count()
   
    # percentage with salary >50K
    higher_education_rich = (higher_education_over_50k/higher_education_count*100).round(1)
    lower_education_rich = (lower_education_over_50k/lower_education_count*100).round(1)
  
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    condition_min_hr=df["hours-per-week"] == min_work_hours
    min_workers = df[condition_min_hr]
    num_min_workers = (min_workers.salary).count()
    min_workers_rich = min_workers[min_workers.salary == ">50K"].salary.count()
    rich_percentage = int((min_workers_rich/num_min_workers)*100)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_countries = df[df['salary'] == ">50K"]['native-country']
    country_count= df['native-country'].value_counts()
    highest_earning_countries_count= highest_earning_countries.value_counts()
    highest_earning_countries_percentage = (highest_earning_countries_count/country_count).sort_values(ascending=False)
    highest_earning_country = highest_earning_countries_percentage.index[0]
    highest_earning_country_percentage = (highest_earning_countries_percentage.max()*100).round(1)


    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['salary'] == ">50K") & (df['native-country'] == "India")]["occupation"].value_counts().index[0]


    if print_data:
        seperator = "------------------------------------------------------"
        print(f"Number of each race:\n {race_count} \n{seperator}") 
        print(f"Average age of men:{average_age_men} \n{seperator}")
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}% \n{seperator}")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}% \n{seperator}")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}% \n{seperator}")
        print(f"Min work time: {min_work_hours} hours/week \n{seperator}")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}% \n{seperator}")
        print(f"Country with highest percentage of rich: {highest_earning_country} \n{seperator}")
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}% \n{seperator}")
        print("Top occupations in India:", top_IN_occupation)

print(calculate_demographic_data())
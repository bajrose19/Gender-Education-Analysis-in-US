#This program uses a data set containing information on the percentage of men and women enrolled in different levels of education, specifically in the USA. The program shows the percentage of enrollment for each year, and shows the average of % of enrollement for men and taverage for women(for each level of education). *primary = elementary school, lower secondary = middle school/junior high, and upper secondary = high school.*

#dataframes and link 
import pandas as pd 
education_link = pd.read_csv("assignments/Education.csv")
import matplotlib.pyplot as plt


female_primary = []
male_primary = []
female_lower_secondary = []
male_lower_secondary = []
female_upper_secondary = []
male_upper_secondary = []
female_bachelor = []
male_bachelor = []

#The csv file will read the year and percentage for each gender and their level of education as values, using for loops and if statements.
for each_value in education_link.values:
  if each_value[2] == "United States" and each_value[0] == "Educational attainment, at least completed primary, population 25+ years, female (%) (cumulative)":
    female_primary.append(each_value)
  if each_value[2] == "United States" and each_value[0] == "Educational attainment, at least completed primary, population 25+ years, male (%) (cumulative)":
    male_primary.append(each_value)
  if each_value[2] == "United States" and each_value[0] == "Educational attainment, at least completed lower secondary, population 25+, female (%) (cumulative)":
    female_lower_secondary.append(each_value)
  if each_value[2] == "United States" and each_value[0] == "Educational attainment, at least completed lower secondary, population 25+, male (%) (cumulative)":
    male_lower_secondary.append(each_value)
  
  if each_value[2] == "United States" and each_value[0] == "Educational attainment, at least completed upper secondary, population 25+, female (%) (cumulative)":
    female_upper_secondary.append(each_value)
  if each_value[2] == "United States" and each_value[0] == "Educational attainment, at least completed upper secondary, population 25+, male (%) (cumulative)":
    male_upper_secondary.append(each_value)
  
  if each_value[2] == "United States" and each_value[0] == "Educational attainment, at least Bachelor's or equivalent, population 25+, female (%) (cumulative)":
    female_bachelor.append(each_value)
  if each_value[2] == "United States" and each_value[0] == "Educational attainment, at least Bachelor's or equivalent, population 25+, male (%) (cumulative)":
    male_bachelor.append(each_value)
  
  

    


#Creates the dataframe for female primary school (elementary school K-5th grade) and prints it out, as well as calculates the average for all the values in the dataframe using pandas.
new_df = pd.DataFrame(data= female_primary, columns = education_link.columns)
sort = (new_df.sort_values("Year"))
sort_1 = sort[["Year","Value"]]
print(f"Percentage of American females that has at least completed primary school:{sort_1}")
meanfemaleprimary = new_df['Value'].mean()
print(f"The average for women that completed in primary education in the US is {int(meanfemaleprimary)}%")

#Creates the dataframe for male primary school (elementary school K-5th grade) and prints it out, as well as calculates the average for all the values in the dataframe using pandas.
new_df1 = pd.DataFrame(data= male_primary, columns = education_link.columns)
sort_male_primary = (new_df1.sort_values("Year"))
sort_male_primary_1 = sort_male_primary[["Year", "Value"]]
print(f"% of American males that have at least completed primary school:         {sort_male_primary_1}")
meanmaleprimary = new_df1['Value'].mean()
print(f"The average for men that completed in primary education in the US is {int(meanmaleprimary)}%")

#Creates the dataframe for female lower secondary school (middle school 6-8th grade) and prints it out, as well as calculates the average for all the values in the dataframe.
new_df2 = pd.DataFrame(data= female_lower_secondary, columns = education_link.columns)
sort_female_lower_secondary = (new_df2.sort_values("Year"))
sort_female_lower_secondary_1 =sort_female_lower_secondary[["Year", "Value"]]
print(f"% of American females that have at least completed lower secondary school:{sort_female_lower_secondary_1}")
meanfemalelowersec = new_df2['Value'].mean()
print(f"The average for women that completed in lower secondary education in the US is {int(meanfemalelowersec)}%")

#Creates the dataframe for male lower secondary school (middle school 6-8th grade) and prints it out, as well as calculates the average for all the values in the dataframe.
new_df3 = pd.DataFrame(data= male_lower_secondary, columns = education_link.columns)
sort_male_lower_secondary = (new_df3.sort_values("Year"))
sort_male_lower_secondary_1 =sort_male_lower_secondary[["Year", "Value"]]
print(f"% of American males that have at least completed lower secondary school:{sort_male_lower_secondary_1}")
meanmalelowersec = new_df3['Value'].mean()
print(f"The average for men that completed in lower secondary education in the US is {int(meanmalelowersec)}%")

#Creates the dataframe for female upper secondary school (high school 8-12th grade) and prints it out, as well as calculates the average for all the values in the dataframe.
new_df4 = pd.DataFrame(data= female_upper_secondary, columns = education_link.columns)
sort_female_upper_secondary = (new_df4.sort_values("Year"))
sort_female_upper_secondary_1 =sort_female_upper_secondary[["Year", "Value"]]
print(f"% of American females that have at least completed upper secondary school:{sort_female_upper_secondary_1}")
meanfemaleuppersec = new_df4['Value'].mean()
print(f"The average for women that completed in upper secondary education in the US is {int(meanfemaleuppersec)}%")

#Creates the dataframe for male upper secondary school (high school 8-12th grade) and prints it out, as well as calculates the average for all the values in the dataframe.
new_df5 = pd.DataFrame(data= male_upper_secondary, columns = education_link.columns)
sort_male_upper_secondary = (new_df5.sort_values("Year"))
sort_male_upper_secondary_1 =sort_male_upper_secondary[["Year", "Value"]]
print(f"% of American males that have at least completed upper secondary school:{sort_male_upper_secondary_1}")
meanmaleuppersec = new_df5['Value'].mean()
print(f"The average for men that completed in upper secondary education in the US is {int(meanmaleuppersec)}%")

#Creates the dataframe for females in college (bachelor years, 4 years) and prints it out, as well as calculates the average for all the values in the dataframe.
new_df6 = pd.DataFrame(data= female_bachelor, columns = education_link.columns)
sort_female_bachelor = (new_df6.sort_values("Year"))
sort_female_bachelor_1 =sort_female_bachelor[["Year", "Value"]]
print(f"% of American females that have at least attained a bachelor's degree:{sort_female_bachelor_1}")
meanfemalebach = new_df6['Value'].mean()
print(f"The average for women that completed in their bachelor degree in college in the US is {int(meanfemalebach)}%")

#Creates the dataframe for males in college (bachelor years, 4 years) and prints it out, as well as calculates the average for all the values in the dataframe.
new_df7 = pd.DataFrame(data= male_bachelor, columns = education_link.columns)
sort_male_bachelor = (new_df7.sort_values("Year"))
sort_male_bachelor_1 =sort_male_bachelor[["Year", "Value"]]
print(f"% of American males that have at least attained a bachelor's degree:{sort_male_bachelor_1}")
meanmalebach = new_df7['Value'].mean()
print(f"The average for men that completed in their bachelor degree in college in the US is {int(meanmalebach)}%")

#This part of the program prints out a bar graph that compares the graduation/completion rate of women vs. 
#men throughout each level of education. Pink for primary, blue for lower secondary, cyan for upper secondary, and purple for bachelors degree. 
#Using matplotlib.pyplot to create these commands.
x_axis=["f primary", "m primary", "f.l. secondary" , "m.l. secondary", "f.u. secondary","m u. secondary.", "f bachelor", "m bachelor"]
height=[98, 98, 93, 92, 88, 87, 33, 33]

plt.bar(x_axis, height, label= "f = female, m = male, l= lower, u = upper")
plt.title("Avg. % of completion in each level of education, women + men in the USA")
plt.xlabel("Average")
plt.ylabel("Percentage")
plt.legend()
plt.xticks(fontsize = 5)
plt.bar(x_axis, height, color=['pink', 'pink', 'blue', 'blue', 'cyan', 'cyan', 'purple', 'purple'])
plt.savefig("bargraph.jpg")
plt.show()

#Another plot diagram, but a line plot comparing the graduation rate between men and women in 
#lower secondary specifically because it's interesting how it increased throughout the years
plt.plot(sort_female_lower_secondary_1["Year"],sort_female_lower_secondary_1["Value"], label="female")
plt.plot(sort_male_lower_secondary_1["Year"],sort_male_lower_secondary_1["Value"], label="male")
plt.title("Lower Sec. Avg. Completion % Women vs. Men Throughout the Years")
plt.xlabel("Years")
plt.ylabel("Percentage")
plt.legend()
plt.show()
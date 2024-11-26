import pandas as pd 
import matplotlib.pyplot as plt


#storing data 

df = pd.DataFrame({
    "name": [
        "Daniel, Mr Masi",
        "chris, Mr Kinungi",
        "tina, Madam moheia",
    ],
    "Age": [20,21,22],
    "sex": ["male", "male", "female"],
})

print(df)

print(df["Age"])

print(df["Age"].max())

print(df.describe())

titanic = pd.read_csv("titanic.csv")

print(titanic)
print(titanic.head(8))

ages = titanic['Age']
print(ages.head())

age_sex = titanic[["Age", "Sex"]]
print(age_sex.head())


above_35 = titanic[titanic["Age"] > 35]
print(above_35.head())

class_2_3 = titanic[titanic["Pclass"].isin([2, 3])]
print(class_2_3.head())

age_no_na = titanic[titanic["Age"].notna()]
print(age_no_na.head())

adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print(adult_names.head())

titanic.iloc[9:25, 2:5]
print(titanic)

air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)
print(air_quality.head())

air_quality.plot()
plt.show()

air_quality["station_paris"].plot()
plt.show()

air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()

air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
print(air_quality.head())
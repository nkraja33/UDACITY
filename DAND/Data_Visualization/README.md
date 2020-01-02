# House Price Data Visualization

##1.  Story Line

 >For Every Person in the world, There are three main things which are the basic need for a human, they are:

   1. **Food**
   2. **Cloth**
   3. **Home**

   One can obtain **Food and clothes** with a low or easily affordable price by doing a small or daily wages, But when coming in to **Home**, it is a big dream for many people. I am one among them, I have been dreamed a lot about buying a new home but money is the main factor to purchase a home and finally I got one.

  Nowadays, It is really hard for anyone to easily buy a home, because the home price is huge based on some key criteria which will decide the house price. One needs to deeply understand the key parameters before looking for a new home based on his budget and requirements

  By knowing the parameters and requirements we can look for a better home which will fit in our budget. One of the parameter which everyone consider is the neighbourhood. So with all this in mind, i will interpret with the parameters in the below data set and will give a clear picture which are all the additional parameters that helps in finding a better home.

>Please take look on "**House_Price_Explanatory_Analysis.html**" file to know about the paramaeters i have used or please use the "**House_Price_Explanatory_Analysis_slided.html**" for a slide show.


 #### About Data:

  > For this Project I used "house_prices.csv" dataset which is downloaded from **UDACITY** `Resource` tab.

  - **house_id**: This columns has discrete values of house id.
  - **neighborhood**: This column has Ordinal values of neighbourhood list which places a key role in deciding the price.
  - **area**: This columns has continuous value of area size for the house in sq. Meters
  - **bedrooms**: This column has discrete values of number of bedrooms.
  - **bathrooms**: This column has discrete values of number of bathrooms.
  - **style**: This column has  Ordinal value of the house type/style which is also key parameter for price.
  - **price**: This is answer column for all other columns, it has continuous values of house price in dollars.

  With all these information let's work on the below data and will get the house price

## 2.  Package Import
> Here I Imported all required libraries and given a alias for each library to access them easily. Then applied the `%matplotlib inline` magic keyword which will plot the chart in the notebook and Also I applied a background style for all the charts that are going to be plotted through out the project using `sns.set_style("whitegrid")`.

##3 . Data Wrangling
> In this section I **Gathered** the data by loading the `house_prices.csv` to a pandas Data Frame.
Then **Assessed** the data for any errors and found only issues they are.
- `house_id` is unique for all rows which will not help us in our analysis so we can drop this column
- Columns `neighborhood` and `style` needs to be converted to category type
Then I have cleaned the data .
>
Then I **Cleaned** the data by fixing the issues that were identified during **Assess**.

## 4 . Exploratory Data Analysis

> Here I analysed the data to get the price of the house by interpreting other parameters. And after each observation I polished all the charts for better View. In this section I applied the below data visualization techniques to plot the parameters.
- Univariate Exploration
- Bivariate Exploration
- Multivariate Exploration
>
With help of these visualization technics I found the below conclusion points from the given data.

## 5. Conclusion

> After interpreting with all the parameters in the given data set, we observed the below key points

- There is a skewness in the area column due to the large area of Victorian houses, in which it indicates these houses are built for luxury and expensive.
- We observed there are **1367** house with 4 bedrooms and **59** houses with 8 bedroomed houses in our data. Also we can see there **245** houses with 0 bedrooms, which are Lodge styles houses
- By the proportion of `Style` and `Neighbourhood` columns, There are many houses with `Victorian` style and Many Houses with `B` as Neighbourhood in the data set.
- By Comparing the both `style` and `neighborhood` parameters, We see that all  Neighbourhood has different styles of houses
- We found that the mean area of all `Neighborhood` as are in same location and as well min, first & third quartile values only the maximum value differs due to the outlier values of Victorian style homes between `Neighborhood` and `area`
- With `Style` and House `Area`. We can see a many outlier points above the max whisker of Victorian box. we can observe there are outlier values for each style houses which decides the price of the house
- By getting the number houses based on the bedrooms for each style, We observed that lodge houses has max 6 bedrooms, where ranch houses has till 5 bedrooms and Victorian houses has 8 bedrooms in the dataset.
- From **Facet Scatter Plot** between `bedrooms`, `area`, `style' and `neighbourhood` we came to know that lodge style home has max 2 bathrooms and Victorian houses has 5 bathrooms and the high area house are in B neighbour in Victorian style houses
- From **Pair Plot** it clearly shows that we have linear relation between `bathrooms` and `bedrooms` and between `area` and `price`
- From **Heat Map** between  `style` and `neighborhood` parameters. We can see that `Neighbourhood B` and `Victorian Style` are more with **1207** house and `Neighbourhood C` and `Lodge Style` are less with **346** houses.
- And Finally from  **Point plot** We got the central tendency uncertainty of the standard deviation error between `style` and `neighborhood` based on `price` parameter.

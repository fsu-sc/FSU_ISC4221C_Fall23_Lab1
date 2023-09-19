<h1 style="text-align:center;">ISC4221C Discrete Algorithms for Science Applications (Fall 2023) Lab 1</h1>

## Goals
The objectives of this lab are to implement two brute force approaches to sorting a real one dimensional array in ascending order; the methods we use are **selection sort** and **bubble sort**. Then, we apply the sort algorithm to the simple problem of determining the closest store location to you from a given list of stores.Locations will be given in latitude and longitude so we must be able to determine distances using these coordinates; to this end, we will introduce the [Haversine](https://en.wikipedia.org/wiki/Haversine_formula) formula. In addition, you will gain experience working with strings of letters in Python.  

**All your answers should be in a single file named `answers_lab.py`, be careful with the names of your functions. Your report should be a self contained markdown file with a summary of your answers and the code copied inside of it.**
 
###  1. (20 points) Selection sort ###
  Implement the Selection Sort algorithm for sorting an array of `n` real numbers in ascending order. You should write a function whose input is the array to be sorted and the output is the sorted array. 
  Your selection sort algorithm should be implemented in a functon called `my_selection_sort` with the following structure:

```python
    def my_selection_sort(array):
        # your code here
        return sorted_array
```

  
###  2.(20 points) Bubble Sort  ###

Implement the Bubble Sort algorithm for sorting an array of `n` real numbers in ascending
order as in Problem 1.

Your bubble sort algorithm should be implemented in a functon called `my_bubble_sort` inside `answers_lab.py`.

### 3. (40 points) Sorting exercise.

In this problem we will use either of the algorithms implemented above to solve a particular
problem. Suppose you work for a company that has stores in 7 cities in Florida and when a potential customer calls, you want to be able to **tell the person what stores are closest and how far away they are**.

We are providing you with the following information:

* The names of the cities where the stores are located and their locations are given in latitude and longtitude (in the unit of degree, in the file “stores_location.dat”)

* Because the locations are given in latitude and longitude, we need a formula to calculate the
distance between two cities. We will use the Haversine formula. Basically if you have coordinates (lat1, lon1) and (lat2, lon2) then the [Haversine](https://en.wikipedia.org/wiki/Haversine_formula) formula is

$$haversin \left (\frac{distance}{R} \right ) =  haversin(lat2 − lat1) + cos(lat1)cos(lat2) haversin(lon2 − lon1)$$

where `R` is the radius of the earth and $haversin(θ) = sin^2(\frac{\theta}{2})$ . Note that when implementing this formula you need to take care of converting degrees to radians. To make sure that you have the conversion
correct, try to test the coordinates of Tallahassee and Gainesville and check if you get the approximate
mileage. 

Your search city function should be implemented in a functon called `cities_distances` inside `answers_lab.py` with the following structure:

```python
    # The function will receive some latitude and longitude and provide a list of cities 
    # and distances to those cities in order of increasing distance.
    def cities_distances((lat,lon)):
        # your code here
        return cities, distances
```

If you want to make the tests work smoothly, the cities should be an array of strings with the names of the cities and the distances should be an array of floats with the distances to the cities.

## Tips for Python

* **Testing your code**. The suggested structure for you code is to have a `main.py` file, that will be used to call your answers in `answers_lab.py`. For example, if you want to test your code for problem 1, you can have the following structure in `main.py`:
```python
import answers_lab as ans
array = [4, 2, 3, 1, 5]
sorted_array = ans.my_selection_sort(array)
print(sorted_array)
```

* **Loading data file**. To load data from files. Here is a sample code:
```python
file1 = open('stores_location.dat', 'r') # open file
Lines = file1.readlines()
# read all lines
file1.close()
# close file
for line in Lines:
# loop over each line
    storeID, location, latitude, tmp, longtitude, tmp = line.split()
    print(storeID,location,latitude,longtitude)
```
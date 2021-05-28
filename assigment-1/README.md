## Matrix manipulation

Implement a class called MetaMat that will allow to manipulate matrices using numpy and pandas. Your class will have state variables `__List`, `__PFrame`, and `__NMatrix` representing a list a numpy matrix and a pandas matrix respectively. All your values in all three models must be of same type.

define a class

```python
class MetaMat:
```

The main function of this class is to synchronize the three representations. That is you initialize the class with

__init__(self, list):

inside you have to store it properly in the three corresponding hidden variables as three distinct representations.

The methods available to user are:


- `appendToList(number)` - it will append a number to the list __List and updates the other representations
- `changeNElement(x,y,value)` - changes single value in the __NMatrix with indexes x and y to value. Other representations must be updated.
- `changePRow(keys, row)` - this function allows to change one or more elements in the Panda dataframe. Keys is one or more column names and row is index from 0 to rows-1

Make a three special internal methods that will simply update two other representations from the other one:
- `updateFromL()` - this function will create new __NMatrix from the __List and a new __PFrame from __List
- `updateFromP()`- this function will create new __NMatrix from the __PFrame and a new  from __List__PFrame
- `updateFromN()`- this function will create new __List from the __NMatrix and a new __PFrame from __NMatrix

Hint to create a new Numpy Array from list use numpy.array or numpy.asarray. To create a new __PFrame dataframe, use the following function
```python
df = pd.DataFrame(a,columns=['C1','C2','C3','C4','C5'])
```
where the columns names you have to generate automatically according to the size of the Numpy Array.
To modify a particular element in the Panda DF you can use `iloc[rowIndex][ColumnKey]`. For example if I create a numpy array A of size 5 by 5, then I create a Pandas dataframe using `df = pd.DataFrame(A,columns=['C1','C2','C3','C4','C5'])`. and then I can modify second row  by

```python
df.iloc[1][:] = data
# or I can modify any element of a row by adding the key of column
df.iloc[1]['C2'] = data
```
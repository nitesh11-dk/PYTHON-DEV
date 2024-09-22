Sure, here are the questions based on the information and commands you provided:

1. **Installation and Import:**
   - What is NumPy? How do you install it?
   - How do you import NumPy in a Python script?

2. **Arrays vs. Lists:**
   - What is an array and how is it different from a list in Python?
   - What is the name of the built-in array class in NumPy?

3. **Rank of an ndarray:**
   - What do you understand by the rank of an ndarray?

4. **Creating NumPy Arrays:**
   - Create a 1-D array called `zeros` with 10 elements all set to zero.
   - Create a 1-D array called `vowels` with the elements ‘a’, ‘e’, ‘i’, ‘o’, and ‘u’.
   - Create a 2-D array called `ones` with 2 rows and 5 columns, all elements set to 1 and dtype as int.
   - Use nested Python lists to create a 2-D array called `myarray1` with 3 rows and 3 columns containing specific values.
   - Create a 2-D array called `myarray2` using `arange()` with 3 rows and 5 columns, start value 4, step size 4, and dtype as float.

5. **Array Properties and Operations:**
   - Find the dimensions, shape, size, data type of the items, and itemsize of the arrays `zeros`, `vowels`, `ones`, `myarray1`, and `myarray2`.
   - Reshape the array `ones` to have all 10 elements in a single row.
   - Display the 2nd and 3rd element of the array `vowels`.
   - Display all elements in the 2nd and 3rd row of the array `myarray1`.
   - Display the elements in the 1st and 2nd column of the array `myarray1`.
   - Display the elements in the 1st column of the 2nd and 3rd row of the array `myarray1`.
   - Reverse the array `vowels`.

6. **Array Operations:**
   - Divide all elements of the array `ones` by 3.
   - Add the arrays `myarray1` and `myarray2`.
   - Subtract `myarray1` from `myarray2` and store the result in a new array.
   - Multiply `myarray1` and `myarray2` elementwise.
   - Perform matrix multiplication of `myarray1` and `myarray2` and store the result in a new array `myarray3`.
   - Divide `myarray1` by `myarray2`.
   - Find the cube of all elements of `myarray1` and divide the resulting array by 2.
   - Find the square root of all elements of `myarray2`, divide by 2, and round to two decimal places.

7. **Advanced Array Operations:**
   - Find the transpose of the arrays `ones` and `myarray2`.
   - Sort the array `vowels` in reverse order.
   - Sort the array `myarray1` such that it brings the lowest value of the column to the first row.
   - Split the array `myarray2` into 5 arrays columnwise using `numpy.split()` and print them.
   - Split the array `zeros` at indices 2, 5, 7, and 8 and store the resulting arrays in `zerosA`, `zerosB`, `zerosC`, and `zerosD`. Print them.
   - Concatenate the arrays `myarray2A`, `myarray2B`, and `myarray2C` into an array with 3 rows and 3 columns.
   - Create a 2-D array called `myarray4` with 14 rows and 3 columns using `arange()`, and split this array rowwise into 3 equal parts. Print the result.

8. **Array Aggregations:**
   - Find the sum of all elements in `myarray4`.
   - Find the sum of all elements rowwise in `myarray4`.
   - Find the sum of all elements columnwise in `myarray4`.
   - Find the maximum of all elements in `myarray4`.
   - Find the minimum of all elements in each row of `myarray4`.
   - Find the mean of all elements in each row of `myarray4`.
   - Find the standard deviation columnwise in `myarray4`.

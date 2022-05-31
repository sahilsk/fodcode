# Matrix Operations

1. Print matrix

```
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        print( matrix[i][j])

```


2. Reverse matrix rows:


```
reversed(matrix)
```

OR

```
i = 0
j = len(matrix) - 1
while i < j:
    tmp = matrix[i]
    matrix[i] = matrix[j]
    matrix[j] = tmp
```

3. Print elements on other side of the diagonal: (**IMPORTANT**)

Use: Used in rotating matrix


```
for i in range(0, len(matrix)):
    for j in range(i+1, i)):
        print(matrix[i][j])
```


3.1 Print elements on lower side of the diagonal (**IMPORTANT**)


```
for i in range(0, len(matrix)):
    for j in range(0, i)):
        print(matrix[i][j])
```
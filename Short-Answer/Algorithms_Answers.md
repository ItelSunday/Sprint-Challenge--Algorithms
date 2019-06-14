Add your answers to the Algorithms exercises here.
## Exercise I

```
a)  a = 0
    while (a < n * n * n) // 0(1) * 0(n) * 0(n) = 0(n)
      a = a + n * n // 0(1)
```
- The loop is 0(n) as it doesn't modifies n, every loop just increases and 0(n) terms dominates 0(1).

```
b)  sum = 0 // 0(1)
    for i in range(n): // 0(n) * 0(n^3) = 0(^4)
      i += 1
      for j in range(i + 1, n): //0(n) * 0(n^2) = 0(^3)
        j += 1
        for k in range(j + 1, n): // 0(n) * 0(n) = 0(^2)
          k += 1
          for l in range(k + 1, 10 + k): //0(n) * 0(n) = 0(^n)
            sum += 1 // 0(1)
```
- 0(1) + 0(n^4) = 0(n^4) The nested for loops dominates

```
c)  def bunnyEars(bunnies):
      if bunnies == 0: //stops then counts back the total of bunney ears.
        return 0

      return 2 + bunnyEars(bunnies-1) //At the reduction, the function calls itself with a smaller number each time
```
- 0(2) + 0(n) = 0(2n) = 0(n)
Recusive function 
It loops through each bunny. 

Note: 
### Time Complexity = how the runtime of a function increases as the size of input increases
- linear O(n)
- constant O(1)
- quadratic O(n^2)
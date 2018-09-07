# Theoretical Homomorphic Bullshit:

## Basic Modular Arithmetic:

Our modulus is **7**. This is the limit of numerical values in our "number system."

If we add some numbers together, then modularly reduce them, we will get the integer value that is above 7, or more accurately, we will compute the remainder when dividing the sum, by our modulus:

```
1 + 2 = 3, mod 7 = 3
2 + 3 = 5, mod 7 = 5
3 + 4 = 7, mod 7 = 0
4 + 5 = 9, mod 7 = 2
```

The only valid values when reducing my a modulus of 7, are the integer values below it, specifically:

```
[ 0, 1, 2, 3, 4, 5, 6 ]
```

Notice there are 7 values, but the largest expressible value is one less than the modulus.

## Modular Multiplicative Inverses

Still, we will use the modulus of **7**. Instead of addition, we will be determining what values, when multiplied together, will have a value of 1, when modularly reduced. These values have a special modular property that we are interested in. Let's define the MMIs for 7:

```
MOD 7
1 * 1 = 1, mod 7 = 1    (Too easy...)
2 * 4 = 8, mod 7 = 1
3 * 5 = 15, mod 7 = 1   (7 * 2 = 14; 15 - 14 = 1)
6 * 6 = 36, mod 7 = 1   (7 * 5 = 35; 36 - 35 = 1)
```

Why might this property be useful?

```
data * mmi0 = x
x * mmi1 = y
y mod 7 = data

data = 3
mmi pair = 3, 5

3 * 3 = 9
9 * 5 = 45
45 mod 7 = 3
```

Keep in mind, the limitations of the modulus we are using:

```
9 * 3 = 27
27 * 5 = 135
135 mod 7 = 2
```

Which is incorrect... but:

```
9 mod 7 = 2
```

## Infinitely Padded Data!

As long as we are aware of our modulus, we know we can add that value (or a multiple of it) to any data integer we input, in order to get that data out of our modular multiplicative inverse operations, as above:

```
Pad? (not really)
data = 3
random integer = 4    (for multiplying by 7 as above)
mmi pair = 2, 4

3 + (7 * 4) = 3 + 28 = 31   (keep in mind, 28 mod 7 = 0)
31 * 2 = 62
62 * 4 = 248
248 mod 7 = 3   (7 * 35 = 245; 248 - 245 = 3)
```

*cough cough*

```
3 + (7 * 93457) = 3 + 654199 = 654202
654202 * (2 * 4) = 654202 * 8 = 5233616   (might as well multiply the inverses together)
5233616 mod 7 = 3
```

## Malleability?

If you notice, if we add 1 to the "**y**" value, our resulting modular reduction will be 1 higher than the value we started with:

```
3 + 28 = 31
31 * 2 = 62
62 * 4 = 248
248 + 1 = 249   <---
249 mod 7 = 4
```

The "**y**" value can be modified directly, with standard arithmetic. However, we can also demonstrate this in other ways:

```
3 + 28 = 31
31 + 1 = 32   <---
32 * 2 = 64
64 * 4 = 256 mod 7 = 4
```

```
3 + 28 = 31
31 * 2 = 62
1 * 2 = 2   <---
62 + 2 = 64   <---
64 * 4 = 256 mod 7 = 4
```

```
3 + 28 = 31
31 * 2 = 62
62 * 3 = 186 mod 7 = 4    <---

62 * 5 = 310 mod 7 = 2    <---
```

But...

```
3 + 28 = 31
31 * 2 = 62
62 + 1 = 63   <---
63 * 4 = 252 mod 7 = 0
```

(Enough strange witchcraft for tonight.)

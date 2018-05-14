- Date : 2018-05-14
- Tags : #programming #random

## Get random number from computer

Today, I read my junior team-mate code and find this line

```php
$number = rand(2,1000)*rand(2,1000);
```

This made me remember that's same idea of my own in many years ago. Then I ask myself, is it good to generate a random number from 2 random numbers ?

So the main reason that he wrote this was making probability of same number at same time must be low. We can know that this will return a random number from 4 to 1000000. So why don't we just do this ?

```php
$number = rand(4,1000000);
```

This function will make probability lower than above function, because above function is commutative (A*B = B*A). So stay away from commutative function (`+`, `*`) when generate a random number.

Need more powerful ? Try Pseudorandom Number Generator (PRNG) !!


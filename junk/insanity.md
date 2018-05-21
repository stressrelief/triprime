# Basics

A segment of a fixed size, statically partitioned into a data segment, nonce, and hash segment (for now)

0 . . . 8 . . . 16. . . 24. . . 32. . . 40. . . 48. . . 56. . . 64. . . 72. . . 80. . . 88
DATASEGMENTDATASEGMENTDATASEGMENTDhashsegmenthashsegmenthashsegmenNONCENONCENONCEN

Let's "zoom out" and set that object above as []

0 . . . 1 . . . 2 . . . 3 . . . 4 . . . 5 . . . 6 . . . 7 . . . 8
[]

We find a prime that is larger than our potential max value of our []. In that way, the prime can encapsulate the data, and recover it without error.

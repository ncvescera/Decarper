# Decarper
A Carpi decripter in python [ We will know the truth !]


# What is a Decarper?
During our course at University called "Architettura degli Elaboratori" with prof. Carpi we noticed how curious his language made of long pauses and short but memorable sentences was.
We wondered if we could manage to get even more useful information from his vocal language and dynamics, so we started thinking how we could build a sweet piece of software to help us.
We ended up with this little program, the Decarper:

What if,  using a microphone attached to the machine and given an arbitrary clock time (such as 1 second), for each time step we write down a 0 (zero) if he's not talking and a 1 (one) if he's talking?
We'll end up with a sequence of numbers that will look like this: 01000101000000011101000110010010......
We then pack all these 0's and 1's into larger groups of 8/16/32 bits (depends on the code we'll use), and convert it into characters (letters A-Z, a-z and numbers). We'll end up again with apparently senseless words and phrases. What if inside this meaningless set of letters we find some hidden secret message or even the answer to some of the fundamental questions the humans have had since they were on this Earth?

Let's find out..

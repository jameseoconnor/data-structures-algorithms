# Tips for an interview

- If there id a question, like the banana one, where you have to iterate over a list and find an optimal number - think math.ceil. So we were trying to find the optimal eating speed, but there was redundancy when the number of bananas didn't fit the hours exactly, so Kokomo was sitting there. TO calculate this redundancy, we used Math.ceil()
- Math.ceil(3/5) = 1, Math.ceil(8/5)=2, Math.ceil(12/5)=3 and so on and so forth.

## Memoization
- If we can figure out what we need to find, based on what we are looking at then if we find it later on we are laughing. So for example, the two sums question, if we create a hashmap of the values we are looknig for and keep running the solution until we hit one, then we can return 
- So if I am trying to find two numbers to add to 10, my first is 4. I'll see if the complement (10-4=6), is in the memo, have we seen it? If not then add 4 to the map and keep going. If we hit a siz, we figure out the complement is 4, check the hashmap and there we have it. 


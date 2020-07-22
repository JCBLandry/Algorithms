#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):

  #base case, he cannot eat anymore cookies
  if cache != None and cache[n]:
    # print(f'Found {n} in cache with value {cache[n]}')
    return cache[n]

  if n == 0:
    if cache != None:
      cache[n] = 1
    return 1

  total_ways = 0
  if n >= 3:
    
    #eat all 3 cookies
    n_3_total = eating_cookies(n-3, cache)
    total_ways += n_3_total
  if n >= 2:
    #eat 2 cookies
    total_ways += eating_cookies(n-2, cache)
  if n >= 1:
    #eat 1 cookie
    total_ways += eating_cookies(n-1, cache)
  if cache != None:   
    cache[n] = total_ways
  return total_ways    


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
from typing import List
import collections
import time

def wrdLadderBFS( start: str, end: str, dict: List[str]) -> int:
    wrdset = set(dict)
    Q = collections.deque()
    Q.append((start, 1))
    wrdLentgh = len(start)
    while Q:
        wrd, step = Q.popleft()
        if wrd == end:
            return step
        for j in range(wrdLentgh):
            for chr in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                newwrd = wrd[:j]+chr+wrd[j+1:]
                if newwrd in wrdset:
                    wrdset.remove(newwrd)
                    Q.append((newwrd, step+1))
    return 0
    
    

def wrdLadderDFS( start, end, dict):

  if not end or not start or not dict or end not in dict \
    or start == end:
    return []

  lnght = len(start)
  allDict = collections.defaultdict(list)
  for wrd in dict:
    for i in range(lnght):
      allDict[wrd[:i] + "*" + wrd[i+1:]].append(wrd)


  Q = collections.deque()
  Q.append(start)
  nd_parent = collections.defaultdict(set)
  seen = set([start])
  found = False 
  depth = 0
  while Q and not found:
    depth += 1 
    length = len(Q)
    # print(Q)
    localseen = set()
    for _ in range(length):
      wrd = Q.popleft()
      for i in range(lnght):
        for nextwrd in allDict[wrd[:i] + "*" + wrd[i+1:]]:
          if nextwrd == wrd:
            continue
          if nextwrd not in seen:
            nd_parent[nextwrd].add(wrd)
            if nextwrd == end:    
              found = True
            localseen.add(nextwrd)
            Q.append(nextwrd)
    seen = seen.union(localseen)

  Result = []
  def dfs(node, path, d):
    if d == 0:
      if path[-1] == start:
        Result.append(path[::-1])
      return 
    for parent in nd_parent[node]:
      path.append(parent)
      dfs(parent, path, d-1)
      path.pop()
  dfs(end, [end], depth)
  return len(Result[0])





file = open("Collins Scrabble Words (2019).txt")
content = file.read()
Dict = content.split('\n')
file.close()
del D[0]
start="DEAD"
end="WARM"


wordList = ["FOOL", "POOL", "FOIL", "FOUL", "COOL", "POLL", "FAIL", "POLE", "PALL", "POPE", "PALE", "PAGE", "SALE", "SAGE", "PIPE", "DOLL", "SOIL", "SOUL", "NAIL", "JAIL", "TAIL", "BAIL", "FALL"]
start="POLE"
end="SOUL"
print("_______________________________________________________")
print("___________________comparison__________________________")
print("_______________________________________________________")
print("Number of steps taken using the DFS-based function:(%d)\n"%(wrdLadderDFS(start,end,wordList)))
print("Number of steps taken using the BFS-based function:(%d)"%(wrdLadderBFS(start,end,wordList)))
print("_______________________________________________________\n")


start = input ("Please enter the word to begin with:")
end   = input ("Please enter the target word:")

print("_______________________________________________________")
print("______________________RESULTS__________________________")
print("_______________________________________________________")
print("Number of steps taken using the DFS-based function:(%d)\n"%(wrdLadderDFS(start,end,Dict)))
print("Number of steps taken using the BFS-based function:(%d)"%(wrdLadderBFS(start,end,Dict)))
print("_______________________________________________________")

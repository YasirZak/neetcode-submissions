class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        map = {beginWord:[]}

        for i in range(len(beginWord)):
            link = beginWord[:i]+"*"+beginWord[i+1:]
            map[beginWord].append(link)
            if link not in map.keys():
                map[link] = []

        for word in wordList:

            for i in range(len(word)):
                parent = word[:i]+"*"+word[i+1:]
                if parent not in map.keys():
                    map[parent]=[]
                if word not in map[parent]:
                    map[parent].append(word)
            if word not in map.keys():
                map[word]=[]

            for i in range(len(word)):
                child = word[:i]+"*"+word[i+1:]
                if child not in map[word]:
                    map[word].append(child)
                if child not in map.keys():
                    map[child]=[]

        print(map)

        pq = []
        dist = {i:1000 for i in map.keys()}
        dist[beginWord]=0
        heapq.heappush(pq,(0,beginWord))

        while len(pq)!=0:
            d, node = heapq.heappop(pq)
            if d>dist[node]:
                continue
            for word in map[node]:
                dist[word]=min(dist[word],d+1)
                heapq.heappush(pq,(d+1,word))

        if dist[endWord]==1000: return 0
        return (dist[endWord]-dist[endWord]//2)+1
                
                    


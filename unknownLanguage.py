from collections import defaultdict
#Auth - Raj Patel 3/16/20

#recursive method (DFS) to visit each connected node and return it's position
#Recursively finds the link which has the most links in it, if no links return zero
def Visit(node, visited, graph, ans):

    maxPos = -1

    if node in visited:
        return visited[node]
    else:
        for n in graph[node]:
            tempMax = None
            if n in visited:
                tempMax = visited[n]
            else:
                tempMax = Visit(n, visited, graph, ans)
            maxPos = max(maxPos,tempMax)

    #if a node didn't have any links from it (Last letter of the language), return 0, else return max(pos of links)+1
    if maxPos != -1:
        val = maxPos +1
    else:
        val = 0

    #add node to visited
    visited[node] = val

    #save position of the current node
    ans[val] = node

    return val

#method to get the graph edge from two words
def GetLink(firstWord, secondWord):

    minLen = min(len(firstWord), len(secondWord))

    for index in range(minLen):
        if firstWord[index] != secondWord[index]:
            return [firstWord[index], secondWord[index]]

    return firstWord[minLen-1]

def MakeGraph(graph, link):

        if len(link) == 1:            #For cases like ['aa','aa'] or ['a','aa']
            if link not in graph:
                graph[link]
        else:
            graph[link[0]].append(link[1])
            if link[1] not in graph:
                graph[link[1]]

#solution method
def UnknownLanguage(words):

    if len(words) == 1: #if input has only one string -> aaaaa or a
        return [words[0][0]]

    graph = defaultdict(list)

    for i in range(len(words)-1):
        link = GetLink(words[i], words[i + 1])
        MakeGraph(graph, link)

    visited = {}
    ans = [None] * len(graph)

    #visit each unvisited node
    for nodeVal in graph:
        if nodeVal not in visited:
            Visit(nodeVal, visited, graph, ans)

    #return reverseOrder
    return ans[::-1]

#Test cases
print(UnknownLanguage(sorted(['ab', 'be', 'bd', 'cf', 'bc', 'cd', 'de', 'ef', 'de', 'ee']))) #abcdef
print(UnknownLanguage(['bac', 'aaa', 'aac'])) #bac
print(UnknownLanguage(['aan', 'aaq', 'nq', 'nb', 'qb', 'qc', 'bc', 'ca', 'cb']))   #anqbc
print(UnknownLanguage(["ktt", "ttt", "ttx"])) #ktx
print(UnknownLanguage(['aa', 'b', 'baa'])) #ab
print(UnknownLanguage(['aa'])) #a
print(UnknownLanguage(['aa', 'aa'])) #a
print(UnknownLanguage(['aa', 'aaa'])) #a

# Analysis
# O(n-words) - To create the graph from the words
# O(n-edge) - We visit each edge once
# Therefore - O(max(n-edge,n-words))

from collections import deque

class Player:

    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"Hello! I am {self.name} and play for {self.team} team")

    

class Team:
    
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def show_players(self):
        for player in self.players:
            player.introduce()

    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)


team_red = Team("Team Red")

team_red.add_player("nico")


team_red.add_player("Jinny")
team_red.show_players()

team_blue = Team("Team Blue")
team_blue.add_player("Lynn")

team_blue.show_players()

class Node():

    def __init__(self,value):
        self.value = value
        self.next = None    
        

class Linkedlist():
    
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append_list(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length =+ 1
        return True

my_list = Linkedlist(1)
my_list.append_list(2)
my_list.append_list(3)


my_list.print_list()



def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start]=True
    print("This is BFS")

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph1 = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
graph2 = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited1 = [False] * 9
visited2 = [False] * 9
dfs(graph1, 1, visited1)
bfs(graph2, 1, visited2)
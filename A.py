from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from collections import deque, namedtuple, defaultdict
import webbrowser

# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')
#Named tuples assign meaning to each position in a tuple and allow for more readable,
# self-documenting code. They can be used wherever regular tuples are used,
# and they add the ability to access fields by name instead of position index.
tryPath = []
totalDistance = 0
savePath2 =[]
pathAll = []
def coordinates(city):
    geolocator = Nominatim(user_agent="locationgeopy")
    location = geolocator.geocode(city)
    print(city, ":(",location.latitude,",",location.longitude,")")
    return (location.latitude, location.longitude)

print("---------Coordinates of cities----------")
KL = coordinates("KL")
NY = coordinates("New York")
HK = coordinates("Hong Kong")
YVR = coordinates("Vancouver")
TWN = coordinates("Taiwan")
LA = coordinates("Los Angeles")
TYO = coordinates("Tokyo")
TX = coordinates("Texas")
DH = coordinates("Doha")
BST = coordinates("Boston")
CCG = coordinates("Chicago")

def make_edge(start, end, cost=1):
    return Edge(start, end, cost)

class Graph:
    #find vertices
    #make them a property, they'll be recounted each time we address the property.
    def __init__(self, edges):
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )
    #add adding and removing functionality.
    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    #find neighbors for every node:
    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        #1. Mark all nodes unvisited and store them.
        # 2. Set the distance to zero for our initial node
        # and to infinity for other nodes.
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            # 3. Select the unvisited node with the smallest distance,
            # it's current node now.
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            # 6. Stop, if the smallest distance
            # among the unvisited nodes is infinity.
            if distances[current_vertex] == inf:
                break
            # 4. Find unvisited neighbors for the current node
            # and calculate their distances through the current node.
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                # Compare the newly calculated distance to the assigned
                # and save the smaller one.
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex
            # 5. Mark the current node as visited
            # and remove it from the unvisited set.
            vertices.remove(current_vertex)
        savePath = []
        #we use deque to maintain a sequence of recently added elements by appending to the right and popping to the left:
        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            savePath.append(current_vertex)
            savePath2.append(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
            savePath.append(current_vertex)

        tryPath.append(path)
        print("\nShortest Path: ",path)
        KL = (3.1516636, 101.6943028)
        NY = (40.7127281, -74.0060152)
        HK = (22.2793278, 114.1628131)
        YVR = (49.2608724, -123.1139529)
        TWN = (23.59829785,120.835363138175)
        LA = (34.0536909,-118.2427666)
        TYO = (35.6828387,139.7594549)
        TX = (31.8160381, -99.5120986)
        DH = (25.2856329, 51.5264162)
        BST = (42.3602534, -71.0582912)
        CCG = (41.8755616, -87.6244212)
        calculatePath = []
        for i in range(0,len(savePath)):
            if savePath[i] == "KL":
                calculatePath.append(KL)
            elif savePath[i] == "NY":
                calculatePath.append(NY)
            elif savePath[i] == "TX":
                calculatePath.append(TX)
            elif savePath[i] == "HK":
                calculatePath.append(HK)
            elif savePath[i] == "CCG":
                calculatePath.append(CCG)
            elif savePath[i] == "TYO":
                calculatePath.append(TYO)
            elif savePath == "LA":
                calculatePath.append(LA)
            elif savePath[i] == "TWN":
                calculatePath.append(TWN)
            elif savePath[i] == "DH":
                calculatePath.append(DH)
            elif savePath[i] == "BST":
                calculatePath.append(BST)
            elif savePath[i] == "YVR":
                calculatePath.append(YVR)
        length = 0
        # Time complexity = O(n-1)
        for i in range(0,len(calculatePath)-1):
            length += distance(calculatePath[i],calculatePath[i+1])
        # print("Total Distance: ",round(length,3)," km")
        return length

def distance(city1, city2):
    return geodesic(city1, city2).kilometers

def getDistance(city1, city2):
    print(round(distance(city1, city2), 3), "km", sep='')

def filterCountry(unsafeCountry, safeCountry):
    # Time complexity = O(n)
    for i in range(0, len(unsafeCountry)):
        if unsafeCountry[i] == "HongKong":
            graph.remove_edge("HK", "YVR", distance(HK, YVR))
        elif unsafeCountry[i] == "Vancouver":
            graph.remove_edge("HK", "YVR", distance(HK, YVR))
            graph.remove_edge("TWN", "YVR", distance(TWN, LA))
            graph.remove_edge("TYO", "YVR", distance(TYO, YVR))
            graph.remove_edge("YVR", "NY", distance(YVR, NY))
            graph.remove_edge("YVR", "LA", distance(YVR, LA))
            graph.remove_edge("YVR", "TX", distance(YVR, TX))
        elif unsafeCountry[i] == "Taiwan":
            graph.remove_edge("TWN", "YVR", distance(TWN, LA))
            graph.remove_edge("KL", "TWN", distance(KL, TWN))
        elif unsafeCountry[i] == "Tokyo":
            graph.remove_edge("TYO", "TX", distance(TYO, TX))
            graph.remove_edge("TYO", "YVR", distance(TYO, YVR))
            graph.remove_edge("TYO", "BST", distance(TYO, BST))
            graph.remove_edge("KL", "TYO", distance(KL, TYO))
        elif unsafeCountry[i] == "Doha":
            graph.remove_edge("DH", "BST", distance(DH, BST))
            graph.remove_edge("KL", "DH", distance(KL, DH))
        elif unsafeCountry[i] == "Texas":
            graph.remove_edge("TYO", "TX", distance(TYO, TX))
            graph.remove_edge("YVR", "TX", distance(YVR, TX))
            graph.remove_edge("LA", "TX", distance(LA, TX))
            graph.remove_edge("TX", "NY", distance(TX, NY))
        elif unsafeCountry[i] == "Boston":
            graph.remove_edge("TYO", "BST", distance(TYO, BST))
            graph.remove_edge("TYO", "BST", distance(TYO, BST))
        elif unsafeCountry[i] == "Los Angeles":
            graph.remove_edge("YVR", "LA", distance(YVR, LA))
            graph.remove_edge("LA", "NY", distance(LA, NY))
            graph.remove_edge("LA", "TX", distance(LA, TX))
            graph.remove_edge("LA", "CCG", distance(LA, CCG))
        elif unsafeCountry[i] == "Chicago":
            graph.remove_edge("LA", "CCG", distance(LA, CCG))
            graph.remove_edge("BST", "CCG", distance(BST, CCG))
            graph.remove_edge("CCG", "NY", distance(CCG, NY))
            graph.remove_edge("YVR", "CCG", distance(YVR, CCG))
    print("\n---------------Safe country after filter----------")
    print(safeCountry)
    print("\n---------------unsafe country after filter----------")
    print(unsafeCountry)

def ranking (n1,n2):
    while len(pathAll) < 5:
        graph.dijkstra(n1, n2)
        KL = (3.1516636, 101.6943028)
        NY = (40.7127281, -74.0060152)
        HK = (22.2793278, 114.1628131)
        YVR = (49.2608724, -123.1139529)
        TWN = (23.59829785, 120.835363138175)
        LA = (34.0536909, -118.2427666)
        TYO = (35.6828387, 139.7594549)
        TX = (31.8160381, -99.5120986)
        DH = (25.2856329, 51.5264162)
        BST = (42.3602534, -71.0582912)
        CCG = (41.8755616, -87.6244212)
        calculatePath = []
        for i in range(0, len(savePath2)):
            if savePath2[i] == "KL":
                calculatePath.append(KL)
            elif savePath2[i] == "NY":
                calculatePath.append(NY)
            elif savePath2[i] == "TX":
                calculatePath.append(TX)
            elif savePath2[i] == "HK":
                calculatePath.append(HK)
            elif savePath2[i] == "CCG":
                calculatePath.append(CCG)
            elif savePath2[i] == "TYO":
                calculatePath.append(TYO)
            elif savePath2 == "LA":
                calculatePath.append(LA)
            elif savePath2[i] == "TWN":
                calculatePath.append(TWN)
            elif savePath2[i] == "DH":
                calculatePath.append(DH)
            elif savePath2[i] == "BST":
                calculatePath.append(BST)
            elif savePath2[i] == "YVR":
                calculatePath.append(YVR)

        for i in range(1, len(savePath2) - 1):
            graph.remove_edge(savePath2[i + 1], savePath2[i], distance(calculatePath[i + 1], calculatePath[i]))

        for i in range(1, len(savePath2)):
            if savePath2[i] in pathAll:
                continue
            else:
                pathAll.append(savePath2[i])

        savePath2.clear()
        calculatePath.clear()

    for i in range(0, len(pathAll) - 1):
        graph.add_edge(pathAll[i + 1], pathAll[i])

graph = Graph([
    ("KL", "HK", distance(KL, HK)), ("KL", "TYO", distance(KL, TYO)),
    ("KL", "DH", distance(KL, DH)), ("KL", "TWN", distance(KL, TWN)),
    ("HK", "YVR", distance(HK, YVR)), ("TWN", "YVR", distance(TWN, YVR)),
    ("TYO", "TX", distance(TYO, TX)), ("TYO","YVR", distance(TYO,YVR)),
    ("TYO","BST",distance(TYO,BST)),("DH", "BST", distance(DH, BST)),
    ("YVR", "NY", distance(YVR, NY)), ("YVR","LA", distance(YVR,LA)),
    ("YVR","TX",distance(YVR,TX)),("LA", "NY", distance(LA, NY)),("YVR","CCG",distance(YVR,CCG)),
    ("LA","TX",distance(LA,TX)), ("LA","CCG",distance(LA,CCG)),
    ("TX", "NY", distance(TX, NY)), ("BST", "NY", distance(BST, NY)),
    ("BST","CCG",distance(BST,CCG)),("CCG", "NY", distance(CCG, NY))])
# Variables
cities = ["HongKong", "Vancouver", "Taiwan", "Los Angeles", "Tokyo", "Texas", "Doha", "Boston", "Chicago"]
d = 256
f1 = open("stopword.txt","r")
stop = f1.read()
f1.close()
safeCountry = []
unsafeCountry = []
chooseOption = 6
chooseDestination = 0
#time complexity = O(f*p)
with open("safeCountry.txt", 'r') as f:
    for line in f:
        for word in line.split():
            safeCountry.append(word)
# Time complexity = O(f*p)
with open("unsafeCountry.txt", 'r') as f:
    for line in f:
        for word in line.split():
            unsafeCountry.append(word)
# time complexity = O(1)
while chooseOption!=0:
    print("\n1. View routes")
    print("2. Choose destination")
    print("3. Political sentiment")
    print("4. Ranking")
    chooseOption = int(input("Please select one [PRESS 0 TO EXIT] "))
    if chooseOption == 1:
        print("\n1. Chicago")
        print("2. New York")
        print("3. Los Angeles")
        userOption = int(input("Please select your destination: "))
        if userOption == 1:
            print("1. All possible path")
            print("2. Shortest path")
            choosePath = int(input("Select one: "))
            if choosePath == 1:
                webbrowser.open_new_tab('allPathCCG.html')
            elif choosePath == 2:
                webbrowser.open_new_tab('pathCCG2.html')
        if userOption == 2:
            print("1. All possible path")
            print("2. Shortest path")
            choosePath = int(input("Select one: "))
            if choosePath == 1:
                webbrowser.open_new_tab('allNewYork.html')
            elif choosePath == 2:
                webbrowser.open_new_tab('pathDH.html')
        if userOption == 3:
            print("1. All possible path")
            print("2. Shortest path")
            choosePath = int(input("Select one: "))
            if choosePath == 1:
                webbrowser.open_new_tab('allPathLA.html')
            elif choosePath == 2:
                webbrowser.open_new_tab('pathLA1.html')
    elif chooseOption == 2:
        print("\n1. Chicago")
        print("2. New York")
        print("3. Los Angeles")
        chooseDestination = int(input("Select your destination: "))
        if chooseDestination == 1:
            print("Shortest path before filter....")
            print("Total distance: ", graph.dijkstra("KL", "CCG"), " km")
            filterCountry(unsafeCountry, safeCountry)
            print("Shortest path after filter...")
            print("Total distance: ",graph.dijkstra("KL","CCG")," km")
            viewP = int(input("Press 1 to view map/polyline:"))
            if viewP == 1:
                webbrowser.open_new_tab('pathCCG2.html')
        elif chooseDestination == 2:
            print("Shortest path before filter....")
            print("Total distance: ", graph.dijkstra("KL", "NY"), " km")
            filterCountry(unsafeCountry, safeCountry)
            print("Shortest path after filter...")
            print("Total distance: ",graph.dijkstra("KL","NY")," km")
            viewP = int(input("Press 1 to view map/polyline:"))
            if viewP == 1:
                webbrowser.open_new_tab('pathDH.html')
        elif chooseDestination == 3:
            print("Shortest path before filter....")
            print("Total distance: ", graph.dijkstra("KL", "LA"), " km")
            filterCountry(unsafeCountry, safeCountry)
            print("Shortest path after filter...")
            print("Total distance: ",graph.dijkstra("KL","LA")," km")
            viewP = int(input("Press 1 to view map/polyline:"))
            if viewP == 1:
                webbrowser.open_new_tab('pathLA1.html')
    elif chooseOption == 3:
        print("\n1. Word Graph")
        print("2. Positive and Negative word for each country")
        print("3. Percentage of positive and negative sentiment in all countries")
        userOption = int(input("Please select one: "))
        if userOption == 1:
            print("\n1. Hong Kong")
            print("2. Doha")
            print("3. Taiwan")
            print("4. Tokyo")
            print("5. Vancouver")
            print("6. Texas")
            print("7. Boston")
            print("8. Los Angeles")
            print("9. Chicago")
            country = int(input("Please select one: "))
            if country == 1:
                webbrowser.open_new_tab('Hong Kong.html')
            if country == 2:
                webbrowser.open_new_tab('Doha.html')
            if country == 3:
                webbrowser.open_new_tab('Taiwan.html')
            if country == 4:
                webbrowser.open_new_tab('Tokyo.html')
            if country == 5:
                webbrowser.open_new_tab('Vancouver.html')
            if country == 6:
                webbrowser.open_new_tab('Texas.html')
            if country == 7:
                webbrowser.open_new_tab('Boston.html')
            if country == 8:
                webbrowser.open_new_tab('LA.html')
            if country == 9:
                webbrowser.open_new_tab('Chicago.html')
        if userOption == 2:
            print("\n1. Hong Kong")
            print("2. Doha")
            print("3. Taiwan")
            print("4. Tokyo")
            print("5. Vancouver")
            print("6. Texas")
            print("7. Boston")
            print("8. Los Angeles")
            print("9. Chicago")
            country = int(input("Please select one: "))
            if country == 1:
                webbrowser.open_new_tab('HongkongH.html')
            if country == 2:
                webbrowser.open_new_tab('DohaH.html')
            if country == 3:
                webbrowser.open_new_tab('TaiwanH.html')
            if country == 4:
                webbrowser.open_new_tab('TokyoH.html')
            if country == 5:
                webbrowser.open_new_tab('VancouverH.html')
            if country == 6:
                webbrowser.open_new_tab('TexasH.html')
            if country == 7:
                webbrowser.open_new_tab('BostonH.html')
            if country == 8:
                webbrowser.open_new_tab('LAH.html')
            if country == 9:
                webbrowser.open_new_tab('ChicagoH.html')
        if userOption == 3:
                print(" __________________")
                print("| CITIES  | POSITIVE SENTIMENT | NEGATIVE SENTIMENT |")
                print("|---------------------------------------------------|")
                print("| CHICAGO | 4.488050465871895  | 1.1618106946922258 |")
                print("|---------------------------------------------------|")
                print("| BOSTON  | 4.465186422006515  | 2.530276560875997  |")
                print("|---------------------------------------------------|")
                print("| DOHA    | 6.472933351905743  | 1.2200064758929416 |")
                print("|---------------------------------------------------|")
                print("| TEXAS   | 2.999518174062704  | 3.011907938696633  |")
                print("|---------------------------------------------------|")
                print("| TOKYO   | 1.9290416766771634 | 3.040547076725738  |")
                print("|---------------------------------------------------|")
                print("| LA      | 4.5559297440777105 | 1.9174264880928802 |")
                print("|---------------------------------------------------|")
                print("| TAIWAN  | 3.9500443867064847 | 2.400935825277189  |")
                print("|---------------------------------------------------|")
                print("| VAN     | 4.213821313064217  | 1.56742037537088   |")
                print("|---------------------------------------------------|")
                print("|HONG KONG| 4.176705085163742  | 3.383516244234605  |")
                print("-----------------------------------------------------")
                webbrowser.open_new_tab('HistogramPercentage.html')
                webbrowser.open_new_tab('testing.html')
    elif chooseOption == 4:
        print("\n1. Chicago")
        print("2. New York")
        print("3. Los Angeles")
        chooseDestination = int(input("Select your destination: "))
        if chooseDestination == 1:
            filterCountry(unsafeCountry, safeCountry)
            savePath2.clear()
            ranking("KL", "CCG")

        elif chooseDestination == 2:
            filterCountry(unsafeCountry, safeCountry)
            savePath2.clear()
            ranking("KL", "NY")

        elif chooseDestination == 3:
            filterCountry(unsafeCountry, safeCountry)
            savePath2.clear()
            ranking("KL", "LA")
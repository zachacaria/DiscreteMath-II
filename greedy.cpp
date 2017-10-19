// A C++ program to implement greedy algorithm for graph coloring
#include <iostream>
#include <list>
using namespace std;

// A class that represents an undirected graph
class Graph
{
	int V; // No. of vertices
	list<int> *adj; // A dynamic array of adjacency lists
public:
	
	Graph(int V) { this->V = V; adj = new list<int>[V]; }
	~Graph()	 { delete [] adj; }

	// function to add an edge to graph
	void addEdge(int v, int w);

	// Prints greedy coloring of the vertices
	void greedyColoring();
};

void Graph::addEdge(int v, int w)
{
	adj[v].push_back(w);
	adj[w].push_back(v);
}

/* Assigns colors (starting from 0) to all vertices and prints
    the assignment of colors */
void Graph::greedyColoring()
{
	int result[V];

	// Assign the first color to first vertex
	result[0] = 0;

	for (int u = 1; u < V; u++)
		result[u] = -1;

	
	bool available[V];
	for (int cr = 0; cr < V; cr++)
		available[cr] = false;

	
	for (int u = 1; u < V; u++)
	{
		
		list<int>::iterator i;
		for (i = adj[u].begin(); i != adj[u].end(); ++i)
			if (result[*i] != -1)
				available[result[*i]] = true;

		
		int cr;
		for (cr = 0; cr < V; cr++)
			if (available[cr] == false)
				break;

		result[u] = cr; // Assign the found color

		
		for (i = adj[u].begin(); i != adj[u].end(); ++i)
			if (result[*i] != -1)
				available[result[*i]] = false;
	}

	
	for (int u = 0; u < V; u++)
		cout << "Vertex " << u << " ---> Color "
			<< result[u] << endl;
}

// Driver program to test above function
int main()
{
    /*
     
           0------------1
          /|          / |
         / |         /  |
        /  |        /   |
        6-----------7   |
        |  |        |   |
        |  |        |   |
        |  |        |   |
        |  5--------|---2
        | /         |  /
        |/          | /
        4-----------3/
     
     */
	Graph g1(8);
	g1.addEdge(0, 1);
	g1.addEdge(0, 5);
	g1.addEdge(0, 6);
	g1.addEdge(1, 2);
    g1.addEdge(1, 7);
	g1.addEdge(2, 3);
    g1.addEdge(2, 5);
	g1.addEdge(3, 4);
    g1.addEdge(3, 7);
    g1.addEdge(4, 5);
    g1.addEdge(4, 6);
    g1.addEdge(6, 7);
	cout << "Coloring of graph 1 \n";
	g1.greedyColoring();
    
    
    /*
      
     
               1
              / \
             /   \
            /     \
           0   3---2
           \       /
            \     /
             \   /
              \ /
               4-----5
     */

	Graph g2(6);
	g2.addEdge(0, 1);
	g2.addEdge(0, 4);
	g2.addEdge(1, 2);
	g2.addEdge(2, 3);
	g2.addEdge(2, 4);
	g2.addEdge(4, 5);
	cout << "\nColoring of graph 2 \n";
	g2.greedyColoring();
    
    /*
     
     should work for most graphs. create an instance of Graph g1,g2,g3,...gn. add
     the edges where they are connected via the addEdge method.
     
    */
   

	return 0;
}


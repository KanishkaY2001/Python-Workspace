# Package Details

* Graph Searching Algorithms
    * Breadth First Search
        * Time Complexity: O(V + E) (vertices + edges)
        * Finds the optimal solution by exploring each depth before the next
        * Uses a queue data structure (First In First Out)
    * Depth First Search
        * Time Complexity: O(V + E) (vertices + edges)
        * Not guaranteed to find optimal solution
        * Searches as deep as possible for each traversal of vertices
        * Uses a stack data structure (Last In First Out)
    * Depth Limited Search
        * Time Complexity: O(V^D) (vertices ^ limit)
        * Similar to DFS but searches only as deep as the given depth limit
        * Not guaranteed to find a solution at all, based on given limit
        * DLS is not complete and is therefore not optimal
    * Interative Deepening Depth First Search  
        * Time Complexity: O(B^D) (branching factor ^ limit)
        * Similar to DLS but searches iteratively from depth 0 to depth x
        * The search stops once the target vertex is reached
        * Finds the optimal solution by exploring as deep as possible for each limit
        * Uses a stack data structure (Last In First Out)
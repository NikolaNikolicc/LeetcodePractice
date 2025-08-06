class Solution {
private:
    unordered_map<int, vector<int>> mapNodeGroup;
    unordered_set<int> visited;
    vector<int> topoSortGroups;
    vector<int> finalTopo;
    unordered_map<int, vector<int>> adjGroup;

    // topological sort for groups
    unordered_set<int> path;
    bool topoSortGroup(int groupNode){
        if (path.count(groupNode)) return false;
        if (visited.count(groupNode))return true;

        path.insert(groupNode);
        for (auto nei: adjGroup[groupNode]){
            if (!topoSortGroup(nei)){
                return false;
            }
        }
        path.erase(groupNode);
        visited.insert(groupNode);
        topoSortGroups.push_back(groupNode);
        return true;
    }

    // topological sort for node in the same group
    bool topo(int node, int myGroup, vector<int>& group, vector<vector<int>>& beforeItems){
        if (path.count(node)) return false;
        if (visited.count(node))return true;

        if (myGroup == group[node]) visited.insert(node);
        path.insert(node);
        for (auto nei: beforeItems[node]){
            if (!topo(nei, myGroup, group, beforeItems)){
                return false;
            }
        }
        path.erase(node);
        if (myGroup == group[node]) finalTopo.push_back(node);

        return true;
    }

public:
    vector<int> sortItems(int n, int m, vector<int>& group, vector<vector<int>>& beforeItems) {
       
        for (int g = 0; g < n; g++){
            if (group[g] == -1){
                group[g] = m++;
            }
            mapNodeGroup[group[g]].push_back(g);
        }

        for (int g = 0; g < n; g++){
            for (auto b: beforeItems[g]){
                if (group[g] != group[b])
                    adjGroup[group[g]].push_back(group[b]);
            }
        }

        for (int g = 0; g < m; g++){
            if (!topoSortGroup(g)){
                return vector<int>();
            }
        }
        path.clear();
        visited.clear();
        for (int i = 0; i < topoSortGroups.size(); i++){
            int g = topoSortGroups[i];
            cout << "g: " << g << " elems: ";
            for (auto node: mapNodeGroup[g]){
                cout << node << " ";
                if (!topo(node, g, group, beforeItems)){
                    return vector<int>();
                }
            }
            cout << endl;
        }

        return finalTopo;
    }
};
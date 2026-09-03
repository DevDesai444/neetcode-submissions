class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxa = 0;
        int dr[4] = {1, 0, -1, 0};
        int dc[4] = {0, 1, 0, -1};
        set<pair<int,int>> vis;

        for (int i = 0; i < (int)grid.size(); i++) {
            for (int j = 0; j < (int)grid[0].size(); j++) {
                if (vis.count({i, j}) == 0) {
                    vis.insert({i, j});
                    int area = 0;
                    if (grid[i][j] == 1) {
                        vector<pair<int,int>> q;
                        q.push_back({i, j});
                        area = 1;
                        while (!q.empty()) {
                            int r = q[0].first;
                            int c = q[0].second;
                            q.erase(q.begin());
                            for (int d = 0; d < 4; d++) {
                                int nr = r + dr[d];
                                int nc = c + dc[d];
                                if (vis.count({nr, nc}) == 0) {
                                    vis.insert({nr, nc});
                                    if (0 <= nr && nr < (int)grid.size() && 0 <= nc && nc < (int)grid[0].size() && grid[nr][nc] == 1) {
                                        area++;
                                        q.push_back({nr, nc});
                                    }
                                }
                            }
                        }
                        if (area >= maxa) {
                            maxa = area;
                        }
                    }
                }
            }
        }
        return maxa;
    }
};
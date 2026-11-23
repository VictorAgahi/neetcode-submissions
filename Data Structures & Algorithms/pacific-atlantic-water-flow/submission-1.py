class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacifique = set()
        atlantique = set()

        def explorer(r, c, visites, hauteur_precedente):
            if (
                r < 0 or r >= rows or           
                c < 0 or c >= cols or           
                (r, c) in visites or            
                heights[r][c] < hauteur_precedente
            ):
                return
            
            visites.add((r, c))
            
            explorer(r + 1, c, visites, heights[r][c])
            explorer(r - 1, c, visites, heights[r][c])
            explorer(r, c + 1, visites, heights[r][c])
            explorer(r, c - 1, visites, heights[r][c])

        for c in range(cols):
            explorer(0, c, pacifique, heights[0][c])              
            explorer(rows - 1, c, atlantique, heights[rows - 1][c])

        for r in range(rows):
            explorer(r, 0, pacifique, heights[r][0])              
            explorer(r, cols - 1, atlantique, heights[r][cols - 1])

        resultat = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacifique and (r, c) in atlantique:
                    resultat.append([r, c])
                    
        return resultat
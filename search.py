from pyamaze import maze,agent,COLOR
from collections import deque

# algoritmo para busca em profundidade
def profundidade(map, start= None):
    
    # inicialização das variaveis necessarias
    start=(m.rows, m.cols)
    
    # deque para adiconar e remover dos dois lados da fila
    # borda armazena as poisçoes possiveis de explorar
    borda=deque()
    borda.append(start)
    
    # visitados armazena as posiçoes ja visitadas
    visitados=[start]
    dfsCaminho={}
    dSearch=[]
    
    while len(borda)>0:
        atual=borda.pop()
        dSearch.append(atual)
        
        if atual == m._goal:
            break
        poss=0
        for d in 'ESNW':
            # maze_map é um dicionario das posiçoes da matriz, com cada posiçao contendo um dicionario das direçoes ESNW
            # cada uma das direçoes de cada posiçoes possui 1 ou 0, sinalizando se existe ou nao uma parede
            # ou seja, se é ou nao possivel ir para aquela direçao
            if m.maze_map[atual][d]==True:
                if d=='E':
                    child=(atual[0], atual[1]+1)
                elif d=='S':
                    child=(atual[0]+1, atual[1])
                elif d=='N':
                    child=(atual[0]-1, atual[1])
                elif d=='W':
                    child=(atual[0], atual[1]-1)
                
                if child in visitados:
                    continue
                poss+=1
                visitados.append(child)
                borda.append(child)
                dfsCaminho[child]=atual
                dSearch.append(child)
        if poss>1:
            m.markCells.append(atual)
    
    return dSearch, dfsCaminho

# algoritmo para busca em largura
def largura(map):
    # inicialização das variaveis necessarias
    start=(m.rows, m.cols)
    
    # deque para adiconar e remover dos dois lados da fila
    # borda armazena as poisçoes possiveis de explorar
    borda=deque()
    borda.append(start)
    
    # visitados armazena as posiçoes ja visitadas
    visitados=[start]
    bfsCaminho={}
    bSearch=[]
    
    while len(borda)>0:
        atual = borda.popleft()    
        if atual == m._goal:
            break
        
        for d in 'ESNW':
            # maze_map é um dicionario das posiçoes da matriz, com cada posiçao contendo um dicionario das direçoes ESNW
            # cada uma das direçoes de cada posiçoes possui 1 ou 0, sinalizando se existe ou nao uma parede
            # ou seja, se é ou nao possivel ir para aquela direçao
            if m.maze_map[atual][d]==True:
                if d=='E':
                    child=(atual[0], atual[1]+1)
                elif d=='S':
                    child=(atual[0]+1, atual[1])
                elif d=='N':
                    child=(atual[0]-1, atual[1])
                elif d=='W':
                    child=(atual[0], atual[1]-1)
                
                if child in visitados:
                    continue
                
                borda.append(child)
                visitados.append(child)
                bfsCaminho[child]=atual
                bSearch.append(child)
    print(f'{bfsCaminho}')
    
    return bSearch, bfsCaminho

if __name__=='__main__':
    m=maze(10,10)
    
    # duas opçoes de labirintos ja gerados: looppercent0.csv e looppercent50.csv
    # 0 tendo apenas uma soluçao, e quanto maior o numero mais caminhos sao possiveis
    # apagando o parametro, ira gerar um labirinto aleatorio com soluçao unica
    m.CreateMaze(loadMaze='looppercent100.csv')
    
    # profundidade ou largura
    search, caminho=profundidade(m)

    a=agent(m,footprints=True,color=COLOR.blue, shape = 'square')  
    b=agent(m,1,1,footprints=True,color=COLOR.cyan, shape='square', filled=True, goal=(m.rows, m.cols)) 
    
    # agente 1 que explora o labirinto
    m.tracePath({a:search}, delay=500) 
    
    # agente 2 que mostra o caminho mais rapido descoberto
    m.tracePath({b:caminho})

    m.run()
from pyamaze import maze,agent,textLabel
# Priority queue arranges value in prioriy,The lowest priority value is retrieved first
from queue import PriorityQueue 

def h(cell1,cell2):
    x1,y1= cell1
    x2,y2=cell2
    return(abs(x2-x1)+abs(y2-y1))

def a_star(m):
    #in maze graph the rows and column of the final block is the start block
    start=(m.rows,m.cols)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(1,1))

    open = PriorityQueue()
    open.put((h(start,(1,1)),h(start,(1,1)),start))
    a_path={}
    while not open.empty():
        current_cell=open.get()[2]
        if current_cell==(1,1):
            break
        for d in 'EWNS':
            if m.maze_map[current_cell][d]==True:
                if d=='E':
                    child_cell=(current_cell[0],current_cell[1]+1)
                if d=='W':
                    child_cell=(current_cell[0],current_cell[1]-1)
                if d=='N':
                    child_cell=(current_cell[0]-1,current_cell[1])
                if d=='S':
                    child_cell=(current_cell[0]+1,current_cell[1])
                
                temp_g_score=g_score[current_cell]+1
                temp_f_score=temp_g_score+h(child_cell,(1,1))

                if temp_f_score < f_score[child_cell]:
                    g_score[child_cell]=temp_g_score
                    f_score[child_cell]=temp_f_score
                    open.put((temp_f_score,h(child_cell,(1,1)),child_cell))
                    a_path[child_cell]=current_cell
    if(1,1) not in a_path:
        print("Not found!!!!")
        return{}
        
    fwd_path={}
    cell=(1,1)
    while cell!=start:
        fwd_path[a_path[cell]]=cell
        cell=a_path[cell]
    return fwd_path


if __name__=='__main__':
    m=maze(17,17)
    m.CreateMaze()
    path=a_star(m)

    a=agent(m, footprints=True)
    m.tracePath({a:path},delay=2)
    l=textLabel(m,'A_star Path length',len(path)+1)
    m.run()
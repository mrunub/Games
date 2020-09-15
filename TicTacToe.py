def clearscreen1():
    print("\n"*1000)
def tictactoe_print(ttt):
    for i in ttt:
        for j in i:
            print(j,end='')
        print()
def ask_to_play():
    set_YN=['Y','N']
    reply = 'S'
    while reply not in set_YN:
        reply=input("Want to play?\nSay\n 'Y' for yes \n 'N' for no \n")
        if reply.upper() not in set_YN:
            print("Enter either 'Y' OR 'N' ")
        elif reply.upper() == 'Y':
            print("Let's play!")
            return True
        else:
            print("Come again next time!")
            return False
import  string
def choose_symbol(i):
    symb=['0','0']
    #s='1'
    print(f"Choose symbol for player {i+1} :\n")
    while symb[i] not in string.ascii_letters:
        symb[i]=input("Enter only alphabet:")
        #print(symb)
    return symb[i]
def show_numpad():
    ttt=[['7',' | ','8',' | ','9'],['--','|','---','|','--- '],['4',' | ','5',' | ','6'],['--','|','---','|','--- '],['1',' | ','2',' | ','3']]
    tictactoe_print(ttt)
    print("\n(between 1 to 9 as on numpad)")
def ask_position():
    pos=100
    print("\nEnter position to play :")
    while int(pos) not in range(1,10):
        i=input("Enter digit on the numpad:")
        if i.isdigit() and int(i) in range(1,10):
            pos=i        
    return pos
def co_ord(position):
    d={'1':[4,0],'2':[4,2],'3':[4,4],'4':[2,0],'5':[2,2],'6':[2,4],'7':[0,0],'8':[0,2],'9':[0,4]}
    return d[position]  
def put_symbol(symb,position,ttt):
    #ttt=[[' ',' | ',' ',' | ',' '],['--','|','---','|','--- '],[' ',' | ',' ',' | ',' '],['--','|','---','|','--- '],[' ',' | ',' ',' | ',' ']]
    pos=co_ord(position)
    ttt[pos[0]][pos[1]]=symb
    tictactoe_print(ttt)
    return ttt
def row_check(r,axis,index):
    #print(f"Row: {r}")
    return [len(set(r))==1 and not list(set(r))[0]==' ',axis,index]
def win_check(ttt):
    valid_index=[0,2,4]
    flag_list=[False,0,0]
    r1,r2=[],[]
    for i in valid_index:
        flag_list=row_check(ttt[i][::2],0,i)
        if flag_list[0]:
            return flag_list
    for j in valid_index:
        flag_list=row_check([i[j] for i in ttt[::2]],1,j)
        if flag_list[0]:
            return flag_list
    for k in valid_index:
        r1.append(ttt[k][k])
    flag_list=row_check(r1,2,1)
    if flag_list[0]:
            return flag_list
    for k in valid_index:
        r2.append(ttt[k][4-k])
    flag_list=row_check(r2,2,2)
    if flag_list[0]:
            return flag_list
    return flag_list     
def replay():
    print("Play Again?")
    tictactoe()
def tictactoe():
    
    ttt=[[' ',' | ',' ',' | ',' '],['--','|','---','|','--- '],[' ',' | ',' ',' | ',' '],['--','|','---','|','--- '],[' ',' | ',' ',' | ',' ']]
   
    
    # Clear screen 
    #clearscreen1()
    
    # Ask for permission
    
    # Show tictactoe box
    tictactoe_print(ttt)
    
    # Boolean for want-to-play
    if ask_to_play():
        
        symb=['','']
        # Choose symbol for players
        symb[0]=choose_symbol(0)
        symb[1]=choose_symbol(1)
        if symb[1]==symb[0]:
            print("Use different symbol: ")
            symb[1]=choose_symbol(1)
        
        # Show numpad
        show_numpad()
        
        flag=False
        
        occupied=[]
        i=-1
        while not flag:
            i+=1
            # Ask position
            position=ask_position()
            if int(position) not in occupied:
                # Put symbol
                ttt=put_symbol(symb[i%2],position,ttt)
                occupied.append(int(position))
            
                flag_list = win_check(ttt)
                if flag_list[0]:
                    d={'0': 'Row', '1':'Column','2':'Diagonal'}
                    if flag_list[1] in [0,1]:
                        flag_list[2]//=2
                    print(f"{d[str(flag_list[1])]} {flag_list[2]} is full.\nPlayer {i%2+1} : {symb[i%2]} won! ")
                    replay()
                    flag=True
                    break
                if set(occupied)==set(range(1,10)):
                    replay()
                    break
                    
            else:
                avail=set(range(1,10)).difference(set(occupied))
                #print(f"Occupied: {occupied} Avail: {avail}")
                print(f"Sorry, try some other block in {avail}\n")
                
  

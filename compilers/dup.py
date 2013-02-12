def duplicate():
    list = [1,2,3,4,2,5,6,7,8]
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if(list[j] == list[i]):
                print "i: %d" % i
                print "j: %d" % j
                print True
                return True
    print False
    return False
    
def def_use():
    list =  [ ["x", []], ["y", ["y", "x"]], ["w", ["x","w"]], ["x", ["x","z"]] ]
    arr = []
    err = []
    
    if len(list[0][1]) != 0:
        err.append(list[0][0])
        for j in range(0,list[0][1]):
            arr.append(list[i][1][j])

    arr.append(list[0][0])
    
    for i in range(1,len(list)):
        for j in range(0,len(list[i][1])):
            if list[i][1][j] not in arr:
                if list[i][1][j] == list[i][0]:
                    err.append(list[i][0])
                arr.append(list[i][1][j])
        if list[i][0] not in arr:
                arr.append(list[i][0])
    
    print "printing err:"
    for i in range(0,len(err)):
        print err[i]

def search(k,arr):
    if len(arr)!=-1:
        for i in range(0,len(arr)):
            if k == arr[i]:
                return i
    return -1

def rearrange(x,i,list,arr,cnt):
    n = search(x,arr)
    if i+1 <= len(list):
        for j in range(i+1,len(list)):
            for l in range(0,len(list[j][1])):
                if cnt[n] == 0:
                    list[j][1][l] = list[j][1][l]
                else:
                    list[j][1][l] = list[j][1][l] + str(cnt[n])
    
def ssa():
    list = [ ["x", []],  ["y", ["x"]],  ["x", ["x","y"]], ["z", ["x","y"]], ["y", ["z","x"]]]
    
    arr = []
    cnt = []
    
    arr.append(list[0][0])
    cnt.append(0)
    
    for i in range(1,len(list)):
        k = search(list[i][0],arr)
        if k == -1:
            arr.append(list[i][0])
            cnt.append(0)
            print list[i][0]
        else:
            cnt[k] = cnt[k]+1
            list[i][0] = list[i][0] + str(cnt[k])
            rearrange(list[i][0],i,list,arr,cnt)
                                   
    print arr
    print list
    
duplicate()
def_use()
print "\nSSA:\n"
ssa()

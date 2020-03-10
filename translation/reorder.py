import nltk
from translation import variables


a=[]
#root=variables.root

def token(root):
   # global z
#    print(nltk.tree.Tree.label(root))
    cnt=nltk.tree.Tree.__len__(root)
    
    for subtree in root:
       if type(subtree) == nltk.tree.Tree:
             a.append(subtree)
            # print(a)
    a.append(root)
   # print(a)
    i=0
    while(i<= cnt):
        a[i]=mirror(a[i])
        #print(a[i])
        a[i]=generate_tree(a[i])
       # print(a[i])
        i=i+1
   
    
    i=0
    while(i<cnt):
     if(nltk.tree.Tree.label(a[i]) == 'NP'):
        preorder(a[i])
        variables.z=" ".join([variables.z,b])
     elif(nltk.tree.Tree.label(a[i]) == 'PP'):
        #print(a[i])
        preorder(a[i])
        variables.z=" ".join([variables.z,b])
     elif(nltk.tree.Tree.label(a[i]) == 'VP'):
        #print(a[i])
        for subtree in a[i]:
            if(nltk.tree.Tree.label(subtree) == 'NP'):
                subtree=mirror(subtree)
                #print(subtree)
                postorder(subtree)
                #print(c)
               # variables.z=" ".join([variables.z,c])
            else:
                #print(subtree)
                postorder(subtree)
                #print(c)
               # variables.z=" ".join([variables.z,c]) 
            #else:
        #postorder(a[i])
        variables.z=" ".join([variables.z,c])
       # c=""
     elif(nltk.tree.Tree.label(a[i]) == 'ADVP'):
        #print(a[i])
        #preorder(a[i])
        postorder(a[i])
        variables.z=" ".join([variables.z,b])
     elif(nltk.tree.Tree.label(a[i]) == 'ADJP'):
        #print(a[i])
        #mirror(a[i])
        postorder(a[i])
        variables.z=" ".join([variables.z,c])
     else:
     #   print(a[i])
        preorder(a[i]) 
       # print(x)
        variables.z=" ".join([variables.z,b])
     i=i+1


c=""
def postorder(tree):
    global c
    cnt=nltk.tree.Tree.__len__(tree)
    for subtree in tree:
       if type(subtree) == nltk.tree.Tree:
           while(cnt is not 0):
             cnt=cnt-1
             postorder(subtree)
             break  
       elif(nltk.tree.Tree.leaves(subtree)):
             c=" ".join([c,subtree])
             #print(c)
               
                   

b=""
def preorder(tree):
    global b
    cnt=nltk.tree.Tree.__len__(tree)
   # print("node :",nltk.tree.Tree.label(tree))
    for subtree in tree:
       if type(subtree) == nltk.tree.Tree:
           while(cnt is not 0):
             cnt=cnt-1
             preorder(subtree)
             break
       elif(nltk.tree.Tree.leaves(subtree)):
           b=" ".join([b,subtree])
          # print(b)
    

def generate_tree(tree): # to rearrange tokens from parsed treee  
  cnt1=len(tree)
  k=1
  tree1=tree[0]
    #print(tree)
  while k<cnt1:
         #print(k)
   tree1.append(tree[k])
  # print(tree)
   k=k+1
   #print(array)     
     
 # print(tree1)
  return (tree1)  
def mirror(root):
    #nltk.tree.Tree.label(a[i])
    #if(nltk.tree.Tree.label(root)=='NP'):
     #  return root
    cnt=nltk.tree.Tree.__len__(root)
   #print(cnt)
    no=cnt
    #print(root)
    a=nltk.tree.Tree.copy(root)
  #  print(a)
    while no>0:
      a.pop()
      no=no-1
    
    #print(root)
    i=1
    j=cnt
    array=[a]
    #print(array)
    for subtree in root:
       if type(subtree) == nltk.tree.Tree:
         array.append(subtree)
       elif(nltk.tree.Tree.leaves(subtree)):
            array.append(subtree)  
            return (array)
    #print(array)
    if cnt%2 is not 0:
      while i!=j:
          temp=array[i]
          array[i]=array[j]
          array[j]=temp
          i=i+1
          j=j-1
    elif cnt%2 is 0:
       while i<j:
          temp=array[i]
          array[i]=array[j]
          array[j]=temp
          i=i+1
          j=j-1
    #print(array)
    l=1
    while l<=cnt:
        tree=mirror(array[l])
        #print(tree)
        global generate_tree
        tree1=generate_tree(tree)
        #print(tree1)
        array[l]=tree1
      #  print(array)
        l=l+1    
    return (array)

#token(root)
#print("hello")

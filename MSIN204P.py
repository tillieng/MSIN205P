##Import a CSV module
import csv
import time as t
import matplotlib.pyplot as plt

#import matplotlib.pyplot as plt


#Open the CSV file being used and pull out specific data (name, value, weight) from the spreadsheet and save it to a list variable
def getfile():
 with open('ftse100.csv','rU') as csvdatafile:
    combineList = []
    parsing = []
    name = []
    value = []
    weight = []

    csvreader = csv.reader(csvdatafile) 
    
    for row in csvreader:        #Read rows
        name.append(row[0])     #Insert name 
        temp1 = float(row[1].replace(",", "")) #remove ',' and typecast to float
        temp2 = float(row[2].replace(",", "")) #remove ',' and typecast to float
        value.append(int(temp1) )
        weight.append(int(temp2))


    #In another format
    for index in range(0, len(name)):
        temp = []
        temp.append(weight[index])
        temp.append(value[index]);
        temp.append(name[index]);
        parsing.append(tuple(temp))

 return name, value, weight, parsing





#Bottom-up approach
#Return the maximum value given the constraint of capacity W
#toConsider: items that have nodes higher up in the tree that are yet to be considered
#avail: amount of capacity that is still available
def MaxVal(toConsider, avail):
    
#memo: a parameter to keep track of solutions to subproblems that have already been solved
    if (len(toConsider),avail)in memo:
        result = memo[(len(toConsider),avail)]

#Base Case: If there are no items in the knapsack, the outcome will be zero, therefore return 0
    elif toConsider == [] or avail == 0:
        return 0

#If the weight is greater than the capacity available, it cannot be included in the Knapsack and hence cannot be included in the optimal solution 
    elif toConsider [0].getWeight() > avail:
        result = MaxVal(toConsider[1:],avail,memo)
        
#Find the difference between the capacity and the weight of the nth item
#Add the maximum value of n-1 items to the value of the nextItem
    else:
        nextItem = toConsider[0]
        withVal, withToTake = MaxVal(toConsider[1:],avail - nextItem.getWeight(),memo)
        withVal += nextItem.getValue()
        
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],avail,memo)

#Compare the values and return the one which gives a greater value
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider),avail)] = result
    return result
                                        

#Recursive structure
#Return the maximum value given the constraint of:
#W = capacity
#wt = weight
#val = value
#n = number of items
def recursive(W , wt , val , n):
 
    # Base Case: If weight of the nth item is 0 and the capacity of the Knapsack (W) is 0, we return 0
    if n == 0 or W == 0 :
        return 0
 
    # If weight of the nth item is more than Knapsack of capacity W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W , wt , val , n-1)
 
    # Return the maximum of two cases:
    # (1) nth item is included
    # (2) nth item is not included
    #Find the difference between the capacity and the weight of the nth item
    #Add the maximum value of n-1 items to the value of the next item
    else:
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1),
                   knapSack(W , wt , val , n-1))


#Dynamic programming using bottom-up approach
#Return the maximum value that can be put in a knapsack of capacity W
#W = capacity
#wt = weight
#val = value
#n = number of items
def dynamicButtomUP(W, wt, val):
    n = len(wt)
    K = [[0 for x in range(W+1)for x in range(n+1)]]
    
    #Build table K[][] in bottom up manner
    for i in range (n+1):
        for w in range (W+1):
    # Initialize the tables by filling the 0 row (no items)
            if i==0 or w==0:
                K[i][w]=0
    #If this item weighs less than or equal to the previous item 
            elif wt[i-1]<=w:
                K[i][w]=max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w])
            else:
                K[i][w]=K[i-1][w]

    return K[n][W]


def dynamicTopDown(W, wt, val, n):
    # Initialize the tables by filling the 0 row (no items)
    for j in range(0, W+1): 
        m.append([])
        for i in range(0, n+1):
            m[j].append(0)
    for i in range(0, n+1):
        for j in range(0, W+1):
            if i == 0 or j == 0:
                m[j][i] = 0
            elif weights[i - 1] <= j:
                m[j][i] = max(m[j][i - 1], m[j - weights[i - 1]][i - 1] + values[i - 1])
            else:
                m[j][i] = m[j][i - 1]

def get_solution(k, weights, n, W):
    items = []
    for i in range(0, n):
        k.append(0)
    cap = W + 1
    for i in xrange(n, 0, -1):
        # instead of 0/1 keep array we use the condition if upper cell is smaller then we pick this item
        if m[cap - 1][i] > m[cap - 1][i - 1]:
            k[i - 1] = 1
            cap = cap - weights[i - 1]

    value = m[W][n]
    for i in xrange(0, n):
        if k[i] == 1:
            items.append(i+1)
    return value, items

#-------------------------------------------


def itemSize(item): return item[0]
def itemValue(item): return item[1]
def itemName(item): return item[2]

def recursive(items,sizeLimit):
	P = {}
	for nItems in range(len(items)+1):
		for lim in range(sizeLimit+1):
			if nItems == 0:
				P[nItems,lim] = 0
			elif itemSize(items[nItems-1]) > lim:
				P[nItems,lim] = P[nItems-1,lim]
			else:
				P[nItems,lim] = max(P[nItems-1,lim],
				    P[nItems-1,lim-itemSize(items[nItems-1])] +
					itemValue(items[nItems-1]))
	return P[len(items),sizeLimit]



#Caluculate max investments using dynamic bottom up approach
def dynamicBU(items,sizeLimit):
        global loopcounter
	P = {}
	for nItems in range(len(items)+1):
                loopcounter = loopcounter + 1
		for lim in range(sizeLimit+1):
                        loopcounter = loopcounter + 1
			if nItems == 0:
				P[nItems,lim] = 0
			elif itemSize(items[nItems-1]) > lim:
				P[nItems,lim] = P[nItems-1,lim]
			else:
				P[nItems,lim] = max(P[nItems-1,lim],
				    P[nItems-1,lim-itemSize(items[nItems-1])] +
					itemValue(items[nItems-1]))
	
	L = []		
	nItems = len(items)
	lim = sizeLimit
	while nItems > 0:
                loopcounter = loopcounter + 1
		if P[nItems,lim] == P[nItems-1,lim]:
			nItems -= 1
		else:
			nItems -= 1
			L.append(itemName(items[nItems]))
			lim -= itemSize(items[nItems])

	L.reverse()
	return L

def calculate_dynamicBP_sum(ftse, L):
    price = []
    for company in L:
       for x in range(len(ftse)):
          if ftse[x][2] == company:
              price.append(ftse[x][1])
    return sum(price)




#Main function
name, value, weight, example = getfile()
exampleSizeLimit = 1000

global loopcounter
loopcounter = 0
print("results:")
start = t.time()
L = dynamicBU(example,exampleSizeLimit)
end1 = t.time()
print (L)
print("Timer1 :"+ str(end1-start) +"\n")


start = t.time()
print("return value = " + str(calculate_dynamicBP_sum(example, L)))
end2 = t.time() - start    #end time
print("Time2: " + str(end2))
print("Number of loops " + str(loopcounter) )


#Complexity Calculation
weightValue = []
timevalue = []
loopNum = []
for w in range(100, 30000, 600): 
      weightValue.append(w)
      count = t.time()
      loopcounter = 0
      L = dynamicBU(example, w)
      val = calculate_dynamicBP_sum(example, L)
      endtime = t.time() - count
      timevalue.append(endtime)
      loopNum.append(loopcounter)


print(weightValue);print(timevalue);print(loopNum)
  
plt.subplot(211)
plt.plot(weightValue, timevalue)
plt.axis([0, 32000, 0, 5])
plt.ylabel('time in seconds')
plt.xlabel('input Weight')
plt.grid(True)
   
plt.subplot(212)
plt.plot(weightValue, loopNum)
plt.axis([0, 8500, 0, 800000 ])
plt.ylabel('Number of loops')
plt.xlabel('input Weight')
plt.grid(True)

plt.show()




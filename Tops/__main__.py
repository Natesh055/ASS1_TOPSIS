import numpy as np

def step1(dec_matrix):
    # Compute the square root of the sum of squares along axis 0 (column-wise)
    sqrtSum = np.sqrt(np.sum(np.square(dec_matrix), axis=0))
    # Normalize the matrix by dividing each element by the column's sqrtSum
    dec_matrix = dec_matrix / sqrtSum
    return dec_matrix



def step2(dec_matrix,weights):
    return dec_matrix*weights




def step3a(dec_matrix,impact):
    col=len(dec_matrix[0])
    row=len(dec_matrix)
    minValues=np.min(dec_matrix, axis=0) 
    maxValues=np.max(dec_matrix, axis=0)
    
    idealSol=np.zeros((1,col))
    for i in range(0,col):
        if(impact[i]==1):
            idealSol[0][i]=maxValues[i]
        else:
            idealSol[0][i]=minValues[i]
    return idealSol






def step3b(dec_matrix,impact):
    col=len(dec_matrix[0])
    row=len(dec_matrix)
    minValues=np.min(dec_matrix, axis=0) 
    maxValues=np.max(dec_matrix, axis=0)
    
    negIdealSol=np.zeros((1,col))
    for i in range(0,col):
        if(impact[i]==1):
            negIdealSol[0][i]=minValues[i]
        else:
            negIdealSol[0][i]=maxValues[i]
    return negIdealSol 







def step4a(idealSol,dec_matrix):
    return np.sqrt(np.sum(np.square(dec_matrix-idealSol),axis=1))

def step4b(negIdealSol,dec_matrix):
    return np.sqrt(np.sum(np.square(dec_matrix-negIdealSol),axis=1))






def step5(idealSol,negIdealSol):
    return (negIdealSol)/(idealSol+negIdealSol)







def topsisCalc(dec_matrix,weights,impacts):
    dec_matrix=step1(dec_matrix)
    dec_matrix=step2(dec_matrix,weights)
    idealSol=step3a(dec_matrix,impacts)
    negIdealSol=step3b(dec_matrix,impacts)
    eucIdeal=step4a(idealSol,dec_matrix)
    eucNonIdeal=step4b(negIdealSol,dec_matrix)
    relClos=step5(eucIdeal,eucNonIdeal)
    print("BEST DESICION: ",max(relClos),"\n")
    print("WORST DESICION: ",min(relClos),"\n")





if __name__ == "__main__":
  
    # parse command line arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument("InputDataFile", help="Enter the name of CSV file with .csv extention",type=str)
    parser.add_argument("Weights", nargs=1, help="Enter the weight vector comma separated" ,type=str)
    parser.add_argument("Impacts", nargs=1, help="Enter the impact vector comma separated",type=str)
    args = parser.parse_args()
    

    main(vars(args))
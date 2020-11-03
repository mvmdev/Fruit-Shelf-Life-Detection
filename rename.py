import os 
  
# Function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir("E:\photo ml\crop\day 5")): 
        dst ="Day5_" + str(count) + ".jpg"
        src ='E:\photo ml\crop\day 5\\'+ filename 
        dst ='E:\photo ml\crop\day 5\\'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main()
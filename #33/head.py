import sys
import argparse

#Main function to mimic head command
def main(files, n, c):

    #Check args has file name. If not then take in the 
    #consle input
    if not files:
        while True:
            print(input())
        pass

    #Loop through multiple files
    for file in files:
        count = 0
        print(f"==> {file} <==")

        #Conditional logic based on line or byte request

        if n:
            file_1 = open(file, 'r')
            for i in range(int(n)):
                line = file_1.readline()

                #End if document ends before the n lines 
                if not line:
                    break
                count += 1
                print(line.strip())

        elif c:
            file_1 = open(file, 'rb')
            file = file_1.read(int(c))
            #Ignoring non ascii cahracters while printing byte stream
            print(file.decode('ascii', errors = 'ignore'))

        #If no flags, then print entire document
        else:
            while line := file_1.readline():

                count += 1
                print(line.strip())
        
        

if __name__ == "__main__":

    parser = argparse.ArgumentParser("Displays the top n lines of text")
    parser.add_argument('-n', help="Displays top n lines")
    parser.add_argument('-c', help="Displays top n bytes")
    parser.add_argument('files', nargs="*", help="List of files")
    args = parser.parse_args()
    
    main(**vars(args))
import mmh3    #for hash function
import math

file1 = open('books.txt', 'r')   #opens file with book titles
file2 = open('data.txt', 'r')    #open file with book's data

books_lst = file1.readlines()    #list of books
data_lst = file2.readlines()     #list of data

books = []
data = []

for i in books_lst:
    books.append(i.strip())
for j in data_lst:
    data.append(j.strip())

#for nested list of data
i=0                         
info=[]
while i<len(data):
  info.append(data[i:i+3])
  i+=3
     
def bit_array(n):  #returns bit array size
    
    bin_array = [0] * (int((2 * n)/math.log(2))) #2 number 0f hash functions
    return bin_array

#to populate the bit array with 1's using hash functions
def add(lines):                     
    bin_array = bit_array(52)
    for i in lines: 
        index1 = mmh3.hash(i) % len(bin_array)
        index2 = hash(i) % len(bin_array)
        bin_array[index1] = 1   #changing 0s to 1s
        bin_array[index2] = 1   #changing 0s to 1s
    return bin_array

#main bllom functions
def bloom(obj):
    bin_array = add(books)
    in1 = mmh3.hash(obj) % len(bin_array)  #constant complexity, as it is comparing only, with given index.
    in2 = hash(obj) % len(bin_array)
    if bin_array[in1]==1 & bin_array[in2]==1:   #to check if there are 1s at specific index
        return True                             #item found
    else: return False                          #item not found
    
    
#extra functionality
    
def Book_details(obj):
    if (bloom(obj)):                                #if object found
        if obj in books:                            #to know if we have false positive
            index_book =  books.index(obj)          #index of that object, to use it for extra data
            author =   info[index_book][0]          #gives the author of book from nested list
            ratings = info[index_book][1]           #gives the rating of book from nested list
            genre = info[index_book][2]             ##gives the genre of book from nested list
            new = []
            for i in range(len(books_lst)):
                if info[index_book][2] == info[i][2]:   #to find boks with similar genres
                    new.append(books[i])
            similar = ""
            for i in range(1, len(new)):
                similar+= str(i)+". "+new[i]+"\n"       # string of books with similar genres
        
            out = ("You have read this book. \nBook's Title: " + obj + "\nThe author of this book is: " + author + "\nYour Rating: " + ratings + "\nThe Genre is: " + genre ) 
        else: out = "False Poaitive"
    else: 
        similar = "   No books found :("
        out = ("Book's Title: "+ obj +"\nYou have not read this book.")
    
    return out,"Similar Books are:\n"+similar

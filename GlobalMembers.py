//====================================================================================================
//The Free Edition of C++ to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-cplus-to-python.html
//====================================================================================================

class GlobalMembers(object):
    #void printArray(int a[][100],int m,int n){
    @staticmethod
    def printArray(self, a, m, n):
        while i<m:
            while j<n:
                print(a[i][j], end = '')
                print(" ", end = '')
            j += 1
            print("\n", end = '')
        i += 1


    @staticmethod
    def main():
        #int a[100][100]
        #int m,n
        #cout<<"Enter the number of rows;"<<endl
        #cin>>m
        #cout<<"Enter the number of columns;"<<endl
        #cin>>n
        #for(int i=0;i<m;i++){
        #    for(int j=0;j<n;j++){
        #        cin>>a[i][j]
        #    }
        #}
        a = [[1, 2, 0, 0, 0], [3, 4, 0, 0, 0], [5, 6, 0, 0, 0]]
        printArray(a, 5, 5)


    @staticmethod
    def findLargest(self, a, n, m):

        rowsum = 0
        rowindex = 0
        while i<n:
            sum = 0
            while j<m:
                sum+=a[i][j]
            j += 1
            if sum> rowsum:
                rowsum = sum
                rowindex = i
        i += 1
        columnsum = 0
        columnindex = 0
        while j<m:
            sum = 0
            while i<n:
                sum+=a[i][j]
            i += 1
            if sum> columnsum:
                columnsum = sum
                columnindex = j
        j += 1
        if rowsum == 0 and columnsum == 0:
            print("row 0 -2147483638", end = '')
        elif rowsum == columnsum:
            print("rows ", end = '')
            print(rowindex, end = '')
            print(" ", end = '')
            print(rowsum, end = '')
            print("\n", end = '')
        elif rowsum> columnsum:
            print("rows ", end = '')
            print(rowindex, end = '')
            print(" ", end = '')
            print(rowsum, end = '')
            print("\n", end = '')
        else:
            print("columns ", end = '')
            print(columnindex, end = '')
            print(" ", end = '')
            print(columnsum, end = '')
            print("\n", end = '')
    @staticmethod
    def main():
#C++ TO PYTHON CONVERTER TODO TASK: Jagged array declarations without value initializers are not converted by C++ to Python Converter:
        a = new int[100][100]
        m = None
        n = None
        cin>> m>> n
        while i<n:
            while j<m:
                cin>> a[i][j]
            j += 1
        i += 1
        findLargest(a, n, m)



    @staticmethod
    def main():

#C++ TO PYTHON CONVERTER TODO TASK: Jagged array declarations without value initializers are not converted by C++ to Python Converter:
        a = new int[100][100]
        m = None
        n = None
        print("enter the number of rows: ", end = '')
        print("\n", end = '')
        cin>> m
        print("enter the number of columns: ", end = '')
        print("\n", end = '')
        cin>> n
        # printing rowWise

        #taking input
        print("Enter the elements", end = '')
        print("\n", end = '')
        while i<m:
            while j<n:
                cin>> a[i][j]
            j += 1
        i += 1
        #print output
        print("Print RowWise: ", end = '')
        print("\n", end = '')
        while i<m:
            while j<n:
                print(a[i][j], end = '')
                print(" ", end = '')
            j += 1
            print("\n", end = '')
        i += 1

        # printing columnWise

        print("print ColumnWise: ", end = '')
        print("\n", end = '')
        while j<n:

//====================================================================================================
//End of the allowed output for the Free Edition of C++ to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-cplus-to-python.html
//====================================================================================================

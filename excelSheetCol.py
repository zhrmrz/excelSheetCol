class Sol:
    def excelSheetCol(self,num):
        res=""
        while num:
            res+=chr((num-1)%26+ord("A"))
            num=(num-1)//26
        return res[::-1]
if __name__ == '__main__':
    p1=Sol()
    print(p1.excelSheetCol(28))


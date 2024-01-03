class Lib:
    def __init__(self,book_name,book_id,year,author,is_borrowed):
        self.book_name = book_name
        self.book_id = book_id
        self.year = year
        self.author = author
        self.is_borrowed = is_borrowed
    #查詢書本
    def find_book(self,book,book_id):
        for book in self.book_name:
            if self.book_id == book_id:
                return book
            return print("沒有查閱到此書")
    #借閱書本
    def borrow(self):
        if(self.is_borrowed == True):
            return print("該書已被借閱,請之後再借")
        else:
            self.is_borrowed = True
            return print('成功借閱到此書！')
    #歸還書本
    def return_book(self):
        if(self.is_borrowed == True):
            self.is_borrowed = False
            return print("成功歸還此書！")
        else:
            return print("歸還失敗,可能查無此書或者已經歸還!")
            
            
    
def  main():
    obj1 = Lib('馬斯克傳','1234','2023/09/27','Walter Isaacson',False)
    obj1.find_book('馬哥傳','65555')
    obj1.borrow()
    obj1.return_book()
    obj1.return_book()
if __name__ == '__main__':
    main()

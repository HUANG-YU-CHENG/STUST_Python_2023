from datetime import datetime
class Lib:
    def __init__(self,book_name,book_id,year,author,is_borrowed,borrow_time,lib_postion):
        self.book_name = book_name
        self.book_id = book_id
        self.year = year
        self.author = author
        self.is_borrowed = is_borrowed
        self.borrow_time = borrow_time
        self.lib_postion = lib_postion
    #查詢書本
    def find_book(self,book_id):
        if self.book_id == book_id:
            return print(self.book_name)
        return print("沒有查閱到此書")
    #借閱書本
    def borrow(self):
        if(self.is_borrowed == True):
            return print("該書已被借閱,請之後再借")
        else:
            self.is_borrowed = True
            return print(f'成功借閱到此書！借閱時間為{self.borrow_time}')
    #歸還書本
    def return_book(self):
        if(self.is_borrowed == True):
            self.is_borrowed = False
            return print("成功歸還此書！")
        else:
            return print("歸還失敗,可能查無此書或者已經歸還!")
def  main():
    borrow_time = datetime.now().strftime("%Y年%m月%d日 %H時%M分%S秒 %p")
    obj1 = Lib('馬斯克傳','1234','2023/09/27','Walter Isaacson',False,borrow_time,'B')
    obj1.find_book('1234')
    obj1.borrow()
    obj1.return_book()
if __name__ == '__main__':
    main()

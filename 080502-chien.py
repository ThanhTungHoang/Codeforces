#Quan ly dia CD: TenCD, Casi, Sobaihat, Gia thanh,
#khi mua CD: So luong CD hien co,

import csv

#Tim
    #input: Ten CD, Ten Casi
    #output: list cua thong tin CD do
def searchCD(keyCD, dataCD, lstCD):
    infoCD = []
    if keyCD == "nameSinger":
        # print(len(lstCD))
        for item in range(0,len(lstCD)):
            if dataCD == lstCD[item][1]:
                infoCD.append(lstCD[item])
    elif keyCD == "nameCD":
        for item in range(0,len(lstCD)):
            if dataCD == lstCD[item][0]:
                # infoCD.append(lstCD[item])
                infoCD = lstCD[item]
    # print(infoCD)
    return infoCD

#Sua
    #input: ten Cd can sua, danh sach chua cai cd đó
    #output: list cd mà có cái cd đã sửa đó
#[["aaa", "a", 12, 100, 22], ["bbb", "b", 10, 200, 10], ["abcd", "a", 22, 400, 9]]
def modifyCD(cdNameToModify, lstCDToModify):
    # cdAfterModify = []
    check = True
    for i in range(0,len(lstCDToModify)):
        if(cdNameToModify == lstCDToModify[i][0]):
            while(check):
                print("Lua chon thong tin can sua. \nNhap 0: sua ten album\nNhap 1: sua ten ca si. \nNhap 2: sua so luong bai hat.\nNhap 3: sua gia tien \nNhap 4: sua so luong ton kho")
                select = int(input("Lua chon cua ban la: "))
                if(select == 0):
                    lstCDToModify[i][select] = input("Ten album moi la: ")
                elif(select == 1):
                    lstCDToModify[i][select] = input("Ten ca si moi la: ")
                elif(select == 2):
                    lstCDToModify[i][select] = int(input("So luong bai hat moi la: "))
                elif(select == 3):
                    lstCDToModify[i][select] = int(input("Gia tien moi la: "))
                elif(select == 4):
                    lstCDToModify[i][select] = int(input("So luong ton kho moi la: "))
                else:
                    print("Ban nhap sai, nhap lai \n-----------")
                    continue
                continueMod = input("ban co muon sua tiep cac thong tin khac khong(Y/N)")
                if(continueMod == "N" or continueMod == "n"):
                    check = False
    return lstCDToModify
#Xoa
    #input: Ten Cd can xoa, danh sach chua cai cd do
    #output: lít cd ma co cai cd cần xóa đi đó
def deleteCD(cdNameToDelete, lstCDToDelete):
    checkDelete = 0
    for item in lstCDToDelete:
        if(item[0] == cdNameToDelete):
            lstCDToDelete.remove(item)
        else:
            checkDelete = checkDelete + 1
    if (checkDelete == len(lstCDToDelete)):
        print("Khong ton tai CD co ten la %s" %cdNameToDelete)
    return lstCDToDelete
#In
    #input: list chứa tất cả cd mà m muốn in
    #output: không có chi
def printListCD(lstCDToPrint):
    for item in lstCDToPrint:
            print("# %s - %s - %d - %d - %d" %(item[0], item[1], item[2], item[3], item[4]))
#Menu
    #input: danh sách cd mà chúng ta làm việc
    #output: chức năng người dùng chọn
def menu():
    pass
#Them
    #Them moi
    #THem vao nhung dia da co => so luong
    #input: List:TenCD, Casi, Sobaihat, Gia thanh, so luong
    #output: list da them vao
def update(lstUpdate, lstCDUPdate):
    checkExist = len(lstCDUPdate)
    for item in range(0, len(lstCDUPdate)):
        if lstUpdate[0] == lstCDUPdate[item][0]:
            lstCDUPdate[item][4] = lstCDUPdate[item][4] + lstUpdate[4]
        else:
            checkExist = checkExist - 1
            # lstCDUPdate.append(lstUpdate)
    if checkExist == 0:
        lstCDUPdate.append(lstUpdate)
    lstAfterUpdate = lstCDUPdate
    return lstAfterUpdate

# Lay danh sach tu file csv co san
    #input: duongd dan cua file csv do
    #output: list chứa thông tin của cd
def getListCD(path):
    lstCDInitial = []
    with open(path, 'r', newline='') as file:
        spamreader = csv.reader(file, delimiter=' ', quotechar='|')
        line = 0
        for row in spamreader:
            singleCD = list()
            if line == 0:
                line += 1
            else:
                singleCD = row[0].split(",")
                singleCD[2] = int(singleCD[2])
                singleCD[3] = int(singleCD[3])
                singleCD[4] = int(singleCD[4])
                line += 1
                lstCDInitial.append(singleCD)
    return lstCDInitial

# Save danh sach cd vao file csv
    #input: duong dan cua file csv do, danh sach can luu vao
    #output: 
def saveListCD(path, lstCDToSave):
    lstCDToSave.insert(0, ["CDName", "Singer", "Songs", "Price", "Stock"])
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lstCDToSave)
    

def main():
    pathCSV = 'C:/Users/ADMIN/Desktop/data.csv'
    lst = getListCD(pathCSV)
    # lst = [["aaa", "a", 12, 100, 0], ["bbb", "b", 10, 200, 20], ["abcd", "a", 22, 400, 9]]
    check = True
    while(check):
        print("\t\t---***    Chương trình quản lý đĩa CD    ***---")#61+8+8
        print("-"*77)
        print("\t\t      ---*** Danh sách CD hiện tại ***---")
        printListCD(lst)
        # print(lst)
        print("-"*77)
        print("Lựa chọn chức năng cần có")
        print("Chọn 1 để thêm CD mới \nChọn 2 để sửa CD có sẵn.\nChọn 3 để xóa CD\nChọn 4 để cập nhật số lượng tồn kho")
        selectOpt = int(input("Lựa chọn của bạn là: "))
        print("-"*77)
        if (selectOpt == 1):
            lstCDUpdateM = []
            print("\t\t   ---***Nhập thông tin CD cần update***---")
            lstCDUpdateM.append(input("Tên Ablum: "))
            lstCDUpdateM.append(input("Tên Ca sĩ: "))
            lstCDUpdateM.append(int(input("SL bài hát: ")))
            lstCDUpdateM.append(int(input("Giá tiền: ")))
            lstCDUpdateM.append(int(input("SL đĩa: ")))
            lst = update(lstCDUpdateM, lst)
        elif(selectOpt == 2):
            modifyCDName = input("Ten album can sua la: ")
            lst = modifyCD(modifyCDName, lst)
        elif(selectOpt == 3):
            deleteCDName = input("Ten album can xoa la: ")
            lst = deleteCD(deleteCDName, lst)
        elif(selectOpt == 4):
            print("List ban dau", lst)
            updateCDName = input("Ten album ban muon them so luong dia: ")
            thisCD = searchCD("nameCD", updateCDName, lst).copy()
            soLuongDia = int(input("So luong dia can them vao: "))
            thisCD[4] = soLuongDia
            lst = update(thisCD, lst)
        printListCD(lst)
        # print(lst)
        check = False
        
    
    # lst = [["aaa", "a", 12, 100, 22], ["bbb", "b", 10, 200, 10], ["abcd", "a", 22, 400, 9]]
    # lst = update(["axax", "b", 10, 200, 20], lst)
    # lstSearch = searchCD("nameSinger", "a", lst)
    # print(lstSearch)
    # lst = deleteCD("avvvvvv", lst)
    # lst = deleteCD("aaa", lst)
    # printListCD(lst)
    # print(infoCDafterSearch)  

if __name__ == "__main__":
    main()
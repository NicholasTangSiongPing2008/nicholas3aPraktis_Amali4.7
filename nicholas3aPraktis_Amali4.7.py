pi=3.142
def kira_kuboid(a,b,c):
    isipadu_kuboid=a * b * c
    return isipadu_kuboid           
def kira_silinder(a,b):
    isipadu_silinder=pi*a**2*b
    return isipadu_silinder
def kira_kon(a,b):
    isipadu_kon=1/3*pi*a**2*b
    return isipadu_kon
def kira_sfera(a):
    isipadu_sfera=4/3*pi*a**3
    return isipadu_sfera
def repeat():
    jwp=int(input("*********************************\n          Menu Mengira Isi padu\n*********************************\n1.Kuboid\n2.Silinder\n3.Kon\n4.Sfera\n*********************************\nMasukkan pilihan anda: [1 - 4]: ___"))
    if jwp==1:
        tinggi=float(input("Masukkan tinggi:"))
        lebar=float(input("Masukkan lebar:"))
        panjang=float(input("Masukkan panjang:"))
        print("Isipadu kuboid=",kira_kuboid(tinggi,lebar,panjang))
    else:
        r=float(input("Masukkan radius:"))
        if jwp==4:
            print("Isipadu bagi sfera ini ialah",kira_sfera(r))
        else:
            h=float(input("Masukkan ketinggian:"))
            if jwp == 2:
                print("Isipadu bagi silinder ialah",kira_silinder(r,h))
            else:
                print("Isipadu bagi kon ini ialah",kira_kon(r,h))
ulang="y"  
while ulang==("y"):
    repeat()
    ulang=str(input("Mahu kira lagi? Tekan [y] atau [t]:"))
print("\nTerima kasih")

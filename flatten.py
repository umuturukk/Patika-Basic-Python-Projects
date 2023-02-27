n = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatlist = [] 

def flatten(n):
    for i in n:
        # i objesi list sınıfının bir instance'ı mı?
        if isinstance(i, list):
            flatten(i) # Eğer i objesi list sınıfından bir instance ise flatten fonksiyonunu tekrar çağır. (recursive function)
        else:
            flatlist.append(i) # i objesi list sınıfından bir instance değilse, örneğin bir string, integer veya herhangi bir veri tipiyse zaten düz non-scalar haldedir. Bundan dolayı direkt olarak boş olan flatlist'imizin içine ekleyebiliriz.

flatten(n) # Fonksiyonu vermiş olduğumuz n listesi için çağırıyoruz.
print(flatlist) # n listesinin düzleşmiş olan son halini print ediyoruz.
l = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(l):
    l = l[::-1] # l.reverse() fonksiyonu da kullanılabilirdi.
    reverseL = [l[i][::-1] for i in range(len(l))] # Reverse edilmiş olan l listesinin içinde index index dolaşarak liste halinde olan indexlerin içindeki elemanları da ters çevirmiş olacağız. l listesinin uzunluğu kadar iterasyon yaparak indexleri dolaşıyoruz.
    return reverseL

print(reverse(l))

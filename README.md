Herkese merhaba,
Acil kan ihtiyacı, kaybolan hayvanlar insanlar vb. postları uplamak istiyoruz; ama tepedeki bir postu uplamak saçma olduğundan sonra uplarım deyip geçiyoruz, sonra da unutulabiliyor. Bunun için çok önemli gördüğümüz postları belli aralıklarla otomatik uplamak için birşeyler yaptım, biraz donanımhaber postu gibi olacak maalesef. Sırasıyla yaparsanız karışık olmayacak:

Önemli: Linux ve Mac kullananlar kullanabilir.
ÖNEMLİ: Yanlış veya kötüye kullanırsanız muhtemelen gruptan atılırsınız, https://eksisozluk.com/entry/4375173 .

1. https://developers.facebook.com/tools/explorer a girin
2. Üstten ikinci çubuktaki v2.3 ü seçin
3. Sağda "Get Token" a basıp, sonra "Get User Access Token" a dıkhlayın
4. publish_actions ve user_groups u seçip devam edin
5. Devam edin
6. Access token yazan çubuktaki token ı kopyalayın. ÖNEMLİ: Kimseye vermeyin.
7. Eklediğim dosyaları (upla.py,upla.sh ve upposts.txt) seçtiğiniz bir klasörün içine koyun, Desktop gibi
8. upla.py yi açın, 'insert token' yazan yeri bulup, insert token yazısını silip (öh) token ı yapıştırın.
9. upposts.txt dosyasının içine post id leri yazmanız lazım (see figure).
10. Terminal denen o uygulamayı bulun ve açın (hollywood filmlerindeki siyah ekran)
11. /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"      
yazıp enter a basın (bekleyin de bitsin)
12. brew install python      
yazıp enter a basın (bekleyin de bitsin)
13. sudo easy_install -U requests     
yazıp enter a basın, şifre isteyecek, şifrenizi yazıp enter a basın (bekleyin de bitsin)
14. Dosyaları 7. de Desktop'a koyduysanız, 
Linux için: cd /home/{bilgisayar kullanıcı adı}/Desktop      
Mac için: cd /Users/{bilgisayar kullanıcı adı}/Desktop (örnek: cd /home/mahmut/Desktop)      
yazıp enter a basın
15. upla.sh dosyasında b=3, 3 kere uplama yapacaksınız demek, istediğiniz sayıyla değiştirin. sleep 10m, 10 dakika aralıklarla uplayacaksınız demek. sleep 5s ile değiştirirseniz 5 saniye, sleep 3h ile değiştirirseniz 3 saat arayla uplar vs. Değişiklikleri yapıp, dosyayı kaydedip çıkın. ÖNEMLİ: bu maddede ekstra bir yeri değiştirirseniz yan basabilirsiniz, yapmayın.
16. sh upla.sh     
yazıp enter a basın

Upladık hayırlı olsun. Aa dur ya hala uplıyo. Hehe tamam bitti. Sorunuz varsa sorabilirsiniz, iyi akşamlar. 

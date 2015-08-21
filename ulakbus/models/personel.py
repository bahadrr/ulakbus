'''
aciklama  		explanation
ad                      name
adaylik                 nomination
adres_il_kod            address_city_code
adres_ilce_kod          address_town_code
adress1                 address1
adress2                 address2
aile_sira_no            family_serial_no
ana_ad                  mother_name
anket                   survey
arsiv                   archive
askerlik_nevi		soldiery_type
asil_ad 		reel_name
asil_dogum_tarihi	reel_birth_date
asil_soyad		reel_surname
astegmen_nasp_tarihi	astegmen_nasip_date
ayrilma_nedeni		quit_job_reason 

baba_ad                 father_name
bagkur_meslek		bagkur_job
banka_sandık_kod	bank_chest_dode
bolum 			graduation_department
bolum_adı		department_name
brans                   branch

cep_telefon             mobile_phone
cilt_no                 volume_no
cinsiyet                gender

denklik_bolum		equivalent_departmen
denklik_okul		equivalent_school
denklik_tarihi		equivalent_date
dogum_tarih             birth_date
dogum_yer               birth_place
durum 			status

ek_gosterge             additional_indicator
emekli_giris_tarih      retirement_start_date
emekli_sicil_no         retirement_no
emekli_sicil6495	retirement_registry6495
eposta1                 primary_email
eposta2                 secondary_email
ev_telefon              home_phone

gecerli_dogum_tarihi	valid_birth_date
gorev 			duty 
gorev_aciklama          task_desc
goreve_baslama_tarihi   assignment_start_date
gorev_bitis_tarihi      assignment_end_date
gorev_tarihi6495	duty_time6495
gorev_uzatma            duty_time_extension
gun_sayisi		number_of_days

hazırlık		prep_class
hitap_ack               hitap_ack ???
hitap_gonderme_tarih    hitap_request_departure_date
hitap_hata_kod          hitap_error_code
hitap_hata_mesaj        hitap_error_message
hitap_id                hitap_id
hizmet_sinif_kod        labour_class_code

il_kod                  city
ilce_kod                town_code
ilk_soyad               first_surname
is_adres                work_address
is_telefon              work_phone

kadrosuzluk		not_on_the_permanent_staff
kamu_isyeri_adı		ssk_kamu_workspace_name
kan_grup                blood_type
karar_kesinlestirme_tarihi	judgment_confirmation_date
karar_tarihi		judgment_date
karar_sayisi		judgment_count
kha_durumu		kha_status
kıdem_tazminatı_durumu 	severance_pay_status
kimlik_seri             identity_serial_no
kimlik_no               identity_no
kimlik_veren_yer        place_of_identity_given
kimlik_kayit_no         identity_registry_no
kimlik_verilis_neden    identity_delivery_reason
kimlik_verilis_tarihi   identity_date_of_issue
kita_baslama_tarihi	continent_start_date
kita_bitis_tarihi	continent_end_date
kontrol                 control
kurs_nevi		course_type
kurs_ogrenim_suresi	period_of_study 
kurum_sicili            corporation_registry
kuruma_baslam_tarihi 	corporation_start_tarihi

mahalle_koy             neighborhood
mahkeme_ad		court_name
makam 			position
maluliyet_kod		invalidity_code
medeni_hal              marital_status
memuriyete_baslama_tarihi       job_start_date
mezuniyet_tarihi		graduation_date
min_derece              min_degree
min_kademe              min_grade
muafiyet_tarihi			extemption_date

notlar                  notes

ogrenim_durumu		learning_status
ogrenim_suresi 		learning_period
ogrenim_yeri		learning_place
okul_ad			school_name
onceki_soyad            former_surname
ozel_isyeri_adı		ssk_ozel_workspace_name
ozluk_sebep             registry_reason
ozurlu_derece           degree_of_disabled
ozur_grup_kod           disabled_group_code
ozur_oran               disabled_ratio

parola                  password
personel_tip            staff_type
posta_kod               postal_code

saglik_durum            health_status
sayilmayan_gun_sayisi	uncounted_days
sebep 			reason
sgk_nevi		sgk_type
sgk_sicil_no		sgk_registry_no
sicil_no                registry_code
sinifi_okulu_sicili		class_school_registry
sira_no                 item_no
soyad                   surname
statu_kod               status_code
subay_okul_giris_tarihi	subay_entered_date
subayliktan_erlige_gecis_tarihi	subayliktan_erlige_transfered_date
sure 					period

tashih_ad 		correction_name 
tashih_dogum_tarihi	correction_birth_date
tashih_soyad 		correction_surname
tag1                    tag1
tag2                    tag2
tag3                    tag3
tazminat_tarihi		compensation_date
tazminat_bitis_tarihi	compensation_end_date
tegmen_nasp_tarihi	tegmen_nasp_date
temsil			representation
terfi_aciklama          promotion_desc
terfi_asker             promotion_military_service
terfi_bakanlik_gelen    promotion_order_ministry
terfi_ceza              promotion_penalty
terfi_sicil             promotion_registry
terfi_ucretsiz          promotion_unpaid

ulke_kod                country_code

vergi_no                tax_no

web_sayfa               web

yedek_subay_er_ogrenim_yer 	yedek_subay_er_ogrenim_yer
yetki_servisi		authorisation_level		

'''

# üst classtaki değişkenleri aşağıdaki class a aldım. Gerekli miydi?
# cinsiyeti kontrol et 5a

# "Hitaptaki Parametre Adı"		bizim kullanacağımız parametre adları = field.asdasd("Açıklama", index=True)

"acigaAlinmaTarih"	suspension_date = field.Date("Açığa Alınma Tarihi", index=True)
"acikAylikBasTarihi"	monthly_start_date = field.Date("Aylık Ödenen Süre Başlangı Tarihi", index=True)
"acikAylikBitTarihi"	monthly_stop_date = field.Date("Aylık Ödenen Süre Bitis Tarihi", index=True)	
"aciklama"		explanation = field.String("Açıklama", index=True)
"aciktanAtanmaTarihi"	openly_designation_date = field.Date("Açıktan Atandığı Tarih", index=True)
"acikSekil"		suspension = field.Integer("Açığa Alınma Şekli", index=True)
"ad"			first_name = field.String("Adı", index=True)
"asilAd"		reel_name = field.String("Asıl Ad(Eski Ad)", index=True)
"asilDogumTarihi"	reel_birth_date = field.Date("Asıl Doğum Tarihi(Eski Doğum Tarihi)", index=True)
"asilSoyad"		reel_surname = field.String("Asıl Soyad(Eski Soyad)", index=True)
"asilVekil"		reel_agent = field.String("Asıl Vekil", index=True)
"askerlikNevi"		soldiery_type = field.Integer("ASkerlik Nevi", index=True)
"astegmenNaspTarihi"	astegmen_nasip_date = field.Date("Asteğmenliğe Nasp Tarihi", index=True)
"atamaSekli"		appointment_type = field.String("Atama Sekli", index=True)
"ayrilmaNedeni"		quit_job_reason = field.String("SSK Hizmetinden Ayrılma Sebebi", index=True)
"ayrilmaTarihi"		quit_job_date = field.Date("Son Kurumdan Ayrılma Tarihi", index=True)			
"bagKurMeslek"		bagkur_job = field.String("Bağkur Mesleki Faaliyeri", index=True)
"bankaSandıkKod"	bank_chest_dode = field.Integer("Banka Sandık Kodu", index=True)
"baslamaTarihi"		start_date = field.Date("Başlangıç Tarihi", index=True, format="%d.%m.%Y")
"baslamaTarihiBorclanma"start_date_debt = field.Date("Borçlanma Başlangıç Tarihi", index=True)
"bitisTarihi"		end_date = field.Date("Bitiş Tarihi", index=True, format="%d.%m.%Y")
"bitisTarihiBorclanma"	end_date_debt = field.Date("Borçlanma Bitiş Tarihi", index=True)
"bolum"			graduation_department = field.String("Mezun Olunan Bölüm", index=True)
"bolumAd"		department_name = field.String("Varsa bölüm adı", index=True)
"borclanmaTarihi"	establisment_date = field.Date("Tahakkuk Tarihi", index=True)
"borcNevi"		debt_type = field.String("Borç Nevi", index=True)
"calistigiKurum"	work_place = field.String("Borçlandığı Tarihte Çalıştığı Kurum", index=True)
"cinsiyet"		gender = field.String("Cinsiyet", index=True)
"denklikBolum"		equivalent_department = field.String("Denklik Alınan Bölümün Adı", index=True)
"denklikOkul"		equivalent_school = field.String("Denklik Alınan Okulun Adı", index=True)
"denklikTarihi"		equivalent_date = field.Date("Denklik Tarihi", index=True)
"derece"		degree = field.Integer("Borçlanmaya Esas Derece", index=True)
"dogumTarihi"		birth_date = field.Date("Doğum Tarihi", index=True)
"durum"			status = field.String("Durum", index=True)
"durum" 		return_status = field.Integer("İade Şekli/Nedeni", index=True)
"durumKod"		status_code = field.Integer("Sigortalının Son Durumu", index=True)
"durumAçıklama"		status_explanation = field.String("Durum Kodu Açıklaması", index=True)
"ekgosterge"		indicator = field.Integer("Borçlanmaya Esas Ek Gösterge", index=True)
"emekliDerece"		retirement_degree = field.Integer("Emeklilik Derece", index=True)
"emekliKademe"          retirement_grade = field.Integer("Emeklilik Kademe", index=True)
"emekliEkGosterge"      retirement_indicator = field.Float("Emeklilik Gösterge", index=True)
"emekliSicil"		retirement_registry = field.String("Sigortalının Emeklilik Sicil Numarası", index=True)
"emekliSicilNo"		retirement_no = field.Integer("Emekli Sicil No", intex=True)
"emeklisicil6495"	retirement_registry6495 = field.Integer("2. Emekli Sicil No", index=True)
"fhzOrani"		fhz_ratio = field.Float("Unvana İlişkin FHZ katsayısı", index=True)
"gecerliDogumTarihi"	valid_birth_date = field.Date("Emeklilikte Geçerli Doğum Tarihi", index=True)
"gorev(Birimi)"		duty_unit = field.String("Görev Yaptığı Yer/Birim")
"gorev"			assignment = field.String("Görev", index_as='text_tr')
"gorev"			duty = field.Integer("Sigortalının Görev Tazminatı Göst", index=True)
"gorevTarihi6495"	duty_time6495 = field.Date("Emeklilik Sonrası Göreve Başlama Tarihi", index=True, format="%d.%m.%Y")
"goreveIadeIstemTarihi" duty_return_request_date = field.Date("Göreve İade İsteminde Bulunduğu Tarih", index=True)
"goreveIadeTarihi"	duty_return_date = index.Date("Göreve İade Edildiği Tarih", index=True)
"goreveSonAylıkBasTar"	duty_last_month_start_date = field.Date("Göreve Son Aylık Başlama Tarihi", index=True)
"goreveSonAylıkBitTar"	duty_last_month_end_date = field.Date("Göreve Son Aylık Bitis Tarihi", index=True)
"goreveSonTarih"	duty_end_date = field.Date("Görevine Son Verildiği Tarih", index=True)
"gunSayisi"		number_of_days = field.Integer("İntibakta değerlendirilen Gun Sayısı", index=True)
"gunSayisiBorclanan"	number_of_days_debt = field.Integer("Borçlanılan Gün Sayısı", index=True)
"hareketSebepKod"	motion_reason_code = field.Integer("Sigortalının Mevcut Hareket Kodu", index=True)
"hareketSebepAciklama"	motion_reason_explanation = field.String("Hareket Sebep Kod Açıklaması", index=True)
"hazirlik"		prep_class = field.Integer("Hazırlık Sınıfı", index=True)
"hizmetDurum"		duty_status = field.Integer("Hizmet Alma Durumu", index=True)
"hizmetSinifi"		duty_class = field.String("Hizmet Sınıfı", index=True)
"husus"			case = field.String("Husus", index=True)
"ilkSoyAd"		first_surname = field.String("Memuriyete Girişteki ilk Soyadı", index=True)
"ihzNevi"		ihz_type = field.Integer("İHZ Nevi", index=True)
"isyeriil"		work_place_country = field.String("Kurum İl", index=True)
"isteriilce"		work_place_district = field.String("Kurum İlçe", index=True)
"kademe"		grade = field.Integer("Borçlanmaya Esas Kademe", index=True)
"kadroDerece"		position_degree = field.String("Kadro Derece", index_as='text_tr')
"kadrosuzluk"		not_on_the_permanent_staff = field.Integer("Sigortalının kadrosuzluk Tazminat Oranı", index=True)
"kamuIsyeriAd"		ssk_kamu_workspace_name = field.String("Kamuda Çalıştığı SSK İşyeri Adı", index=True)
"kanunKod"		law_code = field.Integer("Kanun Numarası", index=True)			
"kararTarihi"		judgment_date = field.Date("Mahkeme Karar Tarihi", index=True)
"kararSayisi"		judgment_count = field.Integer("Mahkeme Karar Sayısı", index=True)
"kesinlesirmeTarihi"	judgment_confirmation_date = field.Date("Karar Kesinleştirme Tarihi", index=True)
"kayitNo"		record_id = field.Integer("Kayıt No", index=True)
"kazanilmisHADerece"	aquired_degree = field.Integer("Kazanılmış Hak Aylığı Derece", index=True)
"KazanilmisHAKademe"    aquired_grade = field.Integer("Kazanılmış Hak Aylığı Kademe", index=True)
"kazanilmisHAEkGosterge"aquired_sup_indicator = field.Float("Kazanılmış Hak Aylığı Ek gösterge", index=True)
"khaDurum"		kha_status = field.String("KHA durumu", index=True)
"kıdemTazminatıDurumu"  severance_pay_status = field.Integer("Kıdem Tazminatı Ödeme Durumu", index=True)
"kitaBaslamaTarihi"	continent_start_date = field.Date("Kıta Hizmeti Başlama Tarihi", index=True)
"kitaBitisTarihi"	continent_end_date = field.Date("Kıta Hizmeti Bitiş Tarihi", index=True)
"kursNevi"		course_type = field.Integer("Kurs Türü", index=True)
"kursOgrenimSuresi"	period_of_study = field.Integer("Kurs Süresi", index=True)
"kurumaBaslamaTarihi"	kuruma_baslam_tarihi = field.Date("Kuruma Başlama Tarihi", index=True)
"kurumOnayTarihi"	approval_date = field.Date("Kurum Onay Tarihi", index=True)
"kurumSicil"		corporation_registry = field.String("Kurum Sicili", index=True)
"mahkemeAd"		court_name = field.String("Kararın Verildiği Mahkemenin Adi", index=True)
"makam"			position = field.Integer("Sigortalının Makam Tazminatı Göst", index=True)
"maluliyetKod"		invalidity_code = field.String("Maluliyet Kod integer/string",index=True)
"memuriyetBaşlamaTarihi"job_start_date = field.Date("Memuriyete İlk Başlama Tarihi",index=True)
"mezuniyetTarihi"	graduation_date = field.Date("Mezuniyet Tarihi", index=True)
"muafiyetNedeni"	extemption_reason = field.String("Askerlikten Muafiyet Nedeni", index=True)
"odemeDerece"		pay_degree = field.Integer("Ödemeye Esas Derece", index=True)
"odemeEkgosterge"       pay_sup_indicator = field.Float("Ödeme Ek Gösterge", index=True)
"odemeKademe"	        pay_grade = field.Integer("Ödemeye Esas Kademe", index=True)
"odemeTarihi"		pay_date = field.Date("Odeme Tarihi", index=True)
"odenenMiktar"		be_paid_price = field.Float("Ödenen Tutar", index=True)
"ogrenimDurumu"		learning_status = field.Integer("OGrenim Durumu", index=True)
"ogrenimSuresi"		learning_period = field.Integer("Okul Süresi(Başarılı Öğrenim Süresi", index=True)
"ogrenimYer"		learning_place = field.String("Öğrenim Yeri", index=True)
"okulAd"		school_name = field.String("Okul Adı/ Kurs Eğitim Yeri", index=True)
"ozelIsyeriAd"		ssk_ozel_workspace_name = field.String("Özelde Çalıştığı SSK İş Yeri Adı", index=True)
"sayilmayanGunSayisi"	uncounted_days = field.Integer("Askerlikten Sayılmayan Gun Sayisi", index=True)
"sebep"			reason = field.Integer("Sebep",index=True)
"sebepKod"		reason_code = field.Integer("Sebep Kodu", index=True)
"sinifOkulSicil"	class_school_registry = field.String("Sınıfı, Dönemi, Sicili", index=True)
"sgkNevi"		sgk_type = field.Integer("Sgk Nevi", index=True)
"sgkSicilNo"		sgk_registry_no = field.String("Sosyal Güvenlik Numarası", index=True)
"sonucKod"		result_code = field.Integer("Sorgulamanın Sonucunu Belirten Kod", index=True)
"sonucMesaj"		result_message = field.String("Sonuc Kodunun Açıklanması", index=True)
"soyad"			last_name = field.String("Soyadı", index=True)
"subayliktanErligeGecis"subayliktan_erlige_transfered_date = field.Date("Yedek Subaylıktan Erliğe veya Erlikten Yedek Subaylığa Geçiş Tarihi", index=True)
"subayOkulGirisTarihi"	subay_entered_date = field.Date("Yedek Subay Okuluna Giriş Tarihi", index=True)
"sure"			period = field.Integer("Prim Gün Sayısı", index=True)
"sYonetimKaldTarih"	state_of_siege_remove_date = field.Date("Sıkı Yönetimin İlde Kaldırıldığı Tarih", index=True)
"tashihAd"		correction_name = field.String("Tashih Adı(Yeni Ad)", index=True)
"tashihDogumTarihi"	correction_birth_date = field.Date("Tashih Doğum Tarihi(Yeni Doğum Tarihi)", index=True)	
"tashihSoyad"		correction_surname = field.String("Tashih Soyadı(Yeni Soyad)", index=True)
"tazminat_tarihi"	compensation_date = field.Date("Sigortalının Tazminat Başlama Tarihi", index=True)
"tazminat_bitis_tarihi" compensation_end_date = field.Date("Sigortalını Tazminat Bitiş Tarihi", index=True)
"Tckn"			pno = field.String("Sigortalının TC Kimlik No", index=True)
"tegmenNaspTarihi"	tegmen_nasp_date = field.String("Teğmenliğe Nasp Tarihi", index=True)
"temsil"		representation = field.Integer("Sigortalının Temsil Tazminatı Göst", index=True)
"toplamTutar"		total_price = field.Float("Toplam Borç Tutarı", index=True)
"ucret"			salary = field.String("Ücret", index=True)
"ulkeKod"		country_code = field.Integer("Ülke Kodu", index=True)
"unvanKod"		title_code = field.Integer("Ünvan Kodu", index=True)
"unvanTarihi"		title_date = field.Date("Ünvan Aldığı Tarih", index=True)
"unvanBitisTarihi"	title_end_date = field.Date("Ünvanın Sona Erdiği Tarih", index=True)
"yedekSubayErOgrenimYer"yedek_subay_er_ogrenim_yer = field.String("Yedek Subay/ Er Öğrt Görev Yeri", index=True)
"yetkiAciklama"		authorisation_explanation = field.String("Yetki Kodu Açıklaması", index=True)
"yetkiKodu"		authorisation_code = field.Integer("Yetki Kodu", index=True)	
"yetkiSeviyesi"		authorisation_level = field.String("Yetki Seviyesi", index=True)
"yevmiye"		wage = field.String("Yemiye", index=True)




    
staff_type = field.String("Personel Türü", index=True)
mobile_phone = field.String("Cep Telefonu", index=True)

  
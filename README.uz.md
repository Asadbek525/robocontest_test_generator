[![uz](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Asadbek525/robocontest_test_generetor/blob/main/README.md)
# Robocontest Test Generator
Robocontest.uz ga yangi masalalar qo'shishda, ba'zi yangi foydalanuvchilar test holatlarni yaratishda muammoga duch kelishadi. 
Ushbu repository ularga yordam berishi mumkin!

## Foydalanish yo'riqnomasi
### Ushbu loyihani o'zingizga yuklab oling yoki clone qilib oling
```sh
git clone https://github.com/Asadbek525/robocontest_test_generator.git
```
### Loyiha joylashgan directoryga kirsh
```sh
cd robocontest_test_generator
```

### Har bir masala uchun alohida papka va fayllar ochiladi. sample_problem - masala nomi.  
```sh
python main.py sample_problem
```

### Masala uchun ochilgan papkaga kirib, o'zingizning xohishingizga ko'ra va generate.cpp yoki generate.py faylini tahrirlashni boshlang

### Keyin generate.py  yoki generate.cpp ni ishga tushiring

### Bu esa o'sha papkasini ichida ```tests``` papkasini ochib unda mos testlarni yaratib beradi.

### Testlar tayyor holatga kelganidan keyin zipper.py fileni ishga tushurish orqali ziplangan faylni hosil qilishingiz mumkin.
```sh
python zipper.py
```

### tests.zip faylini [robocontest.uz](https://robocontest.uz/home) ga joylashtirishingiz mumkin.

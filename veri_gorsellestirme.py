#TODO Veri Seti & İlk Adımlar (1.Bölüm)_______________

import seaborn as sns
import pandas as pd

#TODO Veriye İlk Bakış
planets = sns.load_dataset("planets")
df = planets.copy()
fist5 = df.head() # ilk 5 veri
last5 = df.tail() # son 5 veri

#TODO Veri Setinin Yapısal Bilgileri
df.info()
df.dtypes # değişkenerin tip bilgileri
#df.method = pd.Categorical(df.method)

df.shape #(1035, 6)
df.columns #Index(['method', 'number', 'orbital_period', 'mass', 'distance', 'year'], dtype='object')
df.describe()
df.describe().T
df.describe(include = "all").T

#TODO Eksik Değerler
df.isnull().values.any() #True
df.isnull().sum()

# orbital_period'taki eksik bilgileri 0 yapıyoruz.
df["orbital_period"].fillna(0, inplace = True)
df.isnull().sum()

# mass'taki eksik bilgileri ortalama değer yapıyoruz.
df["mass"].fillna(df.mass.mean(), inplace = True)
df.isnull().sum()

# Tüm eksik bilgileri ortalama değer yapıyoruz.
df.fillna(df.mean(), inplace = True)
df.isnull().sum()

# Yaptığımız işlemleri geri alıyoruz.
df = planets.copy()
df.isnull().sum()

#TODO Kategorik Değişken Özetleri
kat_df = df.select_dtypes(include = ["object"])
kat_df.head()

# Kategorik değişkenin sınıflarına ve sınıf sayısına erişmek
degiskenin_siniflari = kat_df.method.unique() # değişkenin sınıfları
sinif_sayisi = kat_df["method"].value_counts().count() # sınıf sayısı

# Kategorik değişkenin sınıflarının frekanslarına erişmek
frekans = kat_df["method"].value_counts()

# Grafik
df["method"].value_counts().plot.barh();

#TODO Sürekli Değişken Özetleri
df_select_dtypes = df.select_dtypes(include = ["float64", "int64"])
df_select_dtypes_describeT = df_select_dtypes.describe().T
df_select_dtypes_describe_distance = df_select_dtypes["distance"].describe()

print("\nOrtalama:", str(df_select_dtypes["distance"].mean()))
print("Dolu Gözlem Sayısı:", str(df_select_dtypes["distance"].count()))
print("Maksimum Değer:", str(df_select_dtypes["distance"].max()))
print("Minimum Değer:", str(df_select_dtypes["distance"].min()))
print("Medyan:", str(df_select_dtypes["distance"].median()))
print("Standart Sapma:", str(df_select_dtypes["distance"].std()), "\n")

#%%
#TODO Sütun Grafik (BarPlot) (2.Bölüm)_______________

#TODO Veri Seti Hikayesi
"""
price: dolar cinsinde fiyat(326-18,823)
carat: ağırlık(0.2-5.01)
cut: kalite(Fair, Good, Very Good, Premium, Ideal)
color: renk(from J(worst) to D(best))
clarity: temizliği, berraklığı(I1(worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF(best))
x: length in mm(0-10.74)
y: length in mm(0-58.9)
z: length in mm(0-31.8)
depth: toplam derinlik yüksekliği = z/mean(x,y) = 2*z/(x+y)(43-79)
table: elmasın en geniş noktasına göre genişliği(43-95)
"""
import seaborn as sns
diamonds = sns.load_dataset("diamonds")
df = diamonds.copy()
head = df.head()

# Veri Setine Hızlı Bakış
df.info()
df.describe().T
df["cut"].value_counts() # cut frekans
df["color"].value_counts() # color frekans

# Ordinal tanımlama
from pandas.api.types import CategoricalDtype
df.cut.head()
df.cut.astype(CategoricalDtype(ordered = True))
df.dtypes
df.cut.head(1)

cut_categories = ["Fair", "Good", "Very Good", "Premium", "Ideal"]
df.cut = df.cut.astype(CategoricalDtype(categories = cut_categories, ordered = True))
df.cut.head(1)

#TODO Grafikler
#df["cut"].value_counts().plot.barh();
"""
(df["cut"]
 .value_counts()
 .plot.barh()
 .set_title("Cut Değişkeninin Sınıf Frekansları"));
"""
#sns.barplot(x="cut", y=df.cut.index, data=df)

#TODO Çaprazlamalar
#sns.catplot(x="cut", y="price", data=df)
#sns.barplot(x="cut", y="price", hue="color", data=df)
#df.groupby(["cut", "color"])["price"].mean()


#%%
#TODO Histogram ve Yoğunluk Grafikleri (3.Bölüm)_______________
import seaborn as sns
diamonds = sns.load_dataset("diamonds")
df = diamonds.copy()

#TODO Grafikler
#sns.distplot(df.price, kde=False)
#?sns.displot
#sns.distplot(df.price, bins=1000, kde=False)
#sns.distplot(df.price)
#sns.distplot(df.price, hist=False)
#sns.kdeplot(df.price, shade=True)

#TODO Histogram ve Yoğunluk Çaprazlamalar
#sns.kdeplot(df.price, shade=True)
"""
(sns
 .FacetGrid(df,
            hue="cut",
            height=5,
            xlim=(0,10000),)
 .map(sns.kdeplot, "price", shade=True)
 .add_legend()
);
"""
#sns.catplot(x="cut", y="price", hue="color", kind="point", data=df)

#%%
#TODO Kutu Grafik (BoxPlot) (4.bölüm)_______________
# Veri Seti Hikayesi
"""
total_bill: yemeğin toplam fiyatı (bahşiş ve vergi dahil)
tip: bahşiş
sex: ücreti ödeyen kişinin cinsiyeti (0=male, 1=female)
smoker: grupta sigara içen var mı? (0=No, 1=Yes)
day: gün (3=Thur, 4=Fri, 5=Sat, 6=Sun)
time: ne zaman? (0=Day, 1=Night)
size: grupta kaç kişi var?
"""
import seaborn as sns
tips = sns.load_dataset("tips")
df = tips.copy()
df.head()
df.describe().T
df["sex"].value_counts()
df["smoker"].value_counts()
df["day"].value_counts()
df["time"].value_counts()
df["size"].value_counts()

#TODO Grafikler
#sns.boxplot(x=df["total_bill"]);
#sns.boxplot(x=df["total_bill"], orient="v")

#TODO Çaprazlamalar
# Hangi günler daha fazla kazanıyoruz?
#sns.boxplot(x="day", y="total_bill", data=df)

# Sabah mı akşam mı daha çok kazanıyoruz?
#sns.boxplot(x="time", y="total_bill", data=df)

# Yemeğe gelen kişi sayısıyla kazanç doğru orantılı mı?
#sns.boxplot(x="size", y="total_bill", data=df)

# Gün - Toplam Hesap - Cinsiyet
#sns.boxplot(x="day", y="total_bill", hue="sex", data=df)

#%%
#TODO Violin Grafik (5.bölüm)_______________
import seaborn as sns
tips = sns.load_dataset("tips")
df = tips.copy()

#sns.catplot(y="total_bill", kind="violin", data=df)

#TODO Çaprazlamalar
#sns.catplot(x="day", y="total_bill", kind="violin", data=df)
#sns.catplot(x="day", y="total_bill", hue="sex", kind="violin", data=df)

#%%
#TODO Korelasyon Grafikleri (6.bölüm)_______________

#TODO Scatterplot
import seaborn as sns
tips = sns.load_dataset("tips")
df = tips.copy()

#sns.scatterplot(x="total_bill", y="tip", data=df)

#TODO Çaprazlamalar
#sns.scatterplot(x="total_bill", y="tip", hue="time", data=df)
#sns.scatterplot(x="total_bill", y="tip", hue="time", style="time", data=df)
#sns.scatterplot(x="total_bill", y="tip", hue="day", style="day", data=df)
#sns.scatterplot(x="total_bill", y="tip", hue="day", style="time", data=df)
#sns.scatterplot(x="total_bill", y="tip", style="size", data=df)
#sns.scatterplot(x="total_bill", y="tip", hue="size", style="size", data=df)

#TODO Doğrusal İlişkinin Gösterilmesi
#sns.lmplot(x="total_bill", y="tip", data=df)
#sns.lmplot(x="total_bill", y="tip", hue="smoker", data=df)
#sns.lmplot(x="total_bill", y="tip", hue="smoker", col="time", data=df)
#sns.lmplot(x="total_bill", y="tip", hue="smoker", col="time", row="sex", data=df)

#TODO Scatterplot Matrisi
iris = sns.load_dataset("iris")
df = iris.copy()
df.head()
df.info()
df.dtypes
df.shape
df.describe()
df.describe().T

#sns.pairplot(df)
#sns.pairplot(df, hue="species")
#sns.pairplot(df, hue="species", markers=["o","s","D"])
#sns.pairplot(df, kind="reg")
sns.pairplot(df, kind="reg", hue="species")

#%%
#TODO Isı Haritası (Heat Map)
import seaborn as sns
flights = sns.load_dataset("flights")
df = flights.copy()
df.head()
df.shape
df["passengers"].describe()

df = df.pivot("month", "year", "passengers")
df

sns.heatmap(df)
sns.heatmap(df, annot = True, fmt = "d")
sns.heatmap(df, annot = True, fmt = "d", linewidths = .5)
sns.heatmap(df, annot = True, fmt = "d", linewidths = .5, cbar = False)

#%%
#TODO Çizgi Grafik
import seaborn as sns
fmri = sns.load_dataset("fmri")
df = fmri.copy()
df.head()
df.shape
df["timepoint"].describe()
df["signal"].describe()
df.groupby("timepoint")["signal"].count()
df.groupby("signal")["timepoint"].count()
df.groupby("signal").count()
df.groupby("timepoint")["signal"].describe()

#TODO Grafikler
#sns.lineplot(x="timepoint", y="signal", data=df)
#sns.lineplot(x="timepoint", y="signal", hue="event", data=df)
#sns.lineplot(x="timepoint", y="signal", hue="event", style="event", data=df)
sns.lineplot(x="timepoint", 
             y="signal", 
             hue="event", 
             style="event", 
             markers=True, dashes=False,
             data=df)
sns.lineplot(x="timepoint", 
             y="signal", 
             hue="region", 
             style="event", 
             data=df)

#%%
#TODO Basit Zaman Serisi Grafiği
import pandas_datareader as pr
df = pr.get_data_yahoo("AAPL", start="2016-01-01", end="2019-08-25")
df.head()
df.shape
kapanis = df["Close"]
kapanis.head()
kapanis.plot()
kapanis.index 
kapanis.index = pd.DatetimeIndex(kapanis.index)
kapanis.index
kapanis.plot()

#%%
"""
DAĞILIM GRAFİKLERİ
Kategorik değişkenler için:
    Sütun grafik (Bar plot)
Sayısal değişkenler için:
    Histogram
    Kutu grafik (Box plot)
    Violin

KORELASYON GRAFİKLERİ

ÇİZGİ GRAFİK

BASİT ZAMAN SERİSİ
"""

























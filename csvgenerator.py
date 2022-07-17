import csv
import random

files = {
    "file__15m.csv":10000
}


fieldnames=['id','full_name','age','city', "weight", "height", "isActive", "col_int1", "col_int2", "col_int3", "col_float1", "col_float2", "col_float3", "col_float4", "col_float5", "col_float6", "col_float7", "col_float8", "col_float9", "col_float10" ]
names=["Elfriede Florián", "Mtendere Santina", "Adrien Michael", "Kanako Carolina", "Julinha Izzy", "Brandie Bosmat", "Chikere Rayen", "Nélida Carolina", "Albin Imamu", "Zoe Benjamin", "Shaked Wilda", "Isabela Jessie", "Concettina Marisol", "Deepak", "Sangeeta", "Geetika", "Anubhav", "Sahil", "Akshay", 'James Mary','Robert Patricia','John Jennifer','Michael Linda','David Elizabeth','William Barbara','Richard Susan','Joseph Jessica','Thomas Sarah','Charles Karen','Christopher Lisa','Daniel Nancy','Matthew Betty','Anthony Margaret','Mark Sandra','Donald Ashley','Steven Kimberly','Paul Emily','Andrew Donna','Joshua Michelle','Kenneth Carol','Kevin Amanda','Brian Dorothy','George Melissa','Timothy Deborah','Ronald Stephanie','Edward Rebecca','Jason Sharon','Jeffrey Laura','Ryan Cynthia','Jacob Kathleen','Gary Amy','Nicholas Angela','Eric Shirley','Jonathan Anna','Stephen Brenda','Larry Pamela','Justin Emma','Scott Nicole','Brandon Helen','Benjamin Samantha','Samuel Katherine','Gregory Christine','Alexander Debra','Frank Rachel','Patrick Carolyn','Raymond Janet','Jack Catherine','Dennis Maria','Jerry Heather','Tyler Diane','Aaron Ruth','Jose Julie','Adam Olivia','Nathan Joyce','Henry Virginia','Douglas Victoria','Zachary Kelly','Peter Lauren','Kyle Christina','Ethan Joan','Walter Evelyn','Noah Judith','Jeremy Megan','Christian Andrea','Keith Cheryl','Roger Hannah','Terry Jacqueline','Gerald Martha','Harold Gloria','Sean Teresa','Austin Ann','Carl Sara','Arthur Madison','Lawrence Frances','Dylan Kathryn','Jesse Janice','Jordan Jean','Bryan Abigail','Billy Alice','Joe Julia','Bruce Judy','Gabriel Sophia','Logan Grace','Albert Denise','Willie Amber','Alan Doris','Juan Marilyn','Wayne Danielle','Elijah Beverly','Randy Isabella','Roy Theresa','Vincent Diana','Ralph Natalie','Eugene Brittany','Russell Charlotte','Bobby Marie','Mason Kayla','Philip Alexis','Louis Lori']
cities=['Washington D.C.', 'lima','Panama City', 'Bogotá', 'Road Town', 'Montevideo','Georgetown', 'Ottawa', 'CDMX', 'NY', 'buenos aires', 'Delhi', 'Kolkata', 'Chennai', 'Mumbai', "Moscow","London","Saint Petersburg","Berlin","Madrid","Kyiv","Rome","Paris","Bucharest","Minsk","Budapest","Hamburg","Warsaw","Vienna","Barcelona","Stockholm","Kharkiv","Novosibirsk","Yekaterinburg","Nizhniy Novgorod","Belgrade","Munich","Milan","Prague","Copenhagen","Sofia","Samara","Omsk","Kazan","Rostov-na-Donu","Chelyabinsk","Ufa","Donetsk","Dublin","Brussels","Odessa","Volgograd","Dnipro","Birmingham","Perm","Koeln","Naples","Krasnoyarsk","Turin","Liverpool","Saratov","Voronezh","Valencia","Marseille","Lodz","Krakow","Riga","Amsterdam","Zaporizhzhya","Lviv","Sevilla","Tolyatti","Zagreb","Sarajevo","Sheffield","Zaragoza","Athens","Frankfurt am Main","Krasnodar","Palermo","Ulyanovsk","Chisinau","Wroclaw","Izhevsk","Kryvyy Rih","Bristol","Yaroslavl","Barnaul","Rotterdam","Essen","Glasgow","Stuttgart","Dortmund","Vladivostok","Irkutsk","Genoa","Oslo","Khabarovsk","Khabarovsk Vtoroy","Duesseldorf","Goeteborg","Poznan","Malaga","Helsinki","Orenburg","Bremen","Vilnius","Novokuznetsk","Ryazan","Tyumen","Lisbon","Lipetsk","Nuernberg","Hannover","Penza","Naberezhnyye Chelny","Leicester","Leipzig","Kalininskiy","Duisburg","Astrakhan","Makhachkala","Dresden","Tomsk","Mykolayiv","Homyel","Kemerovo","Skopje","The Hague","Lyon","Tula","Edinburgh","Sevastopol","Gdansk","Antwerpen","Kirov","Leeds","Luhansk","Cardiff","Cheboksary","Murcia","Kaliningrad","Toulouse","Mariupol","Bryansk","Bratislava","Ivanovo","Magnitogorsk","Wandsbek","Kursk","Szczecin","Palma","Tver","Manchester","Tallinn","Bochum","Sector 3","Las Palmas de Gran Canaria","Nizhny Tagil","Bochum-Hordel","Makiivka","Tirana","Kaunas","Stoke-on-Trent","Vinnytsya","Brno","Mahilyow","Sector 6","Bydgoszcz","Bologna","Stavropol","Wuppertal","Ulan-Ude","Lublin","Coventry","Arkhangel'sk","Bilbao","Thessaloniki","Florence","Sector 2","Belgorod","Kurgan","Vitebsk","Zurich","Plovdiv","Kaluga","Nice","Krasnogvargeisky","Simferopol","Sunderland","Alicante","Bielefeld","Bonn","Brent","Cordoba","Sochi","Birkenhead","Orel","Volzhskiy","Nottingham","Smolensk","Murmansk","Islington","Reading","Iasi","Valladolid","Vladikavkaz","Hrodna","Katowice","Cluj-Napoca","Cherepovets","Timisoara","Vologda","Kingston upon Hull","Preston","Ostrava","Varna","Vladimir","Chita","Mannheim","Chernihiv","Newport","Craiova","Constanta","Saransk","Malmoe","Brest","Surgut","Swansea","Bradford","Vigo","Southend-on-Sea","Sumy","Galati","Bialystok","Tambov","Catania","Utrecht","Kherson","Poltava","Sector 4","Marienthal","Karlsruhe","Hamburg-Nord","Yoshkar-Ola","Taganrog","Horlivka","Kostroma","Gijon","Bari","Nantes","Cherkasy","Brasov","Komsomolsk-on-Amur","Strasbourg","Belfast","Nalchik","Wiesbaden","Ljubljana","Sector 5","Khmelnytskyi","Derby","Muenster","Gelsenkirchen","Sterlitamak","Chernivtsi","Eixample","Aachen","Petrozavodsk","Zhytomyr","Moenchengladbach","Plymouth","Augsburg","Luton","L'Hospitalet de Llobregat","Espoo","Latina","Bratsk","Rivne","Carabanchel","Wolverhampton","Eimsbuettel","Altona","Nis","Porto","Montpellier","Czestochowa","City of Westminster","Chemnitz","Orsk","Southampton","A Coruna","Gdynia","Nizhnevartovsk","Braunschweig","Puente de Vallecas","Angarsk","Mar'ino","Novorossiysk","Khimki","Blackpool","Krefeld","Halle (Saale)","Arhus","Podgorica","Ivano-Frankivsk","Kosice","Sant Marti","Gasteiz / Vitoria","Yakutsk","Granada","Nizhnekamsk","Kamyanske","Hamburg-Mitte","Dzerzhinsk","Kiel","Bordeaux","Gent","Syktyvkar","Elche","Milton Keynes","Magdeburg","Ploiesti","Lille","Ciudad Lineal","Bexley","Kropyvnytskyy","Sosnowiec","Staryy Oskol","Neue Neustadt","Radom","Groznyy","Sector 1","Oviedo","Santa Cruz de Tenerife","Graz","Ternopil","Shakhty","Blagoveshchensk","Banja Luka","Babruysk","Fuencarral-El Pardo","Kremenchuk","Messina","Badalona","Oberhausen","Verona","Prokop'yevsk","Terrassa","Mokotow","Rybinsk","Vykhino-Zhulebino","Freiburg","Northampton","Zelenograd","Archway","Biysk","Novi Sad","Velikiy Novgorod","Centralniy","Lutsk","Bergen","Braila","Norwich","Luebeck","Cartagena","Eindhoven","Rennes","Kielce","Jerez de la Frontera","Oradea","Sabadell","Mostoles","Linz","Alcala de Henares","Debrecen","Padova","Erfurt","Vasyl'evsky Ostrov","Tampere","Harburg","Pskov","Favoriten","Nicosia","Charleroi","Severnyy","Tilburg","Balakovo","Armavir","Bila Tserkva","Dudley","Hagen","Gliwice","Torun","Pamplona","Rostock","Fuenlabrada","Aberdeen","Reims","Engels","Burgas","Kassel","Severodvinsk","Portsmouth","Newcastle upon Tyne","Klaipeda","Zabrze","Zlatoust","Cork","Vantaa","Syzran'","Bytom","Almeria","Sutton","Petropavlovsk-Kamchatsky","Trieste","Donaustadt","Leganes","Le Havre","Swindon","San Sebastian","Mainz","Brescia","Geneve","Cergy-Pontoise","Sants-Montjuic","Santander","Liege","Kamensk-Ural'skiy","Prato","Saarbruecken","Groningen","Taranto","Crawley","Castello de la Plana","Yasenevo","Praga Poludnie","Podolsk","Hamm","Burgos","Amadora","Ipswich","Bielsko-Biala","Yuzhno-Sakhalinsk","Almere Stad","Split","Saint-Etienne","Turku","Wigan","Croydon","Miskolc","Walsall","Herne","Lyublino","Mansfield","Olsztyn","Bacau","Oxford","Muelheim","Albacete","Reggio Calabria","Arad","Baranovichi","Toulon","Angers","Horta-Guinardo","Patra","Alcorcon","Berezniki","Volgodonsk","Breda","Pitesti","Miass","Abakan","Neukoelln","Getafe","Novocherkassk","Osnabrueck","Nou Barris","Warrington","Szeged","Basel","Zenica","Solingen","Pilsen","Nazran'","Slough","Piraeus","Bournemouth","Peterborough","Ludwigshafen am Rhein","Floridsdorf","Leverkusen","Hortaleza","Rubtsovsk","Anderlecht","Mytishchi","Salavat","Oldenburg","Khoroshevo-Mnevniki","Bibirevo","Modena","Nijmegen","Grenoble","Cambridge","Rzeszow","Doncaster","Gol'yanovo","Admiralteisky","San Blas-Canillejas","Ussuriysk","Tiraspol","Pecs","Ruse","Salamanca"]
bool_values = ['true', 'false', 'True', 'False', 'TRUE', 'FALSE']



lines = []



dict_value_field = {}

for field in fieldnames:
    dict_value_field[field] = str()


def get_row(i):
    dict_value_field["id"] = str(i),
    dict_value_field["full_name"] = random.choice(names),
    dict_value_field["age"] = str(random.randint(18,70)),
    dict_value_field["city"] = random.choice(cities),
    dict_value_field["weight"] = str(random.uniform(55.5, 120.5)),
    dict_value_field["height"] = str(random.uniform(1.50, 2.1)),
    dict_value_field["isActive"] = random.choice(bool_values),
    dict_value_field["col_int1"] = str(random.randint(1,2000000)),
    dict_value_field["col_int2"] = str(random.randint(0,100)),
    dict_value_field["col_int3"] = str(random.randint(10000,100000)),
    dict_value_field["col_float1"] = str(round(random.uniform(5.01, 123.99), 2)),
    dict_value_field["col_float2"] = str(round(random.uniform(100.01, 90000.99), 2)),
    dict_value_field["col_float3"] = str(round(random.uniform(0.01, 10.99), 2)),
    dict_value_field["col_float4"] = str(round(random.uniform(2.001, 100.001), 3)),
    dict_value_field["col_float5"] = str(round(random.uniform(100.001, 900.001), 3)),
    dict_value_field["col_float6"] = str(round(random.uniform(0.1, 1.1), 1)),
    dict_value_field["col_float7"] = str(round(random.uniform(1000.1, 99999.01), 2)),
    dict_value_field["col_float8"] = str(round(random.uniform(10.001, 199.001), 3)),
    dict_value_field["col_float9"] = str(round(random.uniform(100.01, 999.01), 2)),
    dict_value_field["col_float10"] = str(round(random.uniform(10000.01, 999999.01), 2))

    row  = ",".join([dict_value_field[field][0] for field in fieldnames])

    return row + '\n'

header = ','.join(fieldnames) + '\n'
for f in files:
    
    with open(f, 'w') as outfile:
        outfile.write(header)
        for i in range(0, files[f]):
            outfile.write(get_row(i))
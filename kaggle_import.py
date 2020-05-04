import csv
import io
import cx_Oracle

my_conn = cx_Oracle.connect("hr/11@localhost:1521/orcl")
cursor = my_conn.cursor()

def year_to_int(year):
    try:
        int(year)
        return int(year)
    except ValueError:
        return 0

with io.open('vgsales.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    count_g = 1
    count_p = 1
    count_pub = 1
    dict_genre = {}
    dict_platform = {}
    dict_publisher = {}
    for row in reader:
        if row["Genre"] in dict_genre.keys():
            pass
        else:
            dict_genre[row['Genre']] = count_g
            count_g += 1


        if row["Platform"] in dict_platform.keys():
            pass
        else:
            dict_platform[row["Platform"]] = count_p
            count_p += 1


        if row["Publisher"] in dict_publisher.keys():
            pass
        else:
            dict_publisher[row["Publisher"]] = count_pub
            count_pub += 1


for i in dict_genre:
    cursor.execute('INSERT INTO genre(genre_id, genre) VALUES (:1, :2)', (dict_genre[i], i))
for i in dict_platform:
    cursor.execute('INSERT INTO platform(platform_id, platfrom) VALUES (:1, :2)', (dict_platform[i], i))
for i in dict_publisher:
    cursor.execute('INSERT INTO companies(company_id, company) VALUES (:1, :2)', (dict_publisher[i], i))
count = 0    
with io.open('vgsales.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    dict_res = {}
    dict_sales = {}
    for row in reader:
        try:
            cursor.execute("""INSERT INTO game(game_rank, genre_id, 
                                           company_id, platform_id, 
                                           year_n, name_of_game)
                           VALUES (:1, :2, :3, :4, :5, :6)""", (int(row['Rank']),
                                                            int(dict_genre[row['Genre']]),
                                                            int(dict_publisher[row['Publisher']]),
                                                            int(dict_platform[row['Platform']]),
                                                            year_to_int(row['Year']),
                                                            row['Name']))
            cursor.execute("""INSERT INTO sales(game_rank, NA_sales,
                            EU_sales, JP_sales, Other_sales)
                            VALUES(:1, :2, :3, :4, :5)""", (int(row['Rank']), float(row['NA_Sales']), 
                                                float(row['EU_Sales']),float(row['JP_Sales']), float(row['Other_Sales'])))
        except UnicodeEncodeError:
            count += 1

print(str(count)+' lines passed because of UnicodeEncodeError')

my_conn.commit()
cursor.close()

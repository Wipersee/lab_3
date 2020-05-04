import cx_Oracle
import csv
import io

my_conn = cx_Oracle.connect("hr/11@localhost:1521/orcl")
cursor = my_conn.cursor()

cursor.execute("""
SELECT game_rank, game.name_of_game, platform.platfrom, year_n, genre.genre, companies.company,
sales.NA_sales, sales.EU_sales, sales.JP_sales, sales.Other_sales, 
(sales.NA_sales + sales.EU_sales + sales.JP_sales + sales.Other_sales) AS Global_sales 
FROM game
INNER JOIN genre USING(genre_id)
INNER JOIN companies USING(company_id)
INNER JOIN platform USING(platform_id)
INNER JOIN sales USING(game_rank)
ORDER BY game_rank
""")

with io.open('text.csv', "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow('Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales'.split(","))
        for row in cursor:
            string = ','.join(map(str, row))
            writer.writerow(string.split(","))

cursor.close()



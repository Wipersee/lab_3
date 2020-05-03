DECLARE
    rows_num INT NOT NULL DEFAULT 4;
    
    TYPE arr_name IS VARRAY(4) OF VARCHAR2(150); 
    TYPE arr_genre IS VARRAY(4) OF VARCHAR2(150); 
    TYPE arr_platform IS VARRAY(4) OF VARCHAR2(150); 
    TYPE arr_companies IS VARRAY(4) OF VARCHAR2(150); 
    TYPE arr_sales IS VARRAY(4) OF DECIMAL(5,2); 
    
    game_n arr_name := arr_name();
    genre_n arr_genre := arr_genre();
    platform_n arr_platform := arr_platform();
    companies_n arr_companies := arr_companies();
    sales_n arr_sales := arr_sales();

BEGIN
    genre_n := arr_genre('Sports', 'Platform', 'Racing', 'Role-Playing');
    game_n := arr_name('Wii Sports', 'Super Mario Bros.', 'Mario Kart Wii', 'Pokemon Red/Pokemon Blue');
    platform_n := arr_platform('XBox360', 'Wii', 'PS3', 'Switch');
    companies_n := arr_companies('Nintendo', 'Microsoft Game Studios', 'Take-Two Interactive', 'Rockstar');
    sales_n := arr_sales(4.58, 5.87, 2.23, 0.23);

    FOR x in 1..rows_num LOOP
    
        INSERT INTO genre
        VALUES (x,genre_n(x));
        
        INSERT INTO platform
        VALUES (x,platform_n(x));
        
        INSERT INTO companies
        VALUES (x,companies_n(x));
    
    END LOOP;
    
    FOR x in 1..rows_num LOOP
        INSERT INTO game
        VALUES(x, x, x, x, 2013+x, game_n(x));
        INSERT INTO sales
        VALUES(x, sales_n(x)*0.3, sales_n(x)*0.21341, sales_n(x)*0.6523 ,sales_n(x)*0.762);
    END LOOP;
    
END;

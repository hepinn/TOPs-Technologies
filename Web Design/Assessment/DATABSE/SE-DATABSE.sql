CREATE DATABASE nobel_win;

USE nobel_win;

CREATE TABLE nobel_win (
YEAR int ,
SUBJECT varchar(50),
WINNER varchar(50),
COUNTRY varchar(30),
CATEGORY varchar(40)	
);

insert into nobel_win
(YEAR, SUBJECT, WINNER, COUNTRY, CATEGORY)
value
(1970, "Physics", "Hannes Alfven", "Sweden", "Scientist" ),
(1970, "Physics", "Louis Neel", "France", "Scientist"),
(1970, "Chemistry", "Luis Federico Leloir", "France", "Scientist"),
(1970, "Physiology", "Ulf Von Euler", "Sweden", "Scientist"),
(1970, "physiology", "Bernard katz", "Germany", "Scientist"),
(1970, "Literature", "Alesandr solzhenitsyn", "Russia", "Linguist"),
(1970, "Economics", "Paul Samuelson", "USA", "Economist"),
(1970, "Physiology", "Julius Axelord", "USA", "Scientist"),
(1971, "Physics", "Dennis Gabor", "Hungary", "Scientist"),
(1971, "Chemistry", "Gerhard Herzberg", "Germany", "Scientist"),
(1971, "Peace", "Willy Brandt", "Germany", "Chancellor"),
(1971, "Literature", "Pablo Neruda", "chile", "Linguist"),
(1971, "Economist", "Simon Kunznets", "Russia", "Economist"),
(1978, "Peace", "Anwar al-Sadat", "Egypt", "President"),
(1978, "Peace", "Menachem Bigin", "israel", "Prime Minister"),
(1987, "Chemistry", "Donald J. Cram", "USA", "Scientist"),
(1987, "Chemistry", "Jean-Marie Lehn", "France", "Scientist"),
(1987, "Physiology", "Susuma Ronegawa", "Japan", "Scientist"),
(1994, "Economics", "Reihard Selten", "Germany", "Economist"),
(1994, "Peace", "Yitzhak Rabin", "Israel", "Prime Minister"),
(1987, "Physics", "Johannes Georg Bednorz", "germany", "Scientist"),
(1987, "Literature", "Joseph Brodsky", "Russia", "Linguist"),
(1987, "Economics", "Robert Solow", "USA", "Economist"),
(1994, "Literature", "Kenzaburo Oe", "Japan", "Linguist");

SELECT * FROM nobel_win;

/*Query-1: Find the nobel prize winner of the year 1970. Return year, subject and winner.*/ 

SELECT YEAR, SUBJECT, WINNER
FROM nobel_win
WHERE year=1970;


/*Query-2: Find the nobel prize winner in chemistry between the year 1965 and 1975. Begin and end value are includeReturn year, subject, winner and country*/

SELECT YEAR, SUBJECT, WINNER, COUNTRY
FROM nobel_win
WHERE SUBJECT = 'CHEMISTRY' AND YEAR >=1965 AND YEAR <=1975;

/*Query-3: Write sql query to retrieve the details of the winners whose first name matches with
the string ‘Louis’. Return year,subject,winner,country*/

SELECT YEAR, SUBJECT, WINNER, COUNTRY
FROM nobel_win
WHERE WINNER LIKE 'Louis %';

/*Query-4(A): Write sql query to find Nobel prize winners for the subject that does not begin with
the letter ‘P’. Order the result by year, descending and winner in ascending*/

SELECT * FROM nobel_win
WHERE SUBJECT NOT LIKE 'P%' 
ORDER BY YEAR DESC, WINNER;

/*Query-4(B): Ascending*/

SELECT * FROM nobel_win
WHERE SUBJECT NOT LIKE 'P%' 
ORDER BY YEAR ASC, WINNER;

/*QUERY-5: Write sql query to find the details of 1970 Nobel prize winners. Order the result by
subject, ascending except for ‘Chemistry’ and ‘Economics’ which will come at the
end of the result set. Return year, subject, winner , country and category.*/

SELECT*FROM nobel_win
WHERE YEAR = 1970 ORDER BY
CASE   
WHEN SUBJECT IN ('Economics', 'Chemistry') then 1
else 0
END ASC, SUBJECT, WINNER;

 



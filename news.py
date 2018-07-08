#!/usr/bin/env python2

import psycopg2
DBNAME = "news"

db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute('''select replace(path,'/article/',''), count(path) from
           log group by path order by count(path) desc limit 3 offset 1;''')
first = c.fetchall()
print "the_most_popular_three_articles_of_all_time"
print str(first[0][0])+" -- "+str(first[0][1])+" views"
print str(first[1][0])+" -- "+str(first[1][1])+" views"
print str(first[2][0])+" -- "+str(first[2][1])+" views"
c.execute('''select authors.name, count(authors.name) from authors, articles,
            log where (articles.slug= replace(path,'/article/','')) and
            (authors.id=articles.author) group by name order by
            count(name) desc;''')
second = c.fetchall()
print "  "
print "the_most_popular_article_authors_of_all_time"
print str(second[0][0])+" -- "+str(second[0][1])+" views"
print str(second[1][0])+" -- "+str(second[1][1])+" views"
print str(second[2][0])+" -- "+str(second[2][1])+" views"
print str(second[3][0])+" -- "+str(second[3][1])+" views"
c.execute('''select substr(cast(log.time as varchar), 1, 10) as date,
            (count(case when status!='200 OK' then 1 else null end)*100)/
            count(substr(cast(log.time as varchar), 1, 10)) as percentage
            from log group by substr(cast(log.time as varchar), 1, 10) having
            (count(case when status!='200 OK' then 1 else null end)*100)/
            count(substr(cast(log.time as varchar), 1, 10))>=1;''')
third = c.fetchall()
print "  "
print "the_percentage_of_error_requests_per_day"
print str(third[0][0])+" -- "+str(third[0][1])+"%"+" error"
db.close()

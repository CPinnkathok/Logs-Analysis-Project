#!/usr/bin/env python2

import datetime
import psycopg2


def main():
    top_three_articles = order_article_views()
    print("The Top three searched articles are: ")
    for i in top_three_articles:
        print('%s - %d views' % (i[0], i[1]))

    top_authors = most_popular_article_authors()
    print("\nThe most popular article authors of all time are: ")
    for i in top_authors:
        print('%s - %d views' % (i[0], i[1]))

    top_day = find_day_with_most_failed_queries()
    print("\nThe day where more than 1%% of requests lead to errors was: ")
    for i in top_day:
        final_date = i[0]
        final_date = final_date.strftime("%B %d, %Y")
        print('%s - %.2f%% errors' % (final_date, i[1]))


def order_article_views():
    (database, cursor) = connect_to_database()
    # Count the number of views per article take top four articles
    # because empty queries are the top query
    sql_command = """
    select articles.title, count(log.path) as num
    from articles, log
    where articles.slug = right(log.path, length(log.path)-9)
    and log.status = '200 OK'
    and log.path LIKE '/article%'
    group by articles.title
    order by num desc
    limit 3;
    """
    cursor.execute(sql_command)
    result = cursor.fetchall()
    database.close()
    return result


def most_popular_article_authors():
    (database, cursor) = connect_to_database()
    # count the most popular article authors
    sql_command = """
    select finaltable.name, sum(finaltable.pathcount) as finalsum
    from
    (select log.path, articles.title, authors.name as name,
    count(log.path) as pathcount
    from log
    join articles on articles.slug = right(log.path, length(log.path)-9)
    join authors on authors.id = articles.author
    where log.status = '200 OK' and log.path LIKE '/article%'
    group by authors.name, articles.title, log.path) as finaltable
    group by finaltable.name
    order by finalsum desc;"""
    cursor.execute(sql_command)
    result = cursor.fetchall()
    database.close()
    return result


def find_day_with_most_failed_queries():
    (database, cursor) = connect_to_database()
    # determine day that had more that 1% of requests lead to errors
    sql_command = """
    select total.simpletime, fails.failtotal*100.0/total.totalcount
    from
    (select count(status) as failtotal, date(time) as simpletime from log
    where status != '200 OK' group by date(time)) as fails,
    (select count(status) as totalcount, date(time) as simpletime
    from log group by date(time)) as total
    where total.simpletime = fails.simpletime and
    fails.failtotal*100.0/total.totalcount > 1.0;
    """
    cursor.execute(sql_command)
    result = cursor.fetchall()
    database.close()
    return result


def connect_to_database():
    try:
        db = psycopg2.connect("dbname=news")
    except ImportError:
        print "I am unable to connect to the database"
    cur = db.cursor()
    return(db, cur)


if __name__ == '__main__':
    main()

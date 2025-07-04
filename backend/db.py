import psycopg2

def get_db_connection():
    """Establish a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            dbname='newsdb',
            user='ubuntu',
            password='ubuntu',
            host='localhost',
            port='5432'
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def get_all_news():
    """Fetch all news items from the database."""
    conn = get_db_connection()
    if not conn:
        return []

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM news")
            news_items = cursor.fetchall()
            news_items_array = []
            for item in news_items:
                news_items_array.append({
                    'name': item[0],
                    'link': item[1],
                    'published': item[2]
                })
            return news_items_array
    except psycopg2.Error as e:
        print(f"Error fetching news: {e}")
        return []
    finally:
        conn.close()

def insert_news_item(title,link,published):
    """Insert a news item into the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO news (name, link, published) VALUES (%s, %s, %s) ON CONFLICT (name) DO NOTHING",
                (title, link, published)
            )
            conn.commit()
            return True
    except psycopg2.Error as e:
        print(f"Error inserting news item: {e}")
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        print("Database connection established successfully.")
        news_items = get_all_news()
        print("Fetched news items:", news_items[0])
        conn.close()
    else:
        print("Failed to connect to the database.")
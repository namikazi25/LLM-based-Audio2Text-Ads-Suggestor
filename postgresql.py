import psycopg2

def insert_ad(description, link, keywords):
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="ads_dbv1",
            user="your_username1",
            password="your_password1",
            host="localhost"
        )
        cursor = conn.cursor()
        
        # Convert keywords list to PostgreSQL array format
        keywords_array = '{' + ','.join(keywords) + '}'
        
        # Insert ad data into the ads table
        cursor.execute("""
            INSERT INTO ads (description, link, keywords) 
            VALUES (%s, %s, %s)
        """, (description, link, keywords_array))
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        print("Ad inserted successfully!")
        
    except Exception as e:
        print(f"Error inserting ad: {e}")

# List of ads to insert
ads_data = [
    {"description": "This ad is from Just Eat. Food and Grocery Delivery Company. They deliver foods and groceries from local restaurants right to your doorstep.", "link": "https://www.youtube.com/watch?v=x12tKphzs14", "keywords": ["food", "grocery", "delivery"]},
    {"description": "This ad is from Reed.co.uk, a popular job searching site. They help with job recruitment, interview guidance, and streamline hiring tasks.", "link": "https://www.youtube.com/watch?v=OK9wrfMoP-Y", "keywords": ["job search", "interview", "recruitment", "hiring"]},
    {"description": "This ad is from Nike, promoting their new Air Max collection. The ad highlights the comfort and style of the new shoes.", "link": "https://www.youtube.com/watch?v=XsO3CFF0O5o", "keywords": ["shoes", "fashion", "sports", "comfort"]},
    {"description": "This ad is from Coca-Cola, featuring their classic beverage enjoyed by friends at a party.", "link": "https://www.youtube.com/watch?v=VGa1imApfdg", "keywords": ["beverage", "party", "refreshment", "friends"]},
    {"description": "This ad is from Apple, showcasing the new features of the iPhone 15.", "link": "https://www.youtube.com/watch?v=XHTrLYShBRQ", "keywords": ["technology", "smartphone", "innovation", "iPhone"]},
    {"description": "This ad is from Amazon Prime Video, highlighting the exclusive content available on their streaming platform.", "link": "https://www.youtube.com/watch?v=C4rqaSy2cxU", "keywords": ["streaming", "movies", "TV shows", "entertainment"]},
    {"description": "This ad is from McDonald's, promoting their new burger with fresh ingredients.", "link": "https://www.youtube.com/watch?v=RWMIUhlmdFs", "keywords": ["food", "fast food", "burger", "restaurant"]},
    {"description": "This ad is from Samsung, demonstrating the features of their new Galaxy S21 smartphone.", "link": "https://www.youtube.com/watch?v=111pLJf7cFE", "keywords": ["technology", "smartphone", "innovation", "Samsung"]},
    {"description": "This ad is from Pepsi, featuring their refreshing drink enjoyed during a beach party.", "link": "https://www.youtube.com/watch?v=7oBZ8sBjdyQ", "keywords": ["beverage", "party", "refreshment", "beach"]},
    {"description": "This ad is from Google, showcasing the capabilities of Google Assistant in daily tasks.", "link": "https://www.youtube.com/watch?v=-qCanuYrR0g", "keywords": ["technology", "assistant", "Google", "smart home"]},
    {"description": "This ad is from Spotify, promoting their premium service with ad-free music.", "link": "https://www.youtube.com/watch?v=ok-aNnc0Dko", "keywords": ["music", "streaming", "ad-free", "Spotify"]},
    {"description": "This ad is from Toyota, highlighting the features of their new hybrid car.", "link": "https://www.youtube.com/watch?v=0BMGH1UMgR8", "keywords": ["car", "hybrid", "Toyota", "eco-friendly"]},
    {"description": "This ad is from Netflix, promoting their new original series available for streaming.", "link": "https://www.youtube.com/watch?v=sY2djp46FeY", "keywords": ["streaming", "series", "Netflix", "entertainment"]},
    {"description": "This ad is from KFC, showcasing their new chicken sandwich.", "link": "https://www.youtube.com/watch?v=pWRYvUZhBsA", "keywords": ["food", "fast food", "chicken", "restaurant"]},
    {"description": "This ad is from Adidas, promoting their new line of athletic wear.", "link": "https://www.youtube.com/watch?v=_R9uWNf7j6c", "keywords": ["fashion", "sports", "clothing", "Adidas"]},
    {"description": "This ad is from Uber, highlighting their ride-sharing service and ease of use.", "link": "https://www.youtube.com/watch?v=3kb7_3Imvuc", "keywords": ["transportation", "ride-sharing", "Uber", "convenience"]},
    {"description": "This ad is from Microsoft, demonstrating the features of the new Surface Pro tablet.", "link": "https://www.youtube.com/watch?v=4Z5VbcLnhBQ", "keywords": ["technology", "tablet", "Microsoft", "Surface Pro"]},
    {"description": "This ad is from Starbucks, promoting their new range of seasonal drinks.", "link": "https://www.youtube.com/watch?v=o-Ikkh5oxuo", "keywords": ["beverage", "coffee", "seasonal", "Starbucks"]},
    {"description": "This ad is from BMW, highlighting the performance and design of their new electric car.", "link": "https://www.youtube.com/watch?v=l7NzjomVrr4", "keywords": ["car", "electric", "BMW", "performance"]},
    {"description": "This ad is from Visa, showcasing the convenience and security of using their credit cards.", "link": "https://www.youtube.com/watch?v=z5xddV_ydr0", "keywords": ["finance", "credit card", "security", "Visa"]}
]

# Insert each ad
for ad in ads_data:
    insert_ad(ad["description"], ad["link"], ad["keywords"])

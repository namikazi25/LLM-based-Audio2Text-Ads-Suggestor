import psycopg2

def update_ad_links(description, link):
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="ads_db",
            user="your_username",
            password="your_password",
            host="localhost"
        )
        cursor = conn.cursor()
        
        # Update the ad link in the ads table
        cursor.execute("""
            UPDATE ads 
            SET link = %s 
            WHERE description = %s
        """, (link, description))
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        print("Ad link updated successfully!")
        
    except Exception as e:
        print(f"Error updating ad link: {e}")

# List of ads to update
ads_data = [
    {"description": "This ad is from Just Eat. Food and Grocery Delivery Company. They deliver foods and groceries from local restaurants right to your doorstep.", "link": "https://www.youtube.com/watch?v=x12tKphzs14"},
    {"description": "This ad is from Reed.co.uk, a popular job searching site. They help with job recruitment, interview guidance, and streamline hiring tasks.", "link": "https://www.youtube.com/watch?v=OK9wrfMoP-Y"},
    {"description": "This ad is from Nike, promoting their new Air Max collection. The ad highlights the comfort and style of the new shoes.", "link": "https://www.youtube.com/watch?v=XsO3CFF0O5o"},
    {"description": "This ad is from Coca-Cola, featuring their classic beverage enjoyed by friends at a party.", "link": "https://www.youtube.com/watch?v=VGa1imApfdg"},
    {"description": "This ad is from Apple, showcasing the new features of the iPhone 13.", "link": "https://www.youtube.com/watch?v=XHTrLYShBRQ"},
    {"description": "This ad is from Amazon Prime Video, highlighting the exclusive content available on their streaming platform.", "link": "https://www.youtube.com/watch?v=C4rqaSy2cxU"},
    {"description": "This ad is from McDonald's, promoting their new burger with fresh ingredients.", "link": "https://www.youtube.com/watch?v=RWMIUhlmdFs"},
    {"description": "This ad is from Samsung, demonstrating the features of their new Galaxy S24 smartphone.", "link": "https://www.youtube.com/watch?v=111pLJf7cFE"},
    {"description": "This ad is from Pepsi, featuring their refreshing drink enjoyed during a beach party.", "link": "https://www.youtube.com/watch?v=7oBZ8sBjdyQ"},
    {"description": "This ad is from Google, showcasing the capabilities of Google Assistant in daily tasks.", "link": "https://www.youtube.com/watch?v=-qCanuYrR0g"},
    {"description": "This ad is from Spotify, promoting their premium service with ad-free music.", "link": "https://www.youtube.com/watch?v=ok-aNnc0Dko"},
    {"description": "This ad is from Toyota, highlighting the features of their new hybrid car.", "link": "https://www.youtube.com/watch?v=0BMGH1UMgR8"},
    {"description": "This ad is from Netflix, promoting their new original series available for streaming.", "link": "https://www.youtube.com/watch?v=sY2djp46FeY"},
    {"description": "This ad is from KFC, showcasing their new chicken sandwich.", "link": "https://www.youtube.com/watch?v=pWRYvUZhBsA"},
    {"description": "This ad is from Adidas, promoting their new line of athletic wear.", "link": "https://www.youtube.com/watch?v=_R9uWNf7j6c"},
    {"description": "This ad is from Uber, highlighting their ride-sharing service and ease of use.", "link": "https://www.youtube.com/watch?v=3kb7_3Imvuc"},
    {"description": "This ad is from Microsoft, demonstrating the features of the new Surface Pro tablet.", "link": "https://www.youtube.com/watch?v=4Z5VbcLnhBQ"},
    {"description": "This ad is from Starbucks, promoting their new range of seasonal drinks.", "link": "https://www.youtube.com/watch?v=o-Ikkh5oxuo"},
    {"description": "This ad is from BMW, highlighting the performance and design of their new electric car.", "link": "https://www.youtube.com/watch?v=l7NzjomVrr4"},
    {"description": "This ad is from Visa, showcasing the convenience and security of using their credit cards.", "link": "https://www.youtube.com/watch?v=z5xddV_ydr0"}
]

# Update each ad
for ad in ads_data:
    update_ad_links(ad["description"], ad["link"])

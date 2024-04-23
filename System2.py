from System1 import Post
from datetime import datetime

class System2:
    def __init__(self):
        """Class to represent a social media system"""
        self.posts = {}

    # Function to add a post to the social media system.
    def add_post(self, post):
        post_datetime = datetime.strptime(post.datetime, "%Y-%m-%d %H:%M") # Convert (using .strptime) the datetime string from the Post object into a datetime object using the specified format ("%Y-%m-%d %H:%M").
        if post_datetime not in self.posts: # Check if the hash value is not already in the posts dictionary.
            self.posts[post_datetime] = [] # Check if the hash value is not already in the posts dictionary.
        self.posts[post_datetime].append(post) # Append the post to the list corresponding to its hash value.


    # Function to search for posts in a specified datetime range.
    def search_posts_in_datetime_range(self, start_datetime, end_datetime):
        found_posts = [] # Empty list to store found posts.
        step_counter = 0  # Step counter initialization
        start_datetime = datetime.strptime(start_datetime, "%Y-%m-%d %H:%M") # Convert (using .strptime) the start datetime string into a datetime object using the specified format ("%Y-%m-%d %H:%M").
        end_datetime = datetime.strptime(end_datetime, "%Y-%m-%d %H:%M") # Convert (using .strptime) the end datetime string into a datetime object using the specified format ("%Y-%m-%d %H:%M").
        for post_datetime, post_list in self.posts.items(): # For loop to iterate through the hash values.
            step_counter += 1  # Increment step counter for each iteration
            if start_datetime <= post_datetime <= end_datetime: # Check if the hash value falls within the specified datetime range.
                found_posts.extend(post_list) # Extend the found_posts list with the posts associated with this hash value.
        print("Number of steps:", step_counter)
        return found_posts

# Test cases:
if __name__ == "__main__":
    system = System2()

    # Adding posts to the social media system Hash Table:
    post1 = Post("2024-03-14 09:45", "Good morning!", "Aliya")
    post2 = Post("2024-04-03 12:34", "Busy Day", "Khaled")
    post3 = Post("2024-01-21 16:20", "Happy Birthday", "Mahra")

    system.add_post(post1)
    system.add_post(post2)
    system.add_post(post3)

    # Allow the user to input start and end datetime range to search for posts:
    start_datetime_input = input("Enter start datetime to search posts (YYYY-MM-DD HH:MM): ")
    end_datetime_input = input("Enter end datetime to search posts (YYYY-MM-DD HH:MM): ")

    # Searching for posts within the specified datetime range:
    found_posts = system.search_posts_in_datetime_range(start_datetime_input, end_datetime_input)

    print("\nPosts within datetime range:")
    if found_posts:
        for post in found_posts:
            print(post.content)
    else:
        print("No posts found within the specified datetime range.")

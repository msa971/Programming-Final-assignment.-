class Post:
    """Class to represent social media posts"""

    # Constructor:
    def __init__(self, datetime, content, account):
        # Attributes of a post.
        self.datetime = datetime
        self.content = content
        self.account = account  # Account who posted the post.


class TreeNode:
    """Class to represent a node in the Binary Search Tree containing a social media post"""

    # Constructor:
    def __init__(self, post):
        self.post = post
        self.left = None
        self.right = None


class System1:
    """Class to represent the social media system"""

    # Constructor:
    def __init__(self):
        self.root = None

    # Function to add a post to the social media system BST.
    def add_post(self, post):
        if self.root is None:
            # If the tree is empty, set the post as the root.
            self.root = TreeNode(post)
        else:
            # Otherwise, traverse the tree to find the appropriate position to insert the new post.
            current = self.root
            while True:
                if post.datetime < current.post.datetime:
                    # Move to the left child of the current node.
                    if current.left is None:
                        # If there's no node to the left, create a new TreeNode with the given post.
                        current.left = TreeNode(post)
                        break
                    else:
                        # If there's a node to the left, update the current node to be the left child.
                        current = current.left
                else:
                    # Move to the right child of the current node.
                    if current.right is None:
                        # If there's no node to the right, create a new TreeNode with the given post.
                        current.right = TreeNode(post)
                        break
                    else:
                        # If there's a node to the right, update the current node to be the right child.
                        current = current.right

    def find_post_by_datetime(self, datetime):
        # Function to find a post by its specific datetime.
        current = self.root
        steps = 0  # Initializing step counter
        while current is not None:
            steps += 1  # Incrementing step counter for each iteration.
            if datetime == current.post.datetime:
                # If the datetime of the current node's post matches the specified datetime, return the post in the current node.
                return current.post, steps
            elif datetime < current.post.datetime:
                # Move to the left child of the current node.
                current = current.left
            else:
                # Move to the right child of the current node.
                current = current.right
        # If the specified datetime was not found in the tree, return None.
        return None, steps

# Test cases:
if __name__ == "__main__":
    # Creating a social media system
    system = System1()

    # Adding posts to the social media system BST:
    post1 = Post("Thursday 14 March 2024, 9:45am", "Good morning!", "Aliya")
    post2 = Post("Wednesday 3 April 2024, 12:34pm", "Busy Day", "Khaled")
    post3 = Post("Sunday 21 January 2024, 4:20pm", "Happy Birthday", "Mahra")

    system.add_post(post1)
    system.add_post(post2)
    system.add_post(post3)

    # Finding posts by datetime:
    datetime_to_find = input("Enter datetime to find post (e.g., Thursday 14 March 2024, 9:45am): ")
    found_post, steps = system.find_post_by_datetime(datetime_to_find)
    if found_post:
        print("Post found with datetime:", found_post.content)
        print("Number of steps:", steps)
    else:
        print("Sorry, no post found with that datetime.")
        print("Number of steps:", steps)
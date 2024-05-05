from instagram_private_api import Client, ClientCompatPatch

# Replace with your own API credentials
username = ''
password = ''

# Create an Instagram API client
api = Client(username, password)
ClientCompatPatch.api(api)

# Example: Get user's profile information
user_id = api.authenticated_user_id
user_info = api.user_info(user_id)
print(user_info)

# Example: Post a photo
photo_path = 'path_to_your_photo.jpg'
caption = 'Check out this photo!'
api.post_photo(photo_path, caption=caption)

# Example: Get user's recent media
recent_media = api.user_feed(user_id)
for media in recent_media:
    print(media)

# Remember to handle exceptions and errors appropriately in your script

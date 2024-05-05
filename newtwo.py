from instagram_private_api import Client, ClientCompatPatch

# Replace with your own API credentials
username = ''
password = ''


# Create an Instagram API client
api = Client(username, password)
ClientCompatPatch.api(api)

# Example: Like a post
post_url = 'https://www.instagram.com/p/CuEC0o1tm8l/?igshid=MzRlODBiNWFlZA=='
post_id = api.media_pk_from_url(post_url)
api.post_like(post_id)

# Example: Comment on a post
comment_text = 'Great photo!'
api.post_comment(post_id, comment_text)

# Remember to handle exceptions and errors appropriately in your script

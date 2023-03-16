import instaloader

# Membuat instance instaloader
loader = instaloader.Instaloader()

# Mengambil URL Instagram Story dari pengguna
story_url = input("Masukkan URL Instagram Story: ")

# Mendapatkan informasi mengenai Instagram Story
story = instaloader.Story.from_url(loader.context, story_url)

# Mengambil video atau foto dari Instagram Story
if story.typename == "Video":
    # Jika Instagram Story berisi video
    loader.download_storyvideo(story, target=story.owner_username + ".mp4")
else:
    # Jika Instagram Story berisi foto
    loader.download_storyphoto(story, target=story.owner_username + ".jpg")

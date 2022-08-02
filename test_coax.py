def hashing_string(string_to_hash):
    hashed = hash(string_to_hash)
    return hashed


def tiktok_gif_converter(video_url, gif_storage, gif_number):
    url = video_url.replace(' ', '-')
    if gif_storage.endswith('/'):
        path_to_gif = f'{gif_storage}{url}-{gif_number}.gif'
    else:
        path_to_gif = f'{gif_storage}/{url}-{gif_number}.gif'
    return path_to_gif

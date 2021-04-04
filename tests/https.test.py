from downloader.elasticdownloader import ElasticDownloader

uri = 'https://i.picsum.photos/id/84/536/354.jpg?hmac=sZKPCkAEBdGnNortqWOUnZFzC702PRotKIlEkWN6GXo'

retriever = ElasticDownloader()
# retriever.download(uri, '.')

res = retriever.retrieve(uri)
print(res)

with open('image.jpg', 'wb') as fh:
    fh.write(res.getvalue())

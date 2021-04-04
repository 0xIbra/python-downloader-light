from downloader.elasticdownloader import ElasticDownloader

uri = 'ftp://phpunit:Ma8cdWG@flux.publi-car.fr/astronaut_spacesuit_reflection_144426_1920x1200.png'

retriever = ElasticDownloader()
res = retriever.retrieve(uri)

print(res)

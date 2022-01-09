#!/usr/bin/python
# -*- coding: utf-8 -*-
from youtube_search import YoutubeSearch
import pafy

usersearch = input('Search: ')
results = YoutubeSearch(usersearch, max_results=1).to_dict()

for v in results:
    link = 'https://www.youtube.com' + v['url_suffix']
video = pafy.new(link)

streams = video.streams

best = video.getbest()
print (best.resolution, best.extension)
best.download()
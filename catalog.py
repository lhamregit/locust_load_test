import json
import ast
import httplib, urllib


class Catalog:
    def __init__(self):
        self.host = 'android.mobile.us'
        self.deviceName = 'LGE-LGMS345'
        self.deviceId = '1234'

    def getArtist(self, client, headers):
        # body = {"artistId":"540804", "includeBio":"true", "countryCode":"us"}
        with client.get("/api/v1/catalog/getArtistByArtistId?artistId=540804&includeBio=true&countryCode=us",
                        headers=headers, name='/api/v1/catalog/getArtistByArtistId[id]', catch_response=True) as response:
            #print "Response content:", response.content
            #print response.headers['Cache-Control']
            artist = json.loads(response.content)
            name = artist['artist']['artistName']
            bio = artist['artist']['artistBio']
            print name

    def getLiveStations(self, client, headers):
        # body = {"artistId":"540804", "includeBio":"true", "countryCode":"us"}
        with client.get("/api/v2/content/liveStations/4243", headers=headers, name='/api/v2/content/liveStations/[id]',catch_response=True) as response:
            #print "Response content:", response.content
            #print response.headers['Cache-Control']
            res = json.loads(response.content)
            #print res

    def getSimilar(self, client, headers):
        # body = {"artistId":"540804", "includeBio":"true", "countryCode":"us"}
        with client.get("/api/v1/catalog/artist/34742/getSimilar", headers=headers,name='/api/v1/catalog/artist/[id]/getSimilar/', catch_response=True) as response:
            #print "Response content:", response.content
            #print response.headers['Cache-Control']
            res = json.loads(response.content)
            #print res


    def searchAll(self, client, headers):
        # body = {"artistId":"540804", "includeBio":"true", "countryCode":"us"}
        with client.get(
                "/api/v1/catalog/searchAll?keywords=rihanna&queryBundle=false&queryKeyword=true&maxRows=3&countryCode=US&startIndex=0&queryStation=true&queryArtist=true&queryTrack=true&queryFeaturedStation=true&queryTalkShow=true&queryTalkTheme=true&boostMarketId=159",
                headers=headers, name='/api/v1/catalog/searchAll?keywords=[keyword]',catch_response=True) as response:
            #print "Response content:", response.content
            #print response.headers['Cache-Control']
            res = json.loads(response.content)
            #print res
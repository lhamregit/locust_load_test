from locust import HttpLocust, TaskSet, task

from catalog import Catalog

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        print "on start called"
        self.userHeaders = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}

    @task(4)
    def GetArtist(self):
        cat = Catalog()
        cat.getArtist(self.client, self.userHeaders)

    @task(1)
    def GetSimilar(self):
        cat = Catalog()
        cat.getSimilar(self.client, self.userHeaders)

    @task(1)
    def Search(self):
        cat = Catalog()
        cat.searchAll(self.client, self.userHeaders)

    @task(2)
    def GetLive(self):
        cat = Catalog()
        cat.getLiveStations(self.client, self.userHeaders)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=2000
    max_wait=4000

#https://github.com/gleicon/locust-swarm
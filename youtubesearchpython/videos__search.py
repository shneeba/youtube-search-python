import urllib.request
import json

from youtubesearchpython.__requesthandler import requesthandler
from youtubesearchpython.videos__pagehandler import pagehandler
from youtubesearchpython.videos__scripthandler import scripthandler


class SearchVideos(requesthandler, pagehandler, scripthandler):

    #########https://github.com/alexmercerind/youtube-search-python#########

    networkError = False
    validResponse = False

    def __init__(self, keyword, offset = 1, mode = "json", max_results = 20):

        #########CLASS CONSTRUCTOR#########

        #########Setting Feilds#########

        self.offset = offset
        self.mode = mode
        self.keyword = keyword
        self.max_results = max_results
        self.searchPreferences = "EgIQAQ%3D%3D"

        #########Executing Entry Point Of Class#########

        self.exec()

    def exec(self):
        
        #########exec PROPERTY#########

        #########Calling network request.#########

        self.request()

        if self.networkError:
            self.networkError = True

        else:

            if not self.validResponse:
                self.scriptResponseHandler()
            
            if self.validResponse:
                self.pageResponseHandler()

    def result(self):

        #########result PROPERTY#########

        #########Checking for network error and returning None to the user in case of it.#########

        if self.networkError:
            return None

        else:

            result = []
            
            #########JSON Result Handling.#########

            if self.mode in ["json", "dict"]:

                for index in range(len(self.ids)):
                    result_index = {
                        "index": index,
                        "id": self.ids[index],
                        "link": self.links[index],
                        "title": self.titles[index],
                        "channel": self.channels[index],
                        "duration": self.durations[index],
                        "views": self.views[index],
                        "thumbnails": self.thumbnails[index]
                    }
                    result+=[result_index]

                if self.mode == "json":
                    return json.dumps({"search_result": result}, indent=4)
                else:
                    return {"search_result": result}
            
            #########List Result Handling.#########

            elif self.mode == "list":
                
                for index in range(len(self.ids)):
                    list_index=[
                            index,
                            self.ids[index],
                            self.links[index],
                            self.titles[index],
                            self.channels[index],
                            self.durations[index],
                            self.views[index],
                            self.thumbnails[index]
                    ]
                    result+=[list_index]
                
                return result
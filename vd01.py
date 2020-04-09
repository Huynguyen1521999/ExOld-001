import web
urls = (
'/', 'index'
)
class index:
    def GET(self):
        return "Welcome !!! Nguyen Trieu Huy - 2715150 !"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["asw"]
mycol = mydb["hw_info"]



class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index_asw.html')

class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
       # noun2 = self.get_argument('noun2')
       # verb = self.get_argument('verb')
      #  noun3 = self.get_argument('noun3')
        sele = self.get_argument('sele')
        print(sele)
        if sele == "Management IP":
            sele = "Management IP "
        cnt = 0
        code = []
        noun2 = 'x'
        if noun2 == 'x':
            for y in mycol.find({sele: {"$regex": noun1}}):
                cnt = cnt + 1
                # {"$regex": "CNS"}}):
                a = "<tr><td>Business Unit:</td><td> %s </td></tr> " % y['Business Unit']
                # code.append(%y['IP Address(Private)'])
                code.append(a)
                b = "<tr><td>Store code:</td><td> %s</td></tr>" % y['Store code']
                code.append(b)
                c = "<tr><td>Management IP:</td><td> %s</td></tr>" % y['Management IP ']
                code.append(c)
                c = "<tr><td>Hostname:</td><td> %s</td></tr>" % y['Hostname']
                code.append(c)
                c = "<tr><td>Device:</td><td> %s</td></tr>" % y['Device']
                code.append(c)
                c = "<tr><td>Model:</td><td> %s</td></tr>" % y['Model']
                code.append(c)
                d = "<tr><td>Serial No:</td><td> %s </td></tr>" % y['Serial No']
                code.append(d)
                d = "<tr><td>Remark:</td><td> %s </td></tr>" % y['Remark']
                code.append(d)
                d = "<tr><td></td></tr>"
                code.append(d)

                print(cnt)

            contents = '''<!DOCTYPE html>
            <html>
            <head>
            <style>
            table, th, td {
              border: 1px solid black;
              border-collapse: collapse;
              word-wrap: initial;
            }
    
            </style>
            <meta content="text/html; charset=ISO-8859-1"
            http-equiv="content-type">
            <title>RDOC Webbrowser</title>
    
    
    
            </head>
            <body>
            
            <table>
            %s
            </table>
            
            
    
            </body>
            </html>
            ''' % (code)
            print(code)
            # self.write('<image src="logo.png">')
            return self.write(contents)
        else:

            self.render('poem.html', roads=noun1, wood=noun2, made=verb,
                difference=sele)



if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), (r'/result', PoemPageHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
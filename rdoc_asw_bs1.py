import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo
import webbrowser

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
                print(code)
                print(cnt)

            contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
            <html>
            <head>
            <style>
            table, th, td {
              border: 1px solid black;
              border-collapse: collapse;
              word-wrap: break-word;
            }
            tr:nth-child(even) {
              background-color: #D6EEEE;
            }
            tr:nth-child(odd) {
              background-color: #D6EEEE;
            }
            </style>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <meta name="description" content="">
                <meta name="author" content="">

                <title>RDOC Admin - Dashboard</title>

                <!-- Bootstrap core CSS-->
                <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

                <!-- Custom fonts for this template-->
                <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">

                <!-- Page level plugin CSS-->
                <link href="vendor/datatables/dataTables.bootstrap4.css" rel="stylesheet">

                <!-- Custom styles for this template-->
                <link href="css/sb-admin.css" rel="stylesheet">

            </head>
             <body id="page-top" class = "bg-dark">

                <nav class="navbar navbar-expand navbar-dark bg-dark static-top">

                  <a class="navbar-brand mr-1" href="index.html">Macroview RDOC Information System</a>

                  <button class="btn btn-link btn-sm text-white order-1 order-sm-0" id="sidebarToggle" href="#">
                    <i class="fas fa-bars"></i>
                  </button>

                  <!-- Navbar Search -->
                  <form class="d-none d-md-inline-block form-inline ml-auto mr-0 mr-md-3 my-2 my-md-0">
                    <div class="input-group">
                      <input type="text" class="form-control" placeholder="Search for..." aria-label="Search" aria-describedby="basic-addon2">
                      <div class="input-group-append">
                        <button class="btn btn-primary" type="button">
                          <i class="fas fa-search"></i>
                        </button>
                      </div>
                    </div>
                  </form>

                  <!-- Navbar -->
                  <ul class="navbar-nav ml-auto ml-md-0">
                    <li class="nav-item dropdown no-arrow mx-1">
                      <a class="nav-link dropdown-toggle" href="#" id="alertsDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i class="fas fa-bell fa-fw"></i>
                        <span class="badge badge-danger">8+</span>
                      </a>
                      <div class="dropdown-menu dropdown-menu-right" aria-labelledby="alertsDropdown">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="#">Something else here</a>
                      </div>
                    </li>
                    <li class="nav-item dropdown no-arrow mx-1">
                      <a class="nav-link dropdown-toggle" href="#" id="messagesDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i class="fas fa-envelope fa-fw"></i>
                        <span class="badge badge-danger">7</span>
                      </a>
                      <div class="dropdown-menu dropdown-menu-right" aria-labelledby="messagesDropdown">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="#">Something else here</a>
                      </div>
                    </li>
                    <li class="nav-item dropdown no-arrow">
                      <a class="nav-link dropdown-toggle" href="#" id="userDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <i class="fas fa-user-circle fa-fw"></i>
                      </a>
                      <div class="dropdown-menu dropdown-menu-right" aria-labelledby="userDropdown">
                        <a class="dropdown-item" href="#">Settings</a>
                        <a class="dropdown-item" href="#">Activity Log</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="#" data-toggle="modal" data-target="#logoutModal">Logout</a>
                      </div>
                    </li>
                  </ul>

                </nav>
         <div id="wrapper">


         <div class="row">
            <div class="col-xl-3 col-sm-6 mb-3">
              <div class="card text-white bg-primary o-hidden h-100">
                <div class="card-body">
                  <div class="card-body-icon">
                    <i class="fas fa-fw fa-road"></i>
                  </div>
                  <div class="mr-5">26 New Tenders!</div>
                </div>
                <a class="card-footer text-white clearfix small z-1" href="#">
                  <span class="float-left">View Details</span>
                  <span class="float-right">
                    <i class="fas fa-angle-right"></i>
                  </span>
                </a>
              </div>
            </div>
            <div class="col-xl-3 col-sm-6 mb-3">
              <div class="card text-red bg-warning o-hidden h-100">
                <div class="card-body">
                  <div class="card-body-icon">
                    <i class="fas fa-fw fa-list"></i>
                  </div>
                  <div class="mr-5">11 New Tasks!</div>
                </div>
                <a class="card-footer text-red clearfix small z-1" href="#">
                  <span class="float-left">View Details</span>
                  <span class="float-right">
                    <i class="fas fa-angle-right"></i>
                  </span>
                </a>
              </div>
            </div>
            <div class="col-xl-3 col-sm-6 mb-3">
              <div class="card text-white bg-success o-hidden h-100">
                <div class="card-body">
                  <div class="card-body-icon">
                    <i class="fas fa-fw fa-upload"></i>
                  </div>
                  <div class="mr-5">123 New Projects!</div>
                </div>
                <a class="card-footer text-white clearfix small z-1" href="#">
                  <span class="float-left">View Details</span>
                  <span class="float-right">
                    <i class="fas fa-angle-right"></i>
                  </span>
                </a>
              </div>
            </div>
            <div class="col-xl-3 col-sm-6 mb-3">
              <div class="card text-white bg-danger o-hidden h-100">
                <div class="card-body">
                  <div class="card-body-icon">
                    <i class="fas fa-fw fa-comments"></i>
                  </div>
                  <div class="mr-5">23 New Quotation!</div>
                </div>
                <a class="card-footer text-white clearfix small z-1" href="#">
                  <span class="float-left">View Details</span>
                  <span class="float-right">
                    <i class="fas fa-angle-right"></i>
                  </span>
                </a>
              </div>
            </div>
          </div>
           </div>
            <div class="card-body">
            <div class="table-responsive">
                  <!-- Sidebar -->
      <ul class="sidebar navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" href="index.html">
            <i class="fas fa-fw fa-tachometer-alt"></i>
            <span>Dashboard</span>
          </a>
        </li>        

    </div>
     
          <!-- DataTables Example -->
          <div class="card mb-3">
            <div class="card-header">
              <i class="fas fa-table"></i>
              Project Management</div>
            <div class="card-body">
              <div class="table-responsive">
                <table>
            %s
            </table>
              <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>
                      <footer class="sticky-footer">
          <div class="container my-auto">
            <div class="copyright text-center my-auto">
              <span>Copyright ?? Macroview RDOC Information System 2022</span>
            </div>
          </div>
        </footer>
                          </div>
            </div>              

             </div>
            </div>
                    

   <a class="scroll-to-top rounded" href="#page-top">
      <i class="fas fa-angle-up"></i>
    </a>
    <!-- Logout Modal-->
    <div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
            <button class="close" type="button" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">??</span>
            </button>
          </div>
          <div class="modal-body">Select "Logout" below if you are ready to end your current session.</div>
          <div class="modal-footer">
            <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
            <a class="btn btn-primary" href="login.html">Logout</a>
          </div>
        </div>
      </div>
    </div>
    <!-- Bootstrap core JavaScript-->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Core plugin JavaScript-->
    <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Page level plugin JavaScript-->
    <script src="vendor/chart.js/Chart.min.js"></script>
    <script src="vendor/datatables/jquery.dataTables.js"></script>
    <script src="vendor/datatables/dataTables.bootstrap4.js"></script>

    <!-- Custom scripts for all pages-->
    <script src="js/sb-admin.min.js"></script>

    <!-- Demo scripts for this page-->
    <script src="js/demo/datatables-demo.js"></script>
    <script src="js/demo/chart-area-demo.js"></script>
    <script src="js/demo/chart-bar-demo.js"></script>
    <script src="js/demo/chart-pie-demo.js"></script>           
            </body>


            </html>

            ''' % (code)

            contents1 = '''<!DOCTYPE html>
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
            <tbody>
            %s
            </tbody>
            </table>


            </body>
            </html>
            ''' % (code)

            filename = 'info.html'
            output = open(filename, "w")
            output.write(contents)
            output.close()
            print(code)
            #webbrowser.open(filename)
            # self.write('<image src="logo.png">')
            return self.write(contents1)
            #self.render('info.html')
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
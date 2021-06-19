from wsgiref.simple_server import make_server



def  run_server(envrion,start_response):
   print('hahaha',envrion)

   start_response("200 OK",[('Content-Type','text/html;charset=utf-8')])
   return [bytes('<h2>旁边的小云好看<h2>',encoding="utf-8"),]
s=make_server('localhost',8000,run_server)
s.serve_forever()
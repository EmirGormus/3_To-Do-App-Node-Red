from livereload import Server,shell
server=Server()
server.watch("*.css")
server.watch("*.html")
server.watch("*.js")
server.serve(port=9999,root='.')
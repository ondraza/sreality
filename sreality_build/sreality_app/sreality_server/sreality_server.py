import os
import psycopg2
import json
import http.server
import socketserver

GREEN = '\033[32m'
NONE = '\033[39m'

'''
ENV_HOSTNAME = os.getenv('HOSTNAME')
ENV_DATABASE = os.getenv('DATABASE')
ENV_PORT = os.getenv('PORT')
ENV_USERNAME = os.getenv('USERNAME')
ENV_PASSWORD = os.getenv('PASSWORD')
'''

ENV_HOSTNAME = 'db'
ENV_DATABASE = 'sreality_db'
ENV_PORT = '5432'
ENV_USERNAME = 'postgres'
ENV_PASSWORD = 'password'

connection = psycopg2.connect(
    host=ENV_HOSTNAME,
    dbname=ENV_DATABASE,
    port=ENV_PORT,
    user=ENV_USERNAME,
    password=ENV_PASSWORD
)

cur = connection.cursor()

cur.execute('SELECT * FROM flats')
flats = cur.fetchall()

# debug
with open('flats_parsed.json', 'w') as json_file:
    json.dump(flats, json_file, indent=4)

tableHtml = '<html>\n\t<table>\n'
for flat in flats:
    flat_info = '{}'.format(flat[1])
    #flat_info = '<b>[{}]</b> {} {} {:,.0f} CZK'.format(flat[0], flat[1], flat[3], float(flat[4]))
    flatHtml = '\t\t<tr><td>'+flat_info+'</td><td><img src=\"'+flat[2]+'\"></td><tr>\n'
    tableHtml += flatHtml
tableHtml += '\t</table>\n</html>'

with open('index.html', 'w', encoding='utf-16') as html_file:
    html_file.write(tableHtml)
 
PORT = 8080

'''
class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = '../index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
 
Handler = HttpRequestHandler
'''

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('0.0.0.0', PORT), Handler) as httpd:
    print(GREEN + 'Http server serving at port ' + str(PORT) + NONE)
    httpd.serve_forever()

from flask import Flask, request, render_template, send_from_directory
from werkzeug.exceptions import BadRequest

from autocomic import AutoComic, GooglePanelFactory
from autocomic.googlesearch import GoogleCustomSearch
from autocomicftp.autocomicview import AutocomicView


app = Flask("autocomicftp", static_url_path='')
app.config.from_object('autocomicftp.CONFIG_SETTINGS')
search_engine_id = ''
client_key = ''


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route("/autocomicforthepeople/", methods=['GET', 'POST'])
def autocomic():

    if request.method == 'POST':
        validate_input()

        autocomic = get_comic()
        comicview = AutocomicView(autocomic, columns=3)
        comicview.prepare_layout()

        response_payload = render_template("autocomicview.html", comicview=comicview)

    if request.method == 'GET':
        response_payload = render_template("autocomicview.html")
    
    return response_payload

def get_comic():
    
    panel_factory = GooglePanelFactory(
        GoogleCustomSearch(cx = app.config['SEARCH_ENGINE_ID'], 
                           api_key = app.config['CLIENT_KEY'])
    )

    script = request.form['script'].split('\n')
    autocomic = AutoComic(script, panel_factory, request.form['title'])
    autocomic.initialize_panels()
    autocomic.set_panels_art()
    
    return autocomic

def validate_input():
    
    if 'script' not in request.form: 
        raise BadRequest(description="Missing value for attribute script.")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


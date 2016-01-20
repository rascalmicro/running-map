from flask import *
import folium

app = Flask(__name__)

@app.route("/")
def hello():
	map_osm = folium.Map(location=[42.398,-71.120], zoom_start=15)
	map_osm.create_map(path='templates/map.html')
	return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

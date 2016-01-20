from flask import *
import folium

app = Flask(__name__)

@app.route("/")
def hello():
	map_osm = folium.Map(location=[42.35341,-71.0829921])
	map_osm.create_map(path='templates/map.html')
	return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

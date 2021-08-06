from flask import Flask, render_template, request

from db_manager import DatabaseManager

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle_request():
    return "dementia server"


@app.route('/append-location', methods=['GET', 'POST'])
def handle_gps_location_set():
    if request.is_json:
        params = request.get_json()
        print(params['longitude'], params['latitude'])
        longitude = params['longitude']
        latitude = params['latitude']
        my_db = DatabaseManager().instance()
        my_db.create_connection(DatabaseManager.DB_WATCH_DATA)
        my_db.get_cursor()
        my_db.insert_row(longitude, latitude,
                         database=DatabaseManager.DB_WATCH_DATA,
                         table_name="SmartWatch"
                         )
        my_db.close_connection(DatabaseManager.DB_WATCH_DATA)
        return 'ok'
    return 'failed'


@app.route('/query-location', methods=['GET', 'POST'])
def query_patient_location():
    my_db = DatabaseManager().instance()
    my_db.create_connection(DatabaseManager.DB_WATCH_DATA)
    my_db.get_cursor()
    long_dict = my_db.select_last_element_of_column(table_name="SmartWatch", column_name="longitude")
    lati_dict = my_db.select_last_element_of_column(table_name="SmartWatch", column_name="latitude")
    my_db.close_connection(DatabaseManager.DB_WATCH_DATA)
    test_str = f"longitude: {long_dict['longitude']}\nlatitude: {lati_dict['latitude']}"
    return test_str


@app.route('/address', methods=['GET', 'POST'])
def address_request():
    return render_template("daum.html")


app.run(host="0.0.0.0", port=5000, debug=True)

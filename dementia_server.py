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
# for signup with userinfo DB
@app.route('/signup',methods=['POST'])
def signup():
    if(request.is_json):
        user_my_db = DatabaseManager.instance()
        user_my_db.create_connection(DatabaseManager.DB_USER_DATA)
        user_my_db.get_cursor()
        
        params = request.get_json()
        id = params['id']
        name = params['name']
        phone = params['phone']
        pw = params['pw']
        patient_id = params['patient']
        field = ["id","pw","name","phone","patient_name"]
        
        user_my_db.insert_with_specific_field(id,pw,name,phone,patient_id,
                                            table_name="parent_user", field_name = field
                                            )
        user_my_db.close_connection(DatabaseManager.DB_USER_DATA)
        return 'success'
    return 'failed'
@app.route('/login',methods=['POST'])
def login():
    if(request.is_json):
        user_my_db = DatabaseManager.instance()
        user_my_db.create_connection(DatabaseManager.DB_USER_DATA)
        user_my_db.get_cursor()

        params = request.get_json()
        login_id = params['id']
        pw = params['pw']
        result = user_my_db.get_login_info(login_id=login_id,pw=pw,table_name="parent_user")
        user_my_db.close_connection(DatabaseManager.DB_USER_DATA)
#        return result
#        print(result)
        if result == "wrong":
            return result
        else: 
            return "success"
        

app.run(host="0.0.0.0", port=5000, debug=True)

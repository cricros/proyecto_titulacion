from flask import Flask, render_template,request
from flask_mysqldb import MySQL
'''
Si estas usando python y quieres usar la flask_mysqldb recuerda instalar primero:
1) sudo apt-get install python-dev default-libmysqlclient-dev libssl-dev y al final
2) pip install --user flask-mysqldb


#iniciar xampp sudo /opt/lampp/manager-linux-x64.run

'''
app = Flask(__name__)
#Conexion BD


#si no te permite conectar con localhost intenta con 127.0.0.1.
app.config['MYSQL_HOST'] = 'ProyectoSusanaas.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'ProyectoSusanaas'
app.config['MYSQL_PASSWORD'] = '123456789az'
app.config['MYSQL_DB'] = 'ProyectoSusanaas$comp_pc'

mysql = MySQL(app)

dic_juego = {1 : "Dota 2", 2 : "Counter-Strike: Global Offensive", 3 : "Path of Exile", 4 : "Age of empires 4", 5: "RUST", 6: "Team Fortress 2", 7:"Apex Legends",
8: "Payday 2", 9: "Football Manager ", 10: "Rainbow six siege", 11: "Final Fantasy XIV", 12: "Destiny 2", 13: "Dead by Deadlight", 14: "GTA V", 15: "ARK", 16: "PUBG BATTLEGROUNDS",
17: "Rocket League", 18: "New World", 19: "Halo infinite", 20: "Read dead redemption 2"}
dic_res = {1 : "1080", 2 : "1440", 3 : "4k"}

"""
@app.route("/")
def index():
    return render_template("index.html") #cambiar el formato de index.hmtl


@app.route('/select') select
def select():
    cursor = mysql.connection.cursor()

    select = cursor.execute("select * from conjunto where juego = '$juego' and calidad = '$calidad';")

    if select > 0:
        #se utiliza fetchall  dado que no esperamos demasiados archivos

        userDetails = cursor.fetchall()

        return render_template('select_table.html',userDetails = userDetails)


"""

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        len_tupla = len(request.form.getlist('cap1'))
        len_tupla_res = len(request.form.getlist('cal1'))

        if len_tupla == 0: #Se selecciona 0 juegos
            if len_tupla_res == 0: # Seleccion de ninguna resolucion
                return render_template("error1.html") #"Selecciona al menos un juego y una resolucion" #check funciona
            elif len_tupla_res != 0 and len_tupla_res < 2: # al menos una resolución y al menos un juego seleccionado
                return render_template("error5.html") #"eh no mames, selecciona un juego" #check funciona

        elif len_tupla > 3:
            if len_tupla_res == 1:
                return render_template("error2.html") #"Selecciona de 1 a 3 juegos y una resolucion" #template error te lo encargo jorge uwu

            return render_template("error4.html") #"selecciona de 1 a 3 juegos y una resolucion"

        #elif len_tupla != 0 and len_tupla < 4: # selecciona al menos un juego pero ninguna calidad
            #if len_tupla_res == 0:
                #return render_template("error6.html") #"e no mames selecciona calidad"
            #elif len_tupla_res != 2 and len_tupla_res < 4:
            #    return render_template("error3.html")

        else:
            lista_juegos = list(map(int, request.form.getlist('cap1')))
            resolucion = int(request.form.get('cal1'))
            max_value = max(lista_juegos) #numero mas grande

            juego = dic_juego.get(max_value)
            res = dic_res.get(resolucion)

            cur = mysql.connection.cursor()
            select = cur.execute(f"select * from conjunto where juego = '{juego}' and calidad = '{res}';") # ya no mover nada!

            if select > 0:
                data = cur.fetchall()
            return render_template("servido.html", config_pc = data,juego=juego,res=res)

    return render_template("checkbox.html") #nuevo index

if __name__ == '__main__':
    app.run(debug=True)



'''

cursor = mysql.connection.cursor()
        select = cursor.execute(f"select NomP  from conjunto where juego = '{juego}' and calidad = '{res}';")
        cursor1 = mysql.connection.cursor()
        select1 = cursor1.execute(f"select NomG  from conjunto where juego = '{juego}' and calidad = '{res}';")
        cursor2 = mysql.connection.cursor()
        select2 = cursor2.execute(f"select MB  from conjunto where juego = '{juego}' and calidad = '{res}';")
        cursor3 = mysql.connection.cursor()
        select3 = cursor3.execute(f"select  Disco  from conjunto where juego = '{juego}' and calidad = '{res}';")
        cursor4 = mysql.connection.cursor()
        select4 = cursor4.execute(f"select  Fuente  from conjunto where juego = '{juego}' and calidad = '{res}';")
        cursor5 = mysql.connection.cursor()
        select5 = cursor5.execute(f"select RAM  from conjunto where juego = '{juego}' and calidad = '{res}';")

        if select > 0 and select1 > 0 and select2 > 0 and select3 > 0 and select4 > 0 and select5 > 0:
        #se utiliza fetchall  dado que no esperamos demasiados archivos

            userDetails = cursor.fetchall()
            userDetails1 = cursor1.fetchall()
            userDetails2 = cursor2.fetchall()
            userDetails3 = cursor3.fetchall()
            userDetails4 = cursor4.fetchall()
            userDetails5 = cursor5.fetchall()

        return render_template("servido.html", juego=juego, res=res, userDetails=userDetails, userDetails1=userDetails1, userDetails2=userDetails2, userDetails3=userDetails3,
        userDetails4=userDetails4, userDetails5=userDetails5) #pagina de visualizacion.
        #return (f'El juego con mayor carga tècnica es: {juego} y tu resolucion seleccionada es: {res}.\n Sus componentes son: {userDetails}')
        #return render_template("servido.html", juego=juego, res=res, userDetails1=userDetails1)
'''

#validaciones
"""





"""
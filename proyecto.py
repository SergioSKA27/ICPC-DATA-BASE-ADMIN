#!/usr/bin/python
from re import I
import PySimpleGUI as sg
from os import execv
import psycopg2 as pgdb

pasword = "postgres"




#INSERT
def  insert_persona(values):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT INTO  persona(id_persona,nombre,apellido_1,apellido_2,fecha_nacimiento,telefono,correo_electronico) VALUES (%s,%s,%s,%s,%s,%s,%s);",
        (values['Id'],values['Nombre'],values['ApellidoP'],values['ApellidoM'],values['FechaN' ],values['Telefono' ],values['CorreoE']))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e


def  insert_Tercia(values):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT INTO  tercia(id_persona,id_equipo) VALUES (%s,%s);",(values['IdPersona'],values['idEqupol4']))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e


def  insert_equipo(values):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT INTO  equipo(id_equipo,nombre,cve_universidad,estatus) VALUES (%s,%s,%s,%s);",
        (values['Idequipo'],values['NombreEquipo'],values[ 'claveUniver'],values['estatus']))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e


def  insert_equipolocal(values):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT INTO  equipo_local(id_equipo,code_competicion,cve_universidad) VALUES (%s,%s,%s);",
        (values['Idequipo'],values['NombreEquipo'],values[ 'claveUniver']))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e


def  insert_equiporegional(values):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT INTO  equipo_regional(id_equipo,code_competicion) VALUES (%s,%s);",
        (values['Idequipo'],values['NombreEquipo']))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e

def  insert_equipomundial(values):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT INTO  equipo_mundial(id_final_mundial,id_equipo) VALUES (%s,%s);",
        (values['Idequipo'],values['NombreEquipo'],values[ 'claveUniver'],values['estatus']))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e


def  insert_juez(values):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        reg_juez = {'IdJuez' : values['-IDJuezL6-'],'idpersona' : values['-IDpersonaL6-'], 'especiaslizacion' : values['-especializacionL6-'],'puntuacion' : values['-puntuacionL6-']}
        cur = conexion.cursor()
        cur.execute("INSERT INTO  juez(id_juez,id_persona,especializacion,puntuacion) VALUES (%s,%s,%s,%s);",
        (values['IdJuez'],values['idpersona'],values['especiaslizacion'],values['puntuacion']))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e 

def  insert_Universidad(values):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT INTO  universidad(cve_universidad,nombre,id_region) VALUES (%s,%s,%s);",
        (values['IdUniver'],values['Nombre'],values['region']))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e

def  insert_problema(values):
    try:
        reg_problem = {'IdProblem' : values['-IDproblemaL9-'],'Desc' : values['-DescProblem-'], 'Tipo' : values['-TipoL9-']}

        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT INTO  problema(code_problema,descripcion,tipo) VALUES (%s,%s,%s);",
        (values['IdProblem'],values['Desc'],values['Tipo']))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e: 
        raise e


def  insert_programa(values):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT INTO  programa(id_programa,code_problema,id_equipo,lenguaje_programacion,valido,tiempo_resolucion_minutos) VALUES (%s,%s,%s,%s,%s,%s);")
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e


def  insert_competencia(values):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT INTO  competicion(code_competicion,descripcion,duracion_hrs,fecha,no_problemas,id_region) VALUES (%s,%s,%s,%s,%s,%s);",
        (values['IdComp'],'Desc',values['TiempoDur'],values['Fecha'],values['numproblems'],values['Region']))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e


def  insert_competecialocal(values):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT INTO  competicion_local(code_competicion,cve_universidad) VALUES (%s,%s);")
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e

def  insert_competeregional(values):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT ")
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e

def  insert_competeciamundial(values):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT INTO  final_mundial(id_final_mundial,code_competicion,fecha,ciudad) VALUES (%s,%s,%s,%s);",
        (values['IdFinalM'],values['Idcomp'],values['fechaR'],values['CiudadR']))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e


#DELETE


def  delete_juez(id_juez):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM juez WHERE id_juez = %s;",(id_juez))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e

def  delete_persona(id_persona):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM persona WHERE id_persona = %s;",(id_persona))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e


def  delete_tercia(id_persona):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM tercia WHERE id_juez = %s;",(id_persona))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e


def  delete_problema(id_problem):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM problema WHERE code_problema = %s;",(id_problem))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e


def  delete_equipo(id_equipo):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM equipo WHERE id_equipo = %s;",(id_equipo))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e


def  delete_universidad(id_univ):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM universidad WHERE cve_universidad = %s;",(id_univ))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e



def  delete_FinalMundial(idFinalM):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM final_mundial WHERE id_final_mundial = %s;",(idFinalM))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e


def  delete_competencia(id):
    try:
        conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM competicion WHERE code_competicion = %s;",(id))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e

#PAISES  
Countries = ["","Afghanistan","Albania","Algeria","Andorra","Angola","Antigua & Deps","Argentina","Armenia","Australia","Austria",
            "Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia",
            "Bosnia Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina","Burundi","Cambodia","Cameroon","Canada",
            "Cape Verde","Central African Rep","Chad","Chile","China","Colombia","Comoros","Congo","Congo {Democratic Rep}",
            "Costa Rica","Croatia","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic",
            "East Timor","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Fiji","Finland",
            "France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau",
            "Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland {Republic}","Israel",
            "Italy","Ivory Coast","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Korea North","Korea South",
            "Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania",
            "Luxembourg","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania",
            "Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar, {Burma}",
            "Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palau",
            "Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russian Federation","Rwanda",
            "St Kitts & Nevis","St Lucia","Saint Vincent & the Grenadines","Samoa","San Marino","Sao Tome & Principe","Saudi Arabia","Senegal",
            "Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Sudan",
            "Spain","Sri Lanka","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Togo",
            "Tonga","Trinidad & Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom",
            "United States","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]



#REGIONES
regions = ["Suroeste (SWERC)","Noroeste (NWERC)","Central (CERC)","Sureste (SEERC)","Noreste (NEERC)",
"África y Arabia (AARPC)","Sudáfrica (SAfrica)","Beijing","Coimbatore (Coim)","Kanpur (Kolkata)","Daca",
"Kaohsiun","Manila","Seúl","Teerán","Xian","Shanghái","Yokohama","Hanói","Pacífico sur (SPacific)",
"México y Centroamérica (CAmerica)","Caribe","Brasil","Suramérica Norte","Suramérica Sur","Pacific Northwest (PacNW)",
"North Central (NCNA)","East Central (ECNA)","Northeastern (NENA)","Rocky Mountain (RM)","Mid-Central (MCUSA)",
"Greater New York (GNY)","Southern California (Scal)","South Central (SCUSA)","Southeast USA (SEUSA)","Mid-Atlantic (MAUSA)",]


sg.theme('LightGreen')
#Este layout contiene los elementos del menu principal --
layout0 = [[sg.Image('logo.png',key='logo1')],[sg.Text('ICPC',auto_size_text=True,font='Helvetica')],
        [sg.Button('AÑADIR REGISTRO',auto_size_button=True),sg.Button('BORRAR REGISTRO',auto_size_button=True)]]
#----------------------------------------------------------------------------------------
#Este layout continene las opciones para añadir elementos a la base de Datos--
layout1 = [[sg.Button('<-', key='-returnl0L1-'),sg.Image('logo.png',key='logo2')],[sg.Text('AÑADIR UN REGISTRO A LA BASE DE DATOS',auto_size_text=True,font='Helvetica')],
        [sg.Button('Añadir Persona', key='-PButton-',auto_size_button=True)],
        [sg.Button('Añadir Tercia', key='-TerButton-',auto_size_button=True)],
        [sg.Button('Añadir Equipo',auto_size_button=True,key='-TButton-')],
        [sg.Button('Añadir Juez',auto_size_button=True,key='-JButton-')],
        [sg.Button('Añadir Competencia',auto_size_button=True,key='-CButton-')],
        [sg.Button('Añadir Universidad',auto_size_button=True,key='-UButton-')],
        [sg.Button('Añadir problema',auto_size_button=True,key='-ProblemButton-')],
        [sg.Button('Añadir Equipo Competencia',auto_size_button=True,key='-TeamCompButton-')],
        [sg.Button('Añadir Competencia Local',auto_size_button=True,key='-LocalComp-')],
        [sg.Button('Añadir Final Mundial',auto_size_button=True,key='-WorldFinalButton-')]] 
#----------------------------------------------------------------------------------------
#Este layout corresponde al registro de una persona
layout2 = [[sg.Button('<-', key='-returnl1L2-'), sg.Text('AÑADIR UNA NUEVA PERSONA A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Persona', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDPersonaL2-',size=(10,8))],
           [sg.Text('Nombre    ', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-Namepersona-',size=(30,30))],
           [sg.Text('Apellido P', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-ApellidoP-',size=(25,25)),
            sg.Text('Apellido M', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-ApellidoM-',size=(25,25))],
           [ sg.Text('Fecha de Nacimiento', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-FechaN-',size=(20,20)),sg.In(key='-CALL2-', enable_events=True, visible=False),
        sg.CalendarButton('Calendar', target='-CALL2-', pad=None, font=('MS Sans Serif', 10, 'bold'),button_color=('black', 'white'), key='_CALENDAR_', format=('%d %B, %Y'))],
            [sg.Text('Telefono    ', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-Telpersona-',size=(30,30))],
             [sg.Text('Correo Electronico    ', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-CorreoE-',size=(30,30))],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregPersona-')]]


#----------------------------------------------------------------------------------------
#Este layout corresponde al registro de una tercia
layout4 = [[sg.Button('<-', key='-returnl1L4-'), sg.Text('AÑADIR UNA NUEVA TERCIA A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Persona', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDPersonaL4-',size=(10,8))],
           [sg.Text('ID Equipo', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDEquipoL4-',size=(30,30))],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregTercia-')]]

#----------------------------------------------------------------------------------------
#Este layout corresponde al registro de un eqiupo
layout5 = [[sg.Button('<-', key='-returnl1L5-'), sg.Text('AÑADIR UN NUEVO EQUIPO A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Equipo', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDequipoL5-',size=(10,8))],
           [sg.Text('Nombre', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-Nameequipo-',size=(30,30))],
           [ sg.Text('Clave Universidad', font=('MS Sans Serif', 10, 'bold')), sg.Input(key='-claveUnivL5-',size=(30,30))],
           [ sg.Text('Estatus', font=('MS Sans Serif', 10, 'bold')), sg.Combo(['True','False'],key='-statusL5-',size=(30,30))],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregEquipo-')]]

#----------------------------------------------------------------------------------------
#Este layout corresponde al registro de un juez
layout6 = [[sg.Button('<-', key='-returnl1L6-'), sg.Text('AÑADIR UN NUEVO JUEZ A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Juez', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDJuezL6-',size=(10,8))],
           [sg.Text('ID Persona', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDpersonaL6-',size=(10,8))],           
           [sg.Text('Especializacion', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-especializacionL6-',size=(30,30))],
           [sg.Text('Puntuacion'),sg.Input(key='-puntuacionL6-',size=(30,30))],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregJuez-')]]

#----------------------------------------------------------------------------------------
#Este layout corresponde al registro de una competencia
layout7 = [[sg.Button('<-', key='-returnl1L7-'), sg.Text('AÑADIR UNA NUEVA COMPETENCIA A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Competicion', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDpruebaL7-',size=(10,8))],
           [sg.Text('Tiempo duracion', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-TiempoDuracion-',size=(30,30))],
           [sg.Text('Numero de Problemas', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-Numproblemas-',size=(30,30))],
           [ sg.Text('Fecha de realizacion', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-FechaRL7-',size=(20,20)),sg.In(key='-CALL7-', enable_events=True, visible=False),
        sg.CalendarButton('Calendar', target='-CALL7-', pad=None, font=('MS Sans Serif', 10, 'bold'),button_color=('black', 'white'), key='_CALENDARL7_', format=('%d %B, %Y'))],
           [ sg.Text('Region', font=('MS Sans Serif', 10, 'bold')), sg.Combo(regions,key='-RegionL7-',size=(30,30))],
            [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregCompetencia-')]]

#{IDpruebaL7,TiempoDuracion,Numproblemas,FechaRL7,RegionL7}
#----------------------------------------------------------------------------------------
#Este layout corresponde al registro de una Universidad
layout8 = [[sg.Button('<-', key='-returnl1L8-'), sg.Text('AÑADIR UNA NUEVA UNIVERSIDAD A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Universidad', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDUniversidadL8-',size=(10,8))],
           [sg.Text('Nombre', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-NombreUniver-',size=(30,30))],
           [ sg.Text('Region', font=('MS Sans Serif', 10, 'bold')), sg.Combo(regions,key='-RegionL8-',size=(30,30))],
            [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregUniversidad-')]]
#{IDUniversidadL8,NombreUniver,RegionL8}
#----------------------------------------------------------------------------------------
#Este layout corresponde al registro de un problema
layout9 = [[sg.Button('<-', key='-returnl1L9-'), sg.Text('AÑADIR UNA NUEVO PROBLEMA COMPETENCIA A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Problema', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDproblemaL9-',size=(10,8))],
           [sg.Text('Tipo', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-TipoL9-',size=(30,30))],
           [sg.Text('Descripcion', font=('MS Sans Serif', 10, 'bold'))],
           [sg.Multiline("",key='-DescProblem-',size=(50,8))],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregProblema-')]]
#{IDproblemaL9,TipoL9,Numproblemas,DescProblem}
#----------------------------------------------------------------------------------------
#Este layout corresponde al registro de un equipo para competencia
layout10 = [[sg.Button('<-', key='-returnl1L10-'), sg.Text('AÑADIR UNA NUEVO EQUIPO PARA COMPETENCIA A LA BASE DE DATOS',font='Helvetica')],
            [sg.Button('Competencia Local',auto_size_button=True,key='-AddregCompetencia-')],
            [sg.Button('Competencia Regional',auto_size_button=True,key='-AddregCompetencia-')],
            [sg.Button('Competencia Mundial',auto_size_button=True,key='-AddregCompetencia-')],
            [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregCompetencia-')]]


#----------------------------------------------------------------------------------------
#Este layout corresponde al registro de competencia local
layout11 = [[sg.Button('<-', key='-returnl1L11-'), sg.Text('AÑADIR UNA NUEVA COMPETENCIA LOCAL A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Competencia', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDCompML11-',size=(10,8))],
           [sg.Text('ID Universidad', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IduniverL11-',size=(30,30))],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregCompLocal-')]]




#----------------------------------------------------------------------------------------
#Este layout corresponde al registro de Final Mundial
layout12 = [[sg.Button('<-', key='-returnl1L12-'), sg.Text('AÑADIR UNA NUEVA FINAL MUNDIAL A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Final Mundial', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDUFinalML12-',size=(10,8))],
           [sg.Text('ID competencia', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IdCompetenciaL12-',size=(30,30))],
           [sg.Text('Ciudad', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-CiudadL12-',size=(30,30))],
           [ sg.Text('Fecha de realizacion', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-FechaRL12-',size=(20,20)),sg.In(key='-CALL12-', enable_events=True, visible=False),
        sg.CalendarButton('Calendar', target='-CALL12-', pad=None, font=('MS Sans Serif', 10, 'bold'),button_color=('black', 'white'), key='_CALENDARL12_', format=('%d %B, %Y'))],
            [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregFinalMundial-')]]

#{IDUFinalML12,IdCompetenciaL12,CiudadL11,FechaRL12}

#----------------------------------------------------------------------------------------
#Este layout continene las opciones para eliminar elementos a la base de Datos--
layout20 = [[sg.Button('<-', key='-returnl0L20-'),sg.Image('logo.png',key='logo2')],[sg.Text('BORRAR UN REGISTRO DE LA BASE DE DATOS',auto_size_text=True,font='Helvetica')],
        [sg.Button('Borrar registro Persona', key='-PButtonDelete-',auto_size_button=True)],
        [sg.Button('Borrar registro Tercia', key='-TerButtonDelete-',auto_size_button=True)],
        [sg.Button('Borrar registro Equipo',auto_size_button=True,key='-TButtonDelete-')],
        [sg.Button('Borrar registro Juez',auto_size_button=True,key='-JButtonDelete-')],

        [sg.Button('Borrar registro Competencia',auto_size_button=True,key='-CButtonDelete-')],
        [sg.Button('Borrar registro Universidad',auto_size_button=True,key='-UButtonDelete-')],
        [sg.Button('Borrar registro problema',auto_size_button=True,key='-ProblemButtonDelete-')],
        [sg.Button('Borrar registro Equipo Competencia',auto_size_button=True,key='-TeamCompButtonDelete-')],
        [sg.Button('Borrar registro Final Mundial',auto_size_button=True,key='-WorldFinalButtonDelete-')]] 

#Este layout corresponde al borrado de una persona
layout21 = [[sg.Button('<-', key='-returnl20L21-'), sg.Text('BORRAR UNA PERSONA DE LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Persona', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IdpersonaL21-',size=(10,8))],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeletePersona-')]]


#Este layout corresponde al borrado de una tercia
layout22 = [[sg.Button('<-', key='-returnl20L22-'), sg.Text('BORRAR UNA TERCIA DE LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Persona', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IdpersonaL22-',size=(10,8))],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeleteTercia-')]]


#Este layout corresponde al borrado de una Juez
layout23 = [[sg.Button('<-', key='-returnl20L23-'), sg.Text('BORRAR UN JUEZ DE LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Persona', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IdpersonaL23-',size=(10,8))],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeleteJuez-')]]


#Este layout corresponde al borrado de una Equipo
layout24 = [[sg.Button('<-', key='-returnl20L24-'), sg.Text('BORRAR UN EQUIPO DE LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Equipo', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IdequipoL24-',size=(10,8))],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeleteEquipo-')]]


#Este layout corresponde al borrado de una competencia
layout25 = [[sg.Button('<-', key='-returnl20L25-'), sg.Text('BORRAR UNA COMPETENCIA DE LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Competicion', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IdcomnpL25-',size=(10,8))],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeleteCompetencia-')]]


#Este layout corresponde al borrado de una universidad
layout26 = [[sg.Button('<-', key='-returnl20L26-'), sg.Text('BORRAR UNA UNIVERSIDAD DE LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Universidad', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IdunivL25-',size=(10,8))],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeleteUniversidad-')]]


#Este layout corresponde al borrado de un Problema 
layout27 = [[sg.Button('<-', key='-returnl20L27-'), sg.Text('BORRAR UN PROBLEMA DE LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Problema', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IdproblemL27-',size=(10,8))],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeleteProblema-')]]


#Este layout corresponde al borrado de una Final Mundial
layout28 = [[sg.Button('<-', key='-returnl20L28-'), sg.Text('BORRAR UN EQUIPO DE LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Final Mundial', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IdFinalML24-',size=(10,8))],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeleteFinalM-')]]


#----------------------------------------------------------------------------------------
#Layout principal 
layout = [[sg.Column(layout=layout0,key='-COL{0}-',visible=True),sg.Column(layout=layout1,key='-COL{1}-',visible=False),sg.Column(layout=layout2,key='-COL{2}-',visible=False),
        sg.Column(layout=layout4,key='-COL{4}-',visible=False),sg.Column(layout=layout5,key='-COL{5}-',visible=False),sg.Column(layout=layout6,key='-COL{6}-',visible=False),
        sg.Column(layout=layout7,key='-COL{7}-',visible=False),sg.Column(layout=layout8,key='-COL{8}-',visible=False),sg.Column(layout=layout9,key='-COL{9}-',visible=False),
        sg.Column(layout=layout10,key='-COL{10}-',visible=False),sg.Column(layout=layout11,key='-COL{11}-',visible=False),sg.Column(layout=layout12,key='-COL{12}-',visible=False),
        sg.Column(layout=layout20,key='-COL{20}-',visible=False), sg.Column(layout=layout21,key='-COL{21}-',visible=False),sg.Column(layout=layout22,key='-COL{22}-',visible=False),
        sg.Column(layout=layout23,key='-COL{23}-',visible=False),sg.Column(layout=layout24,key='-COL{24}-',visible=False),sg.Column(layout=layout25,key='-COL{25}-',visible=False),
        sg.Column(layout=layout26,key='-COL{26}-',visible=False),sg.Column(layout=layout27,key='-COL{27}-',visible=False),sg.Column(layout=layout28,key='-COL{28}-',visible=False),]]





window = sg.Window(title="ICPC DATA BASE ADMIN", layout=layout,auto_size_buttons=True,auto_size_text=True,resizable=True)

def is_num(value):
    """docstring for is_num"""
    val = True
    try:
        for i in value:
            if(i == '0' or i == '1' or i == '2' or i == '3' or
            i == '4' or  i == '5' or i == '6' or i == '7' or 
            i == '8' or  i == '9'): 
                continue
            else: 
                val = False
    except:
        return None
    return val


def CheckPersonaReg(values):
    """CheckPersona reg
    Args:
        values (map): contiene todos los valores del registro de una persona 
    Returns:
        bool: Retorna True si los datos cumplen las condiciones necesarias para agregarlos
    """
    flag = True
    k = 0
    if len(values['-IDPersonaL2-']) > 0 and is_num(values['-IDPersonaL2-']): 
        k += 1
    else:
        flag = False
        
    if len(values['-Namepersona-']) > 0 and len(values['-Namepersona-']) <= 30: 
        k += 1
    else :
        flag = False
        
    if len(values[ '-ApellidoP-']) > 0 and len(values['-ApellidoP-']) <= 30: 
        k += 1
    else :
        flag = False
        
    if len(values['-ApellidoM-']) > 0 and len(values['-ApellidoM-']) <= 30: 
        k += 1
    else :
        flag = False
        
    if len(values['-FechaN-']) > 0 and len(values['-FechaN-']) <= 30: 
        k += 1
    else :
        flag = False
        
        
    if len(values['-Telpersona-']) > 0 and len(values['-Telpersona-']) <= 10: 
        k += 1
    else :
        flag = False 
    
    if len(values['-Telpersona-']) > 0 and len(values['-Telpersona-']) <= 10: 
        k += 1
    else :
        flag = False 
        
    if len(values['-CorreoE-']) > 0 and len(values['-CorreoE-']) <= 20: 
        k += 1
    else :
        flag = False 
    
    if flag:
        return True
    else: 
        return False
    
   
def checkTerciaReg(values):
    flag = True
    k = 0
    
    if len(values['-IDPersonaL4-']) > 0 and is_num(values['-IDPersonaL4-']): 
        k += 1
    else:
        flag = False
    
    if len(values['-IDEquipoL4-']) > 0 and is_num(values['-IDEquipoL4-']): 
        k += 1
    else:
        flag = False
    
    if flag:
        return True
    else: 
        return False


def CheckEquipoReg(values):
    """CheckPersona reg
    Args:
        values (map): contiene todos los valores del registro de un equipo 
    Returns:
        bool: Retorna True si los datos cumplen las condiciones necesarias para agregarlos
    """
    flag = True
    k = 0
    if len(values['-IDequipoL5-']) > 0 and is_num(values['-IDequipoL5-']): 
        k += 1
    else:
        flag = False
        
    if len(values['-Nameequipo-']) > 0 and len(values['-Nameequipo-']) <= 30: 
        k += 1
    else :
        flag = False
        
    if len(values['-claveUnivL5-']) > 0 and len(values['-claveUnivL5-']) <= 3: 
        k += 1
    else :
        flag = False
        
    
        
    if flag:
        return True
    else: 
        return False
   
   
   
def CheckJuezReg(values):
    """CheckPersona reg
    Args:
        values (map): contiene todos los valores del registro de una persona 
    Returns:
        bool: Retorna True si los datos cumplen las condiciones necesarias para agregarlos
    """
    flag = True
    k = 0
    if len(values['-IDpersonaL6-']) > 0 and is_num(values['-IDpersonaL6-']): 
        k += 1
    else:
        flag = False
        
    if len(values['-IDJuezL6-']) > 0 and is_num(values['-IDJuezL6-']): 
        k += 1
    else :
        flag = False
        
    if len(values[ '-especializacionL6-']) > 0 and len(values['-especializacionL6-']) <= 100: 
        k += 1
    else :
        flag = False
        
    if flag:
        return True
    else: 
        return False
     

def CheckUniversidadReg(values):
    """CheckPersona reg
    Args:
        values (map): contiene todos los valores del registro de una persona 
    Returns:
        bool: Retorna True si los datos cumplen las condiciones necesarias para agregarlos
    """
    flag = True
    k = 0
    if len(values['-IDUniversidadL8-']) > 0 and len(values['-IDUniversidadL8-']) <= 3: 
        k += 1
    else:
        flag = False
        
    if len(values['-NombreUniver-']) > 0 and len(values['-NombreUniver-']) <= 50: 
        k += 1
    else :
        flag = False
        
    if len(values[ '-RegionL8-']) > 0 and is_num(values['-RegionL8-']): 
        k += 1
    else :
        flag = False
        
    if flag:
        return True
    else: 
        return False



def CheckCompetenciareg(values):
    """CheckPersona reg
    Args:
        values (map): contiene todos los valores del registro de una persona 
    Returns:
        bool: Retorna True si los datos cumplen las condiciones necesarias para agregarlos
    """
    flag = True
    k = 0
    if len(values['-IDpruebaL7-']) > 0 and is_num(values['-IDpruebaL7-']): 
        k += 1
    else:
        flag = False
        
    if len(values['-TiempoDuracion-']) > 0 and is_num(values['-TiempoDuracion-']): 
        k += 1
    else :
        flag = False
        
    if len(values[ '-Numproblemas-']) > 0 and is_num(values['-Numproblemas-']): 
        k += 1
    else :
        flag = False
        
    if len(values[ '-FechaRL7-']) > 0: 
        k += 1
    else :
        flag = False
    
    if len(values[ '-RegionL7-']) > 0: 
        k += 1
    else :
        flag = False

    if flag:
        return True
    else: 
        return False
    

def Checkproblemareg(values):
    """CheckPersona reg
    Args:
        values (map): contiene todos los valores del registro de una persona 
    Returns:
        bool: Retorna True si los datos cumplen las condiciones necesarias para agregarlos
    """
    flag = True
    k = 0
    if len(values['-IDproblemaL9-']) > 0 and len(values['-IDproblemaL9-']) < 4: 
        k += 1
    else:
        flag = False
        
    if len(values['-TipoL9-']) > 0 and len(values['-TipoL9-']) < 31: 
        k += 1
    else :
        flag = False
        
    if len(values[ '-DescProblem-']) > 0 and len(values[ '-DescProblem-']) < 101: 
        k += 1
    else :
        flag = False

    if flag:
        return True
    else: 
        return False
    


def CheckFinalMReg(values):
    """CheckPersona reg
    Args:
        values (map): contiene todos los valores del registro de una persona 
    Returns:
        bool: Retorna True si los datos cumplen las condiciones necesarias para agregarlos
    """
    flag = True
    k = 0
    if len(values['-IDUFinalML12-']) > 0 and is_num(values['-IDUFinalML12-']): 
        k += 1
    else:
        flag = False
        
    if len(values['-IdCompetenciaL12-']) > 0 and len(values['-IdCompetenciaL12-']) < 4: 
        k += 1
    else :
        flag = False
        
    if len(values['-CiudadL12-']) > 0 and len(values['-CiudadL12-']) < 51: 
        k += 1
    else :
        flag = False

    if len(values['-FechaRL12-']) > 0 : 
        k += 1
    else :
        flag = False

    if flag:
        return True
    else: 
        return False
    

#{IDUFinalML12,IdCompetenciaL12,CiudadL11,FechaRL12}




def date(d):
    x = []
    s = ''
    for i in d:
        if(i != ' ' and i != ','):
            s += i
        else:
            x.append(s),
            s = ''

    if(s != ''): 
        x.append(s)


    if(x[1] == 'January'):
        x[1] = 1
    if(x[1] == 'February'):
        x[1] = 2
    if(x[1] == 'March'):
        x[1] = 3
    if(x[1] == 'April'):
        x[1] = 4
    if(x[1] == 'May'):
        x[1] = 5
    if(x[1] == 'June'):
        x[1] = 6
    if(x[1] == 'July'):
        x[1] = 7
    if(x[1] == 'August'):
        x[1] = 8

    if(x[1] == 'September'):
        x[1] = 9

    if(x[1] == 'October'):
        x[1] = 10

    if(x[1] == 'November'):
        x[1] = 11
    if(x[1] == 'December'):
        x[1] = 12
    
    return (str(x[3])+'/'+str(x[1])+'/'+str(x[0]))

    

# Create an event loop
while True:
    event, values = window.read()#Captura los eventos y los valores de los elementos
    #Evento para cerrar el programa  
    if event == sg.WIN_CLOSED:
        break
    
    #print(event, values)
#-------------------Interfaces de añadir registros -----------------------------------------------------
    #este evento nos lleva a la interfaz de añadir registros
    if event == 'AÑADIR REGISTRO':
        window['-COL{1}-'].update(visible=True)
        window['-COL{0}-'].update(visible=False)
        
    #este evento nos lleva a la interfaz de añadir registro de una persona 
    if event == '-PButton-':
        window['-COL{2}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
    if event == '-CALL2-':
        #print()
        window.Element('-FechaN-').update(value=date(values['-CALL2-']))
    
    if event == '-AddregPersona-' and CheckPersonaReg(values) == True:  
        values_reg = values  
        reg_persona = {'Id' : values['-IDPersonaL2-'],'Nombre' : values['-Namepersona-'], 'ApellidoP' : values['-ApellidoP-'],'ApellidoM' : values['-ApellidoM-'],
                       'FechaN' : values['-FechaN-'],'Telefono': values['-Telpersona-'],'CorreoE' : values['-CorreoE-']}
        insert_persona(reg_persona)
        print(reg_persona)
        window.Element('-IDPersonaL2-').update(value="")
        window.Element('-Namepersona-').update(value="")
        window.Element('-ApellidoP-').update(value="")
        window.Element('-ApellidoM-').update(value="")
        window.Element('-FechaN-').update(value="")
        window.Element('-Telpersona-').update(value="")
        window.Element('-CorreoE-').update(value="")
    elif CheckPersonaReg(values) == False and event == '-AddregPersona-':
        print("Error al crear el registro")
        
 #----------------------------------------------------------------------------------------       
    #este evento nos lleva a la interfaz de añadir registro de una Tercia
    if event == '-TerButton-':
        window['-COL{4}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)

    if event == '-AddregTercia-' and checkTerciaReg(values) == True:  
        values_reg = values  
        reg_tercia = {'IdPersona' : values['-IDPersonaL4-'],'idEqupol4' : values['-IDEquipoL4-'] }
        insert_Tercia(reg_tercia)
        print(reg_tercia)
        window.Element('-IDPersonaL4-').update(value="")
        window.Element('-IDEquipoL4-').update(value="")
        
    elif checkTerciaReg(values) == False and event == '-AddregTercia-':
        print("Error al crear el registro")
        
#----------------------------------------------------------------------------------------    
    #este evento nos lleva a la interfaz de añadir registro de un equipo
    if event == '-TButton-':
        window['-COL{5}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)

    if event == '-AddregEquipo-' and CheckEquipoReg(values) == True:  
        #{'-IDequipoL5-','-Nameequipo-','-claveUnivL5-','-statusL5-'}
        values_reg = values  
        reg_equipo = {'Idequipo' : values['-IDequipoL5-'],'NombreEquipo' : values['-Nameequipo-'], 'claveUniver' : values['-claveUnivL5-'],'estatus' : values['-statusL5-']}
        insert_equipo(reg_equipo)
        print(reg_equipo)
        window.Element('-IDequipoL5-').update(value="")
        window.Element('-Nameequipo-').update(value="")
        window.Element('-claveUnivL5-').update(value="")
        window.Element('-statusL5-').update(value="")

    elif CheckEquipoReg(values) == False and event == '-AddregEquipo-':
        print("Error al crear el registro")
#----------------------------------------------------------------------------------------       
    #este evento nos lleva a la interfaz de añadir registro de un juez
    if event == '-JButton-':
        window['-COL{6}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
    if event == '-AddregJuez-' and CheckJuezReg(values) == True:
        #{IDJuezL6,IDpersonaL6,especializacionL6,puntuacionL6} 
        values_reg = values  
        reg_juez = {'IdJuez' : values['-IDJuezL6-'],'idpersona' : values['-IDpersonaL6-'], 'especiaslizacion' : values['-especializacionL6-'],'puntuacion' : values['-puntuacionL6-']}
        insert_juez(reg_juez)
        print(reg_juez)
        window.Element('-IDJuezL6-').update(value="")
        window.Element('-IDpersonaL6-').update(value="")
        window.Element('-especializacionL6-').update(value="")
        window.Element('-puntuacionL6-').update(value="")
    elif CheckJuezReg(values) == False and event == '-AddregJuez-':
        print("Error al crear el registro")
#----------------------------------------------------------------------------------------   
    #este evento nos lleva a la interfaz de añadir registro de una competencia
    if event == '-CButton-':
        window['-COL{7}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
    if event == '-CALL7-':
        #print()
        window.Element('-FechaRL7-').update(value=date(values['-CALL7-']))
    
    if event == '-AddregCompetencia-' and CheckCompetenciareg(values) == True:  
        values_reg = values 
        #{IDpruebaL7,TiempoDuracion,Numproblemas,FechaRL7,RegionL7}
        reg_comp = {'IdComp' : values['-IDpruebaL7-'],'TiempoDur' : values['-TiempoDuracion-'], 'numproblems' : values['-Numproblemas'],'Fecha' : values['-FechaRL7-'],
                       'Region' : values['-RegionL7-']}
        insert_competencia(reg_comp)
        print(reg_comp)
        window.Element('-IDpruebaL7-').update(value="")
        window.Element('-TiempoDuracion-').update(value="")
        window.Element('-Numproblemas-').update(value="")
        window.Element('-FechaRL7-').update(value="")
        window.find_element('-RegionL7-').update(value="")
    elif CheckCompetenciareg(values) == False and event == '-AddregPersona-':
        print("Error al crear el registro")
#----------------------------------------------------------------------------------------       
    #este evento nos lleva a la interfaz de añadir registro de una universidad
    if event == '-UButton-':
        window['-COL{8}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
    if event == '-AddregUniversidad-' and CheckUniversidadReg(values) == True:
        #{IDUniversidadL8,NombreUniver,RegionL8}  
        values_reg = values  
        reg_universidad = {'IdUniver' : values['-IDUniversidadL8-'],'Nombre' : values['-NombreUniver-'], 'region' : values['-RegionL8-']}
        insert_Universidad(reg_universidad)
        print(reg_universidad)
        window.Element('-IDUniversidadL8-').update(value="")
        window.Element('-NombreUniver-').update(value="")
        window.find_element('-RegionL8-').update(value="")
    elif CheckUniversidadReg(values) == False and event == '-AddregUniversidad-':
        print("Error al crear el registro")
#----------------------------------------------------------------------------------------    
     #este evento nos lleva a la interfaz de añadir registro de un problema
    if event == '-ProblemButton-':
        window['-COL{9}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
    if event == '-AddregProblema-' and Checkproblemareg(values) == True: 
        #{IDproblemaL9,TipoL9,Numproblemas,DescProblem}
        values_reg = values  
        reg_problem = {'IdProblem' : values['-IDproblemaL9-'],'Desc' : values['-DescProblem-'], 'Tipo' : values['-TipoL9-']}
        insert_problema(reg_problem)
        print(reg_problem)
        window.Element('-IDproblemaL9-').update(value="")
        window.Element('-TipoL9-').update(value="")
        window.Element('-DescProblem-').update(value="")
    elif Checkproblemareg(values) == False and event == '-AddregProblema-':
        print("Error al crear el registro")
#----------------------------------------------------------------------------------------    
     #este evento nos lleva a la interfaz de añadir registro de un  Equipo para una competencia(local , regional o mundial)
    if event == '-TeamCompButton-':
        window['-COL{10}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)

    
#----------------------------------------------------------------------------------------
     #este evento nos lleva a la interfaz de añadir registro de una competencia local
    if event == '-LocalComp-':
        window['-COL{11}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
#----------------------------------------------------------------------------------------
     #este evento nos lleva a la interfaz de añadir registro de una Final mundial
    if event == '-WorldFinalButton-':
        window['-COL{12}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
    if event == '-CALL12-':
        #print()
        window.Element('-FechaRL12-').update(value=date(values['-CALL12-']))
    
    if event == '-AddregFinalMundial-' and CheckFinalMReg(values) == True:  
        #{IDUFinalML12,IdCompetenciaL12,CiudadL11,FechaRL12}
        values_reg = values  
        reg_finalM = {'IdFinalM' : values['-IDUFinalML12-'],'Idcomp' : values['-IdCompetenciaL12-'], 'CiudadR' : values['-CiudadL12-'],'fechaR' : values['-FechaRL12-']}
        #insert_competeciamundial(reg_finalM)
        print(reg_finalM)
        window.Element('-IDUFinalML12-').update(value="")
        window.Element('-IdCompetenciaL12-').update(value="")
        window.Element('-CiudadL12-').update(value="")
        window.Element('-FechaRL12-').update(value="")
        
    elif CheckFinalMReg(values) == False and event == '-AddregFinalMundial-':
        print("Error al crear el registro")
    
#----------------------------------------------------------------------------------------
    #este evento nos lleva a la interfaz de borrar registros
    if event == 'BORRAR REGISTRO':
        window['-COL{20}-'].update(visible=True)
        window['-COL{0}-'].update(visible=False)

#----------------------------------------------------------------------------------------
    if event == '-PButtonDelete-':
        window['-COL{21}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)
        
    if event == '-DeletePersona-' and len(values['-IdpersonaL21-']) > 0 :
        delete_persona(values['-IdpersonaL21-'])
        window['-IdpersonaL21-'].update(value="")
    else:
        print("Error al borrar registro")
        

#----------------------------------------------------------------------------------------
    if event == '-TerButtonDelete-':
        window['-COL{22}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)
        
    if event == '-DeleteTercia-' and len(values['-IdpersonaL22-']) > 0 :
        delete_tercia(values['-IdpersonaL22-'])
        window['-IdpersonaL22-'].update(value="")
    else:
        print("Error al borrar registro")


 #----------------------------------------------------------------------------------------       
    if event == '-TButtonDelete-':
        window['-COL{24}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)
        
    if event == '-DeleteEquipo-' and len(values['-IdequipoL24-']) > 0 :
        delete_equipo(values['-IdequipoL24-'])
        window['-IdequipoL24-'].update(value="")
    else:
        print("Error al borrar registro")


#----------------------------------------------------------------------------------------    
    if event == '-JButtonDelete-':
        window['-COL{23}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)

    if event == '-DeleteJuez-' and len(values['-IdpersonaL23-']) > 0 :
        delete_juez(values['-IdpersonaL23-'])
        window['-IdpersonaL23-'].update(value="")
    else:
        print("Error al borrar registro")

#----------------------------------------------------------------------------------------
    if event == '-CButtonDelete-':
        window['-COL{25}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)
        
        
    if event == '-DeleteCompetencia-' and len(values['-IdcomnpL25-']) > 0 :
        delete_competencia(values['-IdcomnpL25-'])
        window['-IdcomnpL25-'].update(value="")
    else:
        print("Error al borrar registro")


#----------------------------------------------------------------------------------------
    if event == '-UButtonDelete-':
        window['-COL{26}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)
        

    if event == '-DeleteUniversidad-' and len(values['-IdunivL25-']) > 0 :
        delete_universidad(values['-IdunivL25-'])
        window['-IdunivL25-'].update(value="")
    else:
        print("Error al borrar registro")


#----------------------------------------------------------------------------------------
    if event == '-ProblemButtonDelete-':
        window['-COL{27}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)
        
    if event == '-DeleteProblema-' and len(values['-IdproblemL27-']) > 0 :
        delete_problema(values['-IdproblemL27-'])
        window['-IdproblemL27-'].update(value="")
    else:
        print("Error al borrar registro")
 #----------------------------------------------------------------------------------------   
    if event == '-WorldFinalButtonDelete-':
        window['-COL{28}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)
        
    if event == '-DeleteFinalM-' and len(values['-IdFinalML24-']) > 0 :
        delete_FinalMundial(values['-IdFinalML24-'])
        window['-IdFinalML24-'].update(value="")
    else:
        print("Error al borrar registro")
    
    
    
    
    
#----------------------------------------------------------------------------------------    
    #Este evento nos regresa a la interfaz principal de añadir registros
    if event == '-returnl0L1-' and window['-COL{1}-'].visible == True:
        window['-COL{1}-'].update(visible=False)
        window['-COL{0}-'].update(visible=True)
        
#----------------------------------------------------------------------------------------       
    #Este evento nos regresa a la interfaz principal de añadir registros
    if event == '-returnl0L20-' and window['-COL{20}-'].visible == True:
        window['-COL{20}-'].update(visible=False)
        window['-COL{0}-'].update(visible=True)
        
    
    
    #Este evento nos regresa a la interfaz principal de añadir registros
    if event == '-returnl1L2-' and window['-COL{2}-'].visible == True:
        window['-COL{2}-'].update(visible=False)
        window['-COL{1}-'].update(visible=True)
        
    
    #Este evento nos regresa a la interfaz principal de añadir registros  
    if event == '-returnl1L4-' and window['-COL{4}-'].visible == True:
        window['-COL{4}-'].update(visible=False)
        window['-COL{1}-'].update(visible=True)
     
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl1L5-' and window['-COL{5}-'].visible == True:
        window['-COL{5}-'].update(visible=False)
        window['-COL{1}-'].update(visible=True)
    
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl1L6-' and window['-COL{6}-'].visible == True:
        window['-COL{6}-'].update(visible=False)
        window['-COL{1}-'].update(visible=True)
        
    
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl1L7-' and window['-COL{7}-'].visible == True:
        window['-COL{7}-'].update(visible=False)
        window['-COL{1}-'].update(visible=True)
    
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl1L8-' and window['-COL{8}-'].visible == True:
        window['-COL{8}-'].update(visible=False)
        window['-COL{1}-'].update(visible=True)
    
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl1L9-' and window['-COL{9}-'].visible == True:
        window['-COL{9}-'].update(visible=False)
        window['-COL{1}-'].update(visible=True)
    
    
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl1L10-' and window['-COL{10}-'].visible == True:
        window['-COL{10}-'].update(visible=False)
        window['-COL{1}-'].update(visible=True)
        
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl1L11-' and window['-COL{11}-'].visible == True:
        window['-COL{11}-'].update(visible=False)
        window['-COL{1}-'].update(visible=True)


    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl1L12-' and window['-COL{12}-'].visible == True:
        window['-COL{12}-'].update(visible=False)
        window['-COL{1}-'].update(visible=True)


    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl20L21-' and window['-COL{21}-'].visible == True:
        window['-COL{21}-'].update(visible=False)
        window['-COL{20}-'].update(visible=True)

        #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl20L22-' and window['-COL{22}-'].visible == True:
        window['-COL{22}-'].update(visible=False)
        window['-COL{20}-'].update(visible=True)

    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl20L23-' and window['-COL{23}-'].visible == True:
        window['-COL{23}-'].update(visible=False)
        window['-COL{20}-'].update(visible=True)

    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl20L24-' and window['-COL{24}-'].visible == True:
        window['-COL{24}-'].update(visible=False)
        window['-COL{20}-'].update(visible=True)

    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl20L25-' and window['-COL{25}-'].visible == True:
        window['-COL{25}-'].update(visible=False)
        window['-COL{20}-'].update(visible=True)


    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl20L26-' and window['-COL{26}-'].visible == True:
        window['-COL{26}-'].update(visible=False)
        window['-COL{20}-'].update(visible=True)


    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl20L27-' and window['-COL{27}-'].visible == True:
        window['-COL{27}-'].update(visible=False)
        window['-COL{20}-'].update(visible=True)


    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl20L28-' and window['-COL{28}-'].visible == True:
        window['-COL{28}-'].update(visible=False)
        window['-COL{20}-'].update(visible=True)
        
        

    
    
        

    
    
window.close() #Cerramos la ventana



# C:\Users\sergi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\pyinstaller.exe

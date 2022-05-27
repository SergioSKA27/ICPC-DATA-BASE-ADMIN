#!/usr/bin/python
import PySimpleGUI as sg
import psycopg2 as pgdb
conexion = pgdb.connect(host="localhost",database="ProyectoFinal", user="postgres", password="AlmaDeli159")#conectamos la base de datos 

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

sg.theme('LightGreen')
#Este layout contiene los elementos del menu principal --
layout0 = [[sg.Image('logo.png',key='logo1')],[sg.Text('ICPC',auto_size_text=True,font='Helvetica')],
        [sg.Button('AÑADIR REGISTRO',auto_size_button=True),sg.Button('BORRAR REGISTRO',auto_size_button=True)]]

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
        [sg.Button('Añadir Final Mundial',auto_size_button=True,key='-WorldFinalButton-')],
        ] 

#Este layout corresponde al registro de una persona
layout2 = [[sg.Button('<-', key='-returnl1L2-'), sg.Text('AÑADIR UNA NUEVA PERSONA A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Persona', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDPersonaL2-',size=(10,8))],
           [sg.Text('Nombre    ', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-Namepersona-',size=(30,30))],
           [sg.Text('Apellido P', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-ApellidoP-',size=(25,25)),
            sg.Text('Apellido M', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-ApellidoM-',size=(25,25))],
           [ sg.Text('Fecha de Nacimiento', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-FechaN-',size=(20,20)),sg.In(key='-CALL2-', enable_events=True, visible=False),
        sg.CalendarButton('Calendar', target='-CALL2-', pad=None, font=('MS Sans Serif', 10, 'bold'),button_color=('black', 'white'), key='_CALENDAR_', format=('%d %B, %Y'))],
           [ sg.Text('Pais', font=('MS Sans Serif', 10, 'bold')), sg.Combo(Countries,key='-ContryP-',default_value="")],
            [sg.Text('Telefono    ', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-Telpersona-',size=(30,30))],
             [sg.Text('Correo Electronico    ', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-CorreoE-',size=(30,30))],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregPersona-')]]



#Este layout corresponde al registro de una tercia
layout4 = [[sg.Button('<-', key='-returnl1L4-'), sg.Text('AÑADIR UNA NUEVA TERCIA A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Persona', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDPersonaL4-',size=(10,8))],
           [sg.Text('ID Equipo', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDEquipoL4-',size=(30,30))],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregTercia-')]]


#Este layout corresponde al registro de un eqiupo
layout5 = [[sg.Button('<-', key='-returnl1L5-'), sg.Text('AÑADIR UN NUEVO EQUIPO A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Equipo', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDequipoL5-',size=(10,8))],
           [sg.Text('Nombre', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-Nameequipo-',size=(30,30))],
           [ sg.Text('Clave Universidad', font=('MS Sans Serif', 10, 'bold')), sg.Input(key='-claveUnivL5-',size=(30,30))],
           [ sg.Text('Estatus', font=('MS Sans Serif', 10, 'bold')), sg.Combo(['True','False'],key='-statusL5-',size=(30,30))],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregEquipo-')]]

#Este layout corresponde al registro de un juez
layout6 = [[sg.Button('<-', key='-returnl1L6-'), sg.Text('AÑADIR UN NUEVO JUEZ A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Juez', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDJuezL6-',size=(10,8))],
           [sg.Text('ID Persona', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDpersonaL6-',size=(10,8))],           
           [sg.Text('Especializacion', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-especializacionL6-',size=(30,30))],
           [sg.Text('Puntuacion'),sg.Input(key='-puntuacionL6-',size=(30,30))],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregJuez-')]]


#Este layout corresponde al registro de una competencia
layout7 = [[sg.Button('<-', key='-returnl1L7-'), sg.Text('AÑADIR UNA NUEVA COMPETENCIA A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Competicion', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDpruebaL7-',size=(10,8))],
           [sg.Text('Tiempo duracion', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-TiempoDuracion-',size=(30,30))],
           [sg.Text('Numero de Problemas', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-Numproblemas-',size=(30,30))],
           [ sg.Text('Fecha de realizacion', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-FechaR-',size=(20,20)),sg.In(key='-CALL7-', enable_events=True, visible=False),
        sg.CalendarButton('Calendar', target='-CALL7-', pad=None, font=('MS Sans Serif', 10, 'bold'),button_color=('black', 'white'), key='_CALENDARL7_', format=('%d %B, %Y'))],
           [ sg.Text('Region', font=('MS Sans Serif', 10, 'bold')), sg.Combo([' Suroeste (SWERC)','Noroeste (NWERC)'],key='-statusL5-',size=(30,30))],
            [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregCompetencia-')]]


#Este layout corresponde al registro de una Universidad
layout8 = [[sg.Button('<-', key='-returnl1L8-'), sg.Text('AÑADIR UNA NUEVA UNIVERSIDAD A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Universidad', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDUniversidadL8-',size=(10,8))],
           [sg.Text('Nombre', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-NombreUniver-',size=(30,30))],
           [ sg.Text('Region', font=('MS Sans Serif', 10, 'bold')), sg.Combo([' Suroeste (SWERC)','Noroeste (NWERC)'],key='-statusL5-',size=(30,30))],
            [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregUniversidad-')]]

#Este layout corresponde al registro de un problema
layout9 = [[sg.Button('<-', key='-returnl1L9-'), sg.Text('AÑADIR UNA NUEVO PROBLEMA COMPETENCIA A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Problema', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDproblemaL9-',size=(10,8))],
           [sg.Text('Tipo', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-TipoL9-',size=(30,30))],
           [sg.Text('Descripcion', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-Numproblemas-',size=(30,30))],
           [sg.Multiline("",key='-DescProblem-',size=(50,8))],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregProblema-')]]


#Este layout corresponde al registro de un equipo para competencia
layout10 = [[sg.Button('<-', key='-returnl1L10-'), sg.Text('AÑADIR UNA NUEVO EQUIPO PARA COMPETENCIA A LA BASE DE DATOS',font='Helvetica')],
            [sg.Button('Competencia Local',auto_size_button=True,key='-AddregCompetencia-')],
            [sg.Button('Competencia Regional',auto_size_button=True,key='-AddregCompetencia-')],
            [sg.Button('Competencia Mundial',auto_size_button=True,key='-AddregCompetencia-')],
            [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregCompetencia-')]]

#Este layout corresponde al registro de Final Mundial
layout11 = [[sg.Button('<-', key='-returnl1L11-'), sg.Text('AÑADIR UNA NUEVA FINAL MUNDIAL A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Final Mundial', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDUFinalML11-',size=(10,8))],
           [sg.Text('ID competencia', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IdCompetenciaL11-',size=(30,30))],
           [sg.Text('Ciudad', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-CiudadL11-',size=(30,30))],
        [ sg.Text('Fecha de realizacion', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-FechaRL11-',size=(20,20)),sg.In(key='-CALL11-', enable_events=True, visible=False),
        sg.CalendarButton('Calendar', target='-CALL11-', pad=None, font=('MS Sans Serif', 10, 'bold'),button_color=('black', 'white'), key='_CALENDARL11_', format=('%d %B, %Y'))],
            [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregUniversidad-')]]


#Este layout continene las opciones para eliminar elementos a la base de Datos--
layout12 = [[sg.Button('<-', key='-returnl0L12-'),sg.Image('logo.png',key='logo2')],[sg.Text('BORRAR UN REGISTRO DE LA BASE DE DATOS',auto_size_text=True,font='Helvetica')],
        [sg.Button('Borrar registro Persona', key='-PButtonDelete-',auto_size_button=True)],
        [sg.Button('Borrar registro Tercia', key='-TerButtonDelete-',auto_size_button=True)],
        [sg.Button('Borrar registro Equipo',auto_size_button=True,key='-TButtonDelete-')],
        [sg.Button('Borrar registro Juez',auto_size_button=True,key='-JButtonDelete-')],
        [sg.Button('Borrar registro Competencia',auto_size_button=True,key='-CButtonDelete-')],
        [sg.Button('Borrar registro Universidad',auto_size_button=True,key='-UButtonDelete-')],
        [sg.Button('Borrar registro problema',auto_size_button=True,key='-ProblemButtonDelete-')],
        [sg.Button('Borrar registro Equipo Competencia',auto_size_button=True,key='-TeamCompButtonDelete-')],
        [sg.Button('Borrar registro Final Mundial',auto_size_button=True,key='-WorldFinalButtonDelete-')]] 



#Layout principal 
layout = [[sg.Column(layout=layout0,key='-COL{0}-',visible=True),sg.Column(layout=layout1,key='-COL{1}-',visible=False),sg.Column(layout=layout2,key='-COL{2}-',visible=False),
        sg.Column(layout=layout4,key='-COL{4}-',visible=False),sg.Column(layout=layout5,key='-COL{5}-',visible=False),sg.Column(layout=layout6,key='-COL{6}-',visible=False),
        sg.Column(layout=layout7,key='-COL{7}-',visible=False),sg.Column(layout=layout8,key='-COL{8}-',visible=False),sg.Column(layout=layout9,key='-COL{9}-',visible=False),
        sg.Column(layout=layout10,key='-COL{10}-',visible=False),sg.Column(layout=layout11,key='-COL{11}-',visible=False),sg.Column(layout=layout12,key='-COL{12}-',visible=False)]]





window = sg.Window(title="ICPC DATA BASE ADMIN", layout=layout,auto_size_buttons=True,auto_size_text=True,resizable=True)


def CheckPersonaReg(values):
    """CheckPersona reg

    Args:
        values (map): contiene todos los valores del registro de una persona 

    Returns:
        bool: Retorna True si los datos cumplen las condiciones necesarias para agregarlos
    """
    flag = True
    k = 0
    if len(values['-IDPersonaL2-']) > 0 and len(values['-IDPersonaL2-']) <= 8: 
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
    
    if len(values['-ContryP-']) > 0:
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
    
    if len(values['-IDPersonaL4-']) > 0 and len(values['-IDPersonaL4-']) <= 8: 
        k += 1
    else:
        flag = False
    
    if len(values['-IDEquipoL4-']) > 0 and len(values['-IDEquipoL4-']) <= 8: 
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
    if len(values['-IDequipoL5-']) > 0 and len(values['-IDequipoL5-']) <= 8: 
        k += 1
    else:
        flag = False
        
    if len(values['-Nameequipo-']) > 0 and len(values['-Nameequipo-']) <= 20: 
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
    if len(values['-IDpersonaL6-']) > 0 and len(values['-IDpersonaL6-']) <= 8: 
        k += 1
    else:
        flag = False
        
    if len(values['-IDJuezL6-']) > 0 and len(values['-IDJuezL6-']) <= 30: 
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
     

def CheckPersonaReg(values):
    """CheckPersona reg

    Args:
        values (map): contiene todos los valores del registro de una persona 

    Returns:
        bool: Retorna True si los datos cumplen las condiciones necesarias para agregarlos
    """
    flag = True
    k = 0
    if len(values['-IDPersonaL2-']) > 0 and len(values['-IDPersonaL2-']) <= 8: 
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
    
    if len(values['-ContryP-']) > 0:
        k += 1
    else :
        flag = False
        
    if flag:
        return True
    else: 
        return False
    
    

# Create an event loop
while True:
    event, values = window.read()#Captura los eventos y los valores de los elementos
    #Evento para cerrar el programa  
    if event == sg.WIN_CLOSED:
        break
    
    print(event, values)
    #este evento nos lleva a la interfaz de añadir registros
    if event == 'AÑADIR REGISTRO':
        window['-COL{1}-'].update(visible=True)
        window['-COL{0}-'].update(visible=False)
        
    #este evento nos lleva a la interfaz de añadir registro de una persona 
    if event == '-PButton-':
        window['-COL{2}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
    if event == '-CALL2-':
        #print(values['-CALL2-'])
        window.Element('-FechaN-').update(value=values['-CALL2-'])
    
    if event == '-AddregPersona-' and CheckPersonaReg(values) == True:  
        values_reg = values  
        reg_persona = {'Id' : values['-IDPersonaL2-'],'Nombre' : values['-Namepersona-'], 'ApellidoP' : values['-ApellidoP-'],'ApellidoM' : values['-ApellidoM-'],
                       'FechaN' : values['-FechaN-'],'Telefono': values['-Telpersona-'],'CorreoE' : values['-CorreoE-']}
        print(reg_persona)
        window.Element('-IDPersonaL2-').update(value="")
        window.Element('-Namepersona-').update(value="")
        window.Element('-ApellidoP-').update(value="")
        window.Element('-ApellidoM-').update(value="")
        window.Element('-FechaN-').update(value="")
        window.Element('-Telpersona-').update(value="")
        window.Element('-CorreoE-').update(value="")
        window.find_element('-ContryP-').update(value="")
    elif CheckPersonaReg(values) == False and event == '-AddregPersona-':
        print("Bad")
        
        
    #este evento nos lleva a la interfaz de añadir registro de una Tercia
    if event == '-TerButton-':
        window['-COL{4}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
    #este evento nos lleva a la interfaz de añadir registro de un equipo
    if event == '-TButton-':
        window['-COL{5}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
        
    #este evento nos lleva a la interfaz de añadir registro de un juez
    if event == '-JButton-':
        window['-COL{6}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
    #este evento nos lleva a la interfaz de añadir registro de una competencia
    if event == '-CButton-':
        window['-COL{7}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
        
    #este evento nos lleva a la interfaz de añadir registro de una competencia
    if event == '-UButton-':
        window['-COL{8}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
     #este evento nos lleva a la interfaz de añadir registro de una competencia
    if event == '-ProblemButton-':
        window['-COL{9}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
     #este evento nos lleva a la interfaz de añadir registro de un  Equipo para una competencia(local , regional o mundial)
    if event == '-TeamCompButton-':
        window['-COL{10}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
     #este evento nos lleva a la interfaz de añadir registro de una Final mundial
    if event == '-WorldFinalButton-':
        window['-COL{11}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
    #este evento nos lleva a la interfaz de borrar registros
    if event == 'BORRAR REGISTRO':
        window['-COL{12}-'].update(visible=True)
        window['-COL{0}-'].update(visible=False)
    
    
    
    
    
    
    #Este evento nos regresa a la interfaz principal de añadir registros
    if event == '-returnl0L1-' and window['-COL{1}-'].visible == True:
        window['-COL{1}-'].update(visible=False)
        window['-COL{0}-'].update(visible=True)
        
        
    #Este evento nos regresa a la interfaz principal de añadir registros
    if event == '-returnl0L12-' and window['-COL{12}-'].visible == True:
        window['-COL{12}-'].update(visible=False)
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
        
        

    
    
        

    
    
window.close() #Cerramos la ventana



# C:\Users\sergi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\pyinstaller.exe  
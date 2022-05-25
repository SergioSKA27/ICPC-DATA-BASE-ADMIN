#!/usr/bin/python
import PySimpleGUI as sg
#conexion = pgdb.connect(host="localhost",database=)

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
layout1 = [[sg.Image('logo.png',key='logo2')],[sg.Text('AÑADIR UN REGISTRO A LA BASE DE DATOS',auto_size_text=True,font='Helvetica')],
        [sg.Button('Añadir Persona', key='-PButton-',auto_size_button=True)],
        [sg.Button('Añadir Participante', key='-ParButton-',auto_size_button=True)],
        [sg.Button('Añadir Tercia', key='-TerButton-',auto_size_button=True)],
        [sg.Button('Añadir Equipo',auto_size_button=True,key='-TButton-')],
        [sg.Button('Añadir Juez',auto_size_button=True,key='-JButton-')],
        [sg.Button('Añadir Competencia',auto_size_button=True,key='-CButton-')],
        [sg.Button('Añadir Patrocinador', key='-PatButton-',auto_size_button=True)]] 

#Este layout corresponde al registro de una persona
layout2 = [[sg.Button('<-', key='-returnl1L2-'), sg.Text('AÑADIR UNA NUEVA PERSONA A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Persona', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDPersonaL2-',size=(10,8))],
           [sg.Text('Nombre    ', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-Namepersona-',size=(30,30))],
           [sg.Text('Apellido P', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-ApellidoP-',size=(25,25)),
            sg.Text('Apellido M', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-ApellidoM-',size=(25,25))],
           [ sg.Text('Fecha de Nacimiento', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-FechaN-',size=(20,20)),sg.In(key='-CALL2-', enable_events=True, visible=False),
        sg.CalendarButton('Calendar', target='-CALL2-', pad=None, font=('MS Sans Serif', 10, 'bold'),button_color=('black', 'white'), key='_CALENDAR_', format=('%d %B, %Y'))],
           [ sg.Text('Pais', font=('MS Sans Serif', 10, 'bold')), sg.Combo(Countries,key='-ContryP-',default_value="")],[sg.Button('Añadir Registro',auto_size_button=True,key='-AddregPersona-')]]

#Este layout corresponde al registro de un participante
layout3 = [[sg.Button('<-', key='-returnl1L3-'), sg.Text('AÑADIR UN NUEVO PARTICIPANTE A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Persona', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDPersonaL3-',size=(10,8))],
           [sg.Text('Tercia ID ', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDterciaL3-',size=(30,30))],
           [sg.Text('Paradigma Dominante', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-ParadigmaD-',size=(25,25))],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregParticipant-')]]

#Este layout corresponde al registro de una tercia
layout4 = [[sg.Button('<-', key='-returnl1L4-'), sg.Text('AÑADIR UNA NUEVA TERCIA A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Trecia', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDTerciaL4-',size=(10,8))],
           [sg.Text('ID Participante 1', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDPart1-',size=(30,30))],
           [sg.Text('ID Participante 2', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDPart2-',size=(30,30))],
           [sg.Text('ID Participante 3', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDPart3-',size=(30,30))],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregTercia-')]]


#Este layout corresponde al registro de un eqiupo
layout5 = [[sg.Button('<-', key='-returnl1L5-'), sg.Text('AÑADIR UN NUEVO EQUIPO A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Equipo', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDequipoL5-',size=(10,8))],
           [sg.Text('ID Tercia', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-Namepersona-',size=(30,30))],
           [ sg.Text('Pais', font=('MS Sans Serif', 10, 'bold')), sg.Combo(Countries,key='-Contry-')],
           [sg.Text('Comentario Especial',)],[sg.Multiline('',autoscroll=True,enter_submits=True,size=(20,5),auto_size_text=True,expand_x=True, expand_y=True,key='-ComentEL5-')],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregEquipo-')]]

#Este layout corresponde al registro de un juez
layout6 = [[sg.Button('<-', key='-returnl1L6-'), sg.Text('AÑADIR UN NUEVO JUEZ A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Persona', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDpersonaL6-',size=(10,8))],
           [sg.Text('Especializacion', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-especializacion-',size=(30,30))],
           [sg.Text('Comentario',)],[sg.Multiline('',autoscroll=True,enter_submits=True,size=(20,5),auto_size_text=True,expand_x=True, expand_y=True,key='-ComentEL5-')],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregJuez-')]]


#Este layout corresponde al registro de una competencia
layout7 = [[sg.Button('<-', key='-returnl1L7-'), sg.Text('AÑADIR UNA NUEVA COMPETENCIA A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Prueba', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDpruebaL7-',size=(10,8))],
           [sg.Text('Tiempo duracion', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-TiempoDuracion-',size=(30,30))],
           [sg.Text('Numero de Problemas', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-Numproblemas-',size=(30,30))],
           [ sg.Text('Fecha de realizacion', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-FechaR-',size=(20,20)),sg.In(key='-CALL7-', enable_events=True, visible=False),
        sg.CalendarButton('Calendar', target='-CALL7-', pad=None, font=('MS Sans Serif', 10, 'bold'),button_color=('black', 'white'), key='_CALENDARL7_', format=('%d %B, %Y'))],
            [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregCompetencia-')]]

#Este layout corresponde al registro de un Patrocinador
layout8 = [[sg.Button('<-', key='-returnl1L8-'), sg.Text('AÑADIR UN NUEVO PATROCINADOR A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Patrocinador', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDpersonaL6-',size=(10,8))],
           [sg.Text('Nombre Patrocinador', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-especializacion-',size=(30,30))],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregPatrocinador-')]]



#Layout principal 
layout = [[sg.Column(layout=layout0,key='-COL{0}-',visible=True),sg.Column(layout=layout1,key='-COL{1}-',visible=False),sg.Column(layout=layout2,key='-COL{2}-',visible=False),
        sg.Column(layout=layout3,key='-COL{3}-',visible=False),sg.Column(layout=layout4,key='-COL{4}-',visible=False),sg.Column(layout=layout5,key='-COL{5}-',visible=False),
        sg.Column(layout=layout6,key='-COL{6}-',visible=False),sg.Column(layout=layout7,key='-COL{7}-',visible=False),sg.Column(layout=layout8,key='-COL{8}-',visible=False)]]





window = sg.Window(title="ICPC DATA BASE ADMIN", layout=layout,auto_size_buttons=True,auto_size_text=True,resizable=True)


def CheckPersonaReg(values):
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
    if len(values['-ContryP-']) > 0:
        k += 1
    else :
        flag = False
        
    if flag and k == 6:
        return True
    else: 
        return False
    

    
    

# Create an event loop
while True:
    event, values = window.read()#Captura los eventos y los valores de los elementos
    #Evento para cerrar el programa  
    if event == sg.WIN_CLOSED:
        break
    
    #print(event, values)
    #este evento nos lleva a la interfaz de añadir registro
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
        window.Element('-IDPersonaL2-').update(value="")
        window.Element('-Namepersona-').update(value="")
        window.Element('-ApellidoP-').update(value="")
        window.Element('-ApellidoM-').update(value="")
        window.Element('-FechaN-').update(value="")
        window.find_element('-ContryP-').update(value="")
    elif CheckPersonaReg(values) == False and event == '-AddregPersona-':
        print("Bad")
        
    #este evento nos lleva a la interfaz de añadir registro de un participante 
    if event == '-ParButton-':
        window['-COL{3}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
        
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
    
    #este evento nos lleva a la interfaz de añadir registro de un patrocinador
    if event == '-PatButton-':
        window['-COL{8}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
    #Este evento nos regresa a la interfaz principal de añadir registros
    if event == '-returnl1L2-' and window['-COL{2}-'].visible == True:
        window['-COL{2}-'].update(visible=False)
        window['-COL{1}-'].update(visible=True)
        
    #Este evento nos regresa a la interfaz principal de añadir registros  
    if event == '-returnl1L3-' and window['-COL{3}-'].visible == True:
        window['-COL{3}-'].update(visible=False)
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
        

    
    
window.close()





# 'C:\Users\sergi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts'
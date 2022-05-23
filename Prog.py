#!/usr/bin/python
from cgitb import text
import PySimpleGUI as sg 
import pgdb 

#conexion = pgdb.connect(host="localhost",database=)

Countries = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua & Deps","Argentina","Armenia","Australia","Austria",
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
#Este layout contiene los elementos del menu principal 
layout0 = [[sg.Image('logo.png')],[sg.Text('ICPC',auto_size_text=True,font='Helvetica')],
        [sg.Button('AÑADIR REGISTRO',auto_size_button=True),sg.Button('BORRAR REGISTRO',auto_size_button=True)]]

#Este layout continene las opciones para añadir elementos a la base de Datos
layout1 = [[sg.Image('logo.png')],[sg.Text('AÑADIR UN REGISTRO A LA BASE DE DATOS',auto_size_text=True,font='Helvetica')],
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
           [sg.Text('Apellido P', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-ApellidoP-',size=(25,25)),sg.Text('Apellido M', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-ApellidoM-',size=(25,25))],
           [ sg.Text('Fecha de Nacimiento', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-FechaN-',size=(20,20)),sg.In(key='-CAL-', enable_events=True, visible=False),
        sg.CalendarButton('Calendar', target='-CAL-', pad=None, font=('MS Sans Serif', 10, 'bold'),button_color=('black', 'white'), key='_CALENDAR_', format=('%d %B, %Y'))],
           [ sg.Text('Pais', font=('MS Sans Serif', 10, 'bold')), sg.Combo(Countries,key='-Contry-')]]

#Este layout corresponde al registro de un participante
layout3 = [[sg.Button('<-', key='-returnl1L3-'), sg.Text('AÑADIR UN NUEVO PARTICIPANTE A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Persona', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDPersonaL3-',size=(10,8))],
           [sg.Text('Tercia ID ', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDterciaL3-',size=(30,30))],
           [sg.Text('Paradigma Dominante', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-ParadigmaD-',size=(25,25))]]

#Este layout corresponde al registro de una tercia
layout4 = [[sg.Button('<-', key='-returnl1L4-'), sg.Text('AÑADIR UNA NUEVA TERCIA A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Trecia', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDTerciaL4-',size=(10,8))],
           [sg.Text('ID Participante 1', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDPart1-',size=(30,30))],
           [sg.Text('ID Participante 2', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDPart2-',size=(30,30))],
           [sg.Text('ID Participante 3', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDPart3-',size=(30,30))]]


#Este layout corresponde al registro de un eqiupo
layout5 = [[sg.Button('<-', key='-returnl1L5-'), sg.Text('AÑADIR UN NUEVO EQUIPO A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Equipo', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDequipoL5-',size=(10,8))],
           [sg.Text('ID Tercia', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-Namepersona-',size=(30,30))],
           [ sg.Text('Pais', font=('MS Sans Serif', 10, 'bold')), sg.Combo(Countries,key='-Contry-')],
           [sg.Text('Comentario Especial',)],[sg.Multiline('',autoscroll=True,enter_submits=True,size=(20,5),auto_size_text=True,expand_x=True, expand_y=True,key='-ComentEL5-')]]








layout = [[sg.Column(layout=layout0,key='-COL{0}-',visible=True),sg.Column(layout=layout1,key='-COL{1}-',visible=False),sg.Column(layout=layout2,key='-COL{2}-',visible=False),
        sg.Column(layout=layout3,key='-COL{3}-',visible=False),sg.Column(layout=layout4,key='-COL{4}-',visible=False),sg.Column(layout=layout5,key='-COL{5}-',visible=False)]]





window = sg.Window(title="ICPC DATA BASE ADMIN", layout=layout,auto_size_buttons=True,auto_size_text=True,resizable=True)


# Create an event loop
while True:
    event, values = window.read()
    
    print(event, values)
    
    if event == 'AÑADIR REGISTRO':
        window['-COL{1}-'].update(visible=True)
        window['-COL{0}-'].update(visible=False)
        
    if event == '-PButton-':
        window['-COL{2}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
        
    if event == '-ParButton-':
        window['-COL{3}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
    if event == '-TerButton-':
        window['-COL{4}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
    if event == '-TButton-':
        window['-COL{5}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
        
    if event == '-returnl1L2-' and window['-COL{2}-'].visible == True:
        window['-COL{2}-'].update(visible=False)
        window['-COL{1}-'].update(visible=True)
        
    if event == '-returnl1L3-' and window['-COL{3}-'].visible == True:
        window['-COL{3}-'].update(visible=False)
        window['-COL{1}-'].update(visible=True)
        
    if event == '-returnl1L4-' and window['-COL{4}-'].visible == True:
        window['-COL{4}-'].update(visible=False)
        window['-COL{1}-'].update(visible=True)
        
    if event == '-returnl1L5-' and window['-COL{5}-'].visible == True:
        window['-COL{5}-'].update(visible=False)
        window['-COL{1}-'].update(visible=True)
        
        
    if event == sg.WIN_CLOSED:
        break
    
window.close()

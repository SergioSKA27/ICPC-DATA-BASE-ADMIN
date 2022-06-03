--
-- PostgreSQL database dump
--

-- Dumped from database version 14.3
-- Dumped by pg_dump version 14.3

-- Started on 2022-06-03 05:42:18

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 216 (class 1259 OID 24594)
-- Name: competicion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.competicion (
    code_competicion character(3) NOT NULL,
    descripcion character varying(100) NOT NULL,
    duracion_hrs integer NOT NULL,
    fecha date NOT NULL,
    no_problemas integer NOT NULL,
    id_region integer
);


ALTER TABLE public.competicion OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 24616)
-- Name: competicion_local; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.competicion_local (
    code_competicion character(3) NOT NULL,
    cve_universidad character(3) NOT NULL
);


ALTER TABLE public.competicion_local OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 24609)
-- Name: equipo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipo (
    id_equipo integer NOT NULL,
    nombre character varying(20) NOT NULL,
    cve_universidad character(3) NOT NULL,
    estatus boolean NOT NULL
);


ALTER TABLE public.equipo OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 24608)
-- Name: equipo_id_equipo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.equipo_id_equipo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.equipo_id_equipo_seq OWNER TO postgres;

--
-- TOC entry 3459 (class 0 OID 0)
-- Dependencies: 221
-- Name: equipo_id_equipo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.equipo_id_equipo_seq OWNED BY public.equipo.id_equipo;


--
-- TOC entry 223 (class 1259 OID 24613)
-- Name: equipo_local; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipo_local (
    id_equipo integer NOT NULL,
    code_competicion character(3) NOT NULL,
    cve_universidad character(3) NOT NULL
);


ALTER TABLE public.equipo_local OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 24632)
-- Name: equipo_mundial; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipo_mundial (
    id_final_mundial integer NOT NULL,
    id_equipo integer NOT NULL
);


ALTER TABLE public.equipo_mundial OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 24586)
-- Name: equipo_regional; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipo_regional (
    id_equipo integer NOT NULL,
    code_competicion character(3) NOT NULL
);


ALTER TABLE public.equipo_regional OWNER TO postgres;

--
-- TOC entry 232 (class 1259 OID 24636)
-- Name: final_mundial; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.final_mundial (
    id_final_mundial integer NOT NULL,
    code_competicion character(3) NOT NULL,
    fecha date NOT NULL,
    ciudad character varying(50) NOT NULL
);


ALTER TABLE public.final_mundial OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 24635)
-- Name: final_mundial_id_final_mundial_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.final_mundial_id_final_mundial_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.final_mundial_id_final_mundial_seq OWNER TO postgres;

--
-- TOC entry 3460 (class 0 OID 0)
-- Dependencies: 231
-- Name: final_mundial_id_final_mundial_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.final_mundial_id_final_mundial_seq OWNED BY public.final_mundial.id_final_mundial;


--
-- TOC entry 210 (class 1259 OID 24577)
-- Name: juez; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.juez (
    id_juez integer NOT NULL,
    id_persona integer NOT NULL,
    especializacion character varying(100),
    puntuacion integer NOT NULL
);


ALTER TABLE public.juez OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 24582)
-- Name: juez_competicion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.juez_competicion (
    id_juez_competicion integer NOT NULL,
    id_juez integer NOT NULL,
    code_competicion character(3) NOT NULL
);


ALTER TABLE public.juez_competicion OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 24581)
-- Name: juez_competicion_id_juez_competicion_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.juez_competicion_id_juez_competicion_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.juez_competicion_id_juez_competicion_seq OWNER TO postgres;

--
-- TOC entry 3461 (class 0 OID 0)
-- Dependencies: 211
-- Name: juez_competicion_id_juez_competicion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.juez_competicion_id_juez_competicion_seq OWNED BY public.juez_competicion.id_juez_competicion;


--
-- TOC entry 209 (class 1259 OID 24576)
-- Name: juez_id_juez_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.juez_id_juez_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.juez_id_juez_seq OWNER TO postgres;

--
-- TOC entry 3462 (class 0 OID 0)
-- Dependencies: 209
-- Name: juez_id_juez_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.juez_id_juez_seq OWNED BY public.juez.id_juez;


--
-- TOC entry 229 (class 1259 OID 24628)
-- Name: pais; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pais (
    id_pais integer NOT NULL,
    nombre character varying(20) NOT NULL
);


ALTER TABLE public.pais OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 24627)
-- Name: pais_id_pais_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pais_id_pais_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pais_id_pais_seq OWNER TO postgres;

--
-- TOC entry 3463 (class 0 OID 0)
-- Dependencies: 228
-- Name: pais_id_pais_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pais_id_pais_seq OWNED BY public.pais.id_pais;


--
-- TOC entry 215 (class 1259 OID 24590)
-- Name: persona; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.persona (
    id_persona integer NOT NULL,
    nombre character varying(50) NOT NULL,
    apellido_1 character varying(50) NOT NULL,
    apellido_2 character varying(50),
    fecha_nacimiento date NOT NULL,
    telefono character(10) NOT NULL,
    correo_electronico character(20) NOT NULL
);


ALTER TABLE public.persona OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 24589)
-- Name: persona_id_persona_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.persona_id_persona_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.persona_id_persona_seq OWNER TO postgres;

--
-- TOC entry 3464 (class 0 OID 0)
-- Dependencies: 214
-- Name: persona_id_persona_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.persona_id_persona_seq OWNED BY public.persona.id_persona;


--
-- TOC entry 218 (class 1259 OID 24600)
-- Name: problema; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.problema (
    code_problema character(3) NOT NULL,
    descripcion character varying(100) NOT NULL,
    tipo character varying(20) NOT NULL
);


ALTER TABLE public.problema OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 24604)
-- Name: programa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.programa (
    id_programa integer NOT NULL,
    code_problema character(3) NOT NULL,
    id_equipo integer NOT NULL,
    lenguaje_programacion character varying(15) NOT NULL,
    valido boolean NOT NULL,
    time_resolucion_minutos integer NOT NULL
);


ALTER TABLE public.programa OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 24603)
-- Name: programa_id_programa_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.programa_id_programa_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.programa_id_programa_seq OWNER TO postgres;

--
-- TOC entry 3465 (class 0 OID 0)
-- Dependencies: 219
-- Name: programa_id_programa_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.programa_id_programa_seq OWNED BY public.programa.id_programa;


--
-- TOC entry 227 (class 1259 OID 24623)
-- Name: region; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.region (
    id_region integer NOT NULL,
    id_pais integer NOT NULL,
    nombre character varying(15) NOT NULL
);


ALTER TABLE public.region OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 24622)
-- Name: region_id_region_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.region_id_region_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.region_id_region_seq OWNER TO postgres;

--
-- TOC entry 3466 (class 0 OID 0)
-- Dependencies: 226
-- Name: region_id_region_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.region_id_region_seq OWNED BY public.region.id_region;


--
-- TOC entry 217 (class 1259 OID 24597)
-- Name: tercia; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tercia (
    id_persona integer NOT NULL,
    id_equipo integer NOT NULL
);


ALTER TABLE public.tercia OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 24619)
-- Name: universidad; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.universidad (
    cve_universidad character(3) NOT NULL,
    nombre character(50) NOT NULL,
    id_region integer NOT NULL
);


ALTER TABLE public.universidad OWNER TO postgres;

--
-- TOC entry 3235 (class 2604 OID 24612)
-- Name: equipo id_equipo; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo ALTER COLUMN id_equipo SET DEFAULT nextval('public.equipo_id_equipo_seq'::regclass);


--
-- TOC entry 3238 (class 2604 OID 24639)
-- Name: final_mundial id_final_mundial; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.final_mundial ALTER COLUMN id_final_mundial SET DEFAULT nextval('public.final_mundial_id_final_mundial_seq'::regclass);


--
-- TOC entry 3231 (class 2604 OID 24580)
-- Name: juez id_juez; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juez ALTER COLUMN id_juez SET DEFAULT nextval('public.juez_id_juez_seq'::regclass);


--
-- TOC entry 3232 (class 2604 OID 24585)
-- Name: juez_competicion id_juez_competicion; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juez_competicion ALTER COLUMN id_juez_competicion SET DEFAULT nextval('public.juez_competicion_id_juez_competicion_seq'::regclass);


--
-- TOC entry 3237 (class 2604 OID 24631)
-- Name: pais id_pais; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pais ALTER COLUMN id_pais SET DEFAULT nextval('public.pais_id_pais_seq'::regclass);


--
-- TOC entry 3233 (class 2604 OID 24593)
-- Name: persona id_persona; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.persona ALTER COLUMN id_persona SET DEFAULT nextval('public.persona_id_persona_seq'::regclass);


--
-- TOC entry 3234 (class 2604 OID 24607)
-- Name: programa id_programa; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.programa ALTER COLUMN id_programa SET DEFAULT nextval('public.programa_id_programa_seq'::regclass);


--
-- TOC entry 3236 (class 2604 OID 24626)
-- Name: region id_region; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.region ALTER COLUMN id_region SET DEFAULT nextval('public.region_id_region_seq'::regclass);


--
-- TOC entry 3437 (class 0 OID 24594)
-- Dependencies: 216
-- Data for Name: competicion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.competicion (code_competicion, descripcion, duracion_hrs, fecha, no_problemas, id_region) FROM stdin;
\.


--
-- TOC entry 3445 (class 0 OID 24616)
-- Dependencies: 224
-- Data for Name: competicion_local; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.competicion_local (code_competicion, cve_universidad) FROM stdin;
\.


--
-- TOC entry 3443 (class 0 OID 24609)
-- Dependencies: 222
-- Data for Name: equipo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.equipo (id_equipo, nombre, cve_universidad, estatus) FROM stdin;
1245	LOS MACS	123	t
13467	mwe	123	t
\.


--
-- TOC entry 3444 (class 0 OID 24613)
-- Dependencies: 223
-- Data for Name: equipo_local; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.equipo_local (id_equipo, code_competicion, cve_universidad) FROM stdin;
\.


--
-- TOC entry 3451 (class 0 OID 24632)
-- Dependencies: 230
-- Data for Name: equipo_mundial; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.equipo_mundial (id_final_mundial, id_equipo) FROM stdin;
\.


--
-- TOC entry 3434 (class 0 OID 24586)
-- Dependencies: 213
-- Data for Name: equipo_regional; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.equipo_regional (id_equipo, code_competicion) FROM stdin;
\.


--
-- TOC entry 3453 (class 0 OID 24636)
-- Dependencies: 232
-- Data for Name: final_mundial; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.final_mundial (id_final_mundial, code_competicion, fecha, ciudad) FROM stdin;
\.


--
-- TOC entry 3431 (class 0 OID 24577)
-- Dependencies: 210
-- Data for Name: juez; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.juez (id_juez, id_persona, especializacion, puntuacion) FROM stdin;
\.


--
-- TOC entry 3433 (class 0 OID 24582)
-- Dependencies: 212
-- Data for Name: juez_competicion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.juez_competicion (id_juez_competicion, id_juez, code_competicion) FROM stdin;
\.


--
-- TOC entry 3450 (class 0 OID 24628)
-- Dependencies: 229
-- Data for Name: pais; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pais (id_pais, nombre) FROM stdin;
0	
1	Afghanistan
2	Albania
3	Algeria
4	Andorra
5	Angola
6	Antigua & Deps
7	Argentina
8	Armenia
9	Australia
10	Austria
11	Azerbaijan
12	Bahamas
13	Bahrain
14	Bangladesh
15	Barbados
16	Belarus
17	Belgium
18	Belize
19	Benin
20	Bhutan
21	Bolivia
22	Bosnia Herzegovina
23	Botswana
24	Brazil
25	Brunei
26	Bulgaria
27	Burkina
28	Burundi
29	Cambodia
30	Cameroon
31	Canada
32	Cape Verde
33	Central African Rep
34	Chad
35	Chile
36	China
37	Colombia
38	Comoros
39	Congo
41	Costa Rica
42	Croatia
43	Cuba
44	Cyprus
45	Czech Republic
46	Denmark
47	Djibouti
48	Dominica
49	Dominican Republic
50	East Timor
51	Ecuador
52	Egypt
53	El Salvador
54	Equatorial Guinea
55	Eritrea
56	Estonia
57	Ethiopia
58	Fiji
59	Finland
60	France
61	Gabon
62	Gambia
63	Georgia
64	Germany
65	Ghana
66	Greece
67	Grenada
68	Guatemala
69	Guinea
70	Guinea-Bissau
71	Guyana
72	Haiti
73	Honduras
74	Hungary
75	Iceland
76	India
77	Indonesia
78	Iran
79	Iraq
80	Ireland {Republic}
81	Israel
82	Italy
83	Ivory Coast
84	Jamaica
85	Japan
86	Jordan
87	Kazakhstan
88	Kenya
89	Kiribati
90	Korea North
91	Korea South
92	Kosovo
93	Kuwait
94	Kyrgyzstan
95	Laos
96	Latvia
97	Lebanon
98	Lesotho
99	Liberia
100	Libya
101	Liechtenstein
102	Lithuania
103	Luxembourg
104	Macedonia
105	Madagascar
106	Malawi
107	Malaysia
108	Maldives
109	Mali
110	Malta
111	Marshall Islands
112	Mauritania
113	Mauritius
114	Mexico
115	Micronesia
116	Moldova
117	Monaco
118	Mongolia
119	Montenegro
120	Morocco
121	Mozambique
122	Myanmar, {Burma}
123	Namibia
124	Nauru
125	Nepal
126	Netherlands
127	New Zealand
128	Nicaragua
129	Niger
130	Nigeria
131	Norway
132	Oman
133	Pakistan
134	Palau
135	Panama
136	Papua New Guinea
137	Paraguay
138	Peru
139	Philippines
140	Poland
141	Portugal
142	Qatar
143	Romania
144	Russian Federation
145	Rwanda
146	St Kitts & Nevis
147	St Lucia
149	Samoa
150	San Marino
151	Sao Tome & Principe
152	Saudi Arabia
153	Senegal
154	Serbia
155	Seychelles
156	Sierra Leone
157	Singapore
158	Slovakia
159	Slovenia
160	Solomon Islands
161	Somalia
162	South Africa
163	South Sudan
164	Spain
165	Sri Lanka
166	Sudan
167	Suriname
168	Swaziland
169	Sweden
170	Switzerland
171	Syria
172	Taiwan
173	Tajikistan
174	Tanzania
175	Thailand
176	Togo
177	Tonga
178	Trinidad & Tobago
179	Tunisia
180	Turkey
181	Turkmenistan
182	Tuvalu
183	Uganda
184	Ukraine
185	United Arab Emirates
186	United Kingdom
187	United States
188	Uruguay
189	Uzbekistan
190	Vanuatu
191	Vatican City
192	Venezuela
193	Vietnam
194	Yemen
195	Zambia
196	Zimbabwe
\.


--
-- TOC entry 3436 (class 0 OID 24590)
-- Dependencies: 215
-- Data for Name: persona; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.persona (id_persona, nombre, apellido_1, apellido_2, fecha_nacimiento, telefono, correo_electronico) FROM stdin;
32536	Juan	Perez	Lopez	2022-06-17	5512832295	gg@gmail.com        
12325	Juan	Perez	Avaraz	2000-04-27	5512345567	sergio@mail.com     
76643	Sergio	Lopez	Martinez	2000-04-27	5512832295	sergio@mail.com     
\.


--
-- TOC entry 3439 (class 0 OID 24600)
-- Dependencies: 218
-- Data for Name: problema; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.problema (code_problema, descripcion, tipo) FROM stdin;
\.


--
-- TOC entry 3441 (class 0 OID 24604)
-- Dependencies: 220
-- Data for Name: programa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.programa (id_programa, code_problema, id_equipo, lenguaje_programacion, valido, time_resolucion_minutos) FROM stdin;
\.


--
-- TOC entry 3448 (class 0 OID 24623)
-- Dependencies: 227
-- Data for Name: region; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.region (id_region, id_pais, nombre) FROM stdin;
0	19	SWERC
1	1	NWERC
2	33	CERC
3	20	SEERC
4	5	NEERC
5	33	AARPC
6	33	SAfrica
7	23	Beijing
8	18	Coim
9	22	Kolkata
10	23	Daca
11	31	Kaohsiun
12	35	Manila
13	8	Seúl
14	17	Teerán
15	5	Xian
16	24	Shanghái
17	13	Yokohama
18	15	Hanói
19	29	SPacific
20	7	CAmerica
21	16	Caribe
22	35	Brasil
23	27	Suramérica N
24	20	Suramérica S
25	29	PacNW
26	4	NCNA
27	8	ECNA
28	29	NENA
29	10	Rocky Mountain
30	27	MCUSA
31	4	GNY
32	9	Scal
33	5	SCUSA
34	7	SEUSA
35	20	MAUSA
\.


--
-- TOC entry 3438 (class 0 OID 24597)
-- Dependencies: 217
-- Data for Name: tercia; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tercia (id_persona, id_equipo) FROM stdin;
12325	1245
\.


--
-- TOC entry 3446 (class 0 OID 24619)
-- Dependencies: 225
-- Data for Name: universidad; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.universidad (cve_universidad, nombre, id_region) FROM stdin;
123	UNAM                                              	20
\.


--
-- TOC entry 3467 (class 0 OID 0)
-- Dependencies: 221
-- Name: equipo_id_equipo_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.equipo_id_equipo_seq', 1, false);


--
-- TOC entry 3468 (class 0 OID 0)
-- Dependencies: 231
-- Name: final_mundial_id_final_mundial_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.final_mundial_id_final_mundial_seq', 1, false);


--
-- TOC entry 3469 (class 0 OID 0)
-- Dependencies: 211
-- Name: juez_competicion_id_juez_competicion_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.juez_competicion_id_juez_competicion_seq', 1, false);


--
-- TOC entry 3470 (class 0 OID 0)
-- Dependencies: 209
-- Name: juez_id_juez_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.juez_id_juez_seq', 1, false);


--
-- TOC entry 3471 (class 0 OID 0)
-- Dependencies: 228
-- Name: pais_id_pais_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pais_id_pais_seq', 1, false);


--
-- TOC entry 3472 (class 0 OID 0)
-- Dependencies: 214
-- Name: persona_id_persona_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.persona_id_persona_seq', 1, false);


--
-- TOC entry 3473 (class 0 OID 0)
-- Dependencies: 219
-- Name: programa_id_programa_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.programa_id_programa_seq', 1, false);


--
-- TOC entry 3474 (class 0 OID 0)
-- Dependencies: 226
-- Name: region_id_region_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.region_id_region_seq', 1, false);


--
-- TOC entry 3248 (class 2606 OID 24649)
-- Name: competicion pk_code_competicion; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.competicion
    ADD CONSTRAINT pk_code_competicion PRIMARY KEY (code_competicion);


--
-- TOC entry 3252 (class 2606 OID 24661)
-- Name: problema pk_code_problema; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.problema
    ADD CONSTRAINT pk_code_problema PRIMARY KEY (code_problema);


--
-- TOC entry 3260 (class 2606 OID 24665)
-- Name: competicion_local pk_competicion_local; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.competicion_local
    ADD CONSTRAINT pk_competicion_local PRIMARY KEY (code_competicion, cve_universidad);


--
-- TOC entry 3262 (class 2606 OID 24667)
-- Name: universidad pk_cve_universidad; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.universidad
    ADD CONSTRAINT pk_cve_universidad PRIMARY KEY (cve_universidad);


--
-- TOC entry 3258 (class 2606 OID 24663)
-- Name: equipo_local pk_equipo_local; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo_local
    ADD CONSTRAINT pk_equipo_local PRIMARY KEY (id_equipo, code_competicion, cve_universidad);


--
-- TOC entry 3268 (class 2606 OID 24655)
-- Name: equipo_mundial pk_equipo_mundial; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo_mundial
    ADD CONSTRAINT pk_equipo_mundial PRIMARY KEY (id_final_mundial, id_equipo);


--
-- TOC entry 3244 (class 2606 OID 24645)
-- Name: equipo_regional pk_equipo_regional; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo_regional
    ADD CONSTRAINT pk_equipo_regional PRIMARY KEY (id_equipo, code_competicion);


--
-- TOC entry 3256 (class 2606 OID 24653)
-- Name: equipo pk_id_equipo; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo
    ADD CONSTRAINT pk_id_equipo PRIMARY KEY (id_equipo);


--
-- TOC entry 3270 (class 2606 OID 24657)
-- Name: final_mundial pk_id_final_mundial; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.final_mundial
    ADD CONSTRAINT pk_id_final_mundial PRIMARY KEY (id_final_mundial);


--
-- TOC entry 3240 (class 2606 OID 24641)
-- Name: juez pk_id_juez; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juez
    ADD CONSTRAINT pk_id_juez PRIMARY KEY (id_juez);


--
-- TOC entry 3242 (class 2606 OID 24647)
-- Name: juez_competicion pk_id_juez_competicion; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juez_competicion
    ADD CONSTRAINT pk_id_juez_competicion PRIMARY KEY (id_juez_competicion);


--
-- TOC entry 3266 (class 2606 OID 24671)
-- Name: pais pk_id_pais; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pais
    ADD CONSTRAINT pk_id_pais PRIMARY KEY (id_pais);


--
-- TOC entry 3246 (class 2606 OID 24643)
-- Name: persona pk_id_persona; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.persona
    ADD CONSTRAINT pk_id_persona PRIMARY KEY (id_persona);


--
-- TOC entry 3254 (class 2606 OID 24651)
-- Name: programa pk_id_programa; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.programa
    ADD CONSTRAINT pk_id_programa PRIMARY KEY (id_programa);


--
-- TOC entry 3264 (class 2606 OID 24669)
-- Name: region pk_id_region; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.region
    ADD CONSTRAINT pk_id_region PRIMARY KEY (id_region);


--
-- TOC entry 3250 (class 2606 OID 24659)
-- Name: tercia pk_tercia_id_persona; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tercia
    ADD CONSTRAINT pk_tercia_id_persona PRIMARY KEY (id_persona);


--
-- TOC entry 3275 (class 2606 OID 24682)
-- Name: equipo_regional fk_code_competicion; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo_regional
    ADD CONSTRAINT fk_code_competicion FOREIGN KEY (code_competicion) REFERENCES public.competicion(code_competicion);


--
-- TOC entry 3273 (class 2606 OID 24692)
-- Name: juez_competicion fk_code_competicion; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juez_competicion
    ADD CONSTRAINT fk_code_competicion FOREIGN KEY (code_competicion) REFERENCES public.competicion(code_competicion);


--
-- TOC entry 3290 (class 2606 OID 24727)
-- Name: final_mundial fk_code_competicion; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.final_mundial
    ADD CONSTRAINT fk_code_competicion FOREIGN KEY (code_competicion) REFERENCES public.competicion(code_competicion);


--
-- TOC entry 3283 (class 2606 OID 24747)
-- Name: equipo_local fk_code_competicion; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo_local
    ADD CONSTRAINT fk_code_competicion FOREIGN KEY (code_competicion, cve_universidad) REFERENCES public.competicion_local(code_competicion, cve_universidad);


--
-- TOC entry 3284 (class 2606 OID 24752)
-- Name: competicion_local fk_code_competicion; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.competicion_local
    ADD CONSTRAINT fk_code_competicion FOREIGN KEY (code_competicion) REFERENCES public.competicion(code_competicion);


--
-- TOC entry 3279 (class 2606 OID 24702)
-- Name: programa fk_code_problema; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.programa
    ADD CONSTRAINT fk_code_problema FOREIGN KEY (code_problema) REFERENCES public.problema(code_problema);


--
-- TOC entry 3281 (class 2606 OID 24712)
-- Name: equipo fk_cve_universidad; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo
    ADD CONSTRAINT fk_cve_universidad FOREIGN KEY (cve_universidad) REFERENCES public.universidad(cve_universidad);


--
-- TOC entry 3285 (class 2606 OID 24757)
-- Name: competicion_local fk_cve_universidad; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.competicion_local
    ADD CONSTRAINT fk_cve_universidad FOREIGN KEY (cve_universidad) REFERENCES public.universidad(cve_universidad);


--
-- TOC entry 3274 (class 2606 OID 24677)
-- Name: equipo_regional fk_id_equipo; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo_regional
    ADD CONSTRAINT fk_id_equipo FOREIGN KEY (id_equipo) REFERENCES public.equipo(id_equipo);


--
-- TOC entry 3280 (class 2606 OID 24707)
-- Name: programa fk_id_equipo; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.programa
    ADD CONSTRAINT fk_id_equipo FOREIGN KEY (id_equipo) REFERENCES public.equipo(id_equipo);


--
-- TOC entry 3289 (class 2606 OID 24722)
-- Name: equipo_mundial fk_id_equipo; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo_mundial
    ADD CONSTRAINT fk_id_equipo FOREIGN KEY (id_equipo) REFERENCES public.equipo(id_equipo);


--
-- TOC entry 3277 (class 2606 OID 24732)
-- Name: tercia fk_id_equipo; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tercia
    ADD CONSTRAINT fk_id_equipo FOREIGN KEY (id_equipo) REFERENCES public.equipo(id_equipo);


--
-- TOC entry 3282 (class 2606 OID 24742)
-- Name: equipo_local fk_id_equipo; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo_local
    ADD CONSTRAINT fk_id_equipo FOREIGN KEY (id_equipo) REFERENCES public.equipo(id_equipo);


--
-- TOC entry 3288 (class 2606 OID 24717)
-- Name: equipo_mundial fk_id_final_mundial; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipo_mundial
    ADD CONSTRAINT fk_id_final_mundial FOREIGN KEY (id_final_mundial) REFERENCES public.final_mundial(id_final_mundial);


--
-- TOC entry 3272 (class 2606 OID 24687)
-- Name: juez_competicion fk_id_juez; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juez_competicion
    ADD CONSTRAINT fk_id_juez FOREIGN KEY (id_juez) REFERENCES public.juez(id_juez);


--
-- TOC entry 3287 (class 2606 OID 24767)
-- Name: region fk_id_pais; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.region
    ADD CONSTRAINT fk_id_pais FOREIGN KEY (id_pais) REFERENCES public.pais(id_pais);


--
-- TOC entry 3271 (class 2606 OID 24672)
-- Name: juez fk_id_persona; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juez
    ADD CONSTRAINT fk_id_persona FOREIGN KEY (id_persona) REFERENCES public.persona(id_persona);


--
-- TOC entry 3278 (class 2606 OID 24737)
-- Name: tercia fk_id_persona; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tercia
    ADD CONSTRAINT fk_id_persona FOREIGN KEY (id_persona) REFERENCES public.persona(id_persona);


--
-- TOC entry 3276 (class 2606 OID 24697)
-- Name: competicion fk_id_region; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.competicion
    ADD CONSTRAINT fk_id_region FOREIGN KEY (id_region) REFERENCES public.region(id_region);


--
-- TOC entry 3286 (class 2606 OID 24762)
-- Name: universidad fk_id_region; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.universidad
    ADD CONSTRAINT fk_id_region FOREIGN KEY (id_region) REFERENCES public.region(id_region);


-- Completed on 2022-06-03 05:42:19

--
-- PostgreSQL database dump complete
--


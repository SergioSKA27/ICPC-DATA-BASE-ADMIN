#!/usr/bin/python
import random
from re import I
import PySimpleGUI as sg
from os import execv
import psycopg2 as pgdb
import re
import sys

#print('Ingrese el nombre de la base de datos: ')
#nombredb = str(input())
#print('Ingrese la contraseña de la base de datos: ')
#pasword = str(input())
nombredb = "proyectofinal"
pasword = 'AlmaDeli159'
#insertar el nombre de la base de datos y la contraseña por ARGV

SQLLNG = [
'A',
'ABORT',
'ABS',
'ABSOLUTE',
'ACCESS',
'ACTION',
'ADA',
'ADD',
'ADMIN',
'AFTER',
'AGGREGATE',
'ALIAS',
'ALL',
'ALLOCATE',
'ALSO',
'ALTER',
'ALWAYS',
'ANALYSE',
'ANALYZE',
'AND',
'ANY',
'ARE',
'ARRAY',
'AS',
'ASC',
'ASENSITIVE',
'ASSERTION',
'ASSIGNMENT',
'ASYMMETRIC',
'AT',
'ATOMIC',
'ATTRIBUTE',
'ATTRIBUTES',
'AUDIT',
'AUTHORIZATION',
'AUTO_INCREMENT',
'AVG',
'AVG_ROW_LENGTH',
'BACKUP',
'BACKWARD',
'BEFORE',
'BEGIN',
'BERNOULLI',
'BETWEEN',
'BIGINT',
'BINARY',
'BIT',
'BIT_LENGTH',
'BITVAR',
'BLOB',
'BOOL',
'BOOLEAN',
'BOTH',
'BREADTH',
'BREAK',
'BROWSE',
'BULK',
'BY',
'C',
'CACHE',
'CALL',
'CALLED',
'CARDINALITY',
'CASCADE',
'CASCADED',
'CASE',
'CAST',
'CATALOG',
'CATALOG_NAME',
'CEIL',
'CEILING',
'CHAIN',
'CHANGE',
'CHAR',
'CHAR_LENGTH',
'CHARACTER',
'CHARACTER_LENGTH',
'CHARACTER_SET_CATALOG',
'CHARACTER_SET_NAME',
'CHARACTER_SET_SCHEMA',
'CHARACTERISTICS',
'CHARACTERS',
'CHECK',
'CHECKED',
'CHECKPOINT',
'CHECKSUM',
'CLASS',
'CLASS_ORIGIN',
'CLOB',
'CLOSE',
'CLUSTER',
'CLUSTERED',
'COALESCE',
'COBOL',
'COLLATE',
'COLLATION',
'COLLATION_CATALOG',
'COLLATION_NAME',
'COLLATION_SCHEMA',
'COLLECT',
'COLUMN',
'COLUMN_NAME',
'COLUMNS',
'COMMAND_FUNCTION',
'COMMAND_FUNCTION_CODE',
'COMMENT',
'COMMIT',
'COMMITTED',
'COMPLETION',
'COMPRESS',
'COMPUTE',
'CONDITION',
'CONDITION_NUMBER',
'CONNECT',
'CONNECTION',
'CONNECTION_NAME',
'CONSTRAINT',
'CONSTRAINT_CATALOG',
'CONSTRAINT_NAME',
'CONSTRAINT_SCHEMA',
'CONSTRAINTS',
'CONSTRUCTOR',
'CONTAINS',
'CONTAINSTABLE',
'CONTINUE',
'CONVERSION',
'CONVERT',
'COPY',
'CORR',
'CORRESPONDING',
'COUNT',
'COVAR_POP',
'COVAR_SAMP',
'CREATE',
'CREATEDB',
'CREATEROLE',
'CREATEUSER',
'CROSS',
'CSV',
'CUBE',
'CUME_DIST',
'CURRENT',
'CURRENT_DATE',
'CURRENT_DEFAULT_TRANSFORM_GROUP',
'CURRENT_PATH',
'CURRENT_ROLE',
'CURRENT_TIME',
'CURRENT_TIMESTAMP',
'CURRENT_TRANSFORM_GROUP_FOR_TYPE',
'CURRENT_USER',
'CURSOR',
'CURSOR_NAME',
'CYCLE',
'DATA',
'DATABASE',
'DATABASES',
'DATE',
'DATETIME',
'DATETIME_INTERVAL_CODE',
'DATETIME_INTERVAL_PRECISION',
'DAY',
'DAY_HOUR',
'DAY_MICROSECOND',
'DAY_MINUTE',
'DAY_SECOND',
'DAYOFMONTH',
'DAYOFWEEK',
'DAYOFYEAR',
'DBCC',
'DEALLOCATE',
'DEC',
'DECIMAL',
'DECLARE',
'DEFAULT',
'DEFAULTS',
'DEFERRABLE',
'DEFERRED',
'DEFINED',
'DEFINER',
'DEGREE',
'DELAY_KEY_WRITE',
'DELAYED',
'DELETE',
'DELIMITER',
'DELIMITERS',
'DENSE_RANK',
'DENY',
'DEPTH',
'DEREF',
'DERIVED',
'DESC',
'DESCRIBE',
'DESCRIPTOR',
'DESTROY',
'DESTRUCTOR',
'DETERMINISTIC',
'DIAGNOSTICS',
'DICTIONARY',
'DISABLE',
'DISCONNECT',
'DISK',
'DISPATCH',
'DISTINCT',
'DISTINCTROW',
'DISTRIBUTED',
'DIV',
'DO',
'DOMAIN',
'DOUBLE',
'DROP',
'DUAL',
'DUMMY',
'DUMP',
'DYNAMIC',
'DYNAMIC_FUNCTION',
'DYNAMIC_FUNCTION_CODE',
'EACH',
'ELEMENT',
'ELSE',
'ELSEIF',
'ENABLE',
'ENCLOSED',
'ENCODING',
'ENCRYPTED',
'END',
'END',
'EXEC',
'ENUM',
'EQUALS',
'ERRLVL',
'ESCAPE',
'ESCAPED',
'EVERY',
'EXCEPT',
'EXCEPTION',
'EXCLUDE',
'EXCLUDING',
'EXCLUSIVE',
'EXEC',
'EXECUTE',
'EXISTING',
'EXISTS',
'EXIT',
'EXP',
'EXPLAIN',
'EXTERNAL',
'EXTRACT',
'FALSE',
'FETCH',
'FIELDS',
'FILE',
'FILLFACTOR',
'FILTER',
'FINAL',
'FIRST',
'FLOAT',
'FLOAT4',
'FLOAT8',
'FLOOR',
'FLUSH',
'FOLLOWING',
'FOR',
'FORCE',
'FOREIGN',
'FORTRAN',
'FORWARD',
'FOUND',
'FREE',
'FREETEXT',
'FREETEXTTABLE',
'FREEZE',
'FROM',
'FULL',
'FULLTEXT',
'FUNCTION',
'FUSION',
'G',
'GENERAL',
'GENERATED',
'GET',
'GLOBAL',
'GO',
'GOTO',
'GRANT',
'GRANTED',
'GRANTS',
'GREATEST',
'GROUP',
'GROUPING',
'HANDLER',
'HAVING',
'HEADER',
'HEAP',
'HIERARCHY',
'HIGH_PRIORITY',
'HOLD',
'HOLDLOCK',
'HOST',
'HOSTS',
'HOUR',
'HOUR_MICROSECOND',
'HOUR_MINUTE',
'HOUR_SECOND',
'IDENTIFIED',
'IDENTITY',
'IDENTITY_INSERT',
'IDENTITYCOL',
'IF',
'IGNORE',
'ILIKE',
'IMMEDIATE',
'IMMUTABLE',
'IMPLEMENTATION',
'IMPLICIT',
'IN',
'INCLUDE',
'INCLUDING',
'INCREMENT',
'INDEX',
'INDICATOR',
'INFILE',
'INFIX',
'INHERIT',
'INHERITS',
'INITIAL',
'INITIALIZE',
'INITIALLY',
'INNER',
'INOUT',
'INPUT',
'INSENSITIVE',
'INSERT',
'INSERT_ID',
'INSTANCE',
'INSTANTIABLE',
'INSTEAD',
'INT',
'INT1',
'INT2',
'INT3',
'INT4',
'INT8',
'INTEGER',
'INTERSECT',
'INTERSECTION',
'INTERVAL',
'INTO',
'INVOKER',
'IS',
'ISAM',
'ISNULL',
'ISOLATION',
'ITERATE',
'JOIN',
'KEY',
'KEY_MEMBER',
'KEY_TYPE',
'KEYS',
'KILL',
'LANCOMPILER',
'LANGUAGE',
'LARGE',
'LAST',
'LAST_INSERT_ID',
'LATERAL',
'LEAD',
'LEADING',
'LEAST',
'LEAVE',
'LEFT',
'LENGTH',
'LESS',
'LEVEL',
'LIKE',
'LIMIT',
'LINENO',
'LINES',
'LISTEN',
'LN',
'LOAD',
'LOCAL',
'LOCALTIME',
'LOCALTIMESTAMP',
'LOCATION',
'LOCATOR',
'LOCK',
'LOGIN',
'LOGS',
'LONG',
'LONGBLOB',
'LONGTEXT',
'LOOP',
'LOW_PRIORITY',
'LOWER',
'MAP',
'MATCH',
'MATCHED',
'MAX',
'MAX_ROWS',
'MAXEXTENTS',
'MAXVALUE',
'MEDIUMBLOB',
'MEDIUMINT',
'MEDIUMTEXT',
'MEMBER',
'MERGE',
'MESSAGE_LENGTH',
'MESSAGE_OCTET_LENGTH',
'MESSAGE_TEXT',
'METHOD',
'MIDDLEINT',
'MIN',
'MIN_ROWS',
'MINUS',
'MINUTE',
'MINUTE_MICROSECOND',
'MINUTE_SECOND',
'MINVALUE',
'MLSLABEL',
'MOD',
'MODE',
'MODIFIES',
'MODIFY',
'MODULE',
'MONTH',
'MONTHNAME',
'MORE',
'MOVE',
'MULTISET',
'MUMPS',
'MYISAM',
'NAME',
'NAMES',
'NATIONAL',
'NATURAL',
'NCHAR',
'NCLOB',
'NESTING',
'NEW',
'NEXT',
'NO',
'NO_WRITE_TO_BINLOG',
'NOAUDIT',
'NOCHECK',
'NOCOMPRESS',
'NOCREATEDB',
'NOCREATEROLE',
'NOCREATEUSER',
'NOINHERIT',
'NOLOGIN',
'NONCLUSTERED',
'NONE',
'NORMALIZE',
'NORMALIZED',
'NOSUPERUSER',
'NOT',
'NOTHING',
'NOTIFY',
'NOTNULL',
'NOWAIT',
'NULL',
'NULLABLE',
'NULLIF',
'NULLS',
'NUMBER',
'NUMERIC',
'OBJECT',
'OCTET_LENGTH',
'OCTETS',
'OF',
'OFF',
'OFFLINE',
'OFFSET',
'OFFSETS',
'OIDS',
'OLD',
'ON',
'ONLINE',
'ONLY',
'OPEN',
'OPENDATASOURCE',
'OPENQUERY',
'OPENROWSET',
'OPENXML',
'OPERATION',
'OPERATOR',
'OPTIMIZE',
'OPTION',
'OPTIONALLY',
'OPTIONS',
'OR',
'ORDER',
'ORDERING',
'ORDINALITY',
'OTHERS',
'OUT',
'OUTER',
'OUTFILE',
'OUTPUT',
'OVER',
'OVERLAPS',
'OVERLAY',
'OVERRIDING',
'OWNER',
'PACK_KEYS',
'PAD',
'PARAMETER',
'PARAMETER_MODE',
'PARAMETER_NAME',
'PARAMETER_ORDINAL_POSITION',
'PARAMETER_SPECIFIC_CATALOG',
'PARAMETER_SPECIFIC_NAME',
'PARAMETER_SPECIFIC_SCHEMA',
'PARAMETERS',
'PARTIAL',
'PARTITION',
'PASCAL',
'PASSWORD',
'PATH',
'PCTFREE',
'PERCENT',
'PERCENT_RANK',
'PERCENTILE_CONT',
'PERCENTILE_DISC',
'PLACING',
'PLAN',
'PLI',
'POSITION',
'POSTFIX',
'POWER',
'PRECEDING',
'PRECISION',
'PREFIX',
'PREORDER',
'PREPARE',
'PREPARED',
'PRESERVE',
'PRIMARY',
'PRINT',
'PRIOR',
'PRIVILEGES',
'PROC',
'PROCEDURAL',
'PROCEDURE',
'PROCESS',
'PROCESSLIST',
'PUBLIC',
'PURGE',
'QUOTE',
'RAID0',
'RAISERROR',
'RANGE',
'RANK',
'RAW',
'READ',
'READS',
'READTEXT',
'REAL',
'RECHECK',
'RECONFIGURE',
'RECURSIVE',
'REF',
'REFERENCES',
'REFERENCING',
'REGEXP',
'REGR_AVGX',
'REGR_AVGY',
'REGR_COUNT',
'REGR_INTERCEPT',
'REGR_R2',
'REGR_SLOPE',
'REGR_SXX',
'REGR_SXY',
'REGR_SYY',
'REINDEX',
'RELATIVE',
'RELEASE',
'RELOAD',
'RENAME',
'REPEAT',
'REPEATABLE',
'REPLACE',
'REPLICATION',
'REQUIRE',
'RESET',
'RESIGNAL',
'RESOURCE',
'RESTART',
'RESTORE',
'RESTRICT',
'RESULT',
'RETURN',
'RETURNED_CARDINALITY',
'RETURNED_LENGTH',
'RETURNED_OCTET_LENGTH',
'RETURNED_SQLSTATE',
'RETURNS',
'REVOKE',
'RIGHT',
'RLIKE',
'ROLE',
'ROLLBACK',
'ROLLUP',
'ROUTINE',
'ROUTINE_CATALOG',
'ROUTINE_NAME',
'ROUTINE_SCHEMA',
'ROW',
'ROW_COUNT',
'ROW_NUMBER',
'ROWCOUNT',
'ROWGUIDCOL',
'ROWID',
'ROWNUM',
'ROWS',
'RULE',
'SAVE',
'SAVEPOINT',
'SCALE',
'SCHEMA',
'SCHEMA_NAME',
'SCHEMAS',
'SCOPE',
'SCOPE_CATALOG',
'SCOPE_NAME',
'SCOPE_SCHEMA',
'SCROLL',
'SEARCH',
'SECOND',
'SECOND_MICROSECOND',
'SECTION',
'SECURITY',
'SELECT',
'SELF',
'SENSITIVE',
'SEPARATOR',
'SEQUENCE',
'SERIALIZABLE',
'SERVER_NAME',
'SESSION',
'SESSION_USER',
'SET',
'SETOF',
'SETS',
'SETUSER',
'SHARE',
'SHOW',
'SHUTDOWN',
'SIGNAL',
'SIMILAR',
'SIMPLE',
'SIZE',
'SMALLINT',
'SOME',
'SONAME',
'SOURCE',
'SPACE',
'SPATIAL',
'SPECIFIC',
'SPECIFIC_NAME',
'SPECIFICTYPE',
'SQL',
'SQL_BIG_RESULT',
'SQL_BIG_SELECTS',
'SQL_BIG_TABLES',
'SQL_CALC_FOUND_ROWS',
'SQL_LOG_OFF',
'SQL_LOG_UPDATE',
'SQL_LOW_PRIORITY_UPDATES',
'SQL_SELECT_LIMIT',
'SQL_SMALL_RESULT',
'SQL_WARNINGS',
'SQLCA',
'SQLCODE',
'SQLERROR',
'SQLEXCEPTION',
'SQLSTATE',
'SQLWARNING',
'SQRT',
'SSL',
'STABLE',
'START',
'STARTING',
'STATE',
'STATEMENT',
'STATIC',
'STATISTICS',
'STATUS',
'STDDEV_POP',
'STDDEV_SAMP',
'STDIN',
'STDOUT',
'STORAGE',
'STRAIGHT_JOIN',
'STRICT',
'STRING',
'STRUCTURE',
'STYLE',
'SUBCLASS_ORIGIN',
'SUBLIST',
'SUBMULTISET',
'SUBSTRING',
'SUCCESSFUL',
'SUM',
'SUPERUSER',
'SYMMETRIC',
'SYNONYM',
'SYSDATE',
'SYSID',
'SYSTEM',
'SYSTEM_USER',
'TABLE',
'TABLE_NAME',
'TABLES',
'TABLESAMPLE',
'TABLESPACE',
'TEMP',
'TEMPLATE',
'TEMPORARY',
'TERMINATE',
'TERMINATED',
'TEXT',
'TEXTSIZE',
'THAN',
'THEN',
'TIES',
'TIME',
'TIMESTAMP',
'TIMEZONE_HOUR',
'TIMEZONE_MINUTE',
'TINYBLOB',
'TINYINT',
'TINYTEXT',
'TO',
'TOAST',
'TOP',
'TOP_LEVEL_COUNT',
'TRAILING',
'TRAN',
'TRANSACTION',
'TRANSACTION_ACTIVE',
'TRANSACTIONS_COMMITTED',
'TRANSACTIONS_ROLLED_BACK',
'TRANSFORM',
'TRANSFORMS',
'TRANSLATE',
'TRANSLATION',
'TREAT',
'TRIGGER',
'TRIGGER_CATALOG',
'TRIGGER_NAME',
'TRIGGER_SCHEMA',
'TRIM',
'TRUE',
'TRUNCATE',
'TRUSTED',
'TSEQUAL',
'TYPE',
'UESCAPE',
'UID',
'UNBOUNDED',
'UNCOMMITTED',
'UNDER',
'UNDO',
'UNENCRYPTED',
'UNION',
'UNIQUE',
'UNKNOWN',
'UNLISTEN',
'UNLOCK',
'UNNAMED',
'UNNEST',
'UNSIGNED',
'UNTIL',
'UPDATE',
'UPDATETEXT',
'UPPER',
'USAGE',
'USE',
'USER',
'USER_DEFINED_TYPE_CATALOG',
'USER_DEFINED_TYPE_CODE',
'USER_DEFINED_TYPE_NAME',
'USER_DEFINED_TYPE_SCHEMA',
'USING',
'UTC_DATE',
'UTC_TIME',
'UTC_TIMESTAMP',
'VACUUM',
'VALID',
'VALIDATE',
'VALIDATOR',
'VALUE',
'VALUES',
'VAR_POP',
'VAR_SAMP',
'VARBINARY',
'VARCHAR',
'VARCHAR2',
'VARCHARACTER',
'VARIABLE',
'VARIABLES',
'VARYING',
'VERBOSE',
'VIEW',
'VOLATILE',
'WAITFOR',
'WHEN',
'WHENEVER',
'WHERE',
'WHILE',
'WIDTH_BUCKET',
'WINDOW',
'WITH',
'WITHIN',
'WITHOUT',
'WORK',
'WRITE',
'WRITETEXT',
'X509',
'XOR',
'YEAR',
'YEAR_MONTH',
'ZEROFILL',
'ZONE'
]

def has_sql(cdn):
    """has_sql

    Args:
        cdn (): string

    Returns:
        bool : retorna true si el script contiene palabras reservadas de SQL
    """
    f = False
    for w in SQLLNG: 
        x = w.lower()
        if (re.search(w,cdn) == None) and (re.search(x,cdn) == None) :
            continue
        else:
            f = True
            break
    
    return f 
            
#----------------------------------------------------------------------------------------
#INSERT
def  insert_persona(values):
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
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
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT INTO  tercia(id_persona,id_equipo) VALUES (%s,%s);",(values['IdPersona'],values['idEqupol4']))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e

def  insert_equipo(values):
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
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
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
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
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
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
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
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
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
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
        conexion = pgdb.connect(host="localhost",database=nombredb ,user="postgres", password=pasword)#conectamos la base de datos
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

        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
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
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT INTO  programa(id_programa,code_problema,id_equipo,lenguaje_programacion,valido,tiempo_resolucion_minutos) VALUES (%s,%s,%s,%s,%s,%s);")
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e

def  insert_competencia(values):
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
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
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT INTO  competicion_local(code_competicion,cve_universidad) VALUES (%s,%s);")
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e

def  insert_competeregional(values):
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("INSERT ")
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e

def  insert_competeciamundial(values):
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
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
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM juez WHERE id_juez = %s",(id_juez,))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        sg.popup(e,title='UN ERROR HA OCURRIDO :|',image='xd.png')

def  delete_persona(id_persona):
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM persona WHERE id_persona = %s",(id_persona,))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        sg.popup(e,title='UN ERROR HA OCURRIDO :|',image='xd.png')

def  delete_tercia(id_persona):
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM tercia WHERE id_persona = %s;",(id_persona,))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        sg.popup(e,title='UN ERROR HA OCURRIDO :|',image='xd.png')

def  delete_problema(id_problem):
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM problema WHERE code_problema = %s",(id_problem,))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        sg.popup(e,title='UN ERROR HA OCURRIDO :|',image='xd.png')

def  delete_equipo(id_equipo):
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM equipo WHERE id_equipo = %s",(id_equipo,))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        sg.popup(e,title='UN ERROR HA OCURRIDO :|',image='xd.png')

def  delete_universidad(id_univ):
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM universidad WHERE cve_universidad = %s",(id_univ,))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        sg.popup(e,title='UN ERROR HA OCURRIDO :|',image='xd.png')

def  delete_FinalMundial(idFinalM):
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM final_mundial WHERE id_final_mundial = %s",(idFinalM,))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        sg.popup(e,title='UN ERROR HA OCURRIDO :|',image='xd.png')

def  delete_competencia(id):
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("DELETE FROM competicion WHERE code_competicion = %s",(id,))
        conexion.commit()
        cur.close()
        conexion.close()
    except Exception as e:
        sg.popup(e,title='UN ERROR HA OCURRIDO :|',image='xd.png')

#----------------------------------------------------------------------------------------
#Funciones Para mostrar las tablas  de la base de datos 
def ShowPersonaTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM persona;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table

def ShowTerciaTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM tercia;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table

def ShowJuezTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM juez;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table
    
def ShowEquipoTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM equipo;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table

def ShowUniversidadTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM universidad;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table

def ShowProblemaTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM problema;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table

def ShowCompeticionTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM competicion;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table    

def ShowPaisTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM pais;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table

def ShowRegionTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM region;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table

def ShowfinamundialTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM final_mundial;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table

def ShowprogramaTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM programa;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table

def ShowJuezCompTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM juez_competicion;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table

def ShowEquipoLocTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM equipo_local;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table

def ShowEquipoRegTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM equipo_regional;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table

def ShowEquipoMunTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM equipo_mundial;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table

def ShowCompeticionLocTable():
    x = []
    table = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute("SELECT * FROM competicion_local;")
        x = cur.fetchall()
        cur.close()
        conexion.close()
    except Exception as e:
        raise e
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    
    return table


#Funcionenes Extra 
def ExecuteQuery(q):
    """ExecuteQuery

    Args:
        q (string): string con la consulta a realizar

    Raises:
        e: excepcion si la conexion o la consulta a la base datos falla 

    Returns:
        list: retorna una lista de strings con las tuplas obtenidas de las consultas  
    """
    x = []
    desc = []
    table = []
    slist = []
    try:
        conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
        cur = conexion.cursor()
        cur.execute(q)
        x = cur.fetchall()
        desc = [desc[0] for desc in cur.description]
        cur.close()
        conexion.close()
    except Exception as e:
        sg.popup(e,title='UN ERROR HA OCURRIDO :|',image='xd.png')
    
    for i in range(0,len(x)):
        table.append(list(x[i]))
        
    slist.append(str(desc))
    
    for j in table:
        slist.append(str(j))
        
    return slist
#----------------------------------------------------------------------------------------
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
regions = ["SWERC","NWERC","CERC","SEERC","NEERC",
"AARPC","SAfrica","Beijing","Coim","Kolkata","Daca",
"Kaohsiun","Manila","Seúl","Teerán","Xian","Shanghái","Yokohama","Hanói","SPacific",
"CAmerica","Caribe","Brasil","Suramérica N","Suramérica S","PacNW",
"NCNA","ECNA","NENA","Rocky Mountain","MCUSA",
"GNY","Scal","SCUSA","SEUSA","MAUSA"]

def addcountries(c):
    
    conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
    cur = conexion.cursor()
    
    for i in range(0,len(c)):
        if len(c[i]) < 21:
            cur.execute("INSERT INTO  pais(id_pais,nombre) VALUES (%s,%s);",
                        (i,c[i]))
    
    conexion.commit()
    cur.close()
    conexion.close()
        
def addregion(r):
    
    conexion = pgdb.connect(host="localhost",database=nombredb, user="postgres", password=pasword)#conectamos la base de datos
    cur = conexion.cursor()
    
    for i in range(0,len(r)):
        if len(r[i]) < 21:
            cur.execute("INSERT INTO  region(id_region,id_pais,nombre) VALUES (%s,%s,%s);",
                        (i,random.randint(1,35),r[i]))
    
    conexion.commit()
    cur.close()
    conexion.close()
    
    


#Usar esta funcion para crear la tabla pais despues comentar la linea
#addcountries(Countries)
#addregion(regions)


#----------------------------------------------------------------------------------------
#Consultas previas para todas  las tablas 

#Persona
personlst = ShowPersonaTable()#Hacemos una consulta previa 
headerpersona = ['ID','NOMBRE','APELLIDO 1', 'APELLIDO 2', 'FECHA NACIMIENTO','TELEFONO','CORREO']
#tecia 
tercialst = ShowTerciaTable()#Hacemos una consulta previa 
headertercia = ['ID Persona','ID Equipo']
#juez
juezlst = ShowJuezTable()#Hacemos una consulta previa 
headerjuez = ['ID JUEZ','ID PERSONA','ESPECILIZACION', 'PUNTUACION']
#equipo
equipolst = ShowEquipoTable()#Hacemos una consulta previa 
headerequipo = ['ID','NOMBRE','CLAVE UNIVERSIDAD', 'ESTATUS']
#uniersidad
Universidadlst = ShowUniversidadTable()#Hacemos una consulta previa 
headerunviersidad = ['ID','NOMBRE','REGION']
#problema 
problemalst = ShowProblemaTable()#Hacemos una consulta previa 
headerproblema = ['ID','DESCRIPCION','TIPO']
#programa 
programlst = ShowprogramaTable()#Hacemos una consulta previa 
headerprogram = ['ID','ID PROBLEMA','ID EQUIPO', 'LENGUAJE','VALIDO','TIEMPO(MIN.)' ]
#juez competcion
juezcomplst = ShowJuezCompTable()#Hacemos una consulta previa 
headerjuezcomp = ['ID','ID JUEZ','CLAVE COMPETICION']
#equipo local
equipoloclst = ShowEquipoLocTable()#Hacemos una consulta previa 
headerequipoloc = ['ID','CLAVE COMPETICION','CLAVE UNIVERSIDAD']
#equipo regional
equiporeglst = ShowEquipoRegTable()#Hacemos una consulta previa 
headerequiporeg = ['ID EQUIPO','CLAVE COMPETICION']
#equipo mundial
equipomunlst = ShowEquipoMunTable()#Hacemos una consulta previa 
headerequipomun = ['ID FINAL','ID EQUIPO']
#competicion local
comptloclst = ShowCompeticionLocTable()#Hacemos una consulta previa 
headercomptloc = ['CLAVE COMPETICION','CLAVE UNIVERSIDAD']
#competicion
comptlst = ShowCompeticionTable()#Hacemos una consulta previa 
headercompt = ['CLAVE COMPETICION','DESCRIPCION','DURACION(HRS)', 'FECHA','NO. PROBLEMAS','ID REGION']
#final mundial
finalmunlst = ShowfinamundialTable()#Hacemos una consulta previa 
headerfinalmun = ['ID','CLAVE COMPETICION','FECHA', 'CIUDAD']
#region
regionlst = ShowRegionTable()#Hacemos una consulta previa 
headerregion = ['ID','ID PAIS','NOMBRE']
#pais 
paislst = ShowPaisTable()#Hacemos una consulta previa 
headerpais = ['ID','NOMBRE']



#----------------------------------------------------------------------------------------
#LAYOUTS 
sg.theme('LightGreen')
#Este layout contiene los elementos del menu principal --
layout0 = [[sg.Image('logo.png',key='logo1')],[sg.Text('ICPC',auto_size_text=True,font='Helvetica')],
        [sg.Button('AÑADIR REGISTRO',auto_size_button=True),sg.Button('BORRAR REGISTRO',auto_size_button=True),
        sg.Button('ACTUALIZAR REGISTRO',auto_size_button=True),sg.Button('QUERY TOOL',auto_size_button=True)],
        [sg.Button('MOSTRAR TABLAS',auto_size_button=True)]
        ]
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
           [ sg.Text('Estatus', font=('MS Sans Serif', 10, 'bold')), sg.Combo(['TRUE','FALSE'],key='-statusL5-',size=(30,30))],
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

#----------------------------------------------------------------------------------------
#Este layout corresponde al registro de una Universidad
layout8 = [[sg.Button('<-', key='-returnl1L8-'), sg.Text('AÑADIR UNA NUEVA UNIVERSIDAD A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Universidad', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDUniversidadL8-',size=(10,8))],
           [sg.Text('Nombre', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-NombreUniver-',size=(30,30))],
           [ sg.Text('Region', font=('MS Sans Serif', 10, 'bold')), sg.Combo(regions,key='-RegionL8-',size=(30,30))],
            [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregUniversidad-')]]

#----------------------------------------------------------------------------------------
#Este layout corresponde al registro de un problema
layout9 = [[sg.Button('<-', key='-returnl1L9-'), sg.Text('AÑADIR UNA NUEVO PROBLEMA COMPETENCIA A LA BASE DE DATOS',font='Helvetica')],
           [sg.Text('ID Problema', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-IDproblemaL9-',size=(10,8))],
           [sg.Text('Tipo', font=('MS Sans Serif', 10, 'bold')),sg.Input(key='-TipoL9-',size=(30,30))],
           [sg.Text('Descripcion', font=('MS Sans Serif', 10, 'bold'))],
           [sg.Multiline("",key='-DescProblem-',size=(50,8))],
           [sg.Button('Añadir Registro',auto_size_button=True,key='-AddregProblema-')]]

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
#----------------------------------------------------------------------------------------
#Este layout corresponde al borrado de una persona
layout21 = [[sg.Button('<-', key='-returnl20L21-'), sg.Text('BORRAR UNA PERSONA DE LA BASE DE DATOS',font='Helvetica')],
           [sg.Table(personlst,max_col_width=50,key='-TablaPersonaL21-',headings=headerpersona)],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeletePersona-')]]

#----------------------------------------------------------------------------------------
#Este layout corresponde al borrado de una tercia
layout22 = [[sg.Button('<-', key='-returnl20L22-'), sg.Text('BORRAR UNA TERCIA DE LA BASE DE DATOS',font='Helvetica')],
            [sg.Table(tercialst,max_col_width=50,key='-TablaTerciaL22-',headings=headertercia)],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeleteTercia-')]]

#----------------------------------------------------------------------------------------
#Este layout corresponde al borrado de una Juez
layout23 = [[sg.Button('<-', key='-returnl20L23-'), sg.Text('BORRAR UN JUEZ DE LA BASE DE DATOS',font='Helvetica')],
           [sg.Table(juezlst,max_col_width=50,key='-TablaJuezL23-',headings=headerjuez)],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeleteJuez-')]]

#----------------------------------------------------------------------------------------
#Este layout corresponde al borrado de una Equipo
layout24 = [[sg.Button('<-', key='-returnl20L24-'), sg.Text('BORRAR UN EQUIPO DE LA BASE DE DATOS',font='Helvetica')],
           [sg.Table(equipolst,max_col_width=50,key='-TablaEquipoL24-',headings=headerequipo)],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeleteEquipo-')]]

#----------------------------------------------------------------------------------------
#Este layout corresponde al borrado de una competencia
layout25 = [[sg.Button('<-', key='-returnl20L25-'), sg.Text('BORRAR UNA COMPETENCIA DE LA BASE DE DATOS',font='Helvetica')],
           [sg.Table(comptlst,max_col_width=50,key='-TablaCompeticionL25-',headings=headercompt)],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeleteCompetencia-')]]

#----------------------------------------------------------------------------------------
#Este layout corresponde al borrado de una universidad
layout26 = [[sg.Button('<-', key='-returnl20L26-'), sg.Text('BORRAR UNA UNIVERSIDAD DE LA BASE DE DATOS',font='Helvetica')],
           [sg.Table(Universidadlst,max_col_width=50,key='-TablaUniversidadL26-',headings=headerunviersidad)],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeleteUniversidad-')]]

#----------------------------------------------------------------------------------------
#Este layout corresponde al borrado de un Problema 
layout27 = [[sg.Button('<-', key='-returnl20L27-'), sg.Text('BORRAR UN PROBLEMA DE LA BASE DE DATOS',font='Helvetica')],
           [sg.Table(problemalst,max_col_width=50,key='-TablaProblemaL27-',headings=headerproblema)],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeleteProblema-')]]

#----------------------------------------------------------------------------------------
#Este layout corresponde al borrado de una Final Mundial
layout28 = [[sg.Button('<-', key='-returnl20L28-'), sg.Text('BORRAR UN EQUIPO DE LA BASE DE DATOS',font='Helvetica')],
            [sg.Table(finalmunlst,max_col_width=50,key='-TablaFinalMunL28-',headings=headerfinalmun)],
           [sg.Button('Borrar Registro',auto_size_button=True,key='-DeleteFinalM-')]]

#----------------------------------------------------------------------------------------
#layaouts para tablas 

layout100 = [[sg.Button('<-', key='-returnl0L100-'),sg.Image('logo.png',key='logo2')],[sg.Text('MOSTRAR REGISTROS DE LA BASE DE DATOS',auto_size_text=True,font='Helvetica')],
        [sg.Button('registros Persona', key='-Ptable-',auto_size_button=True),sg.Button('registros Pais',auto_size_button=True,key='-PaisButtontable-')],
        [sg.Button('registros Tercia', key='-Tertable-',auto_size_button=True),sg.Button('registros Region',auto_size_button=True,key='-RegionButtontable-')],
        [sg.Button('registros Equipo',auto_size_button=True,key='-Etable-')],
        [sg.Button('registros Juez',auto_size_button=True,key='-Jtable-')],
        [sg.Button('registros Universidad',auto_size_button=True,key='-Utable-')],
        [sg.Button('registros problema',auto_size_button=True,key='-Probtable-')],
        [sg.Button('registros programa',auto_size_button=True,key='-ProgramButtontable-')],
        [sg.Button('registros Juez Competencia',auto_size_button=True,key='-JuezComptable-')],
        [sg.Button('registros Equipo Local',auto_size_button=True,key='-LocalEquButtontable-')],
        [sg.Button('registros Equipo regional',auto_size_button=True,key='-RegionalEquButtontable-')],
        [sg.Button('registros Equipo Mundial',auto_size_button=True,key='-MundialEquButtontable-')],
        [sg.Button('registros Competencia Local',auto_size_button=True,key='-LocalCompButtontable-')],
        [sg.Button('registros Competencia',auto_size_button=True,key='-Ctable-')],
        [sg.Button('registros Final Mundial',auto_size_button=True,key='-WorldFinalButtontable-')]] 

#----------------------------------------------------------------------------------------
#Tabla Persona
layout101 = [[sg.Button('<-', key='-returnl100L101-'), sg.Text('REGISTROS TABLA PERSONA',font='Helvetica')],
             [sg.Table(personlst,max_col_width=50,key='-TablaPersona-',headings=headerpersona)]]
#----------------------------------------------------------------------------------------
#Tabla Tercia
layout102 = [[sg.Button('<-', key='-returnl100L102-'), sg.Text('REGISTROS TABLA TERCIA',font='Helvetica')],
             [sg.Table(tercialst,max_col_width=50,key='-TablaTercia-',headings=headertercia)]]
#----------------------------------------------------------------------------------------
#Tabla Juez
layout103 = [[sg.Button('<-', key='-returnl100L103-'), sg.Text('REGISTROS TABLA JUEZ',font='Helvetica')],
             [sg.Table(juezlst,max_col_width=50,key='-TablaJuez-',headings=headerjuez)]]
#----------------------------------------------------------------------------------------
#Tabla Equipo
layout104 = [[sg.Button('<-', key='-returnl100L104-'), sg.Text('REGISTROS TABLA EQUPO',font='Helvetica')],
             [sg.Table(equipolst,max_col_width=50,key='-TablaEquipo-',headings=headerequipo)]]
#----------------------------------------------------------------------------------------
#Tabla  Universidad
layout105 = [[sg.Button('<-', key='-returnl100L105-'), sg.Text('REGISTROS TABLA UNIVERSIDAD',font='Helvetica')],
             [sg.Table(Universidadlst,max_col_width=50,key='-TablaUniversidad-',headings=headerunviersidad)]]
#----------------------------------------------------------------------------------------
#Tabla  Problema 
layout106 = [[sg.Button('<-', key='-returnl100L106-'), sg.Text('REGISTROS TABLA PROBLEMA',font='Helvetica')],
             [sg.Table(problemalst,max_col_width=50,key='-TablaProblema-',headings=headerproblema)]]
#----------------------------------------------------------------------------------------
#Tabla  Program
layout107 = [[sg.Button('<-', key='-returnl100L107-'), sg.Text('REGISTROS TABLA PERSONA',font='Helvetica')],
             [sg.Table(programlst,max_col_width=50,key='-TablaPrograma-',headings=headerprogram)]]
#----------------------------------------------------------------------------------------
#Tabla Juez Competencia
layout108 = [[sg.Button('<-', key='-returnl100L108-'), sg.Text('REGISTROS TABLA JUEZ COMPETICION',font='Helvetica')],
             [sg.Table(juezcomplst,max_col_width=50,key='-TablaJuezComp-',headings=headerjuezcomp)]]
#----------------------------------------------------------------------------------------
#Tabla Equipo Local
layout109 = [[sg.Button('<-', key='-returnl100L109-'), sg.Text('REGISTROS TABLA EQUIPO LOCAL',font='Helvetica')],
             [sg.Table(equipoloclst,max_col_width=50,key='-TablaEquipoLoc-',headings=headerequipoloc)]]
#----------------------------------------------------------------------------------------
#Tabla Equipo Regional
layout110 = [[sg.Button('<-', key='-returnl100L110-'), sg.Text('REGISTROS TABLA EQUIPO REGIONAL',font='Helvetica')],
             [sg.Table(equiporeglst,max_col_width=50,key='-TablaEquipoReg-',headings=headerequiporeg)]]
#----------------------------------------------------------------------------------------
#Tabla Equipo Mundial
layout111 = [[sg.Button('<-', key='-returnl100L111-'), sg.Text('REGISTROS TABLA EQUIPO MUNDIAL',font='Helvetica')],
             [sg.Table(equipomunlst,max_col_width=50,key='-TablaEquipoMun-',headings=headerequipomun)]]
#----------------------------------------------------------------------------------------
#Tabla Competicion Local
layout112 = [[sg.Button('<-', key='-returnl100L112-'), sg.Text('REGISTROS TABLA COMPETICION LOCAL',font='Helvetica')],
             [sg.Table(comptloclst,max_col_width=50,key='-TablaCompeticionLoc-',headings=headercomptloc)]]
#----------------------------------------------------------------------------------------
#Tabla Competicion
layout113 = [[sg.Button('<-', key='-returnl100L113-'), sg.Text('REGISTROS TABLA COMPETICION',font='Helvetica')],
             [sg.Table(comptlst,max_col_width=50,key='-TablaCompeticion-',headings=headercompt)]]
#----------------------------------------------------------------------------------------
#Tabla Final Mundial
layout114 = [[sg.Button('<-', key='-returnl100L114-'), sg.Text('REGISTROS TABLA FINAL MUNDIAL',font='Helvetica')],
             [sg.Table(finalmunlst,max_col_width=50,key='-TablaFinalMun-',headings=headerfinalmun)]]
#----------------------------------------------------------------------------------------
#Tabla Region
layout115 = [[sg.Button('<-', key='-returnl100L115-'), sg.Text('REGISTROS TABLA REGION',font='Helvetica')],
             [sg.Table(regionlst,max_col_width=50,key='-TablaRegion-',headings=headerregion)]]
#----------------------------------------------------------------------------------------
#Tabla Pais
layout116 = [[sg.Button('<-', key='-returnl100L116-'), sg.Text('REGISTROS TABLA PAIS',font='Helvetica')],
             [sg.Table(paislst,max_col_width=50,key='-TablaPais-',headings=headerpais)]]
#----------------------------------------------------------------------------------------
#Layout para realizar consultas 
qlist = []
qheaders = ['None']

layoutq = [[sg.Button('<-', key='-returnl0Lq-'), sg.Text('HACER UNA CONSULTA A LA BASE DE DATOS',font='Helvetica')],
           [sg.Button('EJECUTAR',auto_size_button=True,key='-executequery-')],
           [sg.Multiline("",key='-scrpitSQL-',size=(100,15))],
           [sg.Combo(qlist,key='-TablaQuery-',size=(100,10))]]
#----------------------------------------------------------------------------------------
#Layout principal 
layout = [[sg.Column(layout=layout0,key='-COL{0}-',visible=True),sg.Column(layout=layout1,key='-COL{1}-',visible=False),sg.Column(layout=layout2,key='-COL{2}-',visible=False),
        sg.Column(layout=layout4,key='-COL{4}-',visible=False),sg.Column(layout=layout5,key='-COL{5}-',visible=False),sg.Column(layout=layout6,key='-COL{6}-',visible=False),
        sg.Column(layout=layout7,key='-COL{7}-',visible=False),sg.Column(layout=layout8,key='-COL{8}-',visible=False),sg.Column(layout=layout9,key='-COL{9}-',visible=False),
        sg.Column(layout=layout10,key='-COL{10}-',visible=False),sg.Column(layout=layout11,key='-COL{11}-',visible=False),sg.Column(layout=layout12,key='-COL{12}-',visible=False),
        sg.Column(layout=layout20,key='-COL{20}-',visible=False), sg.Column(layout=layout21,key='-COL{21}-',visible=False),sg.Column(layout=layout22,key='-COL{22}-',visible=False),
        sg.Column(layout=layout23,key='-COL{23}-',visible=False),sg.Column(layout=layout24,key='-COL{24}-',visible=False),sg.Column(layout=layout25,key='-COL{25}-',visible=False),
        sg.Column(layout=layout26,key='-COL{26}-',visible=False),sg.Column(layout=layout27,key='-COL{27}-',visible=False),sg.Column(layout=layout28,key='-COL{28}-',visible=False),
        sg.Column(layout=layout100,key='-COL{100}-',visible=False),sg.Column(layout=layout101,key='-COL{101}-',visible=False),sg.Column(layout=layout102,key='-COL{102}-',visible=False),
        sg.Column(layout=layout103,key='-COL{103}-',visible=False),sg.Column(layout=layout104,key='-COL{104}-',visible=False),sg.Column(layout=layout105,key='-COL{105}-',visible=False),
        sg.Column(layout=layout106,key='-COL{106}-',visible=False),sg.Column(layout=layout107,key='-COL{107}-',visible=False),sg.Column(layout=layout108,key='-COL{108}-',visible=False),
        sg.Column(layout=layout109,key='-COL{109}-',visible=False),sg.Column(layout=layout110,key='-COL{110}-',visible=False),sg.Column(layout=layout111,key='-COL{111}-',visible=False),
        sg.Column(layout=layout112,key='-COL{112}-',visible=False),sg.Column(layout=layout113,key='-COL{113}-',visible=False),sg.Column(layout=layout114,key='-COL{114}-',visible=False),
        sg.Column(layout=layout115,key='-COL{115}-',visible=False),sg.Column(layout=layout116,key='-COL{116}-',visible=False),sg.Column(layout=layoutq,key='-COL{1000}-',visible=False)]]
#Ventana
window = sg.Window(title="ICPC DATA BASE ADMIN", layout=layout,auto_size_buttons=True,auto_size_text=True,resizable=True)
#----------------------------------------------------------------------------------------
#Funciones para comprobar la validez de un registro
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

def PaisId(name,pais):
    for i in range(0,len(pais)):
        if pais[i] == name:
            return i
    return 0
       
def regionId(name,reg):
    
    for i in range(0,len(reg)):
        if reg[i] == name:
            return i
    
    return 1
    
    
#----------------------------------------------------------------------------------------
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
        print("Error al crear el registro persona")
        
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
        print("Error al crear el registro tercia")
        
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
        print("Error al crear el registro equipo")
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
        print("Error al crear el registro juez")
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
                     'Region' : regionId(values['-RegionL7-'],regions)}
        insert_competencia(reg_comp)
        print(reg_comp)
        window.Element('-IDpruebaL7-').update(value="")
        window.Element('-TiempoDuracion-').update(value="")
        window.Element('-Numproblemas-').update(value="")
        window.Element('-FechaRL7-').update(value="")
        window.find_element('-RegionL7-').update(value="")
    elif CheckCompetenciareg(values) == False and event == '-AddregCompetencia-':
        print("Error al crear el registro competencia")
#----------------------------------------------------------------------------------------       
    #este evento nos lleva a la interfaz de añadir registro de una universidad
    if event == '-UButton-':
        window['-COL{8}-'].update(visible=True)
        window['-COL{1}-'].update(visible=False)
    
    if event == '-AddregUniversidad-' and CheckUniversidadReg(values) == True:
        #{IDUniversidadL8,NombreUniver,RegionL8}  
        values_reg = values  
        reg_universidad = {'IdUniver' : values['-IDUniversidadL8-'],'Nombre' : values['-NombreUniver-'], 
                           'region' : regionId(values['-RegionL8-'],regions)}
        insert_Universidad(reg_universidad)
        print(reg_universidad)
        window.Element('-IDUniversidadL8-').update(value="")
        window.Element('-NombreUniver-').update(value="")
        window.find_element('-RegionL8-').update(value="")
    elif CheckUniversidadReg(values) == False and event == '-AddregUniversidad-':
        print("Error al crear el registro universidad")
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
        print("Error al crear el registro problema")
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
        print("Error al crear el registro Final Mundial")
    
#----------------------------------------------------------------------------------------
    #este evento nos lleva a la interfaz de borrar registros
    if event == 'BORRAR REGISTRO':
        window['-COL{20}-'].update(visible=True)
        window['-COL{0}-'].update(visible=False)

#----------------------------------------------------------------------------------------
    if event == '-PButtonDelete-':
        uperson = ShowPersonaTable() #Hacemos un update a los datos
        window['-TablaPersonaL21-'].update(values=uperson)
        window['-COL{21}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)
        
    if event == '-DeletePersona-' and len(str(values['-TablaPersonaL21-'])) > 0:
        idp = uperson[int(str(values['-TablaPersonaL21-'])[1])]
        delete_persona(idp[0])
        uperson = ShowPersonaTable() #Hacemos un update a los datos
        window['-TablaPersonaL21-'].update(values=uperson)
    elif event == '-DeletePersona-':
        print("Error al borrar registro")
        

#----------------------------------------------------------------------------------------
    if event == '-TerButtonDelete-':
        utercia = ShowTerciaTable() #Hacemos un update a los datos
        window['-TablaTerciaL22-'].update(values=utercia)
        window['-COL{22}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)
        
    if event == '-DeleteTercia-' and len(str(values['-TablaTerciaL22-'])) > 0 :
        print(values['-TablaTerciaL22-'])
        idt = utercia[int(str(values['-TablaTerciaL22-'])[1])]
        delete_tercia(idt[0])
        utercia = ShowTerciaTable() #Hacemos un update a los datos
    elif event == '-DeleteTercia-':
        print("Error al borrar registro")


 #----------------------------------------------------------------------------------------       
    if event == '-TButtonDelete-':
        uequipo = ShowEquipoTable() #Hacemos un update a los datos
        window['-TablaEquipoL24-'].update(values=uequipo)
        window['-COL{24}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)
        
    if event == '-DeleteEquipo-' and len(str(values['-TablaEquipoL24-'])) > 0 :
        idE = uequipo[int(str(values['-TablaEquipoL24-'])[1])]
        delete_equipo(idE)
        uequipo = ShowEquipoTable() #Hacemos un update a los datos
        window['-TablaEquipoL24-'].update(values=uequipo)
    elif event == '-DeleteEquipo-':
        print("Error al borrar registro")


#----------------------------------------------------------------------------------------    
    if event == '-JButtonDelete-':
        ujuez = ShowJuezTable() #Hacemos un update a los datos
        window['-TablaJuezL23-'].update(values=ujuez)
        window['-COL{23}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)

    if event == '-DeleteJuez-' and len(str(values['-TablaJuezL23-'])) > 0 :
        idJ = ujuez[int(str(values['-TablaJuezL23-'])[1])]
        delete_juez(values['-IdpersonaL23-'])
        ujuez = ShowJuezTable() #Hacemos un update a los datos
        window['-TablaJuezL23-'].update(values=ujuez)
    elif event == '-DeleteJuez-':
        print("Error al borrar registro")

#----------------------------------------------------------------------------------------
    if event == '-CButtonDelete-':
        ucomp = ShowCompeticionTable() #Hacemos un update a los datos
        window['-TablaCompeticionL25-'].update(values=ucomp)
        window['-COL{25}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)
           
    if event == '-DeleteCompetencia-' and len(values['-IdcomnpL25-']) > 0 :
        idc = ucomp[int(str(values['-TablaCompeticionL25-'])[1])]
        delete_competencia(idc)
        ucomp = ShowCompeticionTable() #Hacemos un update a los datos
        window['-TablaCompeticionL25-'].update(values=ucomp)
    elif event == '-CButtonDelete-':
        print("Error al borrar registro")

#----------------------------------------------------------------------------------------
    if event == '-UButtonDelete-':
        upuniver = ShowUniversidadTable() #Hacemos un update a los datos
        window['-TablaUniversidadL26-'].update(values=upuniver)
        window['-COL{26}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)
        

    if event == '-DeleteUniversidad-' and len(str(values['-TablaUniversidadL26-'])) > 0 :
        idu = upuniver[int(str(values['-TablaUniversidadL26-'])[1])]
        delete_universidad(idu)
        upuniver = ShowUniversidadTable() #Hacemos un update a los datos
        window['-TablaUniversidadL26-'].update(values=upuniver)
    elif event == '-DeleteUniversidad-':
        print("Error al borrar registro")


#----------------------------------------------------------------------------------------
    if event == '-ProblemButtonDelete-':
        uproblem = ShowProblemaTable() #Hacemos un update a los datos
        window['-TablaProblemaL27-'].update(values=uproblem)
        window['-COL{27}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)
        
    if event == '-DeleteProblema-' and len(str(values['-TablaProblemaL27-'])) > 0 :
        idp = uproblem [int(str(values['-TablaProblemaL27-'])[1])]
        delete_problema(idp)
        uproblem = ShowProblemaTable() #Hacemos un update a los datos
        window['-TablaProblemaL27-'].update(values=uproblem)
    elif event == '-DeleteProblema-':
        print("Error al borrar registro")
 #----------------------------------------------------------------------------------------   
    if event == '-WorldFinalButtonDelete-':
        ufinalm = ShowfinamundialTable() #Hacemos un update a los datos
        window['-TablaFinalMunL28-'].update(values=ufinalm)
        window['-COL{28}-'].update(visible=True)
        window['-COL{20}-'].update(visible=False)
        
    if event == '-DeleteFinalM-' and len(str(values['-TablaFinalMunL28-'])) > 0 :
        idfm = ufinalm[int(str(values['-TablaFinalMunL28-'])[1])]
        delete_FinalMundial(idfm)
        ufinalm = ShowfinamundialTable() #Hacemos un update a los datos
        window['-TablaFinalMunL28-'].update(values=ufinalm)
    elif event == '-DeleteFinalM-':
        print("Error al borrar registro")
#----------------------------------------------------------------------------------------

    if event == 'MOSTRAR TABLAS':
        window['-COL{100}-'].update(visible=True)
        window['-COL{0}-'].update(visible=False)
     
#----------------------------------------------------------------------------------------     
    if event == '-Ptable-':
        uperson = ShowPersonaTable() #Hacemos un update a los datos
        window['-TablaPersona-'].update(values=uperson)
        window['-COL{101}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
         
#----------------------------------------------------------------------------------------         
    if event == '-Tertable-':
        utercia = ShowTerciaTable() #Hacemos un update a los datos
        window['-TablaTercia-'].update(values=utercia)
        window['-COL{102}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
#----------------------------------------------------------------------------------------
        
    if event == '-Etable-':
        uequipo = ShowEquipoTable() #Hacemos un update a los datos
        window['-TablaEquipo-'].update(values=uequipo)
        window['-COL{104}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
         
#----------------------------------------------------------------------------------------      
    if event == '-Jtable-':
        ujuez = ShowJuezTable() #Hacemos un update a los datos
        window['-TablaJuez-'].update(values=ujuez)
        window['-COL{103}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
        
#----------------------------------------------------------------------------------------       
    if event == '-Utable-':
        upuniver = ShowUniversidadTable() #Hacemos un update a los datos
        window['-TablaUniversidad-'].update(values=upuniver)
        window['-COL{105}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
         
#----------------------------------------------------------------------------------------         
    if event == '-Probtable-':
        uproblem = ShowProblemaTable() #Hacemos un update a los datos
        window['-TablaProblema-'].update(values=uproblem)
        window['-COL{106}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
        
#----------------------------------------------------------------------------------------        
    if event == '-ProgramButtontable-':
        uprogram = ShowprogramaTable() #Hacemos un update a los datos
        window['-TablaPprograma-'].update(values=uprogram)
        window['-COL{107}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
         
#----------------------------------------------------------------------------------------         
    if event == '-JuezComptable-':
        ujuezcomp = ShowJuezCompTable() #Hacemos un update a los datos
        window['-TablaJuezComp-'].update(values=ujuezcomp)
        window['-COL{108}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
        
#----------------------------------------------------------------------------------------        
        
    if event == '-LocalEquButtontable-':
        uequloc = ShowEquipoLocTable() #Hacemos un update a los datos
        window['-TablaEquipoLoc-'].update(values=uequloc)
        window['-COL{109}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
#----------------------------------------------------------------------------------------         
         
    if event == '-RegionalEquButtontable-':
        uequreg = ShowEquipoRegTable() #Hacemos un update a los datos
        window['-TablaEquipoReg-'].update(values=uequreg)
        window['-COL{110}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
        
#----------------------------------------------------------------------------------------        
        
        
    if event == '-MundialEquButtontable-':
        uequmun = ShowEquipoMunTable() #Hacemos un update a los datos
        window['-TablaEquipoMun-'].update(values=uequmun)
        window['-COL{111}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
         
#----------------------------------------------------------------------------------------         
    if event == '-LocalCompButtontable-':
        ulocalcomp = ShowCompeticionLocTable() #Hacemos un update a los datos
        window['-TablaCompeticionLoc-'].update(values=ulocalcomp)
        window['-COL{112}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
#----------------------------------------------------------------------------------------        
        
        
    if event == '-Ctable-':
        ucomp = ShowCompeticionTable() #Hacemos un update a los datos
        window['-TablaCompeticion-'].update(values=ucomp)
        window['-COL{113}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
#----------------------------------------------------------------------------------------        
         
         
    if event == '-WorldFinalButtontable-':
        ufinalm = ShowfinamundialTable() #Hacemos un update a los datos
        window['-TablaFinalMun-'].update(values=ufinalm)
        window['-COL{114}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
#----------------------------------------------------------------------------------------        
        
    if event == '-PaisButtontable-':
        upais = ShowPaisTable() #Hacemos un update a los datos
        window['-TablaPais-'].update(values=upais)
        window['-COL{116}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
#----------------------------------------------------------------------------------------         
         
    if event == '-RegionButtontable-':
        uregion = ShowRegionTable() #Hacemos un update a los datos
        window['-TablaRegion-'].update(values=uregion)
        window['-COL{115}-'].update(visible=True)
        window['-COL{100}-'].update(visible=False)
#----------------------------------------------------------------------------------------
    
    if event == 'QUERY TOOL':
        window['-COL{1000}-'].update(visible=True)
        window['-COL{0}-'].update(visible=False)
        
        
    if event == '-executequery-' and len('-scrpitSQL-') > 0:
        quer = ExecuteQuery(values['-scrpitSQL-'])
        window['-TablaQuery-'].update(values=quer)
        #window['-TablaQuery-'].update(headings=quer[0])
        window['-COL{1000}-'].update(visible=True)
        window['-COL{0}-'].update(visible=False)
    
    
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
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl0L100-' and window['-COL{100}-'].visible == True:
        window['-COL{100}-'].update(visible=False)
        window['-COL{0}-'].update(visible=True)
        
     #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L101-' and window['-COL{101}-'].visible == True:
        #print(personlst[int(str(values['-TablaPersona-'])[1])])
        window['-COL{101}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L102-' and window['-COL{102}-'].visible == True:
        window['-COL{102}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L103-' and window['-COL{103}-'].visible == True:
        window['-COL{103}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L104-' and window['-COL{104}-'].visible == True:
        window['-COL{104}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L105-' and window['-COL{105}-'].visible == True:
        window['-COL{105}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L106-' and window['-COL{106}-'].visible == True:
        window['-COL{106}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L107-' and window['-COL{107}-'].visible == True:
        window['-COL{107}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L108-' and window['-COL{108}-'].visible == True:
        window['-COL{108}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L109-' and window['-COL{109}-'].visible == True:
        window['-COL{109}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L110-' and window['-COL{110}-'].visible == True:
        window['-COL{110}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L111-' and window['-COL{111}-'].visible == True:
        window['-COL{111}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L112-' and window['-COL{112}-'].visible == True:
        window['-COL{112}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L113-' and window['-COL{113}-'].visible == True:
        window['-COL{113}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L114-' and window['-COL{114}-'].visible == True:
        window['-COL{114}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L115-' and window['-COL{115}-'].visible == True:
        window['-COL{115}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl100L116-' and window['-COL{116}-'].visible == True:
        window['-COL{116}-'].update(visible=False)
        window['-COL{100}-'].update(visible=True)
        
        
    #Este evento nos regresa a la interfaz principal de añadir registros   
    if event == '-returnl0Lq-' and window['-COL{1000}-'].visible == True:
        window['-COL{1000}-'].update(visible=False)
        window['-COL{0}-'].update(visible=True)
        
    
        

    
    
        

    
    
window.close() #Cerramos la ventana

#C:\Users\sergi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts

# C:\Users\sergi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\pyinstaller.exe

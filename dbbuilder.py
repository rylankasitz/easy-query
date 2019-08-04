import dbmodelgenerator as db_gen
import user_lib.sqlexecution as sqlexecution
import _init_gen
import user_lib.logger as logger

import shutil
import inspect
import os
import types

def build_tables(database: str, tables: str):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    directory = os.path.abspath(os.path.dirname(__file__))
    
    if isinstance(tables, str):
        sqlexecution.run_sqlfile(database, tables, directory)
        db_gen.generate_model(database, tables, directory)
    else:
        for table in table:
            sqlexecution.run_sqlfile(table, directory)
            db_gen.generate_model(table, directory)
            
    _init_gen.build(directory)

def destroy_database(test: str):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    directory = os.path.abspath(os.path.dirname(__file__))
    if os.path.isdir(directory + "\\db\\" + test): 
        shutil.rmtree(directory + "\\db\\" + test)
        logger.log("removed database from directory " + directory + '/db/' + test)
            
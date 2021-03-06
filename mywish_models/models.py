from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from settings.settings_local import mywish_pg_engine

Base = automap_base()
engine = create_engine(mywish_pg_engine)
Base.prepare(engine, reflect=True)

UserSiteBalance = Base.classes.profile_usersitebalance
DUCXContract = Base.classes.contracts_ducxcontract
Contract = Base.classes.contracts_contract
Network = Base.classes.deploy_network

session = Session(engine)

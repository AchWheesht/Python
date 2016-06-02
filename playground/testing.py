import odbchelper
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(odbchelper.buildConnectionString(params))
server=mpilgrim;uid=sa;database=master;pwd=secret
print(odbchelper.buildConnectionString.__doc__)
#Build a connection string from a dictionary

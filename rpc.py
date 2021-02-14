import rpyc
import sys
 
if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))
 
server = sys.argv[1]
 
conn = rpyc.classic.connect(server)
conn.execute('scores = { "Team1" : 10 }')
conn.execute('scores["Team1"] += 1')
conn.execute('scores["Team2"] = 42')
 
local_scores = conn.eval('scores')
print(local_scores)         # {'Team1': 11, 'Team2': 42}
print(local_scores['Team1'])  # 11
 
conn.namespace["scores"]["Team2"] += 58
print(conn.eval('scores'))  # {'Team1': 11, 'Team2': 100}

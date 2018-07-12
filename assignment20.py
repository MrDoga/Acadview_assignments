#Q1.

import pandas as pd
data = {'name':["ram","shyam","bob","tom","lulia"],
        'age':[21,23,24,25,26],
        'e_mail':["ram123@gmail.com","shyam235@rocketmail.com","bob45@rediffmail.com","tom567@msn.com","lulia678@yahoo.com"],
        'phone_no.':[6123561,25346354,456546345,9995465467,23545734]
        }
df = pd.DataFrame(data)
df.loc[5] = [25,"aweadf@gmail.com","hoho",5464523]#adds a new row at a particular index
print df


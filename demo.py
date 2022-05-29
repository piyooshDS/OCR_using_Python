import demjson,axon
import yaml
import json


l=[  
   {  
      "Transaction":"Creditcard\u00ad5412839702037112",
      "null":[  
         ""
      ],
      "Credit":"",
      "Debit":"\u00ad2,000.00",
      "Date":"01/12/2015",
      "Balance":"14,347.00"
   },
   {  
      "Transaction":"ATM CASH 5412820015371620",
      "null":[  
         ""
      ],
      "Credit":"",
      "Debit":"\u00ad2,000.00",
      "Date":"01/12/2015",
      "Balance":"12,347.00"
   },
   {  
      "Transaction":"PNP FRAN DOUGL5412820015371620",
      "null":[  
         ""
      ],
      "Credit":"",
      "Debit":"\u00ad1,741.27",
      "Date":"01/12/2015",
      "Balance":"10,605.73"
   },
   {  
      "Transaction":"PNP FRAN DOUGL5412820015371620",
      "null":[  
         ""
      ],
      "Credit":"",
      "Debit":"\u00ad103.34",
      "Date":"01/12/2015",
      "Balance":"10,502.39"
   },
   {  
      "Transaction":"PNP FRAN DOUGL5412820015371620",
      "null":[  
         ""
      ],
      "Credit":"",
      "Debit":"\u00ad85.48",
      "Date":"01/12/2015",
      "Balance":"10,416.91"
   }
]

d=str(l).decode('utf8').replace("'", '"')
print(d)
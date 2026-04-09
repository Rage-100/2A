from pgmpy.models import BayesianNetwork 
from pgmpy.factors.discrete import TabularCPD 
from pgmpy.inference import VariableElimination 
  
model = BayesianNetwork([('Smoking', 'Disease'), ('Pollution', 'Disease')]) 
model.add_cpds( 
    TabularCPD('Smoking', 2, [[0.7], [0.3]]), 
    TabularCPD('Pollution', 2, [[0.6], [0.4]]), 
    TabularCPD('Disease', 2, 
               [[0.9, 0.7, 0.8, 0.1], 
                [0.1, 0.3, 0.2, 0.9]], 
               evidence=['Smoking', 'Pollution'], 
               evidence_card=[2, 2]) 
) 
  
if model.check_model(): 
    
    result = VariableElimination(model).query( 
        variables=['Disease'], 
        evidence={'Smoking': 1, 'Pollution': 1}, 
        show_progress=False   
    ) 
    print(result)

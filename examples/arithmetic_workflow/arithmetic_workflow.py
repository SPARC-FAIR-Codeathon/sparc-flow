from sparc_flow import Workflow 

with Workflow() as wf:
  wf.load(steps_dir='examples/arithmetic_workflow/tools')

  num1 = wf.add_input(num1='int')
  num2 = wf.add_input(num2='int')

  answer1 = wf.add(x=num1, y=num2) 
  answer2 = wf.multiply(x=answer1, y=num2)

  wf.add_outputs(final_answer=answer2) 

  wf.save('examples/arithmetic_workflow/arithmetic_workflow.cwl', mode='abs')   

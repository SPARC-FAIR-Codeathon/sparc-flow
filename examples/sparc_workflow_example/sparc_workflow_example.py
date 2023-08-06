from sparc_flow import Workflow 

# CWL Workflow to download a SPARC dataset and process it 
with Workflow() as wf: 
  # Load the tools
  wf.load(steps_dir='examples/sparc_workflow_example/tools')

  # Add dataset number as input
  number = wf.add_input(number='int') 

  # Run the tool
  answer1 = wf.sparc_data_tool(number=number) 

  wf.add_outputs(final_answer=answer1) 

  wf.save('sparc_workflow_example.cwl', mode='abs')   

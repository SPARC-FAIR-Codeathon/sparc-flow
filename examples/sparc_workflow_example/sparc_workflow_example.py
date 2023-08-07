from sparc_flow import Workflow 

if __name__ == '__main__':

  # CWL Workflow to download a SPARC dataset and process it 
  with Workflow() as wf: 
    # Load the tools
    wf.load(steps_dir='examples/sparc_workflow_example/tools') 
    
    # Add instruction to add SPARC dataset number in the cwl file as an input to the tool.
    number = wf.add_input(number='int')

    # Add instruction to run the tool in the cwl file
    answer1 = wf.sparc_data_tool(number=number)

    # Add instruction set the output of the workflow step as a file
    wf.add_outputs(final_answer=answer1)

    wf.save('sparc_workflow_example.cwl', mode='abs')


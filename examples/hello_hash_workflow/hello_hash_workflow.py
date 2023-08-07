from sparc_flow import Workflow

# Path: sparc_flow/core/example/cwl_arithmetic_workflow.py 

# workflow = Workflow() #language="cwl")   

from scriptcwl import WorkflowGenerator 
workflow = WorkflowGenerator()

with workflow as wf:  
    wf.load(steps_dir="example/hello_hash_workflow/") 

    users_name = wf.add_input(users_name='string')   

    hashed_name = wf.hash_users_name(name=users_name) 

    greet_user = wf.greet_user(name=hashed_name)

    wf.add_outputs(final_answer = greet_user)
    wf.save("hello_hash_workflow.cwl")

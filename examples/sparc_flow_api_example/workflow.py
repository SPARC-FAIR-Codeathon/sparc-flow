import sparc_flow 

workflow = sparc_flow.Workflow()
workflow.set_steps(tool_path="./examples/sparc_flow_api_example/tools") 
workflow.set_input_value(input_value = 262, input_name = "number", input_type = "int")
workflow.generate_description() 
workflow.create_sds("./resources/generated_datasets/workflow_dataset", "./examples/sparc_flow_api_example/")

workflow.run()
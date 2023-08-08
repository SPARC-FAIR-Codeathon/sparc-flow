import sparc_flow

tool = sparc_flow.Tool()  
tool.set_tool_name("sparc_data_tool") 
tool.set_tool_dir("examples/sparc_flow_api_example/tools")
tool.set_command(["python", "-m", "examples.sparc_workflow_example.tools.sparc_data_tool"])
tool.set_input_type("int")
tool.set_output_type("File")
tool.set_output_path("output.txt")
tool.generate_description()
tool.create_sds("./resources/generated_datasets/tools_dataset", "./examples/sparc_flow_api_example/tools/")
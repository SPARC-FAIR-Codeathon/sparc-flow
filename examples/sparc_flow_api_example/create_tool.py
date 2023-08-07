import sparc_flow

tool = sparc_flow.Tool()  
tool.set_tool_name("sparc_data_tool") 
tool.set_tool_dir("tools")
tool.set_command(["python", "-m", "tools.sparc_data_tool"])
tool.set_input_type("int")
tool.set_output_type("File")
tool.set_output_path("output.txt")
tool.generate_description()
# tool.generate_sds()
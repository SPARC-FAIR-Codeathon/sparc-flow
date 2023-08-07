from scriptcwl import WorkflowGenerator
from sparc_me import Dataset
import subprocess
import os

class Workflow(WorkflowGenerator):   
    def __init__(self, language="cwl"):   
        super().__init__()
        if language == "cwl": 
            pass
        else: 
            raise NotImplementedError("Only CWL is supported at this time.")    
        
        self.input_step = None
        self.input_value = None 
        self.input_name = None
        self.tool_dir = None   
        self.tools = None

    def set_steps(self, tool_path):  
        self.load(steps_dir=tool_path) 
        self.tool_dir = tool_path  
        tools = [tool for tool in os.listdir(tool_path) if tool.endswith(".cwl")] 
        self.tools = [tool.split(".")[0] for tool in tools] 

    def set_input_value(self, input_value, input_name, input_type):   
        self.input_step = self.add_input(number=str(input_type)) # number is hard coded for now, but needs to be set to input_name
        self.input_value = input_value   
        self.input_name = input_name
    
    def generate_description(self):   
        tool_output = self.input_step 

        # for tool in self.tools:  
        #     tool_method = getattr(self, tool)   
        #     tool_output = tool_method(tool_output)  

        tool_output = self.sparc_data_tool(number=tool_output)  # sparc_data_tool is hard coded for now, but need to dynamically call 
                                                                # tool methods of workflow object based of tool name (str)

        self.add_outputs(final_answer=tool_output) 
        self.save(f'{self.tool_dir}/workflow.cwl', mode='abs')    

    def create_sds(self, path):
        dataset_tool = Dataset()
        version = "2.0.0"
        dataset_tool.load_from_template(version)
        save_dir= path
        dataset_tool.set_dataset_path(save_dir)
        dataset_tool.save(save_dir)


         
    def run(self, runner="cwltool"):  

         # subprocess.run(['cwltool', 
        #                 f'{self.tool_dir}/workflow.cwl', 
        #                 f'--{self.input_name}', str(self.input_value)]) 
     
        if(runner == "dockstore"):
            subprocess.run(['dockstore', 
                            'workflow', 
                            'launch',
                            '--local-entry'
                        f'{self.tool_dir}/workflow.cwl', 
                            '--json',
                        f'{self.tool_dir}/inp_job.json']) 
        else:
            subprocess.run(['cwltool', 
                            f'{self.tool_dir}/workflow.cwl', 
                            f'{self.tool_dir}/inp_job.json']) 
    


class Tool:
    def __init__(self):
        self.tool_name = None
        self.command = ""
        self.arguments = []
        self.input_type = None
        self.output_type = None
        self.output_path = "" 
        self.tool_dir = None
    def set_tool_name(self, tool_name): 
        self.tool_name = tool_name 

    def set_command(self, command):
        self.command = command

    def set_arguments(self, arguments):
        self.arguments = arguments

    def set_input_type(self, input_type):
        self.input_type = input_type

    def set_output_type(self, output_type):
        self.output_type = output_type

    def set_output_path(self, output_path):
        self.output_path = output_path 
    
    def set_tool_dir(self, tool_dir): 
        self.tool_dir = tool_dir

    def generate_description(self):
        description = f"""#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: {self.command}

inputs:
    number:
        type: {self.input_type}
        inputBinding:
            position: 1 

outputs:
    output_file:
        type: {self.output_type}
        outputBinding:
            glob: {self.output_path}
                            """
        
        with open(f'{self.tool_dir}/{self.tool_name}.cwl', 'w') as f:
            f.write(description) 
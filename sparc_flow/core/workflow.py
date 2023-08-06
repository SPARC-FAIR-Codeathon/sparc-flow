from scriptcwl import WorkflowGenerator


class Workflow:   
    def __init__(self, language="cwl"): 
        if language == "cwl":
            self.wf = WorkflowGenerator()  
        else: 
            raise NotImplementedError("Only CWL is supported at this time.")
        
    def __enter__(self): 
        return self.wf
    
    def __exit__(self, exc_type, exc_value, traceback): 
        pass 

    def load(self, steps_dir): 
        pass 

    def add_input(self, name, type): 
        pass 

    def add_outputs(self, name, type): 
        pass 

    def save(self, filename): 
        pass 
        

from scriptcwl import WorkflowGenerator

class Workflow(WorkflowGenerator):   
    def __init__(self, language="cwl"):   
        super().__init__()
        if language == "cwl": 
            pass
        else: 
            raise NotImplementedError("Only CWL is supported at this time.")
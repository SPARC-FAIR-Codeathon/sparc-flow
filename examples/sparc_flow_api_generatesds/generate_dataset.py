import sparc_flow
import shutil

workflow = sparc_flow.Workflow()
tool = sparc_flow.Tool()
# shutil.copytree("./examples/sparc_flow_api_example/tools/", "./resources/generated_datasets/tools_dataset/primary/tools")
tool.create_sds("./resources/generated_datasets/tools_dataset", "./examples/sparc_flow_api_example/tools/")

workflow.create_sds("./resources/generated_datasets/workflow_dataset", "./examples/sparc_flow_api_example/")
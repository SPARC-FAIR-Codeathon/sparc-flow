import sparc_flow
import shutil

workflow = sparc_flow.Workflow()
tool = sparc_flow.Tool()
# shutil.copytree("./examples/sparc_flow_api_example/tools/", "./resources/generated_datasets/tools_dataset/primary/tools")
tool.create_sds("./resources/generated_datasets/tools_dataset", "./examples/sparc_flow_api_example/tools/")

workflow.create_sds("./resources/generated_datasets/workflow_dataset", "./examples/sparc_flow_api_example/")

res = workflow.load_workflow("./resources/generated_datasets/workflow_dataset/primary/workflow")

workflow.run()

workflow.run(runner="dockstore")

workflow.generate_dockstore_github_requirements("/workflow.cwl", res["workflow_path"], ["/inp_job.yml"],"Linkun Gao", "hsgshn@gmail.com")
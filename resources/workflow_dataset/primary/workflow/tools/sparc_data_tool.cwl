#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "examples.sparc_workflow_example.tools.sparc_data_tool"]

inputs:
  number:
    type: int
    inputBinding:
      position: 1 

outputs:
  output_file:
    type: File
    outputBinding:
      glob: "output.txt"

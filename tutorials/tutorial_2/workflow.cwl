#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: Workflow
inputs:
  number: int
outputs:
  final_answer:
    outputSource: sparc_data_tool/output_file
    type: File
steps:
  sparc_data_tool:
    run: /home/mfre190/src/2023-team-3/tutorials/tutorial_2/tools/sparc_data_tool.cwl
    in:
      number: number
    out:
    - output_file

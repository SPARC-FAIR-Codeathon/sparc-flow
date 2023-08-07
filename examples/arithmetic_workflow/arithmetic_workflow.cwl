#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: Workflow
inputs:
  num1: int
  num2: int
outputs:
  final_answer:
    outputSource: multiply/answer
    type: int
steps:
  add:
    run: /home/mfre190/src/2023-team-3/examples/arithmetic_workflow/tools/add.cwl
    in:
      x: num1
      y: num2
    out:
    - answer
  multiply:
    run: /home/mfre190/src/2023-team-3/examples/arithmetic_workflow/tools/multiply.cwl
    in:
      x: add/answer
      y: num2
    out:
    - answer

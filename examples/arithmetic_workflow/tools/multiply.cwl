#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "examples.arithmetic_workflow.tools.multiply"]

inputs:
  x:
    type: int
    inputBinding:
      position: 1
  y:
    type: int
    inputBinding:
      position: 2

stdout: cwl.output.json

outputs:
  answer:
    type: int

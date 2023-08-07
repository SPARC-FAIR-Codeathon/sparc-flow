#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "-m", "examples.hello"]

inputs:
  x:
    type: str
    inputBinding:
      position: 1

stdout: cwl.output.json

outputs:
  answer:
    type: int
cwlVersion: v1.0
class: CommandLineTool
baseCommand: python3
inputs:
  script:
    type: File?
    inputBinding:
      position: 1
      loadContents: true
outputs:
  output:
    type: stdout
stdout: output.txt


# How to run workflow example

- Environment setup
  - python: v3.9 or above
  - install requirements
    ```bash
        pip install -r requirements.txt
    ```
- Run example `Hello world`
  ```bash
      cwltool hello_world.cwl inp_job.yml
  ```

# How to setup dockstore locally and run cwl workflow

- General for both users (Linux/Ubuntu/MacOS)

  - Recommond use conda to create an env for dockstore
    ```bash
      conda create --name cwl-dockstore-env python=3.9
      conda activate cwl-dockstore-env
    ```
  - All python related things (include pip install) should run in this env, highly recommand you to install guideline Part 5 python requirements.txt. If not, you may get cwltool version error.
  - Then all CWL workflow can run in this env

- For the Linux/Ubuntu user should follow Dockstore [guideline](https://dockstore.org/quick-start)

- For MacOS user also should follow Dockstore [guideline](https://dockstore.org/quick-start)

  - But, we should noticed, in official guideline said we should install `Java 11`, this is not correctly! We need download Java 17 or above.
  - Also for the MacOS uers, if your terminal is zsh rather than bash, you cannot fully setup guideline Part 2, what you can do is:

  ```bash
    echo $SHELL # check current shell
    chsh -s /bin/zsh # switch to zsh
    chsh -s /bin/bash # swithc to bash
  ```

  - If you meet error to run `chmod +x ~/bin/dockstore`
    ```bash
      sudo chmod +x ~/bin/dockstore
    ```

- How to run dockstore locally with CWL
  - cd in example folder
    ```bash
      cd 2023-team-3/examples/workflow_examples
    ```
  - Make sure you python env activate
    ```bash
      conda activate cwl-dockstore-env
      dockstore --version # check if dockstore is work or not
    ```
  - Then run the dockstore code:
    ```bash
      dockstore tool launch --local-entry hello_world.cwl --yaml inp_job.yml
    ```
  - After run the code:
    - It will generate a datastore folder.
    - Then you can find your inputs and outputs under that folder.

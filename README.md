# SPARC Flow (sparc-flow)
A Python tool to describe and run tools and workflows for processing SPARC datasets in accordance with FAIR principles.

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/SPARC-FAIR-Codeathon/2023-team-3.svg)](https://GitHub.com/SPARC-FAIR-Codeathon/2023-team-3/issues?q=is%3Aissue+is%3Aclosed)
[![Issues][issues-shield]][issues-url]
[![apache License][license-shield]][license-url]
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)
<!--* [![DOI](https://zenodo.org/badge/XXXX.svg)](https://zenodo.org/badge/latestdoi/XXXXX) -->
[![PyPI version fury.io](https://badge.fury.io/py/sparc-flow.svg)](https://pypi.python.org/pypi/sparc-flow/)

[contributors-shield]: https://img.shields.io/github/contributors/SPARC-FAIR-Codeathon/2023-team-3.svg?style=flat-square
[contributors-url]: https://github.com/SPARC-FAIR-Codeathon/2023-team-3/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/SPARC-FAIR-Codeathon/2023-team-3.svg?style=flat-square
[stars-url]: https://github.com/SPARC-FAIR-Codeathon/2023-team-3/stargazers
[issues-shield]: https://img.shields.io/github/issues/SPARC-FAIR-Codeathon/2023-team-3.svg?style=flat-square
[issues-url]: https://github.com/SPARC-FAIR-Codeathon/2023-team-3/issues
[license-shield]: https://img.shields.io/github/license/SPARC-FAIR-Codeathon/2023-team-3.svg?style=flat-square
[license-url]: https://github.com/SPARC-FAIR-Codeathon/2023-team-3/blob/master/LICENSE
[lines-of-code-shield]: https://img.shields.io/tokei/lines/github/SPARC-FAIR-Codeathon/2023-team-3
[lines-of-code-url]: #

## Table of contents
* [About](#about)
* [Introduction](#introduction)
* [The problem](#the-problem)
* [Our solution - sparc-flow](#our-solution---sparc-flow)
* [Impact](#impact)
* [Setting up sparc-flow](#setting-up-sparc-flow)
* [Using sparc-flow](#using-sparc-flow)
* [Reporting issues](#reporting-issues)
* [Contributing](#contributing)
* [Cite us](#cite-us)
* [FAIR practices](#fair-practices)
* [License](#license)
* [Team](#team)
* [Acknowledgements](#acknowledgements)

## About
This is the repository of Team sparc-flow (Team #3) of the 2023 SPARC Codeathon. Click [here](https://sparc.science/help/2023-sparc-fair-codeathon) to find out more about the SPARC Codeathon 2024. Check out the [Team Section](#team) of this page to find out more about our team members.

No work was done on this project prior to the Codeathon.

## Introduction
The NIH Common Fund program on **[Stimulating Peripheral Activity to Relieve Conditions (SPARC)](https://commonfund.nih.gov/sparc) focuses on understanding peripheral nerves** (nerves that connect the brain and spinal cord to the rest of the body), **how their electrical signals control internal organ function**, and **how therapeutic devices could be developed to modulate electrical activity in nerves to improve organ function**. This may provide a potentially powerful way to treat a diverse set of common conditions and diseases such hypertension, heart failure, gastrointestinal disorders, and more. 60 research groups spanning 90 institutions and companies contribute to SPARC and work across over 15 organs and systems in 8 species.

**The [SPARC Portal](http://sparc.science/) provides a single user-facing online interface to resources** that can be shared, cited, visualized, computed, and used for virtual experimentation. A **key offering** of the portal is the **collection of well-curated datasets in a standardised format, including anatomical and computational models** that are being generated both SPARC-funded researchers and the international scientific community. These datasets can be found under the "[Find Data](https://sparc.science/data?type=dataset)" section of the SPARC Portal. Information regarding [how to navigate a SPARC dataset](https://docs.sparc.science/docs/navigating-a-sparc-dataset) and [how a dataset is formatted](https://docs.sparc.science/docs/overview-of-sparc-dataset-format) can be found on the SPARC Portal.

Workflows can be developed that apply tools (e.g. segmentation of images, or running of computational physiology simulations) in a series of steps to process the original data and generate new results, outcomes, and knowledge. These results (derived data) can be stored in a new standardised dataset and also be [contributed to the SPARC Portal](https://docs.sparc.science/docs/submitting-a-dataset-to-sparc) to support further scientific advances.

## The problem
There is **currently no option for**:
- **enabling users to easily describe and run workflows that use SPARC data locally or in cloud computing platforms**
- **ensuring reproducibility of workflow results**
- **enabling reuse of tools developed for processing SPARC data to create new workflows** (tools are currently bundled within and tailored to specific SPARC datasets)

This limits the ability of members of the SPARC and the wider scientific community to apply FAIR principles for:

## Our solution - sparc-flow
To address this problem, we have **developed a Python module called the SPARC Flow (sparc-flow)** that can be used to describe tools and workflows for processing SPARC datasets in accordance with FAIR principles by:

- Enabling tools to be stored in 
sparc-flow provides:

API to easily create workflows using standard language e.g. CWL format and store them in SDS format
API to create tool (workflow step) descriptions and store them in SDS format
Tutorials on how to run the workflows locally, on seven bridges, o2sparc
Best practices to make workflows and tools FAIR

executors supporting multiple backends, leading to GA4GH standards (like TES and WES- minimal APIs describing how a user submits a tool/workflow to an execution engine in a standardized way)

Supported by [58 organisations](https://dockstore.org/organizations) including: 

Workflow language agnostic implementation (support for WDL, Nextflow etc will be included in the future)

Examples and guided tutorials have been created to demonstrate each of the features above. 

Dockstore enable the creation of reproducible workflows and tools

## Impact & Vision

Making it easy for researchers to package tools and create workflows
Enable interoperability
Programmatically creating workflows

Future developments can include:
- Providing a mechanism to
- 


## Setting up sparc-flow

### Pre-requisites 
- [Git](https://git-scm.com/)
- Python. Tested on:
   - 3.9
   
### PyPI

Here is the [link](https://pypi.org/project/sparc-flow/) to our project on PyPI
```
pip install sparc-flow
```

### From source code

#### Downloading source code
Clone the sparc-flow repository from github, e.g.:
```
git clone git@github.com:SPARC-FAIR-Codeathon/2023-team-3.git
```

#### Installing dependencies

1. Setting up a virtual environment (optional but recommended). 
   In this step, we will create a virtual environment in a new folder named **venv**, 
   and activate the virtual environment.
   
   * Linux
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
   
   * Windows
   ```
   python3 -m venv venv
   venv\Scripts\activate
   ```
   
2. Installing dependencies via pip
    ```
    pip install -r requirements.txt
    ```

## Using sparc-flow

### Running tutorials

Guided tutorials have been developed describing how to use sparc-flow in different scenarios:

<table>
<thead>
  <tr>
    <th> Tutorial</th>
    <th> Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/sparc-flow/blob/main/tutorials/tutorial_1_download_data_and_postprocess.ipynb">
    1
    </a></td>
    <td> Creating a workflow (using a simple python script) that downloads an existing curated SDS dataset from the SPARC portal (<a href="https://doi.org/10.26275/vm1h-k4kq">Electrode design characterization for electrophysiology from swine peripheral nervous system</a>) using sparc-me and perform post-processing to generate a new derived SDS dataset.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2023-team-3/blob/main/examples/tutorial_2_creating_standarised_workflow_description.ipynb">
    2
    </a></td>
    <td> Use sparc-flow to programmatically create the workflow described in Tutorial 1 in a standard workflow language (CWL). This tutorial incorporates best practice guidelines to ensure workflows are FAIR.
    </td>
  </tr>
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2023-team-3/blob/main/examples/tutorial_3_running_locally_with_cwltool.ipynb">
    3
    </a></td>
    <td> Use sparc-flow to run the standardised workflow described in Tutorial 2 locally using cwltool (reference implementation provided by the CWL Organisation).</td>
  </tr>
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2023-team-3/blob/main/examples/tutorial_4_running_locally_with_docstore.ipynb">
    4
    </a></td>
    <td> Use sparc-flow to run the standardised workflow described in Tutorial 2 locally using Dockstore.</td>
  </tr> 
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2023-team-3/blob/main/examples/tutorial_5_running_on_dockstore_compatiable_cloud.ipynb">
    5
    </a></td>
    <td> Use sparc-flow to run the standardised workflow described in Tutorial 2 via the cloud using a Dockstore-compatible cloud computing platform (e.g. SevenBridges, Terra, DNAStack, DNA Nexus, NHLBI BioData Catalyst, Galaxy, AnVIL). </td>
  </tr>
  <tr>
    <td><a href="https://github.com/SPARC-FAIR-Codeathon/2023-team-3/blob/main/examples/tutorial_6_running_on_oSPARC.ipynb">
    6
    </a></td>
    <td> Use sparc-flow to run the standardised workflow described in Tutorial 2 on oSPARC.</td>
  </tr>   
  <tr>
    <td>
    7
    </td>
    <td> Use sparc-flow to run the standardised workflow described in Tutorial 2 on the 12 Labours Digital Twin Platform (TBC).</td>
  </tr>      
</tbody>
</table>
<p align="center">
</p>
<br/>

### Running examples

## Reporting issues 
To report an issue or suggest a new feature, please use the [issues page](https://github.com/SPARC-FAIR-Codeathon/2023-team-3/issues). Please check existing issues before submitting a new one.

## Contributing
Fork this repository and submit a pull request to contribute. Before doing so, please read our [Code of Conduct](https://github.com/SPARC-FAIR-Codeathon/2023-team-3/blob/main/CODE_OF_CONDUCT.md) and [Contributing Guidelines](https://github.com/SPARC-FAIR-Codeathon/2023-team-3/blob/main/CONTRIBUTING.md). Please add a GitHub Star to support developments!

### Project structure
* `/sparc_flow/` - Parent directory of sparc-flow python module.
* `/resources/` - Resources for testing sparc_flow.
* `/sparc_flow/core/` - Core classes of sparc-flow.
* `/examples/` - Parent directory of sparc-flow examples and tutorials.
* `/examples/test_data/` - Test data used for sparc-flow examples and tutorials.
* `/docs/images/` - Images used in sparc-flow tutorials.

## Cite us
If you use sparc-flow to make new discoveries or use the source code, please cite us as follows:
```
Jiali Xu, Linkun Gao, Michael Hoffman, Matthew French, Thiranja Prasad Babarenda Gamage, Chinchien Lin (2023). sparc-flow: v1.0.0 - A Python tool to create tools and workflows for processing SPARC datasets in accordance with FAIR principles. 
Zenodo. https://doi.org/XXXX/zenodo.XXXX.
```

## FAIR practices
We have assessed the FAIRness of our sparc-flow tool against the FAIR Principles established for research software. The details are available in the following [document](https://docs.google.com/document/d/1az_LXPivQvaofTsiMktJaWpyy2W_xKGX/edit).

## License
sparc-flow is fully open source and distributed under the very permissive Apache License 2.0. See [LICENSE](https://github.com/SPARC-FAIR-Codeathon/2023-team-3/blob/main/LICENSE) for more information.

## Team
* [Jiali Xu](https://github.com/JialiXu12) (Developer, Writer - Documentation)
* [Linkun Gao](https://github.com/LinkunGao) (Developer, Writer - Documentation)
* [Michael Hoffman](https://github.com/Moffhan) (Developer, Writer - Documentation)
* [Matthew French](https://github.com/frenchmatthew) (Developer, Writer - Documentation)
* [Thiranja Prasad Babarenda Gamage](https://github.com/PrasadBabarendaGamage) (Writer - Documentation)
* [Chinchien Lin](https://github.com/LIN810116) (Lead, SysAdmin)

## Acknowledgements
- We would like to thank the organizers of the 2023 SPARC Codeathon for their guidance and support during this Codeathon.

## References
* Michael R. Crusoe, Sanne Abeln, Alexandru Iosup, Peter Amstutz, John Chilton, Nebojša Tijanić, Hervé Ménager, Stian Soiland-Reyes, Bogdan Gavrilović, Carole Goble, and The CWL Community. 2022. Methods Included: Standardizing Computational Reuse and Portability with the Common Workflow Language. Commun. ACM 65, 6 (June 2022), 54–63. https://doi.org/10.1145/3486897
* Peter Amstutz, Michael R. Crusoe, Nebojša Tijanić (editors), Brad Chapman, John Chilton, Michael Heuer, Andrey Kartashov, Dan Leehr, Hervé Ménager, Maya Nedeljkovich, Matt Scales, Stian Soiland-Reyes, Luka Stojanovic (2016): Common Workflow Language, v1.0. Specification, Common Workflow Language working group. https://w3id.org/cwl/v1.0/ https://doi.org/10.6084/m9.figshare.3115156.v2

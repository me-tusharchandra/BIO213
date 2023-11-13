# README for BIO213: Introduction to Quantitative Biology

## Overview

This project involves the implementation of global and local alignment algorithms and the application of homology modeling techniques using Modeller. The project is structured into two assignments: Assignment 1 and Assignment 3.

### Assignment 1 - Global and Local Alignment

#### Global Alignment (Q1)

- **Functionality:** The program performs global alignment of two sequences and outputs the alignment along with the alignment score.
- **Usage:**
  ```python
  python global_alignment.py
  ```
- **Input:**
  - Default sequences: `seq1 = 'GATGCGCAG'`, `seq2 = 'GGCAGTA'`
  - User input for match, mismatch, and gap scores.

#### Local Alignment

- **Functionality:** Similar to global alignment, but performs local alignment instead.
- **Usage:**
  ```python
  python local_alignment.py
  ```
- **Input:**
  - Default sequences: `seq1 = 'GATGCGCAG'`, `seq2 = 'GGCAGTA'`
  - User input for match, mismatch, and gap scores.

### Assignment 3 - Homology Modeling with Modeller

#### Steps and Questions

1. **Search for Homologous Proteins (Step 1):**
   - Utilizes NCBI BLASTp to find homologous proteins for a given sequence.
   - Answers questions related to selecting the best template based on BLASTp results.

2. **Retrieve PDB Structure (Step 2):**
   - Retrieves the PDB structure of the chosen template and explores its characteristics.
   - Answers questions regarding the experimental method used, total chains, and chain differences.

3. **Prepare Files for Modeller (Step 3):**
   - Follows the Modeller tutorial to prepare files for modeling.

4. **Align Query and Template (Step 4):**
   - Uses `align2d.py` to align the query and template sequences.

5. **Model Building (Step 5):**
   - Utilizes `model-single.py` to build models and selects the best model based on specified parameters.

6. **Visualization (Step 6):**
   - Uses Chimera to visualize the developed model and compares it to the PDB structure.

7. **Evaluation (Step 7):**
   - Generates a Ramachandran Plot using PDBsum to assess model correctness.
   - Answers questions related to the plot and discusses the reliability of the structure.

8. **Advanced Modeling (Question 7):**
   - Discusses the possibility of using multiple templates for better structure in multi-template homology modeling.

## Instructions for Running

1. **Global and Local Alignment:**
   - Run `global_alignment.py` for global alignment and `local_alignment.py` for local alignment.
   - Follow on-screen instructions to input match, mismatch, and gap scores.

2. **Homology Modeling:**
   - Follow the instructions in Assignment 3.
   - Run the steps in sequence and answer the questions accordingly.


## Additional Resources

- Modeller: [https://salilab.org/modeller/](https://salilab.org/modeller/)
- NCBI BLASTp: [https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp)
- Protein Data Bank (PDB): [https://www.rcsb.org/](https://www.rcsb.org/)
- Chimera: [https://www.cgl.ucsf.edu/chimera/download.html](https://www.cgl.ucsf.edu/chimera/download.html)
- PDBsum: [http://www.ebi.ac.uk/thornton-srv/databases/pdbsum/Generate.html](http://www.ebi.ac.uk/thornton-srv/databases/pdbsum/Generate.html)
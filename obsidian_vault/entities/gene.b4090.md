---
entity_id: "gene.b4090"
entity_type: "gene"
name: "rpiB"
source_database: "NCBI RefSeq"
source_id: "gene-b4090"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4090"
  - "rpiB"
---

# rpiB

`gene.b4090`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4090`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpiB (gene.b4090) is a gene entity. It encodes rpiB (protein.P37351). Encoded protein function: FUNCTION: Catalyzes the interconversion of ribulose-5-P and ribose-5-P. It probably also has activity on D-allose 6-phosphate. {ECO:0000269|PubMed:1104357, ECO:0000269|PubMed:18640127, ECO:0000269|PubMed:4909663, ECO:0000269|PubMed:8576032}. EcoCyc product frame: RIB5PISOMB-MONOMER. EcoCyc synonyms: yjcA, alsI. Genomic coordinates: 4313350-4313799. EcoCyc protein note: There are two physically and genetically distinct ribose-5-phosphate isomerases present in E. coli . The constitutive ribose-5-phosphate isomerase A, encoded by the rpiA gene, functions in the NONOXIPENT-PWY. The inducible ribose-5-phosphate isomerase B can substitute for RpiA's function if its expression is induced . There is no sequence similarity between the two enzymes . A crystal structure of RpiB has been solved at 2.2 Å resolution. The enzyme is present as a dimer of dimers in the crystal, and active site residues are located at the dimer interface . A crystal structure of the active site mutant H99N has been solved at 2.1 Å resolution . Expression of rpiB is induced by allose, and an rpiB mutant is unable to catabolize allose . RpiB: "ribosephosphate isomerase B" AlsI: "allose 6-phosphate isomerase" Review:

## Biological Role

Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), glaR (protein.P37338).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37351|protein.P37351]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpiB; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=rpiB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013405,ECOCYC:EG11827,GeneID:948602`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4313350-4313799:+; feature_type=gene

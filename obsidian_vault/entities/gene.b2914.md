---
entity_id: "gene.b2914"
entity_type: "gene"
name: "rpiA"
source_database: "NCBI RefSeq"
source_id: "gene-b2914"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2914"
  - "rpiA"
---

# rpiA

`gene.b2914`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2914`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpiA (gene.b2914) is a gene entity. It encodes rpiA (protein.P0A7Z0). Encoded protein function: FUNCTION: Involved in the first step of the non-oxidative branch of the pentose phosphate pathway. It catalyzes the reversible conversion of ribose-5-phosphate to ribulose 5-phosphate. Can also act on D-ribose-5-diphosphate and D-ribose-5-triphosphate as substrate. {ECO:0000269|PubMed:1104357, ECO:0000269|PubMed:12517338, ECO:0000269|PubMed:4909663}. EcoCyc product frame: RIB5PISOMA-MONOMER. EcoCyc synonyms: ygfC. Genomic coordinates: 3058666-3059325. EcoCyc protein note: There are two physically and genetically distinct ribose-5-phosphate isomerases present in E. coli . The constitutive ribose-5-phosphate isomerase A (RpiA) normally accounts for more than 99% of the ribose-5-phosphate isomerase activity in the cell and functions in the NONOXIPENT-PWY . The inducible ribose-5-phosphate isomerase B can substitute for RpiA's function if its expression is induced . There is no sequence similarity between the two enzymes . Crystal structures of RpiA have been solved and active site residues and an acid-base catalytic mechanism were predicted . An rpiA mutant requires ribose for growth . RpiA: "ribosephosphate isomerase A" Review:

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7Z0|protein.P0A7Z0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009567,ECOCYC:EG11443,GeneID:947407`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3058666-3059325:-; feature_type=gene

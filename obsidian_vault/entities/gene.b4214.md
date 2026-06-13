---
entity_id: "gene.b4214"
entity_type: "gene"
name: "cysQ"
source_database: "NCBI RefSeq"
source_id: "gene-b4214"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4214"
  - "cysQ"
---

# cysQ

`gene.b4214`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4214`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysQ (gene.b4214) is a gene entity. It encodes cysQ (protein.P22255). Encoded protein function: FUNCTION: Converts adenosine-3',5'-bisphosphate (PAP) to AMP. May also convert adenosine 3'-phosphate 5'-phosphosulfate (PAPS) to adenosine 5'-phosphosulfate (APS). Has 10000-fold lower activity towards inositol 1,4-bisphosphate (Ins(1,4)P2). {ECO:0000269|PubMed:10224133, ECO:0000269|PubMed:16682444, ECO:0000269|PubMed:7493934}. EcoCyc product frame: EG10043-MONOMER. EcoCyc synonyms: amt, amtA. Genomic coordinates: 4436755-4437495. EcoCyc protein note: CysQ is an adenosine-3',5'-bisphosphate nucleotidase which recycles adenosine-3',5'-bisphosphate (PAP) that is generated during sulfate assimilation (see SO4ASSIM-PWY) and holo-ACP synthesis for the biosynthesis of fatty acids (see HOLO-ACP-SYNTH-CPLX and EG12221-MONOMER). CysQ is inhibited by Li+, and the enzyme is the main target for lithium toxicity in E. coli . The protein is similar to SuhB and mammalian inositol monophosphatase . cysQ mutants require cysteine or sulfite to grow under aerobic conditions, though they continue to carry out normal uptake of sulfate . A cysQ mutation can be complemented with the rice gene RHL, which encodes an enzyme catalyzing the conversion of adenosine 3'-phosphate 5'-phosphosulfate (PAPS) to adenosine 5'-phosphosulfate (APS)...

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22255|protein.P22255]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=cysQ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013786,ECOCYC:EG10043,GeneID:948728`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4436755-4437495:+; feature_type=gene

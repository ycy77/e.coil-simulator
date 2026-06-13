---
entity_id: "gene.b2026"
entity_type: "gene"
name: "hisI"
source_database: "NCBI RefSeq"
source_id: "gene-b2026"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2026"
  - "hisI"
---

# hisI

`gene.b2026`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2026`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hisI (gene.b2026) is a gene entity. It encodes hisI (protein.P06989). Encoded protein function: Histidine biosynthesis bifunctional protein HisIE [Includes: Phosphoribosyl-AMP cyclohydrolase (PRA-CH) (EC 3.5.4.19); Phosphoribosyl-ATP pyrophosphatase (PRA-PH) (EC 3.6.1.31)] EcoCyc product frame: HISTCYCLOPRATPPHOS. EcoCyc synonyms: hisE, hisIE. Genomic coordinates: 2096614-2097225. EcoCyc protein note: HisI is predicted to be a bifunctional enzyme carrying out the second and third steps in the biosynthesis of histidine. Based largely on sequence comparisons with these enzymes in other organisms, HisI is predicted to be a bifunctional enzyme. The carboxy-terminal domain is expected to catalyze the phosphoribosyl-ATP pyrophosphatase reaction, and the amino-terminal domain is expected to carry out the phosphoribosyl-AMP cyclohydrolase reaction . Only the first activity has been functionally demonstrated to exist in E. coli, via crosschecking with the appropriate Salmonella mutant .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06989|protein.P06989]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hisI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006729,ECOCYC:EG10451,GeneID:946515`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2096614-2097225:+; feature_type=gene

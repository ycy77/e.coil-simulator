---
entity_id: "gene.b3056"
entity_type: "gene"
name: "cca"
source_database: "NCBI RefSeq"
source_id: "gene-b3056"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3056"
  - "cca"
---

# cca

`gene.b3056`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3056`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cca (gene.b3056) is a gene entity. It encodes cca (protein.P06961). Encoded protein function: FUNCTION: Catalyzes the addition and repair of the essential 3'-terminal CCA sequence in tRNAs without using a nucleic acid template (PubMed:3516995). Adds these three nucleotides in the order of C, C, and A to the tRNA nucleotide-73, using CTP and ATP as substrates and producing inorganic pyrophosphate (PubMed:3516995). tRNA 3'-terminal CCA addition is required both for tRNA processing and repair (PubMed:22076379). Also involved in tRNA surveillance by mediating tandem CCA addition to generate a CCACCA at the 3' terminus of unstable tRNAs (PubMed:22076379). While stable tRNAs receive only 3'-terminal CCA, unstable tRNAs are marked with CCACCA and rapidly degraded (PubMed:22076379). The structural flexibility of RNA controls the choice between CCA versus CCACCA addition: following the first CCA addition cycle, nucleotide-binding to the active site triggers a clockwise screw motion, producing torque on the RNA (By similarity). This ejects stable RNAs, whereas unstable RNAs are refolded while bound to the enzyme and subjected to a second CCA catalytic cycle (By similarity). Also shows highest phosphatase activity in the presence of Ni(2+) and hydrolyzes pyrophosphate, canonical 5'-nucleoside tri- and diphosphates, NADP, and 2'-AMP with the production of Pi (PubMed:15210699)...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06961|protein.P06961]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=cca; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010031,ECOCYC:EG10136,GeneID:947553`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3201891-3203129:+; feature_type=gene

---
entity_id: "gene.b3192"
entity_type: "gene"
name: "mlaC"
source_database: "NCBI RefSeq"
source_id: "gene-b3192"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3192"
  - "mlaC"
---

# mlaC

`gene.b3192`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3192`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mlaC (gene.b3192) is a gene entity. It encodes mlaC (protein.P0ADV7). Encoded protein function: FUNCTION: Involved in a phospholipid transport pathway that maintains lipid asymmetry in the outer membrane by retrograde trafficking of phospholipids from the outer membrane to the inner membrane. May transfer phospholipid across the periplasmic space and deliver it to the MlaFEDB complex at the inner membrane. {ECO:0000269|PubMed:19383799, ECO:0000305|PubMed:28388411}. EcoCyc product frame: G7659-MONOMER. EcoCyc synonyms: yrbC. Genomic coordinates: 3337256-3337891. EcoCyc protein note: mlaC encodes the periplasmic chaperone of a phospholipid intermembrane transport system that maintains outer membrane lipid asymmetry. MlaC is implicated in a retrograde phospholipid trafficking pathway that is thought to maintain outer membrane lipid asymmetry by removing phospholipids from the outer membrane and transporting them back to the inner membrane; the Mla system comprises MlaC, the ABC-45-CPLX "MlaFEDB" complex in the inner membrane and an outer membrane lipoprotein G7216-MONOMER "MlaA" . MlaC is predicted to be a lipid-binding protein; MlaC interacts with the MlaFEDB inner membrane complex and the MlaA-OmpF outer membrane complex (see also ). Mechanistic insight into retrograde phospholipid transfer from OmpC-MlaA to MlaC, and from MlaC to MlaD is reported by...

## Biological Role

Activated by marA (protein.P0ACH5).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADV7|protein.P0ADV7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=mlaC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010489,ECOCYC:G7659,GeneID:947710`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3337256-3337891:-; feature_type=gene

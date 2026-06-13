---
entity_id: "gene.b3194"
entity_type: "gene"
name: "mlaE"
source_database: "NCBI RefSeq"
source_id: "gene-b3194"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3194"
  - "mlaE"
---

# mlaE

`gene.b3194`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3194`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mlaE (gene.b3194) is a gene entity. It encodes mlaE (protein.P64606). Encoded protein function: FUNCTION: Part of the ABC transporter complex MlaFEDB, which is involved in a phospholipid transport pathway that maintains lipid asymmetry in the outer membrane by retrograde trafficking of phospholipids from the outer membrane to the inner membrane. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:19383799, ECO:0000269|PubMed:27529189}. EcoCyc product frame: YRBE-MONOMER. EcoCyc synonyms: yrbE. Genomic coordinates: 3338466-3339248. EcoCyc protein note: mlaE encodes an inner membrane subunit of the MlaFEDB transporter complex which functions as part of a retrograde and/or anterograde intermembrane phospholipid trafficking system. MlaE is the predicted permease component of a retrograde phospholipid trafficking pathway; a ΔmlaE mutant displays increased SDS-EDTA sensitivity . MlaE forms a stable complex with MlaF, MlaD, and MlaB...

## Biological Role

Activated by marA (protein.P0ACH5).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64606|protein.P64606]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=mlaE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010495,ECOCYC:EG12800,GeneID:947732`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3338466-3339248:-; feature_type=gene

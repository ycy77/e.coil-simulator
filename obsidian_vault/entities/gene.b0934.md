---
entity_id: "gene.b0934"
entity_type: "gene"
name: "ssuC"
source_database: "NCBI RefSeq"
source_id: "gene-b0934"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0934"
  - "ssuC"
---

# ssuC

`gene.b0934`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0934`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ssuC (gene.b0934) is a gene entity. It encodes ssuC (protein.P75851). Encoded protein function: FUNCTION: Part of a binding-protein-dependent transport system for aliphatic sulfonates. Probably responsible for the translocation of the substrate across the membrane. EcoCyc product frame: YCBM-MONOMER. EcoCyc synonyms: ycbM. Genomic coordinates: 994041-994832. EcoCyc protein note: SsuC is the predicted integral membrane component of an ATP-dependent aliphatic sulfonate uptake system . A ΔssuBC strain is unable to grow using a range of aliphatic sulfonates as sulfur source including ethanesulfonate, hexanesulfonate, octanesulfonate, decanesulfonate, sulfoacetate, 4-phenyl-1-butanesulfonate, N-phenyltaurine, MOPS and HEPES and growth is significantly reduced with propanesulfonate, pentanesulfonate, 2-(4-pyridyl)ethanesulfonate or PIPES as sulfur source. Wild type growth is restored when ssuB and ssuC are expressed from a plasmid . SsuC is predicted to be an inner membrane protein with 6-7 transmembrane domains; topology analysis suggests the N and C termini are located in the cytoplasm .

## Biological Role

Repressed by cysB (protein.P0A9F3). Activated by rpoD (protein.P00579), cbl (protein.Q47083).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75851|protein.P75851]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ssuC; function=+
- `activates` <-- [[protein.Q47083|protein.Q47083]] `RegulonDB` `S` - regulator=Cbl; target=ssuC; function=+
- `represses` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=ssuC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003175,ECOCYC:G6476,GeneID:947216`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:994041-994832:-; feature_type=gene

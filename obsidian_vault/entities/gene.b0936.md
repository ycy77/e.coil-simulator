---
entity_id: "gene.b0936"
entity_type: "gene"
name: "ssuA"
source_database: "NCBI RefSeq"
source_id: "gene-b0936"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0936"
  - "ssuA"
---

# ssuA

`gene.b0936`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0936`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ssuA (gene.b0936) is a gene entity. It encodes ssuA (protein.P75853). Encoded protein function: FUNCTION: Part of a binding-protein-dependent transport system for aliphatic sulfonates. Putative binding protein. EcoCyc product frame: G6478-MONOMER. EcoCyc synonyms: ycbO. Genomic coordinates: 995985-996944. EcoCyc protein note: SsuA is the predicted substrate-binding protein of an ATP-dependent aliphatic sulfonate uptake system . A ΔssuA strain is unable to grow using a range of aliphatic sulfonates as sulfur source including ethanesulfonate, hexanesulfonate, octanesulfonate, decanesulfonate, sulfoacetate, N-phenyltaurine, 4-phenyl-1-butansulfonate, MOPS and HEPES and has significantly reduced growth with propanesulfonate, pentanesulfonate, 2-(4-pyridyl)ethanesulfonate or PIPES as sulfur source. Wild type growth is restored when ssuA is expressed from a plasmid .

## Biological Role

Repressed by cysB (protein.P0A9F3), yeiE (protein.P0ACR4). Activated by rpoD (protein.P00579), cbl (protein.Q47083).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75853|protein.P75853]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ssuA; function=+
- `activates` <-- [[protein.Q47083|protein.Q47083]] `RegulonDB` `S` - regulator=Cbl; target=ssuA; function=+
- `represses` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=ssuA; function=-
- `represses` <-- [[protein.P0ACR4|protein.P0ACR4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003180,ECOCYC:G6478,GeneID:945560`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:995985-996944:-; feature_type=gene

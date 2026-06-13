---
entity_id: "gene.b0933"
entity_type: "gene"
name: "ssuB"
source_database: "NCBI RefSeq"
source_id: "gene-b0933"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0933"
  - "ssuB"
---

# ssuB

`gene.b0933`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0933`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ssuB (gene.b0933) is a gene entity. It encodes ssuB (protein.P0AAI1). Encoded protein function: FUNCTION: Part of the ABC transporter complex SsuABC involved in aliphatic sulfonates import. Responsible for energy coupling to the transport system (Probable). {ECO:0000305|PubMed:10506196, ECO:0000305|PubMed:10781534}. EcoCyc product frame: YCBE-MONOMER. EcoCyc synonyms: ycbE. Genomic coordinates: 993277-994044. EcoCyc protein note: SsuB is the predicted ATP-binding component of an aliphatic sulfonate ABC transporter; SsuB contains sequence motifs conserved in ATP-binding cassette (ABC) proteins . A ΔssuBC strain is unable to grow using a range of aliphatic sulfonates as sulfur source including ethanesulfonate, hexanesulfonate, octanesulfonate, decanesulfonate, sulfoacetate, 4-phenyl-1-butanesulfonate, N-phenyltaurine, MOPS and HEPES and growth is significantly reduced with propanesulfonate, pentanesulfonate, 2-(4-pyridyl)ethanesulfonate or PIPES as sulfur source. Wild type growth is restored when ssuB and ssuC are expressed from a plasmid .

## Biological Role

Repressed by cysB (protein.P0A9F3). Activated by rpoD (protein.P00579), cbl (protein.Q47083).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAI1|protein.P0AAI1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ssuB; function=+
- `activates` <-- [[protein.Q47083|protein.Q47083]] `RegulonDB` `S` - regulator=Cbl; target=ssuB; function=+
- `represses` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=ssuB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003173,ECOCYC:EG12358,GeneID:947220`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:993277-994044:-; feature_type=gene

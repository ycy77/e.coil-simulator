---
entity_id: "gene.b3251"
entity_type: "gene"
name: "mreB"
source_database: "NCBI RefSeq"
source_id: "gene-b3251"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3251"
  - "mreB"
---

# mreB

`gene.b3251`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3251`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mreB (gene.b3251) is a gene entity. It encodes mreB (protein.P0A9X4). Encoded protein function: FUNCTION: Forms membrane-associated dynamic filaments that are essential for cell shape determination (PubMed:15612918, PubMed:21903929). Acts by regulating cell wall synthesis and cell elongation, and thus cell shape (PubMed:21903929). A feedback loop between cell geometry and MreB localization maintains elongated cell shape by targeting cell wall growth to regions of negative cell wall curvature (PubMed:24550515). Filaments rotate around the cell circumference in concert with the cell wall synthesis enzymes. The process is driven by the cell wall synthesis machinery and does not depend on MreB polymerization (PubMed:21903929). Rotation may contribute to the robust maintenance of rod shape (PubMed:21903929). {ECO:0000269|PubMed:15612918, ECO:0000269|PubMed:21903929, ECO:0000269|PubMed:24550515}. EcoCyc product frame: EG10608-MONOMER. EcoCyc synonyms: rodY, envB, mon, mreB_1. Genomic coordinates: 3400044-3401087. EcoCyc protein note: MreB is a homolog of the eukaryotic actin protein (see . MreB is implicated in the formation of rod shape and mecillinam sensitivity . MreB forms left-handed helical filaments beneath the surface of the cell...

## Biological Role

Repressed by bolA (protein.P0ABE2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9X4|protein.P0A9X4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ABE2|protein.P0ABE2]] `RegulonDB` `S` - regulator=BolA; target=mreB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010661,ECOCYC:EG10608,GeneID:948588`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3400044-3401087:-; feature_type=gene

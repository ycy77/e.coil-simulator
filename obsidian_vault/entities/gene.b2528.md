---
entity_id: "gene.b2528"
entity_type: "gene"
name: "iscA"
source_database: "NCBI RefSeq"
source_id: "gene-b2528"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2528"
  - "iscA"
---

# iscA

`gene.b2528`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2528`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

iscA (gene.b2528) is a gene entity. It encodes iscA (protein.P0AAC8). Encoded protein function: FUNCTION: Is able to transfer iron-sulfur clusters to apo-ferredoxin. Multiple cycles of [2Fe2S] cluster formation and transfer are observed, suggesting that IscA acts catalytically. Recruits intracellular free iron so as to provide iron for the assembly of transient iron-sulfur cluster in IscU in the presence of IscS, L-cysteine and the thioredoxin reductase system TrxA/TrxB. EcoCyc product frame: EG12132-MONOMER. EcoCyc synonyms: yfhF. Genomic coordinates: 2659563-2659886.

## Biological Role

Repressed by ryhB (gene.b4451), iscR (protein.P0AGK8). Activated by oxyS (gene.b4458), rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAC8|protein.P0AAC8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[gene.b4458|gene.b4458]] `RegulonDB` `S` - regulator=OxyS; target=iscA; function=+
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=iscA; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=iscA; function=-
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `C` - regulator=IscR; target=iscA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008319,ECOCYC:EG12132,GeneID:946999`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2659563-2659886:-; feature_type=gene

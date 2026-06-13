---
entity_id: "gene.b4764"
entity_type: "gene"
name: "sdhX"
source_database: "NCBI RefSeq"
source_id: "gene-b4764"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4764"
  - "sdhX"
---

# sdhX

`gene.b4764`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4764`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sdhX (gene.b4764) is a gene entity. EcoCyc product frame: RNA0-403. EcoCyc synonyms: rybD. Genomic coordinates: 765050-765150.

## Biological Role

Repressed by ryhB (gene.b4451), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fur (protein.P0A9A9), arcA (protein.P0A9Q1), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (6)

- `represses` --> [[gene.b2296|gene.b2296]] `RegulonDB` `S` - regulator=SdhX; target=ackA; function=-
- `represses` --> [[gene.b3891|gene.b3891]] `RegulonDB` `S` - regulator=SdhX; target=fdhE; function=-
- `represses` --> [[gene.b3892|gene.b3892]] `RegulonDB` `S` - regulator=SdhX; target=fdoI; function=-
- `represses` --> [[gene.b3893|gene.b3893]] `RegulonDB` `S` - regulator=SdhX; target=fdoH; function=-
- `represses` --> [[gene.b3894|gene.b3894]] `RegulonDB` `S` - regulator=SdhX; target=fdoG; function=-
- `represses` --> [[gene.b3942|gene.b3942]] `RegulonDB` `S` - regulator=SdhX; target=katG; function=-

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sdhX; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=sdhX; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sdhX; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sdhX; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=sdhX; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=sdhX; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sdhX; function=-+

## External IDs

- `Dbxref:ECOCYC:G0-17009,GeneID:63925629`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:765050-765150:+; feature_type=gene

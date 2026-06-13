---
entity_id: "gene.b2091"
entity_type: "gene"
name: "gatD"
source_database: "NCBI RefSeq"
source_id: "gene-b2091"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2091"
  - "gatD"
---

# gatD

`gene.b2091`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2091`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gatD (gene.b2091) is a gene entity. It encodes gatD (protein.P0A9S3). Encoded protein function: FUNCTION: Converts galactitol 1-phosphate to D-tagatose 6-phosphate. {ECO:0000269|PubMed:13331868}. EcoCyc product frame: GALACTITOLPDEHYD-MONOMER. Genomic coordinates: 2171833-2172873.

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), nac (protein.Q47005).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9S3|protein.P0A9S3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gatD; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=gatD; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=gatD; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=gatD; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0006924,ECOCYC:EG12417,GeneID:946598`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2171833-2172873:-; feature_type=gene

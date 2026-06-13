---
entity_id: "gene.b1482"
entity_type: "gene"
name: "osmC"
source_database: "NCBI RefSeq"
source_id: "gene-b1482"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1482"
  - "osmC"
---

# osmC

`gene.b1482`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1482`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

osmC (gene.b1482) is a gene entity. It encodes osmC (protein.P0C0L2). Encoded protein function: FUNCTION: Preferentially metabolizes organic hydroperoxides over inorganic hydrogen peroxide. {ECO:0000269|PubMed:14627744}. EcoCyc product frame: EG10680-MONOMER. Genomic coordinates: 1556625-1557056.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by nhaR (protein.P0A9G2), lrp (protein.P0ACJ0), rcsB (protein.P0DMC7).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C0L2|protein.P0C0L2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A9G2|protein.P0A9G2]] `RegulonDB` `S` - regulator=NhaR; target=osmC; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=osmC; function=-+
- `activates` <-- [[protein.P0DMC7|protein.P0DMC7]] `RegulonDB` `C` - regulator=RcsB; target=osmC; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=osmC; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0004944,ECOCYC:EG10680,GeneID:946043`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1556625-1557056:+; feature_type=gene

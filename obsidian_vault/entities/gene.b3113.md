---
entity_id: "gene.b3113"
entity_type: "gene"
name: "tdcF"
source_database: "NCBI RefSeq"
source_id: "gene-b3113"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3113"
  - "tdcF"
---

# tdcF

`gene.b3113`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3113`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tdcF (gene.b3113) is a gene entity. It encodes tdcF (protein.P0AGL2). Encoded protein function: FUNCTION: May be a post-translational regulator that controls the metabolic fate of L-threonine or the potentially toxic intermediate 2-ketobutyrate. EcoCyc product frame: G7626-MONOMER. EcoCyc synonyms: yhaR. Genomic coordinates: 3259721-3260110.

## Biological Role

Activated by crp (protein.P0ACJ8), tdcA (protein.P0ACQ7), tdcR (protein.P11866).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGL2|protein.P0AGL2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=tdcF; function=+
- `activates` <-- [[protein.P0ACQ7|protein.P0ACQ7]] `RegulonDB` `S` - regulator=TdcA; target=tdcF; function=+
- `activates` <-- [[protein.P11866|protein.P11866]] `RegulonDB` `S` - regulator=TdcR; target=tdcF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010240,ECOCYC:G7626,GeneID:947624`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3259721-3260110:-; feature_type=gene

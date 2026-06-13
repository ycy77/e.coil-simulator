---
entity_id: "gene.b4266"
entity_type: "gene"
name: "idnO"
source_database: "NCBI RefSeq"
source_id: "gene-b4266"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4266"
  - "idnO"
---

# idnO

`gene.b4266`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4266`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

idnO (gene.b4266) is a gene entity. It encodes idnO (protein.P0A9P9). Encoded protein function: FUNCTION: Catalyzes the reduction of 5-keto-D-gluconate to D-gluconate, using either NADH or NADPH. Is likely involved in an L-idonate degradation pathway that allows E.coli to utilize L-idonate as the sole carbon and energy source. Is also able to catalyze the reverse reaction in vitro, but the D-gluconate oxidation by the enzyme can only proceed with NAD. {ECO:0000269|PubMed:9658018}. EcoCyc product frame: GLUCONREDUCT-MONOMER. EcoCyc synonyms: yjgU. Genomic coordinates: 4492587-4493351.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9P9|protein.P0A9P9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013971,ECOCYC:G7892,GeneID:947109`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4492587-4493351:-; feature_type=gene

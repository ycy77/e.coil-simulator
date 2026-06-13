---
entity_id: "gene.b4066"
entity_type: "gene"
name: "yjcF"
source_database: "NCBI RefSeq"
source_id: "gene-b4066"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4066"
  - "yjcF"
---

# yjcF

`gene.b4066`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4066`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjcF (gene.b4066) is a gene entity. It encodes yjcF (protein.P32704). Encoded protein function: Uncharacterized protein YjcF EcoCyc product frame: EG11941-MONOMER. Genomic coordinates: 4281783-4283075. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 24, 2017.

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32704|protein.P32704]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yjcF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013325,ECOCYC:EG11941,GeneID:948576`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4281783-4283075:-; feature_type=gene

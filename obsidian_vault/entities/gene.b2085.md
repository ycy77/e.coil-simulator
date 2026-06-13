---
entity_id: "gene.b2085"
entity_type: "gene"
name: "yegR"
source_database: "NCBI RefSeq"
source_id: "gene-b2085"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2085"
  - "yegR"
---

# yegR

`gene.b2085`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2085`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yegR (gene.b2085) is a gene entity. It encodes yegR (protein.P76406). Encoded protein function: Uncharacterized protein YegR EcoCyc product frame: G7122-MONOMER. Genomic coordinates: 2167989-2168306. EcoCyc protein note: No information about this protein was found by a literature search conducted on August 30, 2017.

## Biological Role

Repressed by nac (protein.Q47005). Activated by evgA (protein.P0ACZ4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76406|protein.P76406]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=yegR; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yegR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006907,ECOCYC:G7122,GeneID:946613`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2167989-2168306:-; feature_type=gene

---
entity_id: "gene.b2357"
entity_type: "gene"
name: "yfdN"
source_database: "NCBI RefSeq"
source_id: "gene-b2357"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2357"
  - "yfdN"
---

# yfdN

`gene.b2357`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2357`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfdN (gene.b2357) is a gene entity. It encodes yfdN (protein.P76510). Encoded protein function: Uncharacterized protein YfdN EcoCyc product frame: G7226-MONOMER. EcoCyc synonyms: yzyA. Genomic coordinates: 2472387-2472881. EcoCyc protein note: No information about this protein was found by a literature search conducted on May 22, 2020.

## Biological Role

Activated by ygfI (protein.P52044).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76510|protein.P76510]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=yfdN; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007777,ECOCYC:G7226,GeneID:946419`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2472387-2472881:-; feature_type=gene

---
entity_id: "gene.b2359"
entity_type: "gene"
name: "yfdP"
source_database: "NCBI RefSeq"
source_id: "gene-b2359"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2359"
  - "yfdP"
---

# yfdP

`gene.b2359`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2359`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfdP (gene.b2359) is a gene entity. It encodes yfdP (protein.P76512). Encoded protein function: Uncharacterized protein YfdP EcoCyc product frame: G7228-MONOMER. Genomic coordinates: 2473604-2473966. EcoCyc protein note: No information about this protein was found by a literature search conducted on May 22, 2020.

## Biological Role

Activated by ygfI (protein.P52044).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76512|protein.P76512]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=yfdP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007785,ECOCYC:G7228,GeneID:945565`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2473604-2473966:+; feature_type=gene

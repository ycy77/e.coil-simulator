---
entity_id: "gene.b1568"
entity_type: "gene"
name: "ydfX"
source_database: "NCBI RefSeq"
source_id: "gene-b1568"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1568"
  - "ydfX"
---

# ydfX

`gene.b1568`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1568`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydfX (gene.b1568) is a gene entity. It encodes ydfX (protein.P76165). Encoded protein function: Protein YdfX EcoCyc product frame: G6835-MONOMER. Genomic coordinates: 1647346-1647636. EcoCyc protein note: No information about this protein was found by a literature search conducted on September 4, 2020.

## Biological Role

Repressed by dicA (protein.P06966). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76165|protein.P76165]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ydfX; function=+
- `represses` <-- [[protein.P06966|protein.P06966]] `RegulonDB` `S` - regulator=DicA; target=ydfX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005239,ECOCYC:G6835,GeneID:946112`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1647346-1647636:-; feature_type=gene

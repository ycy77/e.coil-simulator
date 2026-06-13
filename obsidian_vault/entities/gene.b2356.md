---
entity_id: "gene.b2356"
entity_type: "gene"
name: "yfdM"
source_database: "NCBI RefSeq"
source_id: "gene-b2356"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2356"
  - "yfdM"
---

# yfdM

`gene.b2356`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2356`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfdM (gene.b2356) is a gene entity. It encodes yfdM (protein.P76509). Encoded protein function: Putative methyltransferase YfdM (EC 2.1.1.-) EcoCyc product frame: G7225-MONOMER. EcoCyc synonyms: yzyB. Genomic coordinates: 2472112-2472387. EcoCyc protein note: The T1-type lytic phage SW1 utilizes the YfdM protein of the cryptic prophage CPS-53 to replicate .

## Biological Role

Activated by ygfI (protein.P52044).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76509|protein.P76509]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=yfdM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007775,ECOCYC:G7225,GeneID:945416`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2472112-2472387:-; feature_type=gene

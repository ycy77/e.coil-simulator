---
entity_id: "gene.b4721"
entity_type: "gene"
name: "ytiD"
source_database: "NCBI RefSeq"
source_id: "gene-b4721"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4721"
  - "ytiD"
---

# ytiD

`gene.b4721`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4721`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ytiD (gene.b4721) is a gene entity. It encodes ytiD (protein.P0DPC5). Encoded protein function: Protein YtiD EcoCyc product frame: MONOMER0-4392. Genomic coordinates: 4556654-4556797. EcoCyc protein note: YtiD is one of three small proteins encoded upstream of iraD .

## Biological Role

Repressed by dnaA (protein.P03004), csrA (protein.P69913). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DPC5|protein.P0DPC5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ytiD; function=+
- `represses` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `C` - regulator=DnaA; target=ytiD; function=-
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `S` - regulator=CsrA; target=ytiD; function=-

## External IDs

- `Dbxref:ECOCYC:G0-16687,GeneID:38094979`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4556654-4556797:+; feature_type=gene

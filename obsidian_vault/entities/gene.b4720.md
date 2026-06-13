---
entity_id: "gene.b4720"
entity_type: "gene"
name: "ytiC"
source_database: "NCBI RefSeq"
source_id: "gene-b4720"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4720"
  - "ytiC"
---

# ytiC

`gene.b4720`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4720`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ytiC (gene.b4720) is a gene entity. It encodes ytiC (protein.P0DPC4). Encoded protein function: Protein YtiC EcoCyc product frame: MONOMER0-4391. Genomic coordinates: 4556574-4556675. EcoCyc protein note: YtiC is one of three small proteins encoded upstream of iraD . Low levels of expression of YtiC were detected at stationary phase .

## Biological Role

Repressed by dnaA (protein.P03004), csrA (protein.P69913). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DPC4|protein.P0DPC4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ytiC; function=+
- `represses` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `C` - regulator=DnaA; target=ytiC; function=-
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `S` - regulator=CsrA; target=ytiC; function=-

## External IDs

- `Dbxref:ECOCYC:G0-16686,GeneID:38094978`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4556574-4556675:+; feature_type=gene

---
entity_id: "gene.b0157"
entity_type: "gene"
name: "yadS"
source_database: "NCBI RefSeq"
source_id: "gene-b0157"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0157"
  - "yadS"
---

# yadS

`gene.b0157`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0157`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yadS (gene.b0157) is a gene entity. It encodes yadS (protein.P0AFP0). Encoded protein function: UPF0126 inner membrane protein YadS EcoCyc product frame: EG12333-MONOMER. Genomic coordinates: 177001-177624. EcoCyc protein note: No information about this protein was found by a literature search conducted on November 16, 2020.

## Biological Role

Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFP0|protein.P0AFP0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yadS; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=yadS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000540,ECOCYC:EG12333,GeneID:949062`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:177001-177624:-; feature_type=gene

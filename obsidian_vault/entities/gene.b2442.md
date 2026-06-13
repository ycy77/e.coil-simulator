---
entity_id: "gene.b2442"
entity_type: "gene"
name: "intZ"
source_database: "NCBI RefSeq"
source_id: "gene-b2442"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2442"
  - "intZ"
---

# intZ

`gene.b2442`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2442`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

intZ (gene.b2442) is a gene entity. It encodes intZ (protein.P76542). Encoded protein function: FUNCTION: Integrase is necessary for integration of the phage into the host genome by site-specific recombination. In conjunction with excisionase, integrase is also necessary for excision of the prophage from the host genome. EcoCyc product frame: G7272-MONOMER. Genomic coordinates: 2558858-2560066. EcoCyc protein note: No information about this protein was found by a literature search conducted on April 5, 2017.

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76542|protein.P76542]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008052,ECOCYC:G7272,GeneID:946923`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2558858-2560066:+; feature_type=gene

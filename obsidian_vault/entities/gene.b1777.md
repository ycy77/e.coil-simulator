---
entity_id: "gene.b1777"
entity_type: "gene"
name: "yeaC"
source_database: "NCBI RefSeq"
source_id: "gene-b1777"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1777"
  - "yeaC"
---

# yeaC

`gene.b1777`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1777`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeaC (gene.b1777) is a gene entity. It encodes yeaC (protein.P76231). Encoded protein function: Uncharacterized protein YeaC EcoCyc product frame: G6964-MONOMER. Genomic coordinates: 1861702-1861974. EcoCyc protein note: No information about this protein was found by a literature search conducted on October 30, 2018.

## Biological Role

Activated by DNA-binding transcriptional dual regulator Cra (complex.ecocyc.PC00061), cra (protein.P0ACP1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76231|protein.P76231]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.PC00061|complex.ecocyc.PC00061]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=yeaC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005914,ECOCYC:G6964,GeneID:947074`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1861702-1861974:-; feature_type=gene

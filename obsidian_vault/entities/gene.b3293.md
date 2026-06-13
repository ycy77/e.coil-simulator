---
entity_id: "gene.b3293"
entity_type: "gene"
name: "yhdN"
source_database: "NCBI RefSeq"
source_id: "gene-b3293"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3293"
  - "yhdN"
---

# yhdN

`gene.b3293`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3293`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhdN (gene.b3293) is a gene entity. It encodes yhdN (protein.P36677). Encoded protein function: Uncharacterized protein YhdN EcoCyc product frame: EG11970-MONOMER. Genomic coordinates: 3439141-3439509. EcoCyc protein note: No information about this protein was found by a literature search conducted on October 30, 2018.

## Biological Role

Activated by lrp (protein.P0ACJ0), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36677|protein.P36677]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=yhdN; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010795,ECOCYC:EG11970,GeneID:947785`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3439141-3439509:-; feature_type=gene

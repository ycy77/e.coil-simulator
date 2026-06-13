---
entity_id: "gene.b3292"
entity_type: "gene"
name: "zntR"
source_database: "NCBI RefSeq"
source_id: "gene-b3292"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3292"
  - "zntR"
---

# zntR

`gene.b3292`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3292`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

zntR (gene.b3292) is a gene entity. It encodes zntR (protein.P0ACS5). Encoded protein function: FUNCTION: Zinc-responsive transcriptional regulator of zntA. EcoCyc product frame: EG11969-MONOMER. EcoCyc synonyms: yhdM. Genomic coordinates: 3438705-3439130.

## Biological Role

Activated by lrp (protein.P0ACJ0), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACS5|protein.P0ACS5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=zntR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010793,ECOCYC:EG11969,GeneID:947786`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3438705-3439130:-; feature_type=gene

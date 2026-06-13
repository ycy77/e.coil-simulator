---
entity_id: "gene.b0310"
entity_type: "gene"
name: "ykgH"
source_database: "NCBI RefSeq"
source_id: "gene-b0310"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0310"
  - "ykgH"
---

# ykgH

`gene.b0310`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0310`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ykgH (gene.b0310) is a gene entity. It encodes ykgH (protein.P77180). Encoded protein function: Uncharacterized protein YkgH EcoCyc product frame: G6180-MONOMER. Genomic coordinates: 324696-325364. EcoCyc protein note: While wild-type E. coli shows significantly decreased swarming motility upon exposure to volatile organic compounds (VOCs) produced by Bacillus subtilis, a ykgH null mutant shows no significant difference in swarming motility upon VOC treatment .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77180|protein.P77180]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ykgH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001066,ECOCYC:G6180,GeneID:947513`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:324696-325364:-; feature_type=gene

---
entity_id: "gene.b2063"
entity_type: "gene"
name: "yegH"
source_database: "NCBI RefSeq"
source_id: "gene-b2063"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2063"
  - "yegH"
---

# yegH

`gene.b2063`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2063`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yegH (gene.b2063) is a gene entity. It encodes yegH (protein.P76389). Encoded protein function: UPF0053 protein YegH EcoCyc product frame: G7108-MONOMER. Genomic coordinates: 2137902-2139485. EcoCyc protein note: YegH is predicted to be an inner membrane protein with 7 transmembrane helices; PhoA/GFP fusion analysis suggests the C-terminus is located in the cytoplasm .

## Biological Role

Activated by phoB (protein.P0AFJ5), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76389|protein.P76389]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=yegH; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yegH; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006830,ECOCYC:G7108,GeneID:946566`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2137902-2139485:+; feature_type=gene

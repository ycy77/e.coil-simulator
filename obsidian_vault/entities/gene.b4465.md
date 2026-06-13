---
entity_id: "gene.b4465"
entity_type: "gene"
name: "yggP"
source_database: "NCBI RefSeq"
source_id: "gene-b4465"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4465"
  - "yggP"
---

# yggP

`gene.b4465`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4465`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yggP (gene.b4465) is a gene entity. It encodes yggP (protein.P52048). Encoded protein function: Uncharacterized protein YggP EcoCyc product frame: G7520-MONOMER. EcoCyc synonyms: b2931, b2932. Genomic coordinates: 3076179-3077456. EcoCyc protein note: No information about this protein was found by a literature search conducted on April 11, 2017.

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52048|protein.P52048]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yggP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0174095,ECOCYC:G7520,GeneID:2847686`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3076179-3077456:-; feature_type=gene

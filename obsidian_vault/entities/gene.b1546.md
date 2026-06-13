---
entity_id: "gene.b1546"
entity_type: "gene"
name: "tfaQ"
source_database: "NCBI RefSeq"
source_id: "gene-b1546"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1546"
  - "tfaQ"
---

# tfaQ

`gene.b1546`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1546`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tfaQ (gene.b1546) is a gene entity. It encodes tfaQ (protein.P76155). Encoded protein function: Prophage tail fiber assembly protein homolog TfaQ (Tail fiber assembly protein homolog from lambdoid prophage Qin) EcoCyc product frame: G6820-MONOMER. EcoCyc synonyms: ydfM. Genomic coordinates: 1634310-1634885. EcoCyc protein note: No information about this protein was found by a literature search conducted on April 12, 2017.

## Biological Role

Repressed by fur (protein.P0A9A9), nac (protein.Q47005).

## Enriched Pathways

- `eco03258` Virion - Bacteriophage lambda (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76155|protein.P76155]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=tfaQ; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=tfaQ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005166,ECOCYC:G6820,GeneID:946060`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1634310-1634885:-; feature_type=gene

---
entity_id: "gene.b3120"
entity_type: "gene"
name: "yhaB"
source_database: "NCBI RefSeq"
source_id: "gene-b3120"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3120"
  - "yhaB"
---

# yhaB

`gene.b3120`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3120`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhaB (gene.b3120) is a gene entity. It encodes yhaB (protein.P11865). Encoded protein function: Uncharacterized protein YhaB EcoCyc product frame: EG11173-MONOMER. Genomic coordinates: 3267854-3268393. EcoCyc protein note: Expression of yhaB is induced 49-fold upon exposure of cells to the biocide polyhexamethylene biguanide. Overexpression of yhaB has no effect on the MIC of polyhexamethylene biguanide .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11865|protein.P11865]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yhaB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010261,ECOCYC:EG11173,GeneID:947705`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3267854-3268393:+; feature_type=gene

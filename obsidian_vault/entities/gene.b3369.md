---
entity_id: "gene.b3369"
entity_type: "gene"
name: "yhfL"
source_database: "NCBI RefSeq"
source_id: "gene-b3369"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3369"
  - "yhfL"
---

# yhfL

`gene.b3369`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3369`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhfL (gene.b3369) is a gene entity. It encodes yhfL (protein.P64627). Encoded protein function: Uncharacterized protein YhfL EcoCyc product frame: G7722-MONOMER. Genomic coordinates: 3499448-3499615. EcoCyc protein note: YhfL is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ).

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64627|protein.P64627]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yhfL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011016,ECOCYC:G7722,GeneID:947879`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3499448-3499615:+; feature_type=gene

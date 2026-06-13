---
entity_id: "gene.b3172"
entity_type: "gene"
name: "argG"
source_database: "NCBI RefSeq"
source_id: "gene-b3172"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3172"
  - "argG"
---

# argG

`gene.b3172`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3172`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argG (gene.b3172) is a gene entity. It encodes argG (protein.P0A6E4). Encoded protein function: Argininosuccinate synthase (EC 6.3.4.5) (Citrulline--aspartate ligase) EcoCyc product frame: ARGSUCCINSYN-MONOMER. Genomic coordinates: 3318637-3319980.

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), argR (protein.P0A6D0), fur (protein.P0A9A9). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6E4|protein.P0A6E4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=argG; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=argG; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=argG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010428,ECOCYC:EG10068,GeneID:947590`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3318637-3319980:+; feature_type=gene

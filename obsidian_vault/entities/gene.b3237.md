---
entity_id: "gene.b3237"
entity_type: "gene"
name: "argR"
source_database: "NCBI RefSeq"
source_id: "gene-b3237"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3237"
  - "argR"
---

# argR

`gene.b3237`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3237`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argR (gene.b3237) is a gene entity. It encodes argR (protein.P0A6D0). Encoded protein function: FUNCTION: Negatively controls the expression of the four operons of arginine biosynthesis in addition to the carAB operon. Predominantly interacts with A/T residues in ARG boxes. It also binds to a specific site in cer locus. Thus it is essential for cer-mediated site-specific recombination in ColE1. It is necessary for monomerization of the plasmid ColE1. EcoCyc product frame: PD00194. EcoCyc synonyms: Rarg, xerA. Genomic coordinates: 3384703-3385173.

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), argR (protein.P0A6D0), fur (protein.P0A9A9), lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), arcA (protein.P0A9Q1), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6D0|protein.P0A6D0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=argR; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=argR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=argR; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=argR; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010620,ECOCYC:EG10070,GeneID:947861`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3384703-3385173:+; feature_type=gene

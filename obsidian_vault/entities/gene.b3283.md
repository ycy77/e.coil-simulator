---
entity_id: "gene.b3283"
entity_type: "gene"
name: "yrdD"
source_database: "NCBI RefSeq"
source_id: "gene-b3283"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3283"
  - "yrdD"
---

# yrdD

`gene.b3283`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3283`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yrdD (gene.b3283) is a gene entity. It encodes yrdD (protein.P45771). Encoded protein function: Uncharacterized protein YrdD EcoCyc product frame: G7699-MONOMER. Genomic coordinates: 3431420-3431962. EcoCyc protein note: YrdD has sequence similarity to the C-terminal zinc-binding region of EG11013-MONOMER. Purified YrdD contains both zinc and iron ions, but only the zinc-bound form is able to bind ssDNA . An insertion mutant of yrdD was isolated as a suppressor of the rdgB recA(Ts) near-lethal phenotype. As with endonuclease V (Nfi), it is thought that the suppressor effect is due to decreased excision of base analogues (which would normally be removed by RdgB) from DNA and thus a decreased numbers of double-strand breaks (with would normally be repaired by RecA) .

## Biological Role

Activated by zraR (protein.P14375).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45771|protein.P45771]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=yrdD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010768,ECOCYC:G7699,GeneID:947782`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3431420-3431962:-; feature_type=gene

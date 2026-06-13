---
entity_id: "gene.b1502"
entity_type: "gene"
name: "ydeQ"
source_database: "NCBI RefSeq"
source_id: "gene-b1502"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1502"
  - "ydeQ"
---

# ydeQ

`gene.b1502`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1502`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydeQ (gene.b1502) is a gene entity. It encodes ydeQ (protein.P77588). Encoded protein function: Uncharacterized fimbrial-like protein YdeQ EcoCyc product frame: G6792-MONOMER. Genomic coordinates: 1586820-1587734. EcoCyc protein note: E. coli K-12 contains 12 chaperone-usher fimbrial operons, including ydeQRST; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77588|protein.P77588]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ydeQ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005006,ECOCYC:G6792,GeneID:946050`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1586820-1587734:-; feature_type=gene

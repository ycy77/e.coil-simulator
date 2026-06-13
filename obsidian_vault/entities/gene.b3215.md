---
entity_id: "gene.b3215"
entity_type: "gene"
name: "yhcA"
source_database: "NCBI RefSeq"
source_id: "gene-b3215"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3215"
  - "yhcA"
---

# yhcA

`gene.b3215`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3215`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhcA (gene.b3215) is a gene entity. It encodes yhcA (protein.P28722). Encoded protein function: FUNCTION: Could be required for the biogenesis of a putative fimbria. {ECO:0000250}. EcoCyc product frame: EG11515-MONOMER. Genomic coordinates: 3362112-3362786. EcoCyc protein note: YhcA is a hypothetical protein. Sequence similarity suggests that it may be a fimbrial chaperone and/or an outer membrane porin . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including gltF-yhcADEF; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28722|protein.P28722]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yhcA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010552,ECOCYC:EG11515,GeneID:947741`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3362112-3362786:+; feature_type=gene

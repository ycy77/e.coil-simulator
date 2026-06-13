---
entity_id: "gene.b2597"
entity_type: "gene"
name: "raiA"
source_database: "NCBI RefSeq"
source_id: "gene-b2597"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2597"
  - "raiA"
---

# raiA

`gene.b2597`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2597`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

raiA (gene.b2597) is a gene entity. It encodes raiA (protein.P0AD49). Encoded protein function: FUNCTION: During stationary phase prevents 70S dimer formation, probably in order to regulate translation efficiency during transition between the exponential and the stationary phases (PubMed:16324148). During environmental stress such as cold shock or excessive cell density at stationary phase, stabilizes the 70S ribosome against dissociation, inhibits translation elongation and increases translation accuracy (PubMed:11375931, PubMed:15219834). When normal growth conditions are restored, is quickly released from the ribosome (PubMed:11375931). Has been suggested to inhibit translation elongation by blocking the A-site (aminoacyl-tRNA site) (PubMed:11375931). Has also been suggested to inhibit translation initiation by blocking the A-site and P-site (peptidyl-tRNA site) of the ribosome (PubMed:15502846, PubMed:23420694). At 15 degrees Celsius binds 30S subunits and stimulates their association with 50S subunits into idle 70S ribosomes (PubMed:23420694). Crystallization with T...

## Biological Role

Activated by DNA-binding transcriptional dual regulator Cra (complex.ecocyc.PC00061), crp (protein.P0ACJ8), zraR (protein.P14375).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD49|protein.P0AD49]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.PC00061|complex.ecocyc.PC00061]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=raiA; function=+
- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=raiA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008540,ECOCYC:EG11151,GeneID:947129`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2737154-2737495:+; feature_type=gene

---
entity_id: "gene.b0075"
entity_type: "gene"
name: "leuL"
source_database: "NCBI RefSeq"
source_id: "gene-b0075"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0075"
  - "leuL"
---

# leuL

`gene.b0075`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0075`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

leuL (gene.b0075) is a gene entity. It encodes leuL (protein.P0AD79). Encoded protein function: FUNCTION: Involved in control of the biosynthesis of leucine. EcoCyc product frame: EG11280-MONOMER. EcoCyc synonyms: leuLP, leulL, leulLP, leuIP. Genomic coordinates: 83622-83708. EcoCyc protein note: Based on a putative adjacent terminator, observed transcription termination in vitro, demonstrated regulation by attenuation of the similar Salmonella operon, and the presence of four leucines within its sequence, LeuL is presumed to be a leader peptide involved in attenuation of transcription of the leuLABCD operon in response to leucine abundance . Reviews:

## Biological Role

Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD79|protein.P0AD79]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=leuL; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=leuL; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000269,ECOCYC:EG11280,GeneID:946072`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:83622-83708:-; feature_type=gene

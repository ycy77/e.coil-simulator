---
entity_id: "gene.b3442"
entity_type: "gene"
name: "yhhZ"
source_database: "NCBI RefSeq"
source_id: "gene-b3442"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3442"
  - "yhhZ"
---

# yhhZ

`gene.b3442`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3442`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhhZ (gene.b3442) is a gene entity. It encodes yhhZ (protein.P46855). Encoded protein function: hcp1 family member YhhZ EcoCyc product frame: G7759-MONOMER. Genomic coordinates: 3581863-3583041. EcoCyc protein note: A yhhZ mutant was found to be a weak suppressor of the synthetic lethal phenotype of a pta recBC(ts) strain . A ΔyhhZ mutant has aggravating genetic interactions with genes involved in DNA recombination .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46855|protein.P46855]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yhhZ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011244,ECOCYC:G7759,GeneID:947952`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3581863-3583041:+; feature_type=gene

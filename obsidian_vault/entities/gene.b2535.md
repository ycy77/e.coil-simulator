---
entity_id: "gene.b2535"
entity_type: "gene"
name: "csiE"
source_database: "NCBI RefSeq"
source_id: "gene-b2535"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2535"
  - "csiE"
---

# csiE

`gene.b2535`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2535`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

csiE (gene.b2535) is a gene entity. It encodes csiE (protein.P54901). Encoded protein function: Stationary phase-inducible protein CsiE EcoCyc product frame: G7329-MONOMER. EcoCyc synonyms: csi-16. Genomic coordinates: 2665435-2666715. EcoCyc protein note: Expression of csiE is regulated by RpoS (σS) and the cAMP-CRP complex .

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P54901|protein.P54901]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=csiE; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=csiE; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=csiE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008346,ECOCYC:G7329,GeneID:947009`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2665435-2666715:+; feature_type=gene

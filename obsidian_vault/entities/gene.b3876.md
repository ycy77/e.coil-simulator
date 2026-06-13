---
entity_id: "gene.b3876"
entity_type: "gene"
name: "yihO"
source_database: "NCBI RefSeq"
source_id: "gene-b3876"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3876"
  - "yihO"
---

# yihO

`gene.b3876`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3876`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yihO (gene.b3876) is a gene entity. It encodes yihO (protein.P32136). Encoded protein function: FUNCTION: Could be involved in sulfoquinovose import. {ECO:0000269|PubMed:24463506}. EcoCyc product frame: YIHO-MONOMER. EcoCyc synonyms: squO. Genomic coordinates: 4064363-4065766. EcoCyc protein note: An E. coli K-12 ΔyihO strain does not grow when sulfoquinovose is supplied as the sole carbon source. yihO is part of a 10-gene cluster which is conserved across E. coli species and has been implicated in sulfoquinovose catabolism . The YihO protein is a member of the glycoside-pentoside-hexuronide (GPH) cation symporter family of transporters but its transport mechanism has not been experimentally characterised.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32136|protein.P32136]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yihO; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012661,ECOCYC:EG11841,GeneID:948377`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4064363-4065766:-; feature_type=gene

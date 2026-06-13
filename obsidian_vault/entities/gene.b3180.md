---
entity_id: "gene.b3180"
entity_type: "gene"
name: "yhbY"
source_database: "NCBI RefSeq"
source_id: "gene-b3180"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3180"
  - "yhbY"
---

# yhbY

`gene.b3180`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3180`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhbY (gene.b3180) is a gene entity. It encodes yhbY (protein.P0AGK4). Encoded protein function: RNA-binding protein YhbY EcoCyc product frame: EG12794-MONOMER. Genomic coordinates: 3327790-3328083. EcoCyc protein note: YhbY is a ribosome assembly factor that is involved in both 30S and 50S ribosomal subunit assembly . YhbY belongs to the CRM domain family of proteins. It was found to associate with the 50S subunit of the ribosome and was also found to cosediment with a pre-50S ribosomal subunit . The crystal structure of YhbY has been solved at 1.5 Å resolution. The structure of YhbY is similar to that of the C-terminal domain of the translation initiation factor IF3, with a basic exterior surface that is predicted to bind RNA . A ΔyhbY mutant grows more slowly than wild type, accumulates increased levels of pre-50S ribosomal subunits , and is cold-sensitive . In a large genetic interaction screen, yhbY showed genetic interactions with a number of RNases involved in rRNA maturation as well as several ribosome biogenesis factors and ribosomal subunit proteins. A ΔyhbY mutant shows decreased translational fidelity and decreased 5' end processing of rRNAs .

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGK4|protein.P0AGK4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010452,ECOCYC:EG12794,GeneID:947688`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3327790-3328083:+; feature_type=gene

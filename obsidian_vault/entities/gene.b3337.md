---
entity_id: "gene.b3337"
entity_type: "gene"
name: "bfd"
source_database: "NCBI RefSeq"
source_id: "gene-b3337"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3337"
  - "bfd"
---

# bfd

`gene.b3337`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3337`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bfd (gene.b3337) is a gene entity. It encodes bfd (protein.P0AE56). Encoded protein function: FUNCTION: Required for mobilization of iron from the bacterioferritin (BFR) complex (By similarity). {ECO:0000250|UniProtKB:Q9HY80}. EcoCyc product frame: EG11181-MONOMER. EcoCyc synonyms: yheA. Genomic coordinates: 3466797-3466991. EcoCyc protein note: Bfd is thought to be involved in Bfr iron storage and iron release functions or in regulation of EG10113-MONOMER protein Bfr . Bfd is monomeric and contains a [2Fe-2S] cluster . Bfd interacts with Bfr . Overexpression of Bfd results in a slight increase in the MIC of penicillin G . Bfd: "bacterioferritin-associated ferredoxin" Reviews:

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE56|protein.P0AE56]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=bfd; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=bfd; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010906,ECOCYC:EG11181,GeneID:947836`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3466797-3466991:-; feature_type=gene

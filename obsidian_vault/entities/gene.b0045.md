---
entity_id: "gene.b0045"
entity_type: "gene"
name: "yaaU"
source_database: "NCBI RefSeq"
source_id: "gene-b0045"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0045"
  - "yaaU"
---

# yaaU

`gene.b0045`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0045`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yaaU (gene.b0045) is a gene entity. It encodes yaaU (protein.P31679). Encoded protein function: Putative metabolite transport protein YaaU EcoCyc product frame: YAAU-MONOMER. EcoCyc synonyms: yabE. Genomic coordinates: 45807-47138. EcoCyc protein note: The YaaU protein is an uncharacterised member of the Sugar Porter (SP) family within the major facilitator superfamily (MFS) of transporters . yaaU shows differential codon adaptation, resulting in differential translation efficiency signatures, in aerotolerant compared to obligate anaerobic microbes. It was therefore predicted to play a role in the oxidative stress response. A yaaU deletion mutant was shown to be more sensitive than wild-type specifically to hydrogen peroxide exposure, but not other stresses .

## Biological Role

Activated by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31679|protein.P31679]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=yaaU; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000156,ECOCYC:EG11566,GeneID:944766`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:45807-47138:+; feature_type=gene

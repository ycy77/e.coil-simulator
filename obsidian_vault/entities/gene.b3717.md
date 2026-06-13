---
entity_id: "gene.b3717"
entity_type: "gene"
name: "cbrC"
source_database: "NCBI RefSeq"
source_id: "gene-b3717"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3717"
  - "cbrC"
---

# cbrC

`gene.b3717`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3717`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cbrC (gene.b3717) is a gene entity. It encodes cbrC (protein.P31469). Encoded protein function: UPF0167 protein CbrC (CreB-regulated gene C protein) EcoCyc product frame: EG11727-MONOMER. EcoCyc synonyms: yieJ. Genomic coordinates: 3898022-3898609. EcoCyc protein note: Overexpression of CbrC causes a Colicin E2 tolerant ("Cet2") phenotype . Transcription of cbrB, the first gene of the predicted cbrBC transcription unit, is induced by the CreBC two-component system by minimal media growth conditions . Certain cbrBC mutants show hypersensitivity to nitrofurzone . cbrC insertion or deletion mutants are more susceptible to colicin E2 than wild type in the CreC hyperactive mutant background . CbrC: "creB-regulated gene C"

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31469|protein.P31469]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cbrC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012158,ECOCYC:EG11727,GeneID:948230`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3898022-3898609:+; feature_type=gene

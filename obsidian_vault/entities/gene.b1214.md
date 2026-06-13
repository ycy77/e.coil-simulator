---
entity_id: "gene.b1214"
entity_type: "gene"
name: "ychA"
source_database: "NCBI RefSeq"
source_id: "gene-b1214"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1214"
  - "ychA"
---

# ychA

`gene.b1214`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1214`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ychA (gene.b1214) is a gene entity. It encodes ychA (protein.P0AGM5). Encoded protein function: UPF0162 protein YchA (Protein SirB1) EcoCyc product frame: EG11251-MONOMER. EcoCyc synonyms: sirB1. Genomic coordinates: 1267320-1268129. EcoCyc protein note: No information about this protein was found by a literature search conducted on February 6, 2017.

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGM5|protein.P0AGM5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ychA; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ychA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004074,ECOCYC:EG11251,GeneID:945784`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1267320-1268129:+; feature_type=gene

---
entity_id: "gene.b3205"
entity_type: "gene"
name: "rapZ"
source_database: "NCBI RefSeq"
source_id: "gene-b3205"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3205"
  - "rapZ"
---

# rapZ

`gene.b3205`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3205`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rapZ (gene.b3205) is a gene entity. It encodes rapZ (protein.P0A894). Encoded protein function: FUNCTION: Modulates the synthesis of GlmS, by affecting the processing and stability of the regulatory small RNA GlmZ. When glucosamine-6-phosphate (GlcN6P) concentrations are high in the cell, RapZ binds GlmZ and targets it to cleavage by RNase E. Consequently, GlmZ is inactivated and unable to activate GlmS synthesis. Under low GlcN6P concentrations, RapZ is sequestered and inactivated by an other regulatory small RNA, GlmY, preventing GlmZ degradation and leading to synthesis of GlmS (PubMed:17824929, PubMed:23475961). Displays ATPase and GTPase activities in vitro. Can also hydrolyze pNPP (PubMed:19074378). {ECO:0000269|PubMed:17824929, ECO:0000269|PubMed:19074378, ECO:0000269|PubMed:23475961}. EcoCyc product frame: EG12146-MONOMER. EcoCyc synonyms: yhbJ. Genomic coordinates: 3347115-3347969.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A894|protein.P0A894]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rapZ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010522,ECOCYC:EG12146,GeneID:947727`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3347115-3347969:+; feature_type=gene

---
entity_id: "gene.b2013"
entity_type: "gene"
name: "tsuA"
source_database: "NCBI RefSeq"
source_id: "gene-b2013"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2013"
  - "tsuA"
---

# tsuA

`gene.b2013`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2013`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tsuA (gene.b2013) is a gene entity. It encodes tsuA (protein.P33015). Encoded protein function: FUNCTION: Mediates thiosulfate uptake. {ECO:0000269|PubMed:32779574, ECO:0000269|PubMed:32923628}. EcoCyc product frame: EG11895-MONOMER. EcoCyc synonyms: yeeE. Genomic coordinates: 2084467-2085525. EcoCyc protein note: TsuA is an inner membrane protein that imports S2O3 as a sulfur source. Deletion of tsuA inhibits the ability of strains (ΔABC-7-CPLX cysPUWA or ΔEG10183 cysA) lacking the sulfate/thiosulfate ABC-type transporters to grow with thiosulfate as sole sulfur source . EG11894-MONOMER TsuB is required for TsuA-mediated thiosulfate uptake in vivo and the two proteins may physically interact . TsuA is predicted to be an inner membrane protein with nine transmembrane domains; experimental topology analysis suggests the C terminus is located in the cytoplasm . tsuA is a member of the PC00040 CysB regulon; TsuA may be subject to post-transcriptional control by G7459-MONOMER RppH-dependent mRNA degradation; TsuA supports the preferential use of thiosulfate as a sulfur source in ΔrppH cells . Expression of tsuA is downregulated in response to cobalt and upregulated in response to hydroquinone...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33015|protein.P33015]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006691,ECOCYC:EG11895,GeneID:946526`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2084467-2085525:-; feature_type=gene

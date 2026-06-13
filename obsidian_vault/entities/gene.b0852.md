---
entity_id: "gene.b0852"
entity_type: "gene"
name: "rimK"
source_database: "NCBI RefSeq"
source_id: "gene-b0852"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0852"
  - "rimK"
---

# rimK

`gene.b0852`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0852`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rimK (gene.b0852) is a gene entity. It encodes rimK (protein.P0C0U4). Encoded protein function: FUNCTION: An L-glutamate ligase that catalyzes the ATP-dependent post-translational addition of glutamate residues to the C-terminus of ribosomal protein bS6 (RpsF). Is also able to catalyze the synthesis of poly-alpha-glutamate in vitro, via ATP hydrolysis from unprotected glutamate as substrate. The number of glutamate residues added to either RpsF or to poly-alpha-glutamate changes with pH. {ECO:0000255|HAMAP-Rule:MF_01552, ECO:0000269|PubMed:21278279, ECO:0000269|PubMed:2570347}. EcoCyc product frame: EG10852-MONOMER. EcoCyc synonyms: nek. Genomic coordinates: 891967-892869.

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), oxyR (protein.P0ACQ4). Activated by soxS (protein.P0A9E2), marA (protein.P0ACH5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C0U4|protein.P0C0U4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `S` - regulator=SoxS; target=rimK; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=rimK; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=rimK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002903,ECOCYC:EG10852,GeneID:945484`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:891967-892869:+; feature_type=gene

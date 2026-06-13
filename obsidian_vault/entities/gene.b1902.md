---
entity_id: "gene.b1902"
entity_type: "gene"
name: "ftnB"
source_database: "NCBI RefSeq"
source_id: "gene-b1902"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1902"
  - "ftnB"
---

# ftnB

`gene.b1902`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1902`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftnB (gene.b1902) is a gene entity. It encodes ftnB (protein.P0A9A2). Encoded protein function: Bacterial non-heme ferritin-like protein EcoCyc product frame: G7033-MONOMER. EcoCyc synonyms: yecI. Genomic coordinates: 1986925-1987428. EcoCyc protein note: No information about this protein was found by a literature search conducted on September 5, 2006.

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), rpoD (protein.P00579), fur (protein.P0A9A9), cpxR (protein.P0AE88), rpoE (protein.P0AGB6), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9A2|protein.P0A9A2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ftnB; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=ftnB; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=ftnB; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=ftnB; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ftnB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006333,ECOCYC:G7033,GeneID:946407`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1986925-1987428:+; feature_type=gene

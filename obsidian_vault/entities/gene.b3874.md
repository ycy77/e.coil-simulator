---
entity_id: "gene.b3874"
entity_type: "gene"
name: "yihN"
source_database: "NCBI RefSeq"
source_id: "gene-b3874"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3874"
  - "yihN"
---

# yihN

`gene.b3874`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3874`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yihN (gene.b3874) is a gene entity. It encodes yihN (protein.P32135). Encoded protein function: Inner membrane protein YihN EcoCyc product frame: YIHN-MONOMER. Genomic coordinates: 4062247-4063512. EcoCyc protein note: In the Transporter Classification Database, YihN is an uncharacterised member of the Glycerophhosphodiester Uptake (GlpU) Family within the Major Facilitator Superfamily (MFS) . The expression of yihN is repressed in the presence of 10 μM cystine .

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32135|protein.P32135]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=yihN; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012656,ECOCYC:EG11840,GeneID:948365`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4062247-4063512:+; feature_type=gene

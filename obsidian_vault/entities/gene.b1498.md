---
entity_id: "gene.b1498"
entity_type: "gene"
name: "ydeN"
source_database: "NCBI RefSeq"
source_id: "gene-b1498"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1498"
  - "ydeN"
---

# ydeN

`gene.b1498`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1498`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydeN (gene.b1498) is a gene entity. It encodes ydeN (protein.P77318). Encoded protein function: Uncharacterized sulfatase YdeN (EC 3.1.6.-) EcoCyc product frame: G6788-MONOMER. Genomic coordinates: 1580842-1582524. EcoCyc protein note: YdeN is a putative Ser-type sulfatase .

## Biological Role

Repressed by fur (protein.P0A9A9), gadX (protein.P37639). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77318|protein.P77318]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ydeN; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB|EcoCyc` `S` - regulator=Fur; target=ydeN; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=ydeN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004988,ECOCYC:G6788,GeneID:945957`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1580842-1582524:-; feature_type=gene

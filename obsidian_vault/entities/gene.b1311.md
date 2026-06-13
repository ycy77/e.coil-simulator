---
entity_id: "gene.b1311"
entity_type: "gene"
name: "ycjO"
source_database: "NCBI RefSeq"
source_id: "gene-b1311"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1311"
  - "ycjO"
---

# ycjO

`gene.b1311`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1311`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycjO (gene.b1311) is a gene entity. It encodes ycjO (protein.P0AFR7). Encoded protein function: FUNCTION: Part of the ABC transporter complex YcjNOPV primarily involved in maltose uptake (PubMed:40721696). The transporter may also be involved in the uptake of glucosides (PubMed:40721696). In vitro, it actively transports ethidium bromide (EB) (PubMed:40721696). This subunit is responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:40721696, ECO:0000305}. EcoCyc product frame: YCJO-MONOMER. Genomic coordinates: 1373222-1374103. EcoCyc protein note: YcjO is one of two predicted inner membrane components of a putative ATP-binding cassette transporter (YcjNOPV) .

## Biological Role

Repressed by ycjW (protein.P77615).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFR7|protein.P0AFR7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77615|protein.P77615]] `RegulonDB` `S` - regulator=YcjW; target=ycjO; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004405,ECOCYC:G6649,GeneID:945888`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1373222-1374103:+; feature_type=gene

---
entity_id: "gene.b1312"
entity_type: "gene"
name: "ycjP"
source_database: "NCBI RefSeq"
source_id: "gene-b1312"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1312"
  - "ycjP"
---

# ycjP

`gene.b1312`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1312`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycjP (gene.b1312) is a gene entity. It encodes ycjP (protein.P77716). Encoded protein function: FUNCTION: Part of the ABC transporter complex YcjNOPV primarily involved in maltose uptake (PubMed:40721696). The transporter may also be involved in the uptake of glucosides (PubMed:40721696). In vitro, it actively transports ethidium bromide (EB) (PubMed:40721696). This subunit is responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:40721696, ECO:0000305}. EcoCyc product frame: YCJP-MONOMER. Genomic coordinates: 1374090-1374932. EcoCyc protein note: YcjP is one of two predicted inner membrane components of a putative ATP-binding cassette transporter (YcjNOPV) .

## Biological Role

Repressed by glaR (protein.P37338), ycjW (protein.P77615).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77716|protein.P77716]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ycjP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P77615|protein.P77615]] `RegulonDB` `S` - regulator=YcjW; target=ycjP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004409,ECOCYC:G6650,GeneID:945892`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1374090-1374932:+; feature_type=gene

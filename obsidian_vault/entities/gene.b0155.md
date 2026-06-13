---
entity_id: "gene.b0155"
entity_type: "gene"
name: "clcA"
source_database: "NCBI RefSeq"
source_id: "gene-b0155"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0155"
  - "clcA"
---

# clcA

`gene.b0155`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0155`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

clcA (gene.b0155) is a gene entity. It encodes clcA (protein.P37019). Encoded protein function: FUNCTION: Proton-coupled chloride transporter. Functions as antiport system and exchanges two chloride ions for 1 proton. Probably acts as an electrical shunt for an outwardly-directed proton pump that is linked to amino acid decarboxylation, as part of the extreme acid resistance (XAR) response. {ECO:0000269|PubMed:12384697, ECO:0000269|PubMed:14985752, ECO:0000269|PubMed:16341087, ECO:0000269|PubMed:16905147, ECO:0000269|PubMed:18678918}. EcoCyc product frame: YADQ-MONOMER. EcoCyc synonyms: eriC, yadQ. Genomic coordinates: 175107-176528.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37019|protein.P37019]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000533,ECOCYC:EG12331,GeneID:946715`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:175107-176528:+; feature_type=gene

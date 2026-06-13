---
entity_id: "gene.b1592"
entity_type: "gene"
name: "clcB"
source_database: "NCBI RefSeq"
source_id: "gene-b1592"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1592"
  - "clcB"
---

# clcB

`gene.b1592`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1592`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

clcB (gene.b1592) is a gene entity. It encodes clcB (protein.P76175). Encoded protein function: FUNCTION: Probably acts as an electrical shunt for an outwardly-directed proton pump that is linked to amino acid decarboxylation, as part of the extreme acid resistance (XAR) response. {ECO:0000269|PubMed:12384697}. EcoCyc product frame: YNFJ-MONOMER. EcoCyc synonyms: ynfJ, mriT. Genomic coordinates: 1665315-1666571. EcoCyc protein note: ClcB is a member of the ubiquitous ClC family of Cl- channels which promote the the selective flow of Cl- ions across cell membranes . E. coli K-12 contains two chloride channels, one of which - EG12331 "ClcA" - has been characterized as a chloride:H+ antiporter . Cells lacking both ClcB and ClcA do not survive acid shock conditions (pH2.5, 2 hrs at 37°C in minimal medium) and a biological role for them in the extreme acid resistance (XAR) response has been proposed .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76175|protein.P76175]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005317,ECOCYC:G6850,GeneID:947179`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1665315-1666571:+; feature_type=gene

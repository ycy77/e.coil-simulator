---
entity_id: "gene.b0493"
entity_type: "gene"
name: "ybbO"
source_database: "NCBI RefSeq"
source_id: "gene-b0493"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0493"
  - "ybbO"
---

# ybbO

`gene.b0493`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0493`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybbO (gene.b0493) is a gene entity. It encodes ybbO (protein.P0AFP4). Encoded protein function: Uncharacterized oxidoreductase YbbO (EC 1.-.-.-) EcoCyc product frame: G6269-MONOMER. Genomic coordinates: 518340-519149. EcoCyc protein note: YbbO is an NADP+-dependent aldehyde reductase that showed broad substrate activity toward aldehydes with a preference for long-chain fatty aldehydes . Among the substrates tested by , it has the highest activity toward hexanal and octanal ; showed that the enzyme has maximal activity with C16 and C18 chain length aldehydes. A broad survey of aldehyde reductases showed that YbbO was one of several endogenous aldehyde reductases that contribute to the degradation of desired aldehyde end products of metabolic engineering . In recombinant E. coli expressing a β-carotene biosynthesis pathway and β-carotene 15',15'-monooxygenase, production of retinol can be increased by overexpressing ybbO . Deletion of ybbO reduces long chain fatty alcohol production from externally added substrates by 90% .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFP4|protein.P0AFP4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001709,ECOCYC:G6269,GeneID:945337`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:518340-519149:-; feature_type=gene

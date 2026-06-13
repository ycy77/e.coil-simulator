---
entity_id: "gene.b1001"
entity_type: "gene"
name: "yccE"
source_database: "NCBI RefSeq"
source_id: "gene-b1001"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1001"
  - "yccE"
---

# yccE

`gene.b1001`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1001`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yccE (gene.b1001) is a gene entity. It encodes yccE (protein.P36661). Encoded protein function: Uncharacterized protein YccE (ORF-D) EcoCyc product frame: EG12196-MONOMER. Genomic coordinates: 1064036-1065292. EcoCyc protein note: A transposon insertion mutant in yccE shows slower growth than wild-type in the absence of chloramphenicol, but grows like wild-type in the presence of chloramphenicol. Overexpression of yccE enhances the susceptibility of biofilms to tobramycin .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36661|protein.P36661]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003384,ECOCYC:EG12196,GeneID:947468`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1064036-1065292:+; feature_type=gene

---
entity_id: "gene.b0190"
entity_type: "gene"
name: "yaeQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0190"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0190"
  - "yaeQ"
---

# yaeQ

`gene.b0190`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0190`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yaeQ (gene.b0190) is a gene entity. It encodes yaeQ (protein.P0AA97). Encoded protein function: Uncharacterized protein YaeQ EcoCyc product frame: G6098-MONOMER. Genomic coordinates: 214291-214836. EcoCyc protein note: Purified YaeQ protein does not have transcription antitermination activity , although expression of the Salmonella typhimurium yaeQ homolog suppresses the E. coli rfaH mutant defect in expression of the hlyCABD operon . A ΔyaeQ mutant has aggravating genetic interactions with genes involved in DNA recombination .

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA97|protein.P0AA97]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000648,ECOCYC:G6098,GeneID:946809`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:214291-214836:+; feature_type=gene

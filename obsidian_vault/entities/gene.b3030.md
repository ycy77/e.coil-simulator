---
entity_id: "gene.b3030"
entity_type: "gene"
name: "parE"
source_database: "NCBI RefSeq"
source_id: "gene-b3030"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3030"
  - "parE"
---

# parE

`gene.b3030`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3030`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

parE (gene.b3030) is a gene entity. It encodes parE (protein.P20083). Encoded protein function: FUNCTION: Topoisomerase IV is essential for chromosome segregation; it is the principal protein responsible for decatenating newly replicated chromosomes (PubMed:9334322). It relaxes supercoiled DNA (PubMed:15105144, PubMed:21300644, PubMed:23294697, PubMed:23352267). MukB stimulates the relaxation activity of topoisomerase IV and also has a modest effect on decatenation (PubMed:20921377). {ECO:0000269|PubMed:15105144, ECO:0000269|PubMed:20921377, ECO:0000269|PubMed:21300644, ECO:0000269|PubMed:23294697, ECO:0000269|PubMed:23352267, ECO:0000269|PubMed:9334322}. EcoCyc product frame: EG10687-MONOMER. EcoCyc synonyms: nfxD. Genomic coordinates: 3173504-3175396. EcoCyc protein note: The crystal structures of two N-terminal fragments of ParE have been solved .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P20083|protein.P20083]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009950,ECOCYC:EG10687,GeneID:947501`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3173504-3175396:-; feature_type=gene

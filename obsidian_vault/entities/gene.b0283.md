---
entity_id: "gene.b0283"
entity_type: "gene"
name: "paoD"
source_database: "NCBI RefSeq"
source_id: "gene-b0283"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0283"
  - "paoD"
---

# paoD

`gene.b0283`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0283`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paoD (gene.b0283) is a gene entity. It encodes paoD (protein.P77183). Encoded protein function: FUNCTION: Chaperone required for the production of an active PaoABC aldehyde oxidoreductase. Stabilizes the PaoC subunit and is required for the insertion of the molybdenum cofactor into this subunit (PubMed:19368556, PubMed:21081498). Binds molybdenum cofactor. Binds the molybdopterin cytosine dinucleotide (MCD) form of the cofactor after its formation by the molybdenum cofactor cytidylyltransferase MocA (PubMed:24498065). {ECO:0000269|PubMed:19368556, ECO:0000269|PubMed:21081498, ECO:0000269|PubMed:24498065}. EcoCyc product frame: G6154-MONOMER. EcoCyc synonyms: yagQ. Genomic coordinates: 297770-298726.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77183|protein.P77183]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000984,ECOCYC:G6154,GeneID:945010`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:297770-298726:-; feature_type=gene

---
entity_id: "gene.b1336"
entity_type: "gene"
name: "abgT"
source_database: "NCBI RefSeq"
source_id: "gene-b1336"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1336"
  - "abgT"
---

# abgT

`gene.b1336`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1336`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

abgT (gene.b1336) is a gene entity. It encodes abgT (protein.P46133). Encoded protein function: FUNCTION: Essential for aminobenzoyl-glutamate utilization. It catalyzes the concentration-dependent uptake of p-aminobenzoyl-glutamate (PABA-GLU) into the cell and allows accumulation of PABA-GLU to a concentration enabling AbgAB to catalyze cleavage into p-aminobenzoate and glutamate. It also seems to increase the sensitivity to low levels of aminobenzoyl-glutamate. May actually serve physiologically as a transporter for some other molecule, perhaps a dipeptide, and that it transports p-aminobenzoyl-glutamate as a secondary activity. The physiological role of abgABT should be clarified. {ECO:0000269|PubMed:17307853, ECO:0000269|PubMed:20190044}. EcoCyc product frame: ABGT-MONOMER. EcoCyc synonyms: ydaH. Genomic coordinates: 1400247-1401773. EcoCyc protein note: Subject to experimental manipulation, AbgT mediates the transport of p-aminobenzoyl-glutamate - a folate catabolite; the physiological role of the protein has not been confirmed - it may participate in a folate salvage or recycling pathway or it may function to transport an as-yet undefined molecule. Overexpression of abgT supports the growth of p-aminobenzoate auxotrophs on exogenous p-aminobenzoyl glutamate...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46133|protein.P46133]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004488,ECOCYC:EG12853,GeneID:945912`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1400247-1401773:-; feature_type=gene

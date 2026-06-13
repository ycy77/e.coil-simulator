---
entity_id: "gene.b1572"
entity_type: "gene"
name: "ydfB"
source_database: "NCBI RefSeq"
source_id: "gene-b1572"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1572"
  - "ydfB"
---

# ydfB

`gene.b1572`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1572`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydfB (gene.b1572) is a gene entity. It encodes ydfB (protein.P29009). Encoded protein function: Uncharacterized protein YdfB EcoCyc product frame: EG11301-MONOMER. Genomic coordinates: 1648665-1648793. EcoCyc protein note: The YdfB protein is expressed during both exponential and stationary phase . The majority of YdfB partitions into the soluble fraction using a sucrose fractionation protocol .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P29009|protein.P29009]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ydfB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005253,ECOCYC:EG11301,GeneID:946176`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1648665-1648793:+; feature_type=gene

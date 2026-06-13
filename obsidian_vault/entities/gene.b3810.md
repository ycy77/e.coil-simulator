---
entity_id: "gene.b3810"
entity_type: "gene"
name: "yigA"
source_database: "NCBI RefSeq"
source_id: "gene-b3810"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3810"
  - "yigA"
---

# yigA

`gene.b3810`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3810`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yigA (gene.b3810) is a gene entity. It encodes yigA (protein.P23305). Encoded protein function: Uncharacterized protein YigA EcoCyc product frame: EG11201-MONOMER. Genomic coordinates: 3995583-3996290. EcoCyc protein note: No information about this protein was found by a literature search conducted on November 7, 2018.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23305|protein.P23305]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yigA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012444,ECOCYC:EG11201,GeneID:948359`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3995583-3996290:+; feature_type=gene

---
entity_id: "gene.b3196"
entity_type: "gene"
name: "yrbG"
source_database: "NCBI RefSeq"
source_id: "gene-b3196"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3196"
  - "yrbG"
---

# yrbG

`gene.b3196`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3196`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yrbG (gene.b3196) is a gene entity. It encodes yrbG (protein.P45394). Encoded protein function: Inner membrane protein YrbG EcoCyc product frame: YRBG-MONOMER. Genomic coordinates: 3340275-3341252. EcoCyc protein note: YrbG is an uncharacterized member of the CaCA family of metal cation exchangers . Sequence similarity suggests it may function as a sodium ion/calcium ion exchanger. However direct measurement of cytosolic calcium levels using the Ca2+ activated photoprotein, aequorin, suggests that it does not play a role in regulating cytosolic Ca2+ . YrbG is predicted to be an inner membrane protein; sequence alignment and experimental topology analysis suggest that the protein has a two-domain structure each with five transmembrane segments and with opposite orientation in the membrane . yrbG is not essential for growth .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45394|protein.P45394]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yrbG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010502,ECOCYC:EG12802,GeneID:947730`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3340275-3341252:+; feature_type=gene

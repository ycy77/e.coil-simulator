---
entity_id: "gene.b1644"
entity_type: "gene"
name: "ydhJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1644"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1644"
  - "ydhJ"
---

# ydhJ

`gene.b1644`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1644`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydhJ (gene.b1644) is a gene entity. It encodes ydhJ (protein.P76185). Encoded protein function: Uncharacterized protein YdhJ EcoCyc product frame: G6884-MONOMER. Genomic coordinates: 1721264-1722121. EcoCyc protein note: No information about this protein was found by a literature search conducted on December 12, 2012.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76185|protein.P76185]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=ydhJ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005501,ECOCYC:G6884,GeneID:946499`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1721264-1722121:+; feature_type=gene

---
entity_id: "gene.b1606"
entity_type: "gene"
name: "folM"
source_database: "NCBI RefSeq"
source_id: "gene-b1606"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1606"
  - "folM"
---

# folM

`gene.b1606`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1606`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

folM (gene.b1606) is a gene entity. It encodes folM (protein.P0AFS3). Encoded protein function: FUNCTION: Catalyzes the reduction of dihydromonapterin to tetrahydromonapterin. Also has lower activity with dihydrofolate. {ECO:0000269|PubMed:19897652}. EcoCyc product frame: G6862-MONOMER. EcoCyc synonyms: ydgB. Genomic coordinates: 1680976-1681698.

## Enriched Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFS3|protein.P0AFS3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005364,ECOCYC:G6862,GeneID:949096`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1680976-1681698:+; feature_type=gene

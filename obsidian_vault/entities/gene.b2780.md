---
entity_id: "gene.b2780"
entity_type: "gene"
name: "pyrG"
source_database: "NCBI RefSeq"
source_id: "gene-b2780"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2780"
  - "pyrG"
---

# pyrG

`gene.b2780`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2780`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pyrG (gene.b2780) is a gene entity. It encodes pyrG (protein.P0A7E5). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent amination of UTP to CTP with either L-glutamine or ammonia as the source of nitrogen. Regulates intracellular CTP levels through interactions with the four ribonucleotide triphosphates. {ECO:0000269|PubMed:11336655, ECO:0000269|PubMed:8385490, ECO:0000305|PubMed:15157079}. EcoCyc product frame: CTPSYN-MONOMER. Genomic coordinates: 2908029-2909666.

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7E5|protein.P0A7E5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009112,ECOCYC:EG10810,GeneID:946116`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2908029-2909666:-; feature_type=gene

---
entity_id: "gene.b3091"
entity_type: "gene"
name: "uxaA"
source_database: "NCBI RefSeq"
source_id: "gene-b3091"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3091"
  - "uxaA"
---

# uxaA

`gene.b3091`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3091`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uxaA (gene.b3091) is a gene entity. It encodes uxaA (protein.P42604). Encoded protein function: FUNCTION: Catalyzes the dehydration of D-altronate. {ECO:0000269|PubMed:3038546}. EcoCyc product frame: ALTRODEHYDRAT-MONOMER. EcoCyc synonyms: ygjW. Genomic coordinates: 3241827-3243314. EcoCyc protein note: Altronate dehydratase catalyzes the final reaction of the galacturonate branch of the hexuronate degradation pathway . Tagaturonate and fructuronate act as inducers ; production of the enzyme is under catabolite repression .

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42604|protein.P42604]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010164,ECOCYC:EG12734,GeneID:947603`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3241827-3243314:-; feature_type=gene

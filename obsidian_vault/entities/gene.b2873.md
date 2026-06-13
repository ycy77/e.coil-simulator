---
entity_id: "gene.b2873"
entity_type: "gene"
name: "hyuA"
source_database: "NCBI RefSeq"
source_id: "gene-b2873"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2873"
  - "hyuA"
---

# hyuA

`gene.b2873`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2873`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyuA (gene.b2873) is a gene entity. It encodes hyuA (protein.Q46806). Encoded protein function: FUNCTION: Catalyzes the stereospecific hydrolysis of the cyclic amide bond of D-hydantoin derivatives with an aromatic side chains at the 5'-position. Has no activity on dihydropyrimidines. The physiological function is unknown. {ECO:0000269|PubMed:11092864}. EcoCyc product frame: G7492-MONOMER. EcoCyc synonyms: ygeZ. Genomic coordinates: 3010028-3011413. EcoCyc protein note: Phenylhydantoinase is a novel enzyme exhibiting activity toward hydantoin derivatives with an aromatic side chain at the 5' position, with phenylhydantoin and hydroxyphenylhydantoin having the highest activity level. It is not active on dihydropyrimidines. The enzyme has a stereospecific preference for D-enantiomers. The physiological role of the enzyme is not yet known . HyuA has similarity to allantoinase enzymes , including AllB . The enzyme is a homotetramer . HyuA: hydantoin-utilizing enzyme A

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46806|protein.Q46806]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009436,ECOCYC:G7492,GeneID:947359`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3010028-3011413:+; feature_type=gene

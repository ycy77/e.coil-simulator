---
entity_id: "gene.b2147"
entity_type: "gene"
name: "preA"
source_database: "NCBI RefSeq"
source_id: "gene-b2147"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2147"
  - "preA"
---

# preA

`gene.b2147`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2147`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

preA (gene.b2147) is a gene entity. It encodes preA (protein.P25889). Encoded protein function: FUNCTION: Involved in pyrimidine base degradation. Catalyzes physiologically the reduction of uracil to 5,6-dihydrouracil (DHU) by using NADH as a specific cosubstrate. It also catalyzes the reverse reaction and the reduction of thymine to 5,6-dihydrothymine (DHT). {ECO:0000269|PubMed:18482579, ECO:0000269|PubMed:21169495}. EcoCyc product frame: EG11289-MONOMER. EcoCyc synonyms: yeiA. Genomic coordinates: 2235265-2236500. EcoCyc protein note: PreA was shown to form a complex with PreT; PreAT has NAD+-dependent dihydropyrimidine dehydrogenase activity . PreA is expected to be the FMN-binding subunit . Based on sequence similarity, PreA was predicted to be a dihydrothymine/dihydropyrimidine dehydrogenase . PreA has similarity to the C-terminal half of mammalian dihydropyrimidine dehydrogenase . PreA is required for swarming motility . PreA:

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25889|protein.P25889]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007098,ECOCYC:EG11289,GeneID:949037`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2235265-2236500:+; feature_type=gene

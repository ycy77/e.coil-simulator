---
entity_id: "gene.b2146"
entity_type: "gene"
name: "preT"
source_database: "NCBI RefSeq"
source_id: "gene-b2146"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2146"
  - "preT"
---

# preT

`gene.b2146`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2146`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

preT (gene.b2146) is a gene entity. It encodes preT (protein.P76440). Encoded protein function: FUNCTION: Involved in pyrimidine base degradation. Catalyzes physiologically the reduction of uracil to 5,6-dihydrouracil (DHU) by using NADH as a specific cosubstrate. It also catalyzes the reverse reaction and the reduction of thymine to 5,6-dihydrothymine (DHT). {ECO:0000269|PubMed:18482579, ECO:0000269|PubMed:21169495}. EcoCyc product frame: G7145-MONOMER. EcoCyc synonyms: yeiT. Genomic coordinates: 2234033-2235271. EcoCyc protein note: PreT was shown to form a complex with PreA; PreAT has NAD+-dependent dihydropyrimidine dehydrogenase activity . PreT is expected to be the FAD-binding subunit . Based on sequence similarity, PreT was predicted to be a dihydrothymine dehydrogenase or glutamate synthase . PreT has similarity to the N-terminal half of mammalian dihydropyrimidine dehydrogenase . Expression of preT is 20-fold higher in a biofilm than during exponential growth in liquid culture . PreT:

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76440|protein.P76440]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007096,ECOCYC:G7145,GeneID:949049`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2234033-2235271:+; feature_type=gene

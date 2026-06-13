---
entity_id: "gene.b0103"
entity_type: "gene"
name: "coaE"
source_database: "NCBI RefSeq"
source_id: "gene-b0103"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0103"
  - "coaE"
---

# coaE

`gene.b0103`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0103`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

coaE (gene.b0103) is a gene entity. It encodes coaE (protein.P0A6I9). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of the 3'-hydroxyl group of dephosphocoenzyme A to form coenzyme A. {ECO:0000255|HAMAP-Rule:MF_00376, ECO:0000269|PubMed:11292795}. EcoCyc product frame: EG12312-MONOMER. EcoCyc synonyms: yacE. Genomic coordinates: 112599-113219. EcoCyc protein note: Dephospho-CoA kinase catalyzes the final step in coenzyme A biosynthesis . The enzyme appeared to be a monomer in solution ; subsequent analysis of the crystal structure, where it appears as a trimer, led to the discovery that the presence of sulfate ions stabilizes a trimeric state in solution as well. The biological role of the trimeric form is unclear . Crystal structures of the enzyme have been solved . coaE is essential for growth .

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6I9|protein.P0A6I9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000357,ECOCYC:EG12312,GeneID:949060`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:112599-113219:-; feature_type=gene

---
entity_id: "gene.b0505"
entity_type: "gene"
name: "allA"
source_database: "NCBI RefSeq"
source_id: "gene-b0505"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0505"
  - "allA"
---

# allA

`gene.b0505`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0505`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

allA (gene.b0505) is a gene entity. It encodes allA (protein.P77731). Encoded protein function: FUNCTION: Catalyzes the catabolism of the allantoin degradation intermediate (S)-ureidoglycolate, generating urea and glyoxylate. Involved in the anaerobic utilization of allantoin as sole nitrogen source. Reinforces the induction of genes involved in the degradation of allantoin and glyoxylate by producing glyoxylate. {ECO:0000255|HAMAP-Rule:MF_00616, ECO:0000269|PubMed:10601204, ECO:0000269|PubMed:24107613}. EcoCyc product frame: G6275-MONOMER. EcoCyc synonyms: glxA2, ybbT. Genomic coordinates: 532451-532933. EcoCyc protein note: Ureidoglycolate lyase catalyzes the conversion of ureidoglycolate to glyoxylate and urea . E. coli is able to utilize allantoin as a sole source of nitrogen under anaerobic conditions, but can not utilize it as a sole source of carbon. An allA mutant is not impaired in the utilization of allantoin . Ureidoglycolate lyase activity is slightly induced by growth on allantoin as the sole source of nitrogen . Transcription of allA is induced by growth on glyoxylate .

## Biological Role

Repressed by allR (protein.P0ACN4).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77731|protein.P77731]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACN4|protein.P0ACN4]] `RegulonDB` `C` - regulator=AllR; target=allA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001747,ECOCYC:G6275,GeneID:945141`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:532451-532933:+; feature_type=gene

---
entity_id: "gene.b2451"
entity_type: "gene"
name: "eutA"
source_database: "NCBI RefSeq"
source_id: "gene-b2451"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2451"
  - "eutA"
---

# eutA

`gene.b2451`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2451`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eutA (gene.b2451) is a gene entity. It encodes eutA (protein.P76551). Encoded protein function: FUNCTION: Reactivates suicidally inhibited ethanolamine ammonia-lyase (EAL), cyanocobalamin-inactivated EAL and O(2)-inactivated EAL; requires Mg(2+), ATP and adenosylcobalamin. Reactivation probably occurs by the ATP-dependent exchange of cobalamin. {ECO:0000269|PubMed:15466038}. EcoCyc product frame: G7281-MONOMER. EcoCyc synonyms: yffT. Genomic coordinates: 2565481-2566884. EcoCyc protein note: EutA is the reactivating factor for ETHAMLY-CPLX (EAL). EAL is one of a group of adenosylcobalamin-dependent enzymes which undergo suicide inactivation during catalysis and inactivation in the absence of substrate. Reactivation of EAL by EutA takes place in the presence of ATP, Mg2+ and free adenosylcobalamin, and EutA appears to be the sole enzyme responsible for this reaction . EutA: "ethanolamine utilization A"

## Biological Role

Repressed by hipB (protein.P23873).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76551|protein.P76551]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P23873|protein.P23873]] `RegulonDB` `S` - regulator=HipB; target=eutA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008079,ECOCYC:G7281,GeneID:946937`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2565481-2566884:-; feature_type=gene

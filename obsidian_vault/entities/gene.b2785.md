---
entity_id: "gene.b2785"
entity_type: "gene"
name: "rlmD"
source_database: "NCBI RefSeq"
source_id: "gene-b2785"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2785"
  - "rlmD"
---

# rlmD

`gene.b2785`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2785`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rlmD (gene.b2785) is a gene entity. It encodes rlmD (protein.P55135). Encoded protein function: FUNCTION: Catalyzes the formation of 5-methyl-uridine at position 1939 (m5U1939) in 23S rRNA. {ECO:0000255|HAMAP-Rule:MF_01010, ECO:0000269|PubMed:11779873, ECO:0000269|PubMed:12907714}. EcoCyc product frame: EG11247-MONOMER. EcoCyc synonyms: ygcA, rumA. Genomic coordinates: 2913699-2915000. EcoCyc protein note: RlmD is the methyltransferase responsible for methylation of 23S rRNA at the C5 position of the U1939 nucleotide . In vitro, the enzyme methylates full-length 23S rRNA as well as a 70 nt fragment containing nucleotides 1930-1969 . Crystal structures of apo-RlmD and a ternary complex have been solved at 1.95 and 2.15 Å resolution, suggesting active site residues and a mechanism for base selectivity . Since methyltransferase reactions do not involve a redox step, the presence of a [4Fe-4S] iron-sulfur cluster was unexpected. The iron-sulfur cluster was hypothesized to provide a mechanism for regulating RlmD activity under oxidative stress conditions . RumA: RNA uridine methyltransferase Review:

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P55135|protein.P55135]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009127,ECOCYC:EG11247,GeneID:947243`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2913699-2915000:-; feature_type=gene

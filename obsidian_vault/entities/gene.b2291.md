---
entity_id: "gene.b2291"
entity_type: "gene"
name: "yfbR"
source_database: "NCBI RefSeq"
source_id: "gene-b2291"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2291"
  - "yfbR"
---

# yfbR

`gene.b2291`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2291`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfbR (gene.b2291) is a gene entity. It encodes yfbR (protein.P76491). Encoded protein function: FUNCTION: Essential component of the deoxycytidine triphosphate (dCTP) pathway for de novo synthesis of thymidylate. Catalyzes the strictly specific dephosphorylation of 2'-deoxyribonucleoside 5'-monophosphates (dAMP, dGMP, dTMP, dUMP, dIMP and dCMP) and does not dephosphorylate 5'-ribonucleotides or ribonucleoside 3'-monophosphates. {ECO:0000269|PubMed:15489502, ECO:0000269|PubMed:17827303, ECO:0000269|PubMed:18353368}. EcoCyc product frame: G7185-MONOMER. Genomic coordinates: 2408862-2409461. EcoCyc protein note: YfbR is a 5'-deoxynucleotidase that functions as a dCMP phosphohydrolase in a salvage pathway for the synthesis of dUMP in a dcd deoA mutant . The protein contains a conserved HD domain . YfbR has phosphatase activity with deoxyribonucleoside 5'-monophosphates and does not hydrolyze ribonucleotides or deoxyribonucloside 3'-monophosphates. The enzyme requires divalent metal cations for activity . Nucleotidase activity of YfbR was discovered in a high-throughput screen of purified proteins . Crystal structures of YfbR have been solved; based on an analysis of crystal packing and size-exclusion chromatography, it was suggested that the biological unit is a dimer...

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76491|protein.P76491]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007563,ECOCYC:G7185,GeneID:946771`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2408862-2409461:+; feature_type=gene

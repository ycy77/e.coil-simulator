---
entity_id: "protein.P55135"
entity_type: "protein"
name: "rlmD"
source_database: "UniProt"
source_id: "P55135"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rlmD rumA ygcA b2785 JW2756"
---

# rlmD

`protein.P55135`

## Static

- Type: `protein`
- Source: `UniProt:P55135`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of 5-methyl-uridine at position 1939 (m5U1939) in 23S rRNA. {ECO:0000255|HAMAP-Rule:MF_01010, ECO:0000269|PubMed:11779873, ECO:0000269|PubMed:12907714}. RlmD is the methyltransferase responsible for methylation of 23S rRNA at the C5 position of the U1939 nucleotide . In vitro, the enzyme methylates full-length 23S rRNA as well as a 70 nt fragment containing nucleotides 1930-1969 . Crystal structures of apo-RlmD and a ternary complex have been solved at 1.95 and 2.15 Å resolution, suggesting active site residues and a mechanism for base selectivity . Since methyltransferase reactions do not involve a redox step, the presence of a [4Fe-4S] iron-sulfur cluster was unexpected. The iron-sulfur cluster was hypothesized to provide a mechanism for regulating RlmD activity under oxidative stress conditions . RumA: RNA uridine methyltransferase Review:

## Biological Role

Catalyzes RXN-11601 (reaction.ecocyc.RXN-11601). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

FUNCTION: Catalyzes the formation of 5-methyl-uridine at position 1939 (m5U1939) in 23S rRNA. {ECO:0000255|HAMAP-Rule:MF_01010, ECO:0000269|PubMed:11779873, ECO:0000269|PubMed:12907714}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11601|reaction.ecocyc.RXN-11601]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2785|gene.b2785]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P55135`
- `KEGG:ecj:JW2756;eco:b2785;ecoc:C3026_15315;`
- `GeneID:947243;`
- `GO:GO:0003723; GO:0005506; GO:0051539; GO:0070041; GO:0070475`
- `EC:2.1.1.190`

## Notes

23S rRNA (uracil(1939)-C(5))-methyltransferase RlmD (EC 2.1.1.190) (23S rRNA(m5U1939)-methyltransferase)

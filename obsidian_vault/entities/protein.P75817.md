---
entity_id: "protein.P75817"
entity_type: "protein"
name: "rlmC"
source_database: "UniProt"
source_id: "P75817"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rlmC rumB ybjF b0859 JW0843"
---

# rlmC

`protein.P75817`

## Static

- Type: `protein`
- Source: `UniProt:P75817`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of 5-methyl-uridine at position 747 (m5U747) in 23S rRNA. {ECO:0000255|HAMAP-Rule:MF_01012, ECO:0000269|PubMed:12907714}. RlmC is the methyltransferase responsible for methylation of 23S rRNA at the C5 position of the U747 nucleotide . An rlmC mutant shows a specific defect in methylation of position U747 in 23S rRNA . RumB: RNA uridine methyltransferase

## Biological Role

Catalyzes RXN-11600 (reaction.ecocyc.RXN-11600). Bound by an iron-sulfur cluster (molecule.ecocyc.FeS-Centers).

## Annotation

FUNCTION: Catalyzes the formation of 5-methyl-uridine at position 747 (m5U747) in 23S rRNA. {ECO:0000255|HAMAP-Rule:MF_01012, ECO:0000269|PubMed:12907714}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11600|reaction.ecocyc.RXN-11600]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.FeS-Centers|molecule.ecocyc.FeS-Centers]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0859|gene.b0859]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75817`
- `KEGG:ecj:JW0843;eco:b0859;ecoc:C3026_05355;`
- `GeneID:947260;`
- `GO:GO:0005506; GO:0016436; GO:0051539; GO:0070041; GO:0070475`
- `EC:2.1.1.189`

## Notes

23S rRNA (uracil(747)-C(5))-methyltransferase RlmC (EC 2.1.1.189) (23S rRNA(m5U747)-methyltransferase)

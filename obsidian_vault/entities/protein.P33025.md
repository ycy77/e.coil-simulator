---
entity_id: "protein.P33025"
entity_type: "protein"
name: "psuG"
source_database: "UniProt"
source_id: "P33025"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "psuG pscG yeiN b2165 JW2152"
---

# psuG

`protein.P33025`

## Static

- Type: `protein`
- Source: `UniProt:P33025`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible cleavage of pseudouridine 5'-phosphate (PsiMP) to ribose 5-phosphate and uracil. Functions biologically in the cleavage direction, as part of a pseudouridine degradation pathway. {ECO:0000255|HAMAP-Rule:MF_01876, ECO:0000269|PubMed:18591240, ECO:0000269|PubMed:23066817}.

## Biological Role

Component of pseudouridine-5'-phosphate glycosidase (complex.ecocyc.CPLX0-8233).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible cleavage of pseudouridine 5'-phosphate (PsiMP) to ribose 5-phosphate and uracil. Functions biologically in the cleavage direction, as part of a pseudouridine degradation pathway. {ECO:0000255|HAMAP-Rule:MF_01876, ECO:0000269|PubMed:18591240, ECO:0000269|PubMed:23066817}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8233|complex.ecocyc.CPLX0-8233]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b2165|gene.b2165]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33025`
- `KEGG:ecj:JW2152;eco:b2165;ecoc:C3026_12130;`
- `GeneID:946699;`
- `GO:GO:0004730; GO:0005737; GO:0016798; GO:0030145; GO:0032991; GO:0042802; GO:0046113`
- `EC:4.2.1.70`

## Notes

Pseudouridine-5'-phosphate glycosidase (PsiMP glycosidase) (EC 4.2.1.70)

---
entity_id: "protein.P0AE12"
entity_type: "protein"
name: "amn"
source_database: "UniProt"
source_id: "P0AE12"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "amn b1982 JW1963"
---

# amn

`protein.P0AE12`

## Static

- Type: `protein`
- Source: `UniProt:P0AE12`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of the N-glycosidic bond of AMP to form adenine and ribose 5-phosphate. Involved in regulation of AMP concentrations. {ECO:0000255|HAMAP-Rule:MF_01932, ECO:0000269|PubMed:7000783}.

## Biological Role

Catalyzes AMP phosphoribohydrolase (reaction.R00182). Component of AMP nucleosidase (complex.ecocyc.AMP-NUCLEOSID-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of the N-glycosidic bond of AMP to form adenine and ribose 5-phosphate. Involved in regulation of AMP concentrations. {ECO:0000255|HAMAP-Rule:MF_01932, ECO:0000269|PubMed:7000783}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00182|reaction.R00182]] `KEGG` `database` - via EC:3.2.2.4
- `is_component_of` --> [[complex.ecocyc.AMP-NUCLEOSID-CPLX|complex.ecocyc.AMP-NUCLEOSID-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b1982|gene.b1982]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE12`
- `KEGG:ecj:JW1963;eco:b1982;ecoc:C3026_11190;`
- `GeneID:75172115;75202785;946508;`
- `GO:GO:0005829; GO:0008714; GO:0009116; GO:0044209`
- `EC:3.2.2.4`

## Notes

AMP nucleosidase (EC 3.2.2.4)

---
entity_id: "protein.P17846"
entity_type: "protein"
name: "cysI"
source_database: "UniProt"
source_id: "P17846"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysI b2763 JW2733"
---

# cysI

`protein.P17846`

## Static

- Type: `protein`
- Source: `UniProt:P17846`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of the sulfite reductase complex that catalyzes the 6-electron reduction of sulfite to sulfide. This is one of several activities required for the biosynthesis of L-cysteine from sulfate. {ECO:0000255|HAMAP-Rule:MF_01540}. CysI is the β or hemoprotein subunit (SiRHP) of sulfite reductase (SiR). Sulfite reductase is involved in the assimilation of sulfate and catalyzes the transfer of six electrons from NADPH to sulfite to produce sulfide. CysI contains one siroheme and one [4Fe-4S] cluster per polypeptide; it transfers the electrons through the [4Fe-4S] cluster to the siroheme . The heme and iron-sulfur cluster are exchange-coupled . Experiments with the enzyme purified from E. coli B showed that the isolated, monomeric hemoprotein is able to catalyze sulfite reduction at a reduced rate using an artificial electron donor, but not NADPH . Crystal structures of CysI have been solved .

## Biological Role

Component of assimilatory sulfite reductase (NADPH) (complex.ecocyc.SULFITE-REDUCT-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Annotation

FUNCTION: Component of the sulfite reductase complex that catalyzes the 6-electron reduction of sulfite to sulfide. This is one of several activities required for the biosynthesis of L-cysteine from sulfate. {ECO:0000255|HAMAP-Rule:MF_01540}.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.SULFITE-REDUCT-CPLX|complex.ecocyc.SULFITE-REDUCT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2763|gene.b2763]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17846`
- `KEGG:ecj:JW2733;eco:b2763;ecoc:C3026_15185;`
- `GeneID:947231;`
- `GO:GO:0000103; GO:0004783; GO:0009337; GO:0019344; GO:0020037; GO:0046872; GO:0050661; GO:0051539; GO:0070814`
- `EC:1.8.1.2`

## Notes

Sulfite reductase [NADPH] hemoprotein beta-component (SiR-HP) (SiRHP) (EC 1.8.1.2)

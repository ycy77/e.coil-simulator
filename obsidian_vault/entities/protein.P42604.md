---
entity_id: "protein.P42604"
entity_type: "protein"
name: "uxaA"
source_database: "UniProt"
source_id: "P42604"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uxaA ygjW b3091 JW3062"
---

# uxaA

`protein.P42604`

## Static

- Type: `protein`
- Source: `UniProt:P42604`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dehydration of D-altronate. {ECO:0000269|PubMed:3038546}. Altronate dehydratase catalyzes the final reaction of the galacturonate branch of the hexuronate degradation pathway . Tagaturonate and fructuronate act as inducers ; production of the enzyme is under catabolite repression .

## Biological Role

Catalyzes D-altronate hydro-lyase (2-dehydro-3-deoxy-D-gluconate-forming) (reaction.R01540), ALTRODEHYDRAT-RXN (reaction.ecocyc.ALTRODEHYDRAT-RXN).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the dehydration of D-altronate. {ECO:0000269|PubMed:3038546}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01540|reaction.R01540]] `KEGG` `database` - via EC:4.2.1.7
- `catalyzes` --> [[reaction.ecocyc.ALTRODEHYDRAT-RXN|reaction.ecocyc.ALTRODEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3091|gene.b3091]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P42604`
- `KEGG:ecj:JW3062;eco:b3091;ecoc:C3026_16880;`
- `GeneID:75205102;947603;`
- `GO:GO:0008198; GO:0008789; GO:0019698`
- `EC:4.2.1.7`

## Notes

Altronate dehydratase (EC 4.2.1.7) (D-altronate hydro-lyase)

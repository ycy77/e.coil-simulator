---
entity_id: "protein.P39160"
entity_type: "protein"
name: "uxuB"
source_database: "UniProt"
source_id: "P39160"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uxuB b4323 JW4286"
---

# uxuB

`protein.P39160`

## Static

- Type: `protein`
- Source: `UniProt:P39160`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

D-mannonate oxidoreductase (EC 1.1.1.57) (Fructuronate reductase) D-mannonate oxidoreductase is an enzyme of the D-glucuronate degradation pathway, reducing D-fructuronate to D-mannonate. The reaction proceeds via a rapid-equilibrium random bi-bi + dead-end EBQ complex mechanism . Reports differ on whether or not the enzyme is able to use D-glucuronate as a substrate. Where it was measured, the reaction with D-glucuronate appears to proceed via a different mechanism . The enzyme is induced by both glucuronate and fructuronate ; the internal inducer is fructuronate .

## Biological Role

Catalyzes MANNONOXIDOREDUCT-RXN (reaction.ecocyc.MANNONOXIDOREDUCT-RXN).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

D-mannonate oxidoreductase (EC 1.1.1.57) (Fructuronate reductase)

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.MANNONOXIDOREDUCT-RXN|reaction.ecocyc.MANNONOXIDOREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4323|gene.b4323]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39160`
- `KEGG:ecj:JW4286;eco:b4323;ecoc:C3026_23355;`
- `GeneID:946795;`
- `GO:GO:0008866; GO:0019594; GO:0042840`
- `EC:1.1.1.57`

## Notes

D-mannonate oxidoreductase (EC 1.1.1.57) (Fructuronate reductase)

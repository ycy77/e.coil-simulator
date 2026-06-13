---
entity_id: "protein.P24215"
entity_type: "protein"
name: "uxuA"
source_database: "UniProt"
source_id: "P24215"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uxuA b4322 JW4285"
---

# uxuA

`protein.P24215`

## Static

- Type: `protein`
- Source: `UniProt:P24215`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dehydration of D-mannonate. {ECO:0000269|PubMed:3038546}. D-mannonate dehydratase catalyzes the final reaction of the glucuronate branch of the hexuronate degradation pathway . UxuA is monomeric in solution. Crystal structures of the enzyme alone and in complex with D-mannonate have been solved . The enzyme is inducible by glucuronate and fructuronate . Expression of uxuA may be repressed by OxyR . UxuA: "utilization of hexuronate A"

## Biological Role

Catalyzes MANNONDEHYDRAT-RXN (reaction.ecocyc.MANNONDEHYDRAT-RXN).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the dehydration of D-mannonate. {ECO:0000269|PubMed:3038546}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.MANNONDEHYDRAT-RXN|reaction.ecocyc.MANNONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4322|gene.b4322]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24215`
- `KEGG:ecj:JW4285;eco:b4322;ecoc:C3026_23350;`
- `GeneID:947082;`
- `GO:GO:0006974; GO:0008198; GO:0008927; GO:0030145; GO:0042840`
- `EC:4.2.1.8`

## Notes

Mannonate dehydratase (EC 4.2.1.8) (D-mannonate hydro-lyase)

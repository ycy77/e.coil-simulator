---
entity_id: "protein.P32141"
entity_type: "protein"
name: "yihT"
source_database: "UniProt"
source_id: "P32141"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yihT b3881 JW3852"
---

# yihT

`protein.P32141`

## Static

- Type: `protein`
- Source: `UniProt:P32141`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Cleaves 6-deoxy-6-sulfo-D-fructose 1-phosphate (SFP) to form dihydroxyacetone phosphate (DHAP) and 3-sulfolactaldehyde (SLA). {ECO:0000255|HAMAP-Rule:MF_01912, ECO:0000269|PubMed:24463506}. 6-Deoxy-6-sulfofructose-1-phosphate aldolase (YihT) catalyzes the cleavage of CPD-16502 to yield DIHYDROXY-ACETONE-PHOSPHATE and CPD-16503 , a part of the PWY-7446 pathway. Expression of YihT is induced by growth on sulfoquinovose and lactose . A yihT mutant is unable to grow on sulfoquinovose as the sole source of carbon .

## Biological Role

Catalyzes RXN-15298 (reaction.ecocyc.RXN-15298).

## Enriched Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Cleaves 6-deoxy-6-sulfo-D-fructose 1-phosphate (SFP) to form dihydroxyacetone phosphate (DHAP) and 3-sulfolactaldehyde (SLA). {ECO:0000255|HAMAP-Rule:MF_01912, ECO:0000269|PubMed:24463506}.

## Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-15298|reaction.ecocyc.RXN-15298]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3881|gene.b3881]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32141`
- `KEGG:ecj:JW3852;eco:b3881;ecoc:C3026_20980;`
- `GeneID:75204552;948373;`
- `GO:GO:0061595; GO:0061720; GO:1902777`
- `EC:4.1.2.57`

## Notes

Sulfofructosephosphate aldolase (SFP aldolase) (EC 4.1.2.57)

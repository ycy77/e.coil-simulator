---
entity_id: "protein.P0C0L2"
entity_type: "protein"
name: "osmC"
source_database: "UniProt"
source_id: "P0C0L2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "osmC b1482 JW1477"
---

# osmC

`protein.P0C0L2`

## Static

- Type: `protein`
- Source: `UniProt:P0C0L2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Preferentially metabolizes organic hydroperoxides over inorganic hydrogen peroxide. {ECO:0000269|PubMed:14627744}.

## Biological Role

Catalyzes lipoyl:hydroperoxide oxidoreductase (reaction.R12602), lipoyl:hydroperoxide oxidoreductase (reaction.R12603). Component of osmotically inducible peroxiredoxin OsmC (complex.ecocyc.CPLX0-8157).

## Annotation

FUNCTION: Preferentially metabolizes organic hydroperoxides over inorganic hydrogen peroxide. {ECO:0000269|PubMed:14627744}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R12602|reaction.R12602]] `KEGG` `database` - via EC:1.11.1.28
- `catalyzes` --> [[reaction.R12603|reaction.R12603]] `KEGG` `database` - via EC:1.11.1.28
- `is_component_of` --> [[complex.ecocyc.CPLX0-8157|complex.ecocyc.CPLX0-8157]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1482|gene.b1482]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C0L2`
- `KEGG:ecj:JW1477;eco:b1482;ecoc:C3026_08590;`
- `GeneID:75171568;75203185;946043;`
- `GO:GO:0004601; GO:0005829; GO:0006972; GO:0006979; GO:0033194; GO:0042803; GO:0051920`
- `EC:1.11.1.-`

## Notes

Peroxiredoxin OsmC (EC 1.11.1.-) (Osmotically-inducible protein C)

---
entity_id: "protein.P76460"
entity_type: "protein"
name: "atoE"
source_database: "UniProt"
source_id: "P76460"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "atoE b2223 JW2217"
---

# atoE

`protein.P76460`

## Static

- Type: `protein`
- Source: `UniProt:P76460`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: May be responsible for the uptake of short-chain fatty acids. AtoE is an inner membrane protein with ten predicted transmembrane domains. The C terminus is located in the periplasm .

## Biological Role

Catalyzes TRANS-RXN0-281 (reaction.ecocyc.TRANS-RXN0-281).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: May be responsible for the uptake of short-chain fatty acids.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-281|reaction.ecocyc.TRANS-RXN0-281]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2223|gene.b2223]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76460`
- `KEGG:ecj:JW2217;eco:b2223;ecoc:C3026_12425;`
- `GeneID:75172351;946721;`
- `GO:GO:0005886`

## Notes

Putative short-chain fatty acid transporter

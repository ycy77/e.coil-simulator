---
entity_id: "protein.P18392"
entity_type: "protein"
name: "rstB"
source_database: "UniProt"
source_id: "P18392"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rstB uspT b1609 JW1601"
---

# rstB

`protein.P18392`

## Static

- Type: `protein`
- Source: `UniProt:P18392`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system RstB/RstA. RstB functions as a membrane-associated protein kinase that phosphorylates RstA (Probable). {ECO:0000305|PubMed:15522865}. RstB is the sensor histidine kinase of the RstBA two-component signal transduction system . rstB and rstA - encoding its cognate response regulator - are transcribed together in an operon that is induced under low Mg2+ growth conditions through the PhoPQ two-component system This is the phosphorylated form of RSTB-MONOMER RstB - the sensor histidine kinase of the RstBA two-component signal transduction system.

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system RstB/RstA. RstB functions as a membrane-associated protein kinase that phosphorylates RstA (Probable). {ECO:0000305|PubMed:15522865}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1609|gene.b1609]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P18392`
- `KEGG:ecj:JW1601;eco:b1609;ecoc:C3026_09260;`
- `GeneID:948870;`
- `GO:GO:0000155; GO:0005524; GO:0005886; GO:0007165`
- `EC:2.7.13.3`

## Notes

Sensor protein RstB (EC 2.7.13.3)

---
entity_id: "protein.P76175"
entity_type: "protein"
name: "clcB"
source_database: "UniProt"
source_id: "P76175"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "clcB mriT ynfJ b1592 JW5263"
---

# clcB

`protein.P76175`

## Static

- Type: `protein`
- Source: `UniProt:P76175`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Probably acts as an electrical shunt for an outwardly-directed proton pump that is linked to amino acid decarboxylation, as part of the extreme acid resistance (XAR) response. {ECO:0000269|PubMed:12384697}. ClcB is a member of the ubiquitous ClC family of Cl- channels which promote the the selective flow of Cl- ions across cell membranes . E. coli K-12 contains two chloride channels, one of which - EG12331 "ClcA" - has been characterized as a chloride:H+ antiporter . Cells lacking both ClcB and ClcA do not survive acid shock conditions (pH2.5, 2 hrs at 37°C in minimal medium) and a biological role for them in the extreme acid resistance (XAR) response has been proposed .

## Biological Role

Catalyzes chloride:proton antiport (reaction.ecocyc.RXN0-2501). Transports hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Probably acts as an electrical shunt for an outwardly-directed proton pump that is linked to amino acid decarboxylation, as part of the extreme acid resistance (XAR) response. {ECO:0000269|PubMed:12384697}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2501|reaction.ecocyc.RXN0-2501]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1592|gene.b1592]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76175`
- `KEGG:ecj:JW5263;eco:b1592;ecoc:C3026_09170;`
- `GeneID:947179;`
- `GO:GO:0005247; GO:0005886; GO:0034707; GO:0071468; GO:1902476`

## Notes

Voltage-gated ClC-type chloride channel ClcB

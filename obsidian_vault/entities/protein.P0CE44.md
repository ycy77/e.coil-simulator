---
entity_id: "protein.P0CE44"
entity_type: "protein"
name: "uidB"
source_database: "UniProt"
source_id: "P0CE44"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uidB gusB uidP b1616 JW1608"
---

# uidB

`protein.P0CE44`

## Static

- Type: `protein`
- Source: `UniProt:P0CE44`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

Glucuronide carrier protein homolog UidB, also known as GusB, is a proton-dependent transporter specific for α- and β-glucuronides . UidB is a member of the GPH family of galactose-pentose-hexuronide transporters . The uidB gene probably forms part of a three gene operon with uidA and uidC, encoding β-glucuronidase and a membrane protein, respectively. Imported β-glucuronides are cleaved by UidA to yield glucuronate. Expression studies and transport assays of GusBC in E. coli CE1 strain indicate that GusBC mediates the secondary active transport of glucuronide, which is energized by the respiration-generated proton motive force. Separate expression of the GusB protein shows that it is essential for glucuronide transport and is located in the inner membrane, while GusC is an outer membrane protein that can enhance glucuronide uptake by an unknown mechanism. GusC does not transport glucuronide . Functional evaluation of the GusBC transport system was carried out with genes from a natural E. coli isolate. The GusBC system in E. coli K-12 is nonfunctional. This appears to be due to the presence of a proline rather than a leucine at position 100 in GusB .

## Biological Role

Catalyzes glucoronoside:proton symport (reaction.ecocyc.TRANS-RXN-98). Transports beta-D-Glucuronoside (molecule.C03033), hν (molecule.ecocyc.Light).

## Annotation

Glucuronide carrier protein homolog

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-98|reaction.ecocyc.TRANS-RXN-98]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C03033|molecule.C03033]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1616|gene.b1616]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0CE44`
- `KEGG:ecj:JW1608;eco:b1616;ecoc:C3026_09295;`
- `GeneID:947484;`
- `GO:GO:0005886; GO:0006814; GO:0008643; GO:0015293; GO:0055085`

## Notes

Glucuronide carrier protein homolog

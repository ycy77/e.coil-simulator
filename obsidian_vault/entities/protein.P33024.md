---
entity_id: "protein.P33024"
entity_type: "protein"
name: "psuT"
source_database: "UniProt"
source_id: "P33024"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "psuT pscT yeiM b2164 JW2151"
---

# psuT

`protein.P33024`

## Static

- Type: `protein`
- Source: `UniProt:P33024`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Could be involved in pseudouridine transport. PsuT is a member of the Concentrative Nucleoside Transport (CNT) family and is a predicted pseudouridine transport protein in E. coli K-12. psuT is located directly downstream from psuG and psuK which encode proteins involved in pseudouridine degradation. These proteins have been experimentally characterised in uropathogenic E. coli . Additionally pyrimidine auxotrophs of E. coli strains B and W are able to grow with pseudouridine as a sole pyrimidine source . The three proteins have not been characterised in E. coli K-12.

## Biological Role

Catalyzes pseudouridine:proton symport (reaction.ecocyc.TRANS-RXN0-538). Transports Pseudouridine (molecule.C02067), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Could be involved in pseudouridine transport.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-538|reaction.ecocyc.TRANS-RXN0-538]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C02067|molecule.C02067]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2164|gene.b2164]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33024`
- `KEGG:ecj:JW2151;eco:b2164;ecoc:C3026_12125;`
- `GeneID:75206417;946671;`
- `GO:GO:0005337; GO:0005886; GO:0015293; GO:1901642`

## Notes

Putative pseudouridine transporter

---
entity_id: "reaction.ecocyc.TDCEACT1-RXN"
entity_type: "reaction"
name: "TDCEACT1-RXN"
source_database: "EcoCyc"
source_id: "TDCEACT1-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TDCEACT1-RXN

`reaction.ecocyc.TDCEACT1-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TDCEACT1-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction activates 2-ketobutyrate formate-lyase/pyruvate formate-lyase 4 under anaerobic conditions. A single glycine residue in the formate-lyase is oxidized to the corresponding radical glycine. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + KETOBUTFORMLY-INACT-MONOMER + Reduced-flavodoxins -> CH33ADO + KETOBUTFORMLY-MONOMER + Oxidized-flavodoxins; direction=LEFT-TO-RIGHT. This reaction activates 2-ketobutyrate formate-lyase/pyruvate formate-lyase 4 under anaerobic conditions. A single glycine residue in the formate-lyase is oxidized to the corresponding radical glycine.

## Biological Role

Catalyzed by pflA (protein.P0A9N4). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: 5'-deoxyadenosine (molecule.ecocyc.CH33ADO).

## Annotation

This reaction activates 2-ketobutyrate formate-lyase/pyruvate formate-lyase 4 under anaerobic conditions. A single glycine residue in the formate-lyase is oxidized to the corresponding radical glycine.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A9N4|protein.P0A9N4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TDCEACT1-RXN`

## Notes

S-ADENOSYLMETHIONINE + KETOBUTFORMLY-INACT-MONOMER + Reduced-flavodoxins -> CH33ADO + KETOBUTFORMLY-MONOMER + Oxidized-flavodoxins; direction=LEFT-TO-RIGHT

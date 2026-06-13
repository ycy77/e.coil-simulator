---
entity_id: "reaction.ecocyc.1.97.1.4-A-RXN"
entity_type: "reaction"
name: "1.97.1.4-A-RXN"
source_database: "EcoCyc"
source_id: "1.97.1.4-A-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.97.1.4-A-RXN

`reaction.ecocyc.1.97.1.4-A-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.97.1.4-A-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction activates pyruvate formate-lyase under anaerobic conditions. A single glycine residue in pyruvate formate-lyase is oxidized to the corresponding radical glycine. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + PYRUVFORMLY-INACTIVE-CPLX + Reduced-flavodoxins -> PYRUVFORMLY-MONOMER + CH33ADO + MET + Oxidized-flavodoxins; direction=LEFT-TO-RIGHT. This reaction activates pyruvate formate-lyase under anaerobic conditions. A single glycine residue in pyruvate formate-lyase is oxidized to the corresponding radical glycine.

## Biological Role

Catalyzed by pflA (protein.P0A9N4). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: L-Methionine (molecule.C00073), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO).

## Annotation

This reaction activates pyruvate formate-lyase under anaerobic conditions. A single glycine residue in pyruvate formate-lyase is oxidized to the corresponding radical glycine.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `activates` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P0A9N4|protein.P0A9N4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.97.1.4-A-RXN`

## Notes

S-ADENOSYLMETHIONINE + PYRUVFORMLY-INACTIVE-CPLX + Reduced-flavodoxins -> PYRUVFORMLY-MONOMER + CH33ADO + MET + Oxidized-flavodoxins; direction=LEFT-TO-RIGHT

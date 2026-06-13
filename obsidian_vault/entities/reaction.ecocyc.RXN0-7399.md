---
entity_id: "reaction.ecocyc.RXN0-7399"
entity_type: "reaction"
name: "RXN0-7399"
source_database: "EcoCyc"
source_id: "RXN0-7399"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7399

`reaction.ecocyc.RXN0-7399`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7399`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + Menaquinones + HYDROGEN-MOLECULE -> PROTON + Menaquinols; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + Menaquinones + HYDROGEN-MOLECULE -> PROTON + Menaquinols; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by hydrogenase 2 (complex.ecocyc.CPLX0-8762). Substrates: H+ (molecule.C00080), Hydrogen (molecule.C00282), Menaquinone (molecule.C00828). Products: H+ (molecule.C00080), Menaquinol (molecule.C05819).

## Enriched Pathways

- `ecocyc.PWY0-1576` hydrogen to fumarate electron transfer (EcoCyc)
- `ecocyc.PWY0-1577` hydrogen to dimethyl sulfoxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1578` hydrogen to trimethylamine N-oxide electron transfer (EcoCyc)

## Annotation

PROTON + Menaquinones + HYDROGEN-MOLECULE -> PROTON + Menaquinols; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1576` hydrogen to fumarate electron transfer (EcoCyc)
- `ecocyc.PWY0-1577` hydrogen to dimethyl sulfoxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1578` hydrogen to trimethylamine N-oxide electron transfer (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8762|complex.ecocyc.CPLX0-8762]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00282|molecule.C00282]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00237|molecule.C00237]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-BROMOSUCCINIMIDE|molecule.ecocyc.N-BROMOSUCCINIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-7399`

## Notes

PROTON + Menaquinones + HYDROGEN-MOLECULE -> PROTON + Menaquinols; direction=LEFT-TO-RIGHT

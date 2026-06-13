---
entity_id: "reaction.ecocyc.RFFTRANS-RXN"
entity_type: "reaction"
name: "RFFTRANS-RXN"
source_database: "EcoCyc"
source_id: "RFFTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RFFTRANS-RXN

`reaction.ecocyc.RFFTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RFFTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction in the synthesis of TDP-4-acetamido-4,6-dideoxy-D-galactose, which is utilized in ECA biosynthesis. EcoCyc reaction equation: TDP-D-FUCOSAMINE + 2-KETOGLUTARATE -> DTDP-DEOH-DEOXY-GLUCOSE + GLT; direction=REVERSIBLE. This is the first reaction in the synthesis of TDP-4-acetamido-4,6-dideoxy-D-galactose, which is utilized in ECA biosynthesis.

## Biological Role

Catalyzed by dTDP-4-dehydro-6-deoxy-D-glucose transaminase (complex.ecocyc.CPLX0-7990). Substrates: 2-Oxoglutarate (molecule.C00026), dTDP-4-amino-4,6-dideoxy-D-galactose (molecule.C04346). Products: L-Glutamate (molecule.C00025), dTDP-4-oxo-6-deoxy-D-glucose (molecule.C11907).

## Enriched Pathways

- `ecocyc.PWY-7315` dTDP-N-acetylthomosamine biosynthesis (EcoCyc)

## Annotation

This is the first reaction in the synthesis of TDP-4-acetamido-4,6-dideoxy-D-galactose, which is utilized in ECA biosynthesis.

## Pathways

- `ecocyc.PWY-7315` dTDP-N-acetylthomosamine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7990|complex.ecocyc.CPLX0-7990]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C11907|molecule.C11907]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04346|molecule.C04346]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RFFTRANS-RXN`

## Notes

TDP-D-FUCOSAMINE + 2-KETOGLUTARATE -> DTDP-DEOH-DEOXY-GLUCOSE + GLT; direction=REVERSIBLE

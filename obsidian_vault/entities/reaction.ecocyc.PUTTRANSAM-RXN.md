---
entity_id: "reaction.ecocyc.PUTTRANSAM-RXN"
entity_type: "reaction"
name: "PUTTRANSAM-RXN"
source_database: "EcoCyc"
source_id: "PUTTRANSAM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PUTTRANSAM-RXN

`reaction.ecocyc.PUTTRANSAM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PUTTRANSAM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a specific reaction catalyzed by the general diamine transaminase reaction utilizing putrescine as the substrate. This is the first reaction in the degradation of putrescine. EcoCyc reaction equation: PUTRESCINE + 2-KETOGLUTARATE -> 4-AMINO-BUTYRALDEHYDE + GLT; direction=REVERSIBLE. This is a specific reaction catalyzed by the general diamine transaminase reaction utilizing putrescine as the substrate. This is the first reaction in the degradation of putrescine.

## Biological Role

Catalyzed by putrescine aminotransferase (complex.ecocyc.CPLX0-8159). Substrates: 2-Oxoglutarate (molecule.C00026), Putrescine (molecule.C00134). Products: L-Glutamate (molecule.C00025), 4-Aminobutyraldehyde (molecule.C00555).

## Enriched Pathways

- `ecocyc.PUTDEG-PWY` putrescine degradation I (EcoCyc)

## Annotation

This is a specific reaction catalyzed by the general diamine transaminase reaction utilizing putrescine as the substrate. This is the first reaction in the degradation of putrescine.

## Pathways

- `ecocyc.PUTDEG-PWY` putrescine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8159|complex.ecocyc.CPLX0-8159]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00555|molecule.C00555]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PUTTRANSAM-RXN`

## Notes

PUTRESCINE + 2-KETOGLUTARATE -> 4-AMINO-BUTYRALDEHYDE + GLT; direction=REVERSIBLE

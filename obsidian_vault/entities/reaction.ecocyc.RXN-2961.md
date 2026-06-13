---
entity_id: "reaction.ecocyc.RXN-2961"
entity_type: "reaction"
name: "RXN-2961"
source_database: "EcoCyc"
source_id: "RXN-2961"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-2961

`reaction.ecocyc.RXN-2961`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-2961`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-HYDROXYMETHYLGLUTATHIONE -> FORMALDEHYDE + GLUTATHIONE; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: S-HYDROXYMETHYLGLUTATHIONE -> FORMALDEHYDE + GLUTATHIONE; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Substrates: S-(Hydroxymethyl)glutathione (molecule.C14180). Products: Glutathione (molecule.C00051), Formaldehyde (molecule.C00067).

## Enriched Pathways

- `ecocyc.PWY-1801` formaldehyde oxidation II (glutathione-dependent) (EcoCyc)

## Annotation

S-HYDROXYMETHYLGLUTATHIONE -> FORMALDEHYDE + GLUTATHIONE; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-1801` formaldehyde oxidation II (glutathione-dependent) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00067|molecule.C00067]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C14180|molecule.C14180]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-2961`

## Notes

S-HYDROXYMETHYLGLUTATHIONE -> FORMALDEHYDE + GLUTATHIONE; direction=PHYSIOL-RIGHT-TO-LEFT

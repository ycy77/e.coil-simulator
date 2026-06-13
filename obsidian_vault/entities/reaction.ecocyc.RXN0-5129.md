---
entity_id: "reaction.ecocyc.RXN0-5129"
entity_type: "reaction"
name: "RXN0-5129"
source_database: "EcoCyc"
source_id: "RXN0-5129"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5129

`reaction.ecocyc.RXN0-5129`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5129`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Lipopolysaccharides + DTDP-RHAMNOSE -> CPD0-944 + TDP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Lipopolysaccharides + DTDP-RHAMNOSE -> CPD0-944 + TDP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaS (protein.P27126). Substrates: Lipopolysaccharide (molecule.C00338), dTDP-L-rhamnose (molecule.C03319). Products: dTDP (molecule.C00363), a rhamnosyl lipopolysaccharide (molecule.ecocyc.CPD0-944).

## Annotation

Lipopolysaccharides + DTDP-RHAMNOSE -> CPD0-944 + TDP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P27126|protein.P27126]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00363|molecule.C00363]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-944|molecule.ecocyc.CPD0-944]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00338|molecule.C00338]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03319|molecule.C03319]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5129`

## Notes

Lipopolysaccharides + DTDP-RHAMNOSE -> CPD0-944 + TDP; direction=PHYSIOL-LEFT-TO-RIGHT

---
entity_id: "reaction.ecocyc.METBALT-RXN"
entity_type: "reaction"
name: "METBALT-RXN"
source_database: "EcoCyc"
source_id: "METBALT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# METBALT-RXN

`reaction.ecocyc.METBALT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:METBALT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of threonine degradation. EcoCyc reaction equation: O-SUCCINYL-L-HOMOSERINE + WATER -> PROTON + 2-OXOBUTANOATE + SUC + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of threonine degradation.

## Biological Role

Catalyzed by O-succinylhomoserine(thiol)-lyase / O-succinylhomoserine lyase (complex.ecocyc.O-SUCCHOMOSERLYASE-CPLX). Substrates: H2O (molecule.C00001), O-Succinyl-L-homoserine (molecule.C01118). Products: Succinate (molecule.C00042), H+ (molecule.C00080), 2-Oxobutanoate (molecule.C00109), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

This reaction is part of threonine degradation.

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.O-SUCCHOMOSERLYASE-CPLX|complex.ecocyc.O-SUCCHOMOSERLYASE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00109|molecule.C00109]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01118|molecule.C01118]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:METBALT-RXN`

## Notes

O-SUCCINYL-L-HOMOSERINE + WATER -> PROTON + 2-OXOBUTANOATE + SUC + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT

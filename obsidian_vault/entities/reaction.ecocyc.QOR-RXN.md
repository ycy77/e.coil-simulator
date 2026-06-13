---
entity_id: "reaction.ecocyc.QOR-RXN"
entity_type: "reaction"
name: "QOR-RXN"
source_database: "EcoCyc"
source_id: "QOR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# QOR-RXN

`reaction.ecocyc.QOR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:QOR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is responsible for the reduction of a variety of simple quinones. E.C. number provided by SwissProt. EcoCyc reaction equation: NADPH + Quinones + PROTON -> NADP + Semiquinones; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is responsible for the reduction of a variety of simple quinones. E.C. number provided by SwissProt.

## Biological Role

Catalyzed by putative quinone oxidoreductase 1 (complex.ecocyc.QOR-CPLX). Substrates: NADPH (molecule.C00005), H+ (molecule.C00080), a quinone (molecule.ecocyc.Quinones). Products: NADP+ (molecule.C00006), a semiquinone (molecule.ecocyc.Semiquinones).

## Annotation

This reaction is responsible for the reduction of a variety of simple quinones. E.C. number provided by SwissProt.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.QOR-CPLX|complex.ecocyc.QOR-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Semiquinones|molecule.ecocyc.Semiquinones]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Quinones|molecule.ecocyc.Quinones]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:QOR-RXN`

## Notes

NADPH + Quinones + PROTON -> NADP + Semiquinones; direction=PHYSIOL-LEFT-TO-RIGHT

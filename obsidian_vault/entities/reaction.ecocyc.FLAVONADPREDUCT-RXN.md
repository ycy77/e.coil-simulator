---
entity_id: "reaction.ecocyc.FLAVONADPREDUCT-RXN"
entity_type: "reaction"
name: "FLAVONADPREDUCT-RXN"
source_database: "EcoCyc"
source_id: "FLAVONADPREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FLAVONADPREDUCT-RXN

`reaction.ecocyc.FLAVONADPREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FLAVONADPREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction functions as a member of redox chains and in E. coli participates in the activation of anaerobic ribonucleoside reductase, pyruvate-formate lyase and methionine synthase. EcoCyc reaction equation: Reduced-flavodoxins + NADP -> Oxidized-flavodoxins + NADPH + PROTON; direction=REVERSIBLE. This reaction functions as a member of redox chains and in E. coli participates in the activation of anaerobic ribonucleoside reductase, pyruvate-formate lyase and methionine synthase.

## Biological Role

Catalyzed by fpr (protein.P28861). Substrates: NADP+ (molecule.C00006). Products: NADPH (molecule.C00005), H+ (molecule.C00080).

## Annotation

This reaction functions as a member of redox chains and in E. coli participates in the activation of anaerobic ribonucleoside reductase, pyruvate-formate lyase and methionine synthase.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P28861|protein.P28861]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:FLAVONADPREDUCT-RXN`

## Notes

Reduced-flavodoxins + NADP -> Oxidized-flavodoxins + NADPH + PROTON; direction=REVERSIBLE

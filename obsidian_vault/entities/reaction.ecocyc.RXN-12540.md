---
entity_id: "reaction.ecocyc.RXN-12540"
entity_type: "reaction"
name: "Fenton reaction"
source_database: "EcoCyc"
source_id: "RXN-12540"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Fenton reaction

`reaction.ecocyc.RXN-12540`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12540`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction, which involves hydrogen peroxide and ferrous iron and produces a hydroxyl radical, is known as the Fenton reaction, and was suggested by Haber and Weiss in the 1930s.In the presence of physiological bicarbonate the product of the Fenton reaction is a CPD-27514 (see further ). EcoCyc reaction equation: HYDROGEN-PEROXIDE + FE+2 -> CPD-12377 + OH + FE+3; direction=LEFT-TO-RIGHT. This reaction, which involves hydrogen peroxide and ferrous iron and produces a hydroxyl radical, is known as the Fenton reaction, and was suggested by Haber and Weiss in the 1930s.In the presence of physiological bicarbonate the product of the Fenton reaction is a CPD-27514 (see further ).

## Biological Role

Substrates: Hydrogen peroxide (molecule.C00027), Fe2+ (molecule.C14818). Products: Fe3+ (molecule.C14819), hydroxyl radical (molecule.ecocyc.CPD-12377), OH- (molecule.ecocyc.OH).

## Annotation

This reaction, which involves hydrogen peroxide and ferrous iron and produces a hydroxyl radical, is known as the Fenton reaction, and was suggested by Haber and Weiss in the 1930s.In the presence of physiological bicarbonate the product of the Fenton reaction is a CPD-27514 (see further ).

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C14819|molecule.C14819]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-12377|molecule.ecocyc.CPD-12377]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.OH|molecule.ecocyc.OH]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12540`

## Notes

HYDROGEN-PEROXIDE + FE+2 -> CPD-12377 + OH + FE+3; direction=LEFT-TO-RIGHT

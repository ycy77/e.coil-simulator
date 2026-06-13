---
entity_id: "reaction.ecocyc.ACNEULY-RXN"
entity_type: "reaction"
name: "ACNEULY-RXN"
source_database: "EcoCyc"
source_id: "ACNEULY-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACNEULY-RXN

`reaction.ecocyc.ACNEULY-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACNEULY-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction breaks down sialic acid into common metabolic intermediates. Sialic acid is a component of polysaccharide chains of glycoproteins and glycolipids. EcoCyc reaction equation: N-ACETYLNEURAMINATE -> N-acetyl-D-mannosamine + PYRUVATE; direction=. This reaction breaks down sialic acid into common metabolic intermediates. Sialic acid is a component of polysaccharide chains of glycoproteins and glycolipids.

## Biological Role

Substrates: N-Acetylneuraminate (molecule.C00270). Products: Pyruvate (molecule.C00022), N-Acetyl-D-mannosamine (molecule.C00645).

## Annotation

This reaction breaks down sialic acid into common metabolic intermediates. Sialic acid is a component of polysaccharide chains of glycoproteins and glycolipids.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00645|molecule.C00645]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00270|molecule.C00270]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ACNEULY-RXN`

## Notes

N-ACETYLNEURAMINATE -> N-acetyl-D-mannosamine + PYRUVATE; direction=

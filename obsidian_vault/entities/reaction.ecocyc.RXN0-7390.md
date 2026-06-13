---
entity_id: "reaction.ecocyc.RXN0-7390"
entity_type: "reaction"
name: "RXN0-7390"
source_database: "EcoCyc"
source_id: "RXN0-7390"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7390

`reaction.ecocyc.RXN0-7390`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7390`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction breaks down sialic acid into common metabolic intermediates. Sialic acid is a component of polysaccharide chains of glycoproteins and glycolipids. EcoCyc reaction equation: CPD0-2701 -> N-acetyl-D-mannosamine + PYRUVATE; direction=REVERSIBLE. This reaction breaks down sialic acid into common metabolic intermediates. Sialic acid is a component of polysaccharide chains of glycoproteins and glycolipids.

## Biological Role

Catalyzed by N-acetylneuraminate lyase (complex.ecocyc.ACNEULY-CPLX). Substrates: aceneuramate (molecule.ecocyc.CPD0-2701). Products: Pyruvate (molecule.C00022), N-Acetyl-D-mannosamine (molecule.C00645).

## Enriched Pathways

- `ecocyc.PWY0-1324` N-acetylneuraminate and N-acetylmannosamine degradation I (EcoCyc)

## Annotation

This reaction breaks down sialic acid into common metabolic intermediates. Sialic acid is a component of polysaccharide chains of glycoproteins and glycolipids.

## Pathways

- `ecocyc.PWY0-1324` N-acetylneuraminate and N-acetylmannosamine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `catalyzes` <-- [[complex.ecocyc.ACNEULY-CPLX|complex.ecocyc.ACNEULY-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00645|molecule.C00645]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2701|molecule.ecocyc.CPD0-2701]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00168|molecule.C00168]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00184|molecule.C00184]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1144|molecule.ecocyc.CPD0-1144]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1551|molecule.ecocyc.CPD0-1551]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIETHYLPYROCARBONATE|molecule.ecocyc.DIETHYLPYROCARBONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-BROMOSUCCINIMIDE|molecule.ecocyc.N-BROMOSUCCINIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-7390`

## Notes

CPD0-2701 -> N-acetyl-D-mannosamine + PYRUVATE; direction=REVERSIBLE

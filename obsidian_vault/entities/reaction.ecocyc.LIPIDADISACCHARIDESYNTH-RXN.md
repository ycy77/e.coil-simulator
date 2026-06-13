---
entity_id: "reaction.ecocyc.LIPIDADISACCHARIDESYNTH-RXN"
entity_type: "reaction"
name: "LIPIDADISACCHARIDESYNTH-RXN"
source_database: "EcoCyc"
source_id: "LIPIDADISACCHARIDESYNTH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# LIPIDADISACCHARIDESYNTH-RXN

`reaction.ecocyc.LIPIDADISACCHARIDESYNTH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LIPIDADISACCHARIDESYNTH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction produces lipid A disaccharide, a precursor to lipid A. EcoCyc reaction equation: BISOHMYR-GLUCOSAMINYL-1P + OH-MYRISTOYL -> PROTON + BISOHMYR-GLC + UDP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction produces lipid A disaccharide, a precursor to lipid A.

## Biological Role

Catalyzed by lipid A disaccharide synthase (complex.ecocyc.CPLX0-7415). Substrates: UDP-2,3-bis(3-hydroxytetradecanoyl)glucosamine (molecule.C04652), Lipid X (molecule.C04824). Products: UDP (molecule.C00015), H+ (molecule.C00080), Lipid A disaccharide (molecule.C04932).

## Enriched Pathways

- `ecocyc.NAGLIPASYN-PWY` lipid IVA biosynthesis (E. coli) (EcoCyc)

## Annotation

This reaction produces lipid A disaccharide, a precursor to lipid A.

## Pathways

- `ecocyc.NAGLIPASYN-PWY` lipid IVA biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7415|complex.ecocyc.CPLX0-7415]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04932|molecule.C04932]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04652|molecule.C04652]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04824|molecule.C04824]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:LIPIDADISACCHARIDESYNTH-RXN`

## Notes

BISOHMYR-GLUCOSAMINYL-1P + OH-MYRISTOYL -> PROTON + BISOHMYR-GLC + UDP; direction=PHYSIOL-LEFT-TO-RIGHT

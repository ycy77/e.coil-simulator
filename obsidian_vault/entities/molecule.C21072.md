---
entity_id: "molecule.C21072"
entity_type: "small_molecule"
name: "Palmitoleoyl-CoA"
source_database: "KEGG"
source_id: "C21072"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Palmitoleoyl-CoA"
  - "(9Z)-Hexadec-9-enoyl-CoA"
  - "(9Z)-Hexadecenoyl-CoA"
  - "9Z-Hexadecenoyl-CoA"
---

# Palmitoleoyl-CoA

`molecule.C21072`

## Static

- Type: `small_molecule`
- Source: `KEGG:C21072`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Palmitoleoyl-CoA; (9Z)-Hexadec-9-enoyl-CoA; (9Z)-Hexadecenoyl-CoA; 9Z-Hexadecenoyl-CoA Like other fatty acids, CPD-9245 is rarely found in its free form. It is usually found as either Palmitoleoyl-ACPs "palmotoleoyl-[acp]", CPD-10269, or Palmitoleoyl-lipid "incorporated into a lipid".

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Annotation

KEGG compound: Palmitoleoyl-CoA; (9Z)-Hexadec-9-enoyl-CoA; (9Z)-Hexadecenoyl-CoA; 9Z-Hexadecenoyl-CoA

## Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.RXN0-7248|reaction.ecocyc.RXN0-7248]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17008|reaction.ecocyc.RXN-17008]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17009|reaction.ecocyc.RXN-17009]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17019|reaction.ecocyc.RXN-17019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17787|reaction.ecocyc.RXN-17787]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17788|reaction.ecocyc.RXN-17788]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C21072`

## Notes

Included because it appears in at least one E. coli KEGG pathway.

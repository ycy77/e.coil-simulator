---
entity_id: "molecule.C00083"
entity_type: "small_molecule"
name: "Malonyl-CoA"
source_database: "KEGG"
source_id: "C00083"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Malonyl-CoA"
  - "Malonyl coenzyme A"
---

# Malonyl-CoA

`molecule.C00083`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00083`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Malonyl-CoA; Malonyl coenzyme A

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Annotation

KEGG compound: Malonyl-CoA; Malonyl coenzyme A

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R00742|reaction.R00742]] `KEGG` `database` - C00002 + C00024 + C00288 <=> C00008 + C00009 + C00083
- `is_product_of` --> [[reaction.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-RXN|reaction.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5055|reaction.ecocyc.RXN0-5055]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.MALONYL-COA-ACP-TRANSACYL-RXN|reaction.ecocyc.MALONYL-COA-ACP-TRANSACYL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00083`

## Notes

Included because it appears in at least one E. coli KEGG pathway.

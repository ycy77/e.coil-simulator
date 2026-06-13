---
entity_id: "molecule.C00510"
entity_type: "small_molecule"
name: "Oleoyl-CoA"
source_database: "KEGG"
source_id: "C00510"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Oleoyl-CoA"
  - "(9Z)-Octadecenoyl-CoA"
---

# Oleoyl-CoA

`molecule.C00510`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00510`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Oleoyl-CoA; (9Z)-Octadecenoyl-CoA OLEATE-CPD Oleate (oleic acid) is the first unsaturated fatty acid that is generated from the saturated fatty acids produced by the fatty acid synthase. It's name is derived from the olive tree, since it makes up 55-80% of olive oil. Oleate synthesis occurs with membrane-bound systems. The desaturase enzymes that produce oleate have been isolated from fungi, yeast, and mammalian liver and found to be specific for STEAROYL-COA. In plants, on the other hand, oleate is produced via Stearoyl-ACPs, an acyl-carrier-protein bound intermediate . OLEATE-CPD Oleate has also been reported from a few bacteria, including the obligate anaerobic bacterium TAX-1520 and the saprophytic bacterium TAX-1377. Bacterial biosynthesis of OLEATE-CPD does not require oxygen and involves elongation of CPD-17289 . Like other fatty acids, OLEATE-CPD is rarely found in its free form. It is usually found as either Oleoyl-ACPs oleoyl-[acp], OLEOYL-COA, or Oleoyl-lipid "incorporated into a lipid".

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Annotation

KEGG compound: Oleoyl-CoA; (9Z)-Octadecenoyl-CoA

## Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-9644|reaction.ecocyc.RXN-9644]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7239|reaction.ecocyc.RXN0-7239]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17775|reaction.ecocyc.RXN-17775]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00510`

## Notes

Included because it appears in at least one E. coli KEGG pathway.

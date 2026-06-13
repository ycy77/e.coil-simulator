---
entity_id: "molecule.C00256"
entity_type: "small_molecule"
name: "(R)-Lactate"
source_database: "KEGG"
source_id: "C00256"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(R)-Lactate"
  - "D-Lactate"
  - "D-Lactic acid"
  - "D-2-Hydroxypropanoic acid"
  - "D-2-Hydroxypropionic acid"
---

# (R)-Lactate

`molecule.C00256`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00256`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (R)-Lactate; D-Lactate; D-Lactic acid; D-2-Hydroxypropanoic acid; D-2-Hydroxypropionic acid EcoCyc common name: (R)-lactic acid. Lactic acid has a pK of 3.86 and exists at a Lactate:CPD-24845 ratio of 3000:1 at physiological pH . To see the metabolism of lactic acid, see D-LACTATE and L-LACTATE. Lactate, or 2-hydroxypropanoate, was discovered in 1780 by the Swedish chemist Scheele, who isolated it from sour milk. It is the simplest hydroxycarboxylic acid and exists as 2 stereoisomers. Lactate has a pK of 3.86 and exists at a lactate ion:CPD-24845 ratio of 3000:1 at physiological pH .

## Biological Role

Consumed as substrate in 8 reaction(s). Produced in 9 reaction(s).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)

## Annotation

KEGG compound: (R)-Lactate; D-Lactate; D-Lactic acid; D-2-Hydroxypropanoic acid; D-2-Hydroxypropionic acid

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)

## Outgoing Edges (18)

- `is_product_of` --> [[reaction.R01736|reaction.R01736]] `KEGG` `database` - C03451 + C00001 <=> C00051 + C00256
- `is_product_of` --> [[reaction.ecocyc.GLYOXII-RXN|reaction.ecocyc.GLYOXII-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17630|reaction.ecocyc.RXN-17630]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17632|reaction.ecocyc.RXN-17632]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17634|reaction.ecocyc.RXN-17634]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22604|reaction.ecocyc.RXN-22604]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-4641|reaction.ecocyc.RXN0-4641]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5261|reaction.ecocyc.RXN0-5261]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-515|reaction.ecocyc.TRANS-RXN0-515]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00704|reaction.R00704]] `KEGG` `database` - C00256 + C00003 <=> C00022 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R09796|reaction.R09796]] `KEGG` `database` - C00256 <=> C00546 + C00001
- `is_substrate_of` --> [[reaction.ecocyc.DLACTDEHYDROGFAD-RXN|reaction.ecocyc.DLACTDEHYDROGFAD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DLACTDEHYDROGNAD-RXN|reaction.ecocyc.DLACTDEHYDROGNAD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLYOXIII-RXN|reaction.ecocyc.GLYOXIII-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22603|reaction.ecocyc.RXN-22603]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22604|reaction.ecocyc.RXN-22604]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-515|reaction.ecocyc.TRANS-RXN0-515]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN0-7008|reaction.ecocyc.RXN0-7008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.Q46839|protein.Q46839]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00256`

## Notes

Included because it appears in at least one E. coli KEGG pathway.

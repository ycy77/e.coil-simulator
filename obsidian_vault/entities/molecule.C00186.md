---
entity_id: "molecule.C00186"
entity_type: "small_molecule"
name: "(S)-Lactate"
source_database: "KEGG"
source_id: "C00186"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(S)-Lactate"
  - "L-Lactate"
  - "L-Lactic acid"
---

# (S)-Lactate

`molecule.C00186`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00186`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (S)-Lactate; L-Lactate; L-Lactic acid Lactate, or 2-hydroxypropanoate, was discovered in 1780 by the Swedish chemist Scheele, who isolated it from sour milk. It is the simplest hydroxycarboxylic acid and exists as 2 stereoisomers, L-LACTATE and D-LACTATE. Lactate has a pK of 3.86 and exists at a lactate ion:lactic acid ratio of 3000:1 at physiological pH . L-LACTATE has more versatile applications in food, pharmaceutical, textile, and chemical industries than D-LACTATE. It is also an indispensable monomer for the synthesis of poly-Ll-lactic acid, a bio-degradable polymer. EcoCyc common name: (S)-lactic acid. Lactic acid has a pK of 3.86 and exists at a Lactate:CPD-24845 ratio of 3000:1 at physiological pH . To see the metabolism of lactic acid, see D-LACTATE and L-LACTATE.

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)

## Annotation

KEGG compound: (S)-Lactate; L-Lactate; L-Lactic acid

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)

## Outgoing Edges (14)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7689|complex.ecocyc.CPLX0-7689]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.LACTALDDEHYDROG-RXN|reaction.ecocyc.LACTALDDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16819|reaction.ecocyc.RXN-16819]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22603|reaction.ecocyc.RXN-22603]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22605|reaction.ecocyc.RXN-22605]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5269|reaction.ecocyc.RXN0-5269]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-104|reaction.ecocyc.TRANS-RXN-104]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00196|reaction.R00196]] `KEGG` `database` - C00186 + 2 C00125 <=> C00022 + 2 C00126 + 2 C00080
- `is_substrate_of` --> [[reaction.ecocyc.L-LACTDEHYDROGFMN-RXN|reaction.ecocyc.L-LACTDEHYDROGFMN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22605|reaction.ecocyc.RXN-22605]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-25375|reaction.ecocyc.RXN-25375]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5372|reaction.ecocyc.RXN0-5372]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-104|reaction.ecocyc.TRANS-RXN-104]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN0-7008|reaction.ecocyc.RXN0-7008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.Q46839|protein.Q46839]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00186`

## Notes

Included because it appears in at least one E. coli KEGG pathway.

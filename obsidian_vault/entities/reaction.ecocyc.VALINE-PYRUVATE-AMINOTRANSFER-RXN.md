---
entity_id: "reaction.ecocyc.VALINE-PYRUVATE-AMINOTRANSFER-RXN"
entity_type: "reaction"
name: "VALINE-PYRUVATE-AMINOTRANSFER-RXN"
source_database: "EcoCyc"
source_id: "VALINE-PYRUVATE-AMINOTRANSFER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# VALINE-PYRUVATE-AMINOTRANSFER-RXN

`reaction.ecocyc.VALINE-PYRUVATE-AMINOTRANSFER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:VALINE-PYRUVATE-AMINOTRANSFER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The reaction is a reversible transamination between L-alanine and valine. When coupled with the branched-chainaminotransfer reaction, which converts 2-ketoisovalerate and glutamate to 2-ketoglutarate and valine, the overall reaction becomes conversion of pyruvate to L-alanine with glutamate as amino donor. EcoCyc reaction equation: PYRUVATE + VAL -> L-ALPHA-ALANINE + 2-KETO-ISOVALERATE; direction=REVERSIBLE. The reaction is a reversible transamination between L-alanine and valine. When coupled with the branched-chainaminotransfer reaction, which converts 2-ketoisovalerate and glutamate to 2-ketoglutarate and valine, the overall reaction becomes conversion of pyruvate to L-alanine with glutamate as amino donor.

## Biological Role

Catalyzed by avtA (protein.P09053). Substrates: Pyruvate (molecule.C00022), L-Valine (molecule.C00183). Products: L-Alanine (molecule.C00041), 3-Methyl-2-oxobutanoic acid (molecule.C00141).

## Enriched Pathways

- `ecocyc.ALANINE-VALINESYN-PWY` L-alanine biosynthesis I (EcoCyc)

## Annotation

The reaction is a reversible transamination between L-alanine and valine. When coupled with the branched-chainaminotransfer reaction, which converts 2-ketoisovalerate and glutamate to 2-ketoglutarate and valine, the overall reaction becomes conversion of pyruvate to L-alanine with glutamate as amino donor.

## Pathways

- `ecocyc.ALANINE-VALINESYN-PWY` L-alanine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P09053|protein.P09053]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00141|molecule.C00141]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CHLORALAN-CPD|molecule.ecocyc.CHLORALAN-CPD]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:VALINE-PYRUVATE-AMINOTRANSFER-RXN`

## Notes

PYRUVATE + VAL -> L-ALPHA-ALANINE + 2-KETO-ISOVALERATE; direction=REVERSIBLE

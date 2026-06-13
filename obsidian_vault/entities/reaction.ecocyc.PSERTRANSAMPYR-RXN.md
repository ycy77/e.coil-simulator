---
entity_id: "reaction.ecocyc.PSERTRANSAMPYR-RXN"
entity_type: "reaction"
name: "PSERTRANSAMPYR-RXN"
source_database: "EcoCyc"
source_id: "PSERTRANSAMPYR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PSERTRANSAMPYR-RXN

`reaction.ecocyc.PSERTRANSAMPYR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PSERTRANSAMPYR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This aminotransferase reaction is a part of the pyridoxine biosynthesis pathway. EcoCyc reaction equation: 4-PHOSPHONOOXY-THREONINE + 2-KETOGLUTARATE -> 3OH-4P-OH-ALPHA-KETOBUTYRATE + GLT; direction=REVERSIBLE. This aminotransferase reaction is a part of the pyridoxine biosynthesis pathway.

## Biological Role

Catalyzed by phosphoserine/phosphohydroxythreonine aminotransferase (complex.ecocyc.PSERTRANSAM-CPLX). Substrates: 2-Oxoglutarate (molecule.C00026), O-Phospho-4-hydroxy-L-threonine (molecule.C06055). Products: L-Glutamate (molecule.C00025), 2-Oxo-3-hydroxy-4-phosphobutanoate (molecule.C06054).

## Enriched Pathways

- `ecocyc.PYRIDOXSYN-PWY` pyridoxal 5'-phosphate biosynthesis I (EcoCyc)

## Annotation

This aminotransferase reaction is a part of the pyridoxine biosynthesis pathway.

## Pathways

- `ecocyc.PYRIDOXSYN-PWY` pyridoxal 5'-phosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.PSERTRANSAM-CPLX|complex.ecocyc.PSERTRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06054|molecule.C06054]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06055|molecule.C06055]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PSERTRANSAMPYR-RXN`

## Notes

4-PHOSPHONOOXY-THREONINE + 2-KETOGLUTARATE -> 3OH-4P-OH-ALPHA-KETOBUTYRATE + GLT; direction=REVERSIBLE

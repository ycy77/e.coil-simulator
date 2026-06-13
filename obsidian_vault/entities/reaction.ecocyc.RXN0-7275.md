---
entity_id: "reaction.ecocyc.RXN0-7275"
entity_type: "reaction"
name: "RXN0-7275"
source_database: "EcoCyc"
source_id: "RXN0-7275"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7275

`reaction.ecocyc.RXN0-7275`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7275`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

1iNisup6sup-ethenoadenine-in-DNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE + WATER -> DNA-Adenines + CPD-8887 + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 1iNisup6sup-ethenoadenine-in-DNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE + WATER -> DNA-Adenines + CPD-8887 + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkB (protein.P05050). Substrates: H2O (molecule.C00001), Oxygen (molecule.C00007), 2-Oxoglutarate (molecule.C00026), 1,N6-ethenoadenine in DNA (molecule.ecocyc.1iNisup6sup-ethenoadenine-in-DNA). Products: CO2 (molecule.C00011), Succinate (molecule.C00042), glyoxal (molecule.ecocyc.CPD-8887), an adenine in DNA (molecule.ecocyc.DNA-Adenines).

## Annotation

1iNisup6sup-ethenoadenine-in-DNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE + WATER -> DNA-Adenines + CPD-8887 + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P05050|protein.P05050]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-8887|molecule.ecocyc.CPD-8887]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.DNA-Adenines|molecule.ecocyc.DNA-Adenines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.1iNisup6sup-ethenoadenine-in-DNA|molecule.ecocyc.1iNisup6sup-ethenoadenine-in-DNA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7275`

## Notes

1iNisup6sup-ethenoadenine-in-DNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE + WATER -> DNA-Adenines + CPD-8887 + SUC + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

---
entity_id: "reaction.ecocyc.HEMN-RXN"
entity_type: "reaction"
name: "HEMN-RXN"
source_database: "EcoCyc"
source_id: "HEMN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HEMN-RXN

`reaction.ecocyc.HEMN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HEMN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this reaction protoporphyrinogen is synthesized under anaerobic conditions. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + COPROPORPHYRINOGEN_III -> PROTOPORPHYRINOGEN + CARBON-DIOXIDE + MET + CH33ADO; direction=PHYSIOL-LEFT-TO-RIGHT. In this reaction protoporphyrinogen is synthesized under anaerobic conditions.

## Biological Role

Catalyzed by hemN (protein.P32131). Substrates: S-Adenosyl-L-methionine (molecule.C00019), Coproporphyrinogen III (molecule.C03263). Products: CO2 (molecule.C00011), L-Methionine (molecule.C00073), Protoporphyrinogen IX (molecule.C01079), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO).

## Enriched Pathways

- `ecocyc.HEMESYN2-PWY` heme b biosynthesis II (oxygen-independent) (EcoCyc)

## Annotation

In this reaction protoporphyrinogen is synthesized under anaerobic conditions.

## Pathways

- `ecocyc.HEMESYN2-PWY` heme b biosynthesis II (oxygen-independent) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P32131|protein.P32131]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01079|molecule.C01079]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03263|molecule.C03263]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:HEMN-RXN`

## Notes

S-ADENOSYLMETHIONINE + COPROPORPHYRINOGEN_III -> PROTOPORPHYRINOGEN + CARBON-DIOXIDE + MET + CH33ADO; direction=PHYSIOL-LEFT-TO-RIGHT

---
entity_id: "reaction.ecocyc.CARBOXYLATE-REDUCTASE-RXN"
entity_type: "reaction"
name: "CARBOXYLATE-REDUCTASE-RXN"
source_database: "EcoCyc"
source_id: "CARBOXYLATE-REDUCTASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CARBOXYLATE-REDUCTASE-RXN

`reaction.ecocyc.CARBOXYLATE-REDUCTASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CARBOXYLATE-REDUCTASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

Aldehydes + Acceptor + WATER -> Carboxylates + Donor-H2 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: Aldehydes + Acceptor + WATER -> Carboxylates + Donor-H2 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by aldehyde dehydrogenase (complex.ecocyc.CPLX0-7805). Substrates: H2O (molecule.C00001), Aldehyde (molecule.C00071). Products: H+ (molecule.C00080), a carboxylate (molecule.ecocyc.Carboxylates).

## Annotation

Aldehydes + Acceptor + WATER -> Carboxylates + Donor-H2 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7805|complex.ecocyc.CPLX0-7805]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Carboxylates|molecule.ecocyc.Carboxylates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00071|molecule.C00071]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CARBOXYLATE-REDUCTASE-RXN`

## Notes

Aldehydes + Acceptor + WATER -> Carboxylates + Donor-H2 + PROTON; direction=REVERSIBLE

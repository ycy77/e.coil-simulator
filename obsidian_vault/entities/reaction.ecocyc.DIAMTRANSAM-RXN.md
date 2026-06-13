---
entity_id: "reaction.ecocyc.DIAMTRANSAM-RXN"
entity_type: "reaction"
name: "DIAMTRANSAM-RXN"
source_database: "EcoCyc"
source_id: "DIAMTRANSAM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIAMTRANSAM-RXN

`reaction.ecocyc.DIAMTRANSAM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIAMTRANSAM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a general diamine transaminase reaction. EcoCyc reaction equation: Aliphatic-Alpha-Omega-Diamines + 2-KETOGLUTARATE -> Aliphatic-Omega-Amino-Aldehydes + GLT; direction=REVERSIBLE. This is a general diamine transaminase reaction.

## Biological Role

Catalyzed by putrescine aminotransferase (complex.ecocyc.CPLX0-8159). Substrates: 2-Oxoglutarate (molecule.C00026), an aliphatic α,ω-diamine (molecule.ecocyc.Aliphatic-Alpha-Omega-Diamines). Products: L-Glutamate (molecule.C00025), Aliphatic-Omega-Amino-Aldehydes (molecule.ecocyc.Aliphatic-Omega-Amino-Aldehydes).

## Annotation

This is a general diamine transaminase reaction.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8159|complex.ecocyc.CPLX0-8159]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Aliphatic-Omega-Amino-Aldehydes|molecule.ecocyc.Aliphatic-Omega-Amino-Aldehydes]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Aliphatic-Alpha-Omega-Diamines|molecule.ecocyc.Aliphatic-Alpha-Omega-Diamines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DIAMTRANSAM-RXN`

## Notes

Aliphatic-Alpha-Omega-Diamines + 2-KETOGLUTARATE -> Aliphatic-Omega-Amino-Aldehydes + GLT; direction=REVERSIBLE

---
entity_id: "reaction.ecocyc.O-SUCCHOMOSERLYASE-RXN"
entity_type: "reaction"
name: "O-SUCCHOMOSERLYASE-RXN"
source_database: "EcoCyc"
source_id: "O-SUCCHOMOSERLYASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# O-SUCCHOMOSERLYASE-RXN

`reaction.ecocyc.O-SUCCHOMOSERLYASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:O-SUCCHOMOSERLYASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second committed step in methionine synthesis. EcoCyc reaction equation: CYS + O-SUCCINYL-L-HOMOSERINE -> PROTON + SUC + L-CYSTATHIONINE; direction=REVERSIBLE. This is the second committed step in methionine synthesis.

## Biological Role

Catalyzed by O-succinylhomoserine(thiol)-lyase / O-succinylhomoserine lyase (complex.ecocyc.O-SUCCHOMOSERLYASE-CPLX). Substrates: L-Cysteine (molecule.C00097), O-Succinyl-L-homoserine (molecule.C01118). Products: Succinate (molecule.C00042), H+ (molecule.C00080), L-Cystathionine (molecule.C02291).

## Enriched Pathways

- `ecocyc.HOMOSER-METSYN-PWY` L-methionine biosynthesis I (EcoCyc)

## Annotation

This is the second committed step in methionine synthesis.

## Pathways

- `ecocyc.HOMOSER-METSYN-PWY` L-methionine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.O-SUCCHOMOSERLYASE-CPLX|complex.ecocyc.O-SUCCHOMOSERLYASE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02291|molecule.C02291]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01118|molecule.C01118]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:O-SUCCHOMOSERLYASE-RXN`

## Notes

CYS + O-SUCCINYL-L-HOMOSERINE -> PROTON + SUC + L-CYSTATHIONINE; direction=REVERSIBLE

---
entity_id: "reaction.ecocyc.RXN-9661"
entity_type: "reaction"
name: "trans dodec-2-enoyl-[acp] reductase"
source_database: "EcoCyc"
source_id: "RXN-9661"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Enoyl-ACP reductase"
  - "Enoyl acyl-carrier-protein reductase"
  - "NADPH 2-enoyl Co A reductase"
  - "Acyl-ACP dehydrogenase"
---

# trans dodec-2-enoyl-[acp] reductase

`reaction.ecocyc.RXN-9661`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9661`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Dodecanoyl-ACPs + NAD -> Dodec-2-enoyl-ACPs + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: Dodecanoyl-ACPs + NAD -> Dodec-2-enoyl-ACPs + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by enoyl-[acyl-carrier-protein] reductase (complex.ecocyc.CPLX0-8006). Substrates: NAD+ (molecule.C00003). Products: NADH (molecule.C00004), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Annotation

Dodecanoyl-ACPs + NAD -> Dodec-2-enoyl-ACPs + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8006|complex.ecocyc.CPLX0-8006]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9661`

## Notes

Dodecanoyl-ACPs + NAD -> Dodec-2-enoyl-ACPs + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

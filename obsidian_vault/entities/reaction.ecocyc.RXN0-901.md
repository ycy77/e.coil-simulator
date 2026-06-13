---
entity_id: "reaction.ecocyc.RXN0-901"
entity_type: "reaction"
name: "RXN0-901"
source_database: "EcoCyc"
source_id: "RXN0-901"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-901

`reaction.ecocyc.RXN0-901`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-901`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

XdhA-XdhB-XdhC is a putative heterotrimeric xanthine dehydrogenase . EcoCyc reaction equation: XANTHINE + NAD + WATER -> URATE + NADH + PROTON; direction=REVERSIBLE. XdhA-XdhB-XdhC is a putative heterotrimeric xanthine dehydrogenase .

## Biological Role

Catalyzed by putative xanthine dehydrogenase (complex.ecocyc.CPLX0-761). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), Xanthine (molecule.C00385). Products: NADH (molecule.C00004), H+ (molecule.C00080), Urate (molecule.C00366).

## Enriched Pathways

- `ecocyc.PWY-6608` guanosine nucleotides degradation III (EcoCyc)
- `ecocyc.SALVADEHYPOX-PWY` adenosine nucleotides degradation II (EcoCyc)

## Annotation

XdhA-XdhB-XdhC is a putative heterotrimeric xanthine dehydrogenase .

## Pathways

- `ecocyc.PWY-6608` guanosine nucleotides degradation III (EcoCyc)
- `ecocyc.SALVADEHYPOX-PWY` adenosine nucleotides degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-761|complex.ecocyc.CPLX0-761]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00366|molecule.C00366]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00385|molecule.C00385]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-901`

## Notes

XANTHINE + NAD + WATER -> URATE + NADH + PROTON; direction=REVERSIBLE

---
entity_id: "reaction.ecocyc.RXN0-7168"
entity_type: "reaction"
name: "RXN0-7168"
source_database: "EcoCyc"
source_id: "RXN0-7168"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7168

`reaction.ecocyc.RXN0-7168`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7168`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 5-methoxycarbonylmethoxyU34-tRNA -> mcmo5U34m-tRNA + ADENOSYL-HOMO-CYS + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 5-methoxycarbonylmethoxyU34-tRNA -> mcmo5U34m-tRNA + ADENOSYL-HOMO-CYS + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tRNA (cytidine/uridine-2'-O)-ribose methyltransferase (complex.ecocyc.CPLX0-7421). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a 5-(methoxycarbonylmethoxy)uridine34 in tRNA (molecule.ecocyc.5-methoxycarbonylmethoxyU34-tRNA). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a 5-(methoxycarbonylmethoxy)-2'-O-methyluridine34 in tRNA (molecule.ecocyc.mcmo5U34m-tRNA).

## Enriched Pathways

- `ecocyc.PWY0-1554` 5-(methoxycarbonylmethoxy)uridine biosynthesis (EcoCyc)

## Annotation

S-ADENOSYLMETHIONINE + 5-methoxycarbonylmethoxyU34-tRNA -> mcmo5U34m-tRNA + ADENOSYL-HOMO-CYS + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1554` 5-(methoxycarbonylmethoxy)uridine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7421|complex.ecocyc.CPLX0-7421]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.mcmo5U34m-tRNA|molecule.ecocyc.mcmo5U34m-tRNA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.5-methoxycarbonylmethoxyU34-tRNA|molecule.ecocyc.5-methoxycarbonylmethoxyU34-tRNA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7168`

## Notes

S-ADENOSYLMETHIONINE + 5-methoxycarbonylmethoxyU34-tRNA -> mcmo5U34m-tRNA + ADENOSYL-HOMO-CYS + PROTON; direction=LEFT-TO-RIGHT

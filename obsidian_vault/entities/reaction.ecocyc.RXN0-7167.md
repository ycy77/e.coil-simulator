---
entity_id: "reaction.ecocyc.RXN0-7167"
entity_type: "reaction"
name: "RXN0-7167"
source_database: "EcoCyc"
source_id: "RXN0-7167"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7167

`reaction.ecocyc.RXN0-7167`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7167`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 5-oxyacetylU34-tRNA -> 5-methoxycarbonylmethoxyU34-tRNA + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 5-oxyacetylU34-tRNA -> 5-methoxycarbonylmethoxyU34-tRNA + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tRNA cmo5U34 methyltransferase (complex.ecocyc.CPLX0-11245). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a 5-(carboxymethoxy)uridine34 in tRNA (molecule.ecocyc.5-oxyacetylU34-tRNA). Products: S-Adenosyl-L-homocysteine (molecule.C00021), a 5-(methoxycarbonylmethoxy)uridine34 in tRNA (molecule.ecocyc.5-methoxycarbonylmethoxyU34-tRNA).

## Enriched Pathways

- `ecocyc.PWY0-1554` 5-(methoxycarbonylmethoxy)uridine biosynthesis (EcoCyc)

## Annotation

S-ADENOSYLMETHIONINE + 5-oxyacetylU34-tRNA -> 5-methoxycarbonylmethoxyU34-tRNA + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1554` 5-(methoxycarbonylmethoxy)uridine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-11245|complex.ecocyc.CPLX0-11245]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-methoxycarbonylmethoxyU34-tRNA|molecule.ecocyc.5-methoxycarbonylmethoxyU34-tRNA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.5-oxyacetylU34-tRNA|molecule.ecocyc.5-oxyacetylU34-tRNA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7167`

## Notes

S-ADENOSYLMETHIONINE + 5-oxyacetylU34-tRNA -> 5-methoxycarbonylmethoxyU34-tRNA + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT

---
entity_id: "reaction.ecocyc.RXN0-7067"
entity_type: "reaction"
name: "RXN0-7067"
source_database: "EcoCyc"
source_id: "RXN0-7067"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7067

`reaction.ecocyc.RXN0-7067`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7067`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-HYDROXYU34-TRNA + CPD-15403 -> 5-oxyacetylU34-tRNA + ADENOSYL-HOMO-CYS + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 5-HYDROXYU34-TRNA + CPD-15403 -> 5-oxyacetylU34-tRNA + ADENOSYL-HOMO-CYS + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tRNA U34 carboxymethyltransferase (complex.ecocyc.CPLX0-8190). Substrates: a 5-hydroxyuridine34 in tRNA (molecule.ecocyc.5-HYDROXYU34-TRNA), S-adenosyl-S-carboxymethyl-L-homocysteine (molecule.ecocyc.CPD-15403). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a 5-(carboxymethoxy)uridine34 in tRNA (molecule.ecocyc.5-oxyacetylU34-tRNA).

## Enriched Pathways

- `ecocyc.PWY0-1554` 5-(methoxycarbonylmethoxy)uridine biosynthesis (EcoCyc)

## Annotation

5-HYDROXYU34-TRNA + CPD-15403 -> 5-oxyacetylU34-tRNA + ADENOSYL-HOMO-CYS + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1554` 5-(methoxycarbonylmethoxy)uridine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8190|complex.ecocyc.CPLX0-8190]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-oxyacetylU34-tRNA|molecule.ecocyc.5-oxyacetylU34-tRNA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.5-HYDROXYU34-TRNA|molecule.ecocyc.5-HYDROXYU34-TRNA]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15403|molecule.ecocyc.CPD-15403]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7067`

## Notes

5-HYDROXYU34-TRNA + CPD-15403 -> 5-oxyacetylU34-tRNA + ADENOSYL-HOMO-CYS + PROTON; direction=LEFT-TO-RIGHT

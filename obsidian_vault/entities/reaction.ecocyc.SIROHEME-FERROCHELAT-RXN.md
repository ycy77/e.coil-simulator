---
entity_id: "reaction.ecocyc.SIROHEME-FERROCHELAT-RXN"
entity_type: "reaction"
name: "SIROHEME-FERROCHELAT-RXN"
source_database: "EcoCyc"
source_id: "SIROHEME-FERROCHELAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SIROHEME-FERROCHELAT-RXN

`reaction.ecocyc.SIROHEME-FERROCHELAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SIROHEME-FERROCHELAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The final reaction in siroheme biosynthesis. This enzyme catalyzes the third of three steps leading to the EcoCyc reaction equation: SIROHYDROCHLORIN + FE+2 -> PROTON + SIROHEME; direction=LEFT-TO-RIGHT. The final reaction in siroheme biosynthesis. This enzyme catalyzes the third of three steps leading to the

## Biological Role

Catalyzed by siroheme synthase (complex.ecocyc.SIROHEMESYN-CPLX). Substrates: Sirohydrochlorin (molecule.C05778), Fe2+ (molecule.C14818). Products: H+ (molecule.C00080), Siroheme (molecule.C00748).

## Enriched Pathways

- `ecocyc.PWY-5194` siroheme biosynthesis (EcoCyc)

## Annotation

The final reaction in siroheme biosynthesis. This enzyme catalyzes the third of three steps leading to the

## Pathways

- `ecocyc.PWY-5194` siroheme biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.SIROHEMESYN-CPLX|complex.ecocyc.SIROHEMESYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00748|molecule.C00748]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05778|molecule.C05778]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SIROHEME-FERROCHELAT-RXN`

## Notes

SIROHYDROCHLORIN + FE+2 -> PROTON + SIROHEME; direction=LEFT-TO-RIGHT

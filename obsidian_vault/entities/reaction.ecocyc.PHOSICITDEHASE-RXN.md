---
entity_id: "reaction.ecocyc.PHOSICITDEHASE-RXN"
entity_type: "reaction"
name: "PHOSICITDEHASE-RXN"
source_database: "EcoCyc"
source_id: "PHOSICITDEHASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PHOSICITDEHASE-RXN

`reaction.ecocyc.PHOSICITDEHASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHOSICITDEHASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

isocitrate-dehydrogenase + ATP -> ADP + Iso-Cit; direction=REVERSIBLE EcoCyc reaction equation: isocitrate-dehydrogenase + ATP -> ADP + Iso-Cit; direction=REVERSIBLE.

## Biological Role

Catalyzed by isocitrate dehydrogenase kinase / isocitrate dehydrogenase phosphatase (complex.ecocyc.CPLX0-230). Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Annotation

isocitrate-dehydrogenase + ATP -> ADP + Iso-Cit; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (16)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-230|complex.ecocyc.CPLX0-230]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00158|molecule.C00158]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00197|molecule.C00197]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00311|molecule.C00311]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.FRUCTOSE-6P|molecule.ecocyc.FRUCTOSE-6P]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PHOSICITDEHASE-RXN`

## Notes

isocitrate-dehydrogenase + ATP -> ADP + Iso-Cit; direction=REVERSIBLE

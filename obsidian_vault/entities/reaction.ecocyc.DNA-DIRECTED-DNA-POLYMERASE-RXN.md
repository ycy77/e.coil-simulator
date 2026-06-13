---
entity_id: "reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN"
entity_type: "reaction"
name: "DNA-DIRECTED-DNA-POLYMERASE-RXN"
source_database: "EcoCyc"
source_id: "DNA-DIRECTED-DNA-POLYMERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DNA-DIRECTED-DNA-POLYMERASE-RXN

`reaction.ecocyc.DNA-DIRECTED-DNA-POLYMERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DNA-DIRECTED-DNA-POLYMERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Deoxy-Ribonucleoside-Triphosphates + DNA-N -> PPI + DNA-N; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Deoxy-Ribonucleoside-Triphosphates + DNA-N -> PPI + DNA-N; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by DNA polymerase V (complex.ecocyc.CPLX0-3925), polA (protein.P00582), dnaE (protein.P10443), polB (protein.P21189), dinB (protein.Q47155). Substrates: a 2'-deoxyribonucleoside 5'-triphosphate (molecule.ecocyc.Deoxy-Ribonucleoside-Triphosphates). Products: Diphosphate (molecule.C00013).

## Annotation

Deoxy-Ribonucleoside-Triphosphates + DNA-N -> PPI + DNA-N; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3925|complex.ecocyc.CPLX0-3925]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P00582|protein.P00582]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P10443|protein.P10443]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P21189|protein.P21189]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q47155|protein.Q47155]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Deoxy-Ribonucleoside-Triphosphates|molecule.ecocyc.Deoxy-Ribonucleoside-Triphosphates]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-11426|molecule.ecocyc.CPD-11426]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DNA-DIRECTED-DNA-POLYMERASE-RXN`

## Notes

Deoxy-Ribonucleoside-Triphosphates + DNA-N -> PPI + DNA-N; direction=PHYSIOL-LEFT-TO-RIGHT

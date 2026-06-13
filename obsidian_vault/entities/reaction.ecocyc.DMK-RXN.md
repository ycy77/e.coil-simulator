---
entity_id: "reaction.ecocyc.DMK-RXN"
entity_type: "reaction"
name: "DMK-RXN"
source_database: "EcoCyc"
source_id: "DMK-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DMK-RXN

`reaction.ecocyc.DMK-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DMK-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the sixth reaction in menaquinone biosynthesis. Polyprenylpyrophosphate is a polymer of isoprene units. EcoCyc reaction equation: OCTAPRENYL-DIPHOSPHATE + DIHYDROXYNAPHTHOATE + PROTON -> CPD-12115 + PPI + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT. This is the sixth reaction in menaquinone biosynthesis. Polyprenylpyrophosphate is a polymer of isoprene units.

## Biological Role

Catalyzed by menA (protein.P32166). Substrates: H+ (molecule.C00080), 1,4-Dihydroxy-2-naphthoate (molecule.C03657), all-trans-Octaprenyl diphosphate (molecule.C04146). Products: CO2 (molecule.C00011), Diphosphate (molecule.C00013), demethylmenaquinol-8 (molecule.ecocyc.CPD-12115).

## Enriched Pathways

- `ecocyc.PWY-5852` demethylmenaquinol-8 biosynthesis I (EcoCyc)

## Annotation

This is the sixth reaction in menaquinone biosynthesis. Polyprenylpyrophosphate is a polymer of isoprene units.

## Pathways

- `ecocyc.PWY-5852` demethylmenaquinol-8 biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P32166|protein.P32166]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-12115|molecule.ecocyc.CPD-12115]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03657|molecule.C03657]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04146|molecule.C04146]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DMK-RXN`

## Notes

OCTAPRENYL-DIPHOSPHATE + DIHYDROXYNAPHTHOATE + PROTON -> CPD-12115 + PPI + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

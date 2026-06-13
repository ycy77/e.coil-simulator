---
entity_id: "reaction.ecocyc.GLYOHMETRANS-RXN"
entity_type: "reaction"
name: "GLYOHMETRANS-RXN"
source_database: "EcoCyc"
source_id: "GLYOHMETRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYOHMETRANS-RXN

`reaction.ecocyc.GLYOHMETRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYOHMETRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction converts serine to glycine, and is also a major source of one-carbon units for the cell. EcoCyc reaction equation: GLY + METHYLENE-THF-GLU-N + WATER -> SER + THF-GLU-N; direction=REVERSIBLE. This reaction converts serine to glycine, and is also a major source of one-carbon units for the cell.

## Biological Role

Catalyzed by serine hydroxymethyltransferase (complex.ecocyc.GLYOHMETRANS-CPLX). Substrates: H2O (molecule.C00001), Glycine (molecule.C00037), a 5,10-methylenetetrahydrofolate (molecule.ecocyc.METHYLENE-THF-GLU-N). Products: L-Serine (molecule.C00065), THF-polyglutamate (molecule.C03541).

## Enriched Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)
- `ecocyc.GLYSYN-PWY` glycine biosynthesis I (EcoCyc)
- `ecocyc.PWY-2161` folate polyglutamylation (EcoCyc)
- `ecocyc.PWY0-1608` glycine degradation (EcoCyc)

## Annotation

This reaction converts serine to glycine, and is also a major source of one-carbon units for the cell.

## Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)
- `ecocyc.GLYSYN-PWY` glycine biosynthesis I (EcoCyc)
- `ecocyc.PWY-2161` folate polyglutamylation (EcoCyc)
- `ecocyc.PWY0-1608` glycine degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.GLYOHMETRANS-CPLX|complex.ecocyc.GLYOHMETRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03541|molecule.C03541]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.METHYLENE-THF-GLU-N|molecule.ecocyc.METHYLENE-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CL-|molecule.ecocyc.CL-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.METHYLMETHANETHIOSULFONATE|molecule.ecocyc.METHYLMETHANETHIOSULFONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLYOHMETRANS-RXN`

## Notes

GLY + METHYLENE-THF-GLU-N + WATER -> SER + THF-GLU-N; direction=REVERSIBLE

---
entity_id: "reaction.ecocyc.DNA-LIGASE-NAD_-RXN"
entity_type: "reaction"
name: "DNA-LIGASE-NAD+-RXN"
source_database: "EcoCyc"
source_id: "DNA-LIGASE-NAD+-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "DNA JOINASE"
  - "DNA REPAIR ENZYME"
  - "POLYNUCLEOTIDE LIGASE (NAD(+))"
  - "POLYDEOXYRIBONUCLEOTIDE SYNTHASE (NAD(+))"
---

# DNA-LIGASE-NAD+-RXN

`reaction.ecocyc.DNA-LIGASE-NAD_-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DNA-LIGASE-NAD+-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CATALYSES THE FORMATION OF A PHOSPHODIESTER AT THE SITE OF A SINGLE- STRAND BREAK IN DUPLEX DNA. EcoCyc reaction equation: 3-Hydroxy-Terminated-DNAs + 5-Phospho-terminated-DNAs + NAD -> DNA-N + AMP + NICOTINAMIDE_NUCLEOTIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. CATALYSES THE FORMATION OF A PHOSPHODIESTER AT THE SITE OF A SINGLE- STRAND BREAK IN DUPLEX DNA.

## Biological Role

Catalyzed by ligA (protein.P15042), ligB (protein.P25772). Substrates: NAD+ (molecule.C00003). Products: AMP (molecule.C00020), H+ (molecule.C00080), Nicotinamide D-ribonucleotide (molecule.C00455).

## Annotation

CATALYSES THE FORMATION OF A PHOSPHODIESTER AT THE SITE OF A SINGLE- STRAND BREAK IN DUPLEX DNA.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P15042|protein.P15042]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P25772|protein.P25772]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00455|molecule.C00455]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DNA-LIGASE-NAD+-RXN`

## Notes

3-Hydroxy-Terminated-DNAs + 5-Phospho-terminated-DNAs + NAD -> DNA-N + AMP + NICOTINAMIDE_NUCLEOTIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

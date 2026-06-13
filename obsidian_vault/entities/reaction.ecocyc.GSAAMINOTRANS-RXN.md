---
entity_id: "reaction.ecocyc.GSAAMINOTRANS-RXN"
entity_type: "reaction"
name: "GSAAMINOTRANS-RXN"
source_database: "EcoCyc"
source_id: "GSAAMINOTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Glutamate-1-semialdehyde aminotransferase"
---

# GSAAMINOTRANS-RXN

`reaction.ecocyc.GSAAMINOTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GSAAMINOTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the third step in the tRNA-dependent transformation of glutamate to δ-aminolevulinate, the first committed precursor of porphyrin biosynthesis. EcoCyc reaction equation: GLUTAMATE-1-SEMIALDEHYDE -> 5-AMINO-LEVULINATE; direction=LEFT-TO-RIGHT. This reaction is the third step in the tRNA-dependent transformation of glutamate to δ-aminolevulinate, the first committed precursor of porphyrin biosynthesis.

## Biological Role

Catalyzed by glutamate-1-semialdehyde 2,1-aminomutase (complex.ecocyc.GSAAMINOTRANS-CPLX). Substrates: (S)-4-Amino-5-oxopentanoate (molecule.C03741). Products: 5-Aminolevulinate (molecule.C00430).

## Enriched Pathways

- `ecocyc.PWY-5188` uroporphyrinogen-III I (from glutamate) (EcoCyc)

## Annotation

This reaction is the third step in the tRNA-dependent transformation of glutamate to δ-aminolevulinate, the first committed precursor of porphyrin biosynthesis.

## Pathways

- `ecocyc.PWY-5188` uroporphyrinogen-III I (from glutamate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.GSAAMINOTRANS-CPLX|complex.ecocyc.GSAAMINOTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00430|molecule.C00430]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03741|molecule.C03741]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CARBOXYMETHOXYLAMINE|molecule.ecocyc.CARBOXYMETHOXYLAMINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1467|molecule.ecocyc.CPD0-1467]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GSAAMINOTRANS-RXN`

## Notes

GLUTAMATE-1-SEMIALDEHYDE -> 5-AMINO-LEVULINATE; direction=LEFT-TO-RIGHT

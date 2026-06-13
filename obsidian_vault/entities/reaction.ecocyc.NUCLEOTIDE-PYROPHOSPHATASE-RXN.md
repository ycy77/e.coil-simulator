---
entity_id: "reaction.ecocyc.NUCLEOTIDE-PYROPHOSPHATASE-RXN"
entity_type: "reaction"
name: "NUCLEOTIDE-PYROPHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "NUCLEOTIDE-PYROPHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "NTP diphosphatase"
  - "NTP pyrophosphatase"
  - "NTP pyrophosphohydrolase"
  - "nucleoside-triphosphate pyrophosphohydrolase"
  - "Nucleoside-triphosphate diphosphatase"
---

# NUCLEOTIDE-PYROPHOSPHATASE-RXN

`reaction.ecocyc.NUCLEOTIDE-PYROPHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NUCLEOTIDE-PYROPHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Nucleoside-Triphosphates + WATER -> Nucleoside-Monophosphates + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Nucleoside-Triphosphates + WATER -> Nucleoside-Monophosphates + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nucleoside triphosphate pyrophosphohydrolase (complex.ecocyc.CPLX0-7692). Substrates: H2O (molecule.C00001), a nucleoside triphosphate (molecule.ecocyc.Nucleoside-Triphosphates). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), a nucleoside 5'-monophosphate (molecule.ecocyc.Nucleoside-Monophosphates).

## Annotation

Nucleoside-Triphosphates + WATER -> Nucleoside-Monophosphates + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7692|complex.ecocyc.CPLX0-7692]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Nucleoside-Monophosphates|molecule.ecocyc.Nucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Nucleoside-Triphosphates|molecule.ecocyc.Nucleoside-Triphosphates]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[complex.ecocyc.CPLX0-1242|complex.ecocyc.CPLX0-1242]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:NUCLEOTIDE-PYROPHOSPHATASE-RXN`

## Notes

Nucleoside-Triphosphates + WATER -> Nucleoside-Monophosphates + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

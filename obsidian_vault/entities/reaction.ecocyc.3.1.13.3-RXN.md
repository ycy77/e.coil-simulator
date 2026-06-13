---
entity_id: "reaction.ecocyc.3.1.13.3-RXN"
entity_type: "reaction"
name: "3.1.13.3-RXN"
source_database: "EcoCyc"
source_id: "3.1.13.3-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.1.13.3-RXN

`reaction.ecocyc.3.1.13.3-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.13.3-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

from the IUBMB Enzyme Nomenclature web site: "Exonucleolytic cleavage of oligonucleotides to yield nucleoside 5'-phosphates. Also hydrolyses NAD+ to NMN and AMP. Formerly EC 3.1.4.19." EcoCyc reaction equation: Oligonucleotides + WATER -> Nucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT. from the IUBMB Enzyme Nomenclature web site: "Exonucleolytic cleavage of oligonucleotides to yield nucleoside 5'-phosphates. Also hydrolyses NAD+ to NMN and AMP. Formerly EC 3.1.4.19."

## Biological Role

Catalyzed by oligoribonuclease (complex.ecocyc.CPLX0-1821). Substrates: H2O (molecule.C00001), a double-stranded oligonucleotide (molecule.ecocyc.Oligonucleotides). Products: a nucleoside 5'-monophosphate (molecule.ecocyc.Nucleoside-Monophosphates).

## Annotation

from the IUBMB Enzyme Nomenclature web site: "Exonucleolytic cleavage of oligonucleotides to yield nucleoside 5'-phosphates. Also hydrolyses NAD+ to NMN and AMP. Formerly EC 3.1.4.19."

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1821|complex.ecocyc.CPLX0-1821]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Nucleoside-Monophosphates|molecule.ecocyc.Nucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Oligonucleotides|molecule.ecocyc.Oligonucleotides]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00054|molecule.C00054]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3.1.13.3-RXN`

## Notes

Oligonucleotides + WATER -> Nucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT

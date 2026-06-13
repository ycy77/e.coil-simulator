---
entity_id: "reaction.ecocyc.RXN-10814"
entity_type: "reaction"
name: "RXN-10814"
source_database: "EcoCyc"
source_id: "RXN-10814"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-10814

`reaction.ecocyc.RXN-10814`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10814`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the final reaction in the biosynthesis of phenylalanine. EcoCyc reaction equation: PHE + 2-KETOGLUTARATE -> PHENYL-PYRUVATE + GLT; direction=REVERSIBLE. This is the final reaction in the biosynthesis of phenylalanine.

## Biological Role

Catalyzed by aspartate aminotransferase (complex.ecocyc.ASPAMINOTRANS-DIMER), branched-chain-amino-acid aminotransferase (complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX), tyrosine aminotransferase (complex.ecocyc.TYRB-DIMER). Substrates: 2-Oxoglutarate (molecule.C00026), L-Phenylalanine (molecule.C00079). Products: L-Glutamate (molecule.C00025), Phenylpyruvate (molecule.C00166).

## Enriched Pathways

- `ecocyc.PHESYN` L-phenylalanine biosynthesis I (EcoCyc)

## Annotation

This is the final reaction in the biosynthesis of phenylalanine.

## Pathways

- `ecocyc.PHESYN` L-phenylalanine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.ASPAMINOTRANS-DIMER|complex.ecocyc.ASPAMINOTRANS-DIMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX|complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.TYRB-DIMER|complex.ecocyc.TYRB-DIMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00166|molecule.C00166]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00079|molecule.C00079]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00141|molecule.C00141]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01384|molecule.C01384]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1614|molecule.ecocyc.CPD0-1614]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-10814`

## Notes

PHE + 2-KETOGLUTARATE -> PHENYL-PYRUVATE + GLT; direction=REVERSIBLE

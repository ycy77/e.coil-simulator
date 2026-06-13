---
entity_id: "reaction.ecocyc.RXN-12473"
entity_type: "reaction"
name: "RXN-12473"
source_database: "EcoCyc"
source_id: "RXN-12473"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12473

`reaction.ecocyc.RXN-12473`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12473`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Carboxyadenylated-MPT-synthases + MOCS3-Cysteine-Persulfide + Donor-H2 -> Thiocarboxylated-MPT-synthases + MOCS3-Cysteine + AMP + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Carboxyadenylated-MPT-synthases + MOCS3-Cysteine-Persulfide + Donor-H2 -> Thiocarboxylated-MPT-synthases + MOCS3-Cysteine + AMP + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by molybdopterin synthase adenylyltransferase/sulfur transferase (complex.ecocyc.CPLX0-12611), tusA (protein.P0A890), ynjE (protein.P78067). Substrates: a [molybdopterin synthase sulfurtransferase]-S-sulfanyl-L-cysteine (molecule.ecocyc.MOCS3-Cysteine-Persulfide). Products: AMP (molecule.C00020), H+ (molecule.C00080), a [molybdopterin synthase sulfurtransferase]-L-cysteine (molecule.ecocyc.MOCS3-Cysteine).

## Enriched Pathways

- `ecocyc.PWY-6823` molybdopterin biosynthesis (EcoCyc)

## Annotation

Carboxyadenylated-MPT-synthases + MOCS3-Cysteine-Persulfide + Donor-H2 -> Thiocarboxylated-MPT-synthases + MOCS3-Cysteine + AMP + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6823` molybdopterin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-12611|complex.ecocyc.CPLX0-12611]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A890|protein.P0A890]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P78067|protein.P78067]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MOCS3-Cysteine|molecule.ecocyc.MOCS3-Cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.MOCS3-Cysteine-Persulfide|molecule.ecocyc.MOCS3-Cysteine-Persulfide]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12473`

## Notes

Carboxyadenylated-MPT-synthases + MOCS3-Cysteine-Persulfide + Donor-H2 -> Thiocarboxylated-MPT-synthases + MOCS3-Cysteine + AMP + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

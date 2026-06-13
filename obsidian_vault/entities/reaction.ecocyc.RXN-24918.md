---
entity_id: "reaction.ecocyc.RXN-24918"
entity_type: "reaction"
name: "RXN-24918"
source_database: "EcoCyc"
source_id: "RXN-24918"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24918

`reaction.ecocyc.RXN-24918`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24918`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Polyprenyl-Phenol + PREPHENATE + Acceptor + PROTON -> 3-Polyrenyl-benzene-1-2-diols + PHENYL-PYRUVATE + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 2-Polyprenyl-Phenol + PREPHENATE + Acceptor + PROTON -> 3-Polyrenyl-benzene-1-2-diols + PHENYL-PYRUVATE + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2-(all-trans-polyprenyl)phenol 6-hydroxylase (prephenate) (complex.ecocyc.CPLX0-8308). Substrates: H+ (molecule.C00080), Prephenate (molecule.C00254), 2-Polyprenylphenol (molecule.C05807). Products: CO2 (molecule.C00011), Phenylpyruvate (molecule.C00166), a 3-(all-trans-polyprenyl)benzene-1,2-diol (molecule.ecocyc.3-Polyrenyl-benzene-1-2-diols).

## Annotation

2-Polyprenyl-Phenol + PREPHENATE + Acceptor + PROTON -> 3-Polyrenyl-benzene-1-2-diols + PHENYL-PYRUVATE + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8308|complex.ecocyc.CPLX0-8308]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00166|molecule.C00166]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.3-Polyrenyl-benzene-1-2-diols|molecule.ecocyc.3-Polyrenyl-benzene-1-2-diols]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00254|molecule.C00254]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05807|molecule.C05807]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24918`

## Notes

2-Polyprenyl-Phenol + PREPHENATE + Acceptor + PROTON -> 3-Polyrenyl-benzene-1-2-diols + PHENYL-PYRUVATE + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT

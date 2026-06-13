---
entity_id: "reaction.ecocyc.RXN-24718"
entity_type: "reaction"
name: "RXN-24718"
source_database: "EcoCyc"
source_id: "RXN-24718"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24718

`reaction.ecocyc.RXN-24718`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24718`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

OCTAPRENYL-METHYL-METHOXY-BENZQ + PREPHENATE + Acceptor + PROTON -> OCTAPRENYL-METHYL-OH-METHOXY-BENZQ + PHENYL-PYRUVATE + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: OCTAPRENYL-METHYL-METHOXY-BENZQ + PREPHENATE + Acceptor + PROTON -> OCTAPRENYL-METHYL-OH-METHOXY-BENZQ + PHENYL-PYRUVATE + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2-(all-trans-polyprenyl)phenol 6-hydroxylase (prephenate) (complex.ecocyc.CPLX0-8308). Substrates: H+ (molecule.C00080), Prephenate (molecule.C00254), 5-methoxy-2-methyl-3-(all-trans-octaprenyl)benzene-1,4-diol (molecule.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZQ). Products: CO2 (molecule.C00011), Phenylpyruvate (molecule.C00166), 3-demethylubiquinol-8 (molecule.ecocyc.OCTAPRENYL-METHYL-OH-METHOXY-BENZQ).

## Enriched Pathways

- `ecocyc.PWY-8533` ubiquinol-8 biosynthesis (anaerobic) (EcoCyc)

## Annotation

OCTAPRENYL-METHYL-METHOXY-BENZQ + PREPHENATE + Acceptor + PROTON -> OCTAPRENYL-METHYL-OH-METHOXY-BENZQ + PHENYL-PYRUVATE + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8533` ubiquinol-8 biosynthesis (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8308|complex.ecocyc.CPLX0-8308]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00166|molecule.C00166]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.OCTAPRENYL-METHYL-OH-METHOXY-BENZQ|molecule.ecocyc.OCTAPRENYL-METHYL-OH-METHOXY-BENZQ]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00254|molecule.C00254]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZQ|molecule.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZQ]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24718`

## Notes

OCTAPRENYL-METHYL-METHOXY-BENZQ + PREPHENATE + Acceptor + PROTON -> OCTAPRENYL-METHYL-OH-METHOXY-BENZQ + PHENYL-PYRUVATE + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT

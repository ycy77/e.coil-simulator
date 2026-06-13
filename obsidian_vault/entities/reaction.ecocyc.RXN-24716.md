---
entity_id: "reaction.ecocyc.RXN-24716"
entity_type: "reaction"
name: "RXN-24716"
source_database: "EcoCyc"
source_id: "RXN-24716"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24716

`reaction.ecocyc.RXN-24716`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24716`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-OCTAPRENYLPHENOL + PREPHENATE + Acceptor + PROTON -> 2-OCTAPRENYL-6-HYDROXYPHENOL + PHENYL-PYRUVATE + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 2-OCTAPRENYLPHENOL + PREPHENATE + Acceptor + PROTON -> 2-OCTAPRENYL-6-HYDROXYPHENOL + PHENYL-PYRUVATE + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2-(all-trans-polyprenyl)phenol 6-hydroxylase (prephenate) (complex.ecocyc.CPLX0-8308). Substrates: H+ (molecule.C00080), Prephenate (molecule.C00254), 2-(all-trans-octaprenyl)phenol (molecule.ecocyc.2-OCTAPRENYLPHENOL). Products: CO2 (molecule.C00011), Phenylpyruvate (molecule.C00166), 3-(all-trans-octaprenyl)benzene-1,2-diol (molecule.ecocyc.2-OCTAPRENYL-6-HYDROXYPHENOL).

## Enriched Pathways

- `ecocyc.PWY-8533` ubiquinol-8 biosynthesis (anaerobic) (EcoCyc)

## Annotation

2-OCTAPRENYLPHENOL + PREPHENATE + Acceptor + PROTON -> 2-OCTAPRENYL-6-HYDROXYPHENOL + PHENYL-PYRUVATE + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8533` ubiquinol-8 biosynthesis (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8308|complex.ecocyc.CPLX0-8308]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00166|molecule.C00166]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-OCTAPRENYL-6-HYDROXYPHENOL|molecule.ecocyc.2-OCTAPRENYL-6-HYDROXYPHENOL]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00254|molecule.C00254]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.2-OCTAPRENYLPHENOL|molecule.ecocyc.2-OCTAPRENYLPHENOL]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24716`

## Notes

2-OCTAPRENYLPHENOL + PREPHENATE + Acceptor + PROTON -> 2-OCTAPRENYL-6-HYDROXYPHENOL + PHENYL-PYRUVATE + CARBON-DIOXIDE + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT

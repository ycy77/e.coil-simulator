---
entity_id: "reaction.ecocyc.ORNDECARBOX-RXN"
entity_type: "reaction"
name: "ORNDECARBOX-RXN"
source_database: "EcoCyc"
source_id: "ORNDECARBOX-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ORNDECARBOX-RXN

`reaction.ecocyc.ORNDECARBOX-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ORNDECARBOX-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A reaction in one of two paths for the biosynthesis of putrescine and spermidine. EcoCyc reaction equation: PROTON + L-ORNITHINE -> CARBON-DIOXIDE + PUTRESCINE; direction=PHYSIOL-LEFT-TO-RIGHT. A reaction in one of two paths for the biosynthesis of putrescine and spermidine.

## Biological Role

Catalyzed by constitutive ornithine decarboxylase (complex.ecocyc.ORNDECARBOX-BIO-CPLX), inducible ornithine decarboxylase (complex.ecocyc.ORNDECARBOXDEG-CPLX). Substrates: L-Ornithine (molecule.C00077), H+ (molecule.C00080). Products: CO2 (molecule.C00011), Putrescine (molecule.C00134).

## Enriched Pathways

- `ecocyc.ORNDEG-PWY` superpathway of ornithine degradation (EcoCyc)
- `ecocyc.PWY-46` putrescine biosynthesis III (EcoCyc)

## Annotation

A reaction in one of two paths for the biosynthesis of putrescine and spermidine.

## Pathways

- `ecocyc.ORNDEG-PWY` superpathway of ornithine degradation (EcoCyc)
- `ecocyc.PWY-46` putrescine biosynthesis III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (19)

- `activates` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C04494|molecule.C04494]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.ORNDECARBOX-BIO-CPLX|complex.ecocyc.ORNDECARBOX-BIO-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ORNDECARBOXDEG-CPLX|complex.ecocyc.ORNDECARBOXDEG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00077|molecule.C00077]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01005|molecule.C01005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C12147|molecule.C12147]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-3728|molecule.ecocyc.CPD-3728]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1239|molecule.ecocyc.CPD0-1239]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1240|molecule.ecocyc.CPD0-1240]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[protein.ecocyc.CPD0-1515|protein.ecocyc.CPD0-1515]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ORNDECARBOX-RXN`

## Notes

PROTON + L-ORNITHINE -> CARBON-DIOXIDE + PUTRESCINE; direction=PHYSIOL-LEFT-TO-RIGHT

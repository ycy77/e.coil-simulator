---
entity_id: "reaction.ecocyc.RXN0-5359"
entity_type: "reaction"
name: "RXN0-5359"
source_database: "EcoCyc"
source_id: "RXN0-5359"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5359

`reaction.ecocyc.RXN0-5359`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5359`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GTP -> C-DI-GMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GTP -> C-DI-GMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by diguanylate cyclase DgcZ (complex.ecocyc.CPLX0-7802), diguanylate cyclase DgcM (complex.ecocyc.CPLX0-8090), diguanylate cyclase DosC (complex.ecocyc.CPLX0-8218), diguanylate cyclase DgcE (complex.ecocyc.CPLX0-8535), diguanylate cyclase DgcC (complex.ecocyc.CPLX0-8556), dgcN (protein.P46139), dgcT (protein.P75908), dgcJ (protein.P76237), and 2 more. Substrates: GTP (molecule.C00044). Products: Diphosphate (molecule.C00013), 3',5'-Cyclic diGMP (molecule.C16463).

## Annotation

GTP -> C-DI-GMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (17)

- `activates` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7802|complex.ecocyc.CPLX0-7802]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8090|complex.ecocyc.CPLX0-8090]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8218|complex.ecocyc.CPLX0-8218]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8535|complex.ecocyc.CPLX0-8535]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8556|complex.ecocyc.CPLX0-8556]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P46139|protein.P46139]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75908|protein.P75908]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76237|protein.P76237]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76245|protein.P76245]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76330|protein.P76330]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C16463|molecule.C16463]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00438|molecule.C00438]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C16463|molecule.C16463]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5359`

## Notes

GTP -> C-DI-GMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

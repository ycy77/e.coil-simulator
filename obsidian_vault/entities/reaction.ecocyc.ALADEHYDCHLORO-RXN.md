---
entity_id: "reaction.ecocyc.ALADEHYDCHLORO-RXN"
entity_type: "reaction"
name: "ALADEHYDCHLORO-RXN"
source_database: "EcoCyc"
source_id: "ALADEHYDCHLORO-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ALADEHYDCHLORO-RXN

`reaction.ecocyc.ALADEHYDCHLORO-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALADEHYDCHLORO-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is an alternate substrate reaction of D-cysteine desulfhydrase. It may be identical with EC number 4.5.1.2. EcoCyc reaction equation: 3-CHLORO-D-ALANINE + THIOGLYCOLATE -> PROTON + S-CARBOXYMETHYL-D-CYSTEINE + CL-; direction=PHYSIOL-LEFT-TO-RIGHT. This is an alternate substrate reaction of D-cysteine desulfhydrase. It may be identical with EC number 4.5.1.2.

## Biological Role

Catalyzed by D-cysteine desulfhydrase, PLP-dependent / 3-chloro-D-alanine dehydrochlorinase (complex.ecocyc.DCYSDESULF-CPLX). Substrates: 3-chloro-D-alanine (molecule.ecocyc.3-CHLORO-D-ALANINE), thioglycolate (molecule.ecocyc.THIOGLYCOLATE). Products: H+ (molecule.C00080), chloride (molecule.ecocyc.CL-), S-carboxymethyl-D-cysteine (molecule.ecocyc.S-CARBOXYMETHYL-D-CYSTEINE).

## Annotation

This is an alternate substrate reaction of D-cysteine desulfhydrase. It may be identical with EC number 4.5.1.2.

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.DCYSDESULF-CPLX|complex.ecocyc.DCYSDESULF-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CL-|molecule.ecocyc.CL-]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.S-CARBOXYMETHYL-D-CYSTEINE|molecule.ecocyc.S-CARBOXYMETHYL-D-CYSTEINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.3-CHLORO-D-ALANINE|molecule.ecocyc.3-CHLORO-D-ALANINE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.THIOGLYCOLATE|molecule.ecocyc.THIOGLYCOLATE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00192|molecule.C00192]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7702|molecule.ecocyc.CPD-7702]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.L-PENICILLAMINE|molecule.ecocyc.L-PENICILLAMINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHENYLHYDRAZINE|molecule.ecocyc.PHENYLHYDRAZINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ALADEHYDCHLORO-RXN`

## Notes

3-CHLORO-D-ALANINE + THIOGLYCOLATE -> PROTON + S-CARBOXYMETHYL-D-CYSTEINE + CL-; direction=PHYSIOL-LEFT-TO-RIGHT

---
entity_id: "reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN"
entity_type: "reaction"
name: "DIHYDROFOLATEREDUCT-RXN"
source_database: "EcoCyc"
source_id: "DIHYDROFOLATEREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIHYDROFOLATEREDUCT-RXN

`reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIHYDROFOLATEREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

THF-GLU-N + NADP -> DIHYDROFOLATE-GLU-N + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: THF-GLU-N + NADP -> DIHYDROFOLATE-GLU-N + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by dihydromonapterin reductase (complex.ecocyc.CPLX0-8571), folA (protein.P0ABQ4). Substrates: NADP+ (molecule.C00006), THF-polyglutamate (molecule.C03541). Products: NADPH (molecule.C00005), H+ (molecule.C00080), a 7,8-dihydrofolate (molecule.ecocyc.DIHYDROFOLATE-GLU-N).

## Enriched Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)
- `ecocyc.PWY-6614` tetrahydrofolate biosynthesis I (EcoCyc)

## Annotation

THF-GLU-N + NADP -> DIHYDROFOLATE-GLU-N + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)
- `ecocyc.PWY-6614` tetrahydrofolate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (31)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8571|complex.ecocyc.CPLX0-8571]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ABQ4|protein.P0ABQ4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.DIHYDROFOLATE-GLU-N|molecule.ecocyc.DIHYDROFOLATE-GLU-N]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03541|molecule.C03541]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00750|molecule.C00750]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01672|molecule.C01672]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01937|molecule.C01937]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.BA_2|molecule.ecocyc.BA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-14445|molecule.ecocyc.CPD-14445]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-2|molecule.ecocyc.CPD-2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-3682|molecule.ecocyc.CPD-3682]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1581|molecule.ecocyc.CPD0-1581]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1583|molecule.ecocyc.CPD0-1583]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1584|molecule.ecocyc.CPD0-1584]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1585|molecule.ecocyc.CPD0-1585]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1586|molecule.ecocyc.CPD0-1586]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1587|molecule.ecocyc.CPD0-1587]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1588|molecule.ecocyc.CPD0-1588]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1590|molecule.ecocyc.CPD0-1590]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1591|molecule.ecocyc.CPD0-1591]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1594|molecule.ecocyc.CPD0-1594]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.RB|molecule.ecocyc.RB_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DIHYDROFOLATEREDUCT-RXN`

## Notes

THF-GLU-N + NADP -> DIHYDROFOLATE-GLU-N + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

---
entity_id: "reaction.ecocyc.GLYCDEH-RXN"
entity_type: "reaction"
name: "GLYCDEH-RXN"
source_database: "EcoCyc"
source_id: "GLYCDEH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYCDEH-RXN

`reaction.ecocyc.GLYCDEH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYCDEH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in an alternate route of glycerol dissimilation. EcoCyc reaction equation: GLYCEROL + NAD -> DIHYDROXYACETONE + NADH + PROTON; direction=REVERSIBLE. This reaction is involved in an alternate route of glycerol dissimilation.

## Biological Role

Catalyzed by L-1,2-propanediol dehydrogenase / glycerol dehydrogenase (complex.ecocyc.GLYCDEH-CPLX). Substrates: NAD+ (molecule.C00003), Glycerol (molecule.C00116). Products: NADH (molecule.C00004), H+ (molecule.C00080), Glycerone (molecule.C00184).

## Enriched Pathways

- `ecocyc.GLYCEROLMETAB-PWY` glycerol degradation V (EcoCyc)

## Annotation

This reaction is involved in an alternate route of glycerol dissimilation.

## Pathways

- `ecocyc.GLYCEROLMETAB-PWY` glycerol degradation V (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.RB|molecule.ecocyc.RB_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.GLYCDEH-CPLX|complex.ecocyc.GLYCDEH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00184|molecule.C00184]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00116|molecule.C00116]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.8-HYDROXYQUINOLINE|molecule.ecocyc.8-HYDROXYQUINOLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLYCDEH-RXN`

## Notes

GLYCEROL + NAD -> DIHYDROXYACETONE + NADH + PROTON; direction=REVERSIBLE

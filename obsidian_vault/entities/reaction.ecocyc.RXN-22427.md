---
entity_id: "reaction.ecocyc.RXN-22427"
entity_type: "reaction"
name: "lipoprotein release"
source_database: "EcoCyc"
source_id: "RXN-22427"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# lipoprotein release

`reaction.ecocyc.RXN-22427`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22427`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

a-mature-triacylated-lipoprotein + LolA + ATP + WATER -> LolA-Lipoprotein-Complex + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: a-mature-triacylated-lipoprotein + LolA + ATP + WATER -> LolA-Lipoprotein-Complex + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lipoprotein release complex (complex.ecocyc.ABC-62-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), an N-acyl-(S-diacyl-sn-glyceryl)-L-cysteinyl-[lipoprotein] (molecule.ecocyc.a-mature-triacylated-lipoprotein). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-7884` lipoprotein posttranslational modification (Gram-negative bacteria) (EcoCyc)

## Annotation

a-mature-triacylated-lipoprotein + LolA + ATP + WATER -> LolA-Lipoprotein-Complex + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7884` lipoprotein posttranslational modification (Gram-negative bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.ABC-62-CPLX|complex.ecocyc.ABC-62-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.a-mature-triacylated-lipoprotein|molecule.ecocyc.a-mature-triacylated-lipoprotein]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22427`

## Notes

a-mature-triacylated-lipoprotein + LolA + ATP + WATER -> LolA-Lipoprotein-Complex + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

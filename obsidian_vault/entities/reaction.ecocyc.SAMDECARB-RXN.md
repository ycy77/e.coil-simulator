---
entity_id: "reaction.ecocyc.SAMDECARB-RXN"
entity_type: "reaction"
name: "SAMDECARB-RXN"
source_database: "EcoCyc"
source_id: "SAMDECARB-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SAMDECARB-RXN

`reaction.ecocyc.SAMDECARB-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SAMDECARB-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in the spermidine biosynthesis pathway. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + PROTON -> CARBON-DIOXIDE + S-ADENOSYLMETHIONINAMINE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is involved in the spermidine biosynthesis pathway.

## Biological Role

Catalyzed by S-adenosylmethionine decarboxylase (complex.ecocyc.SAMDECARB-CPLX). Substrates: S-Adenosyl-L-methionine (molecule.C00019), H+ (molecule.C00080). Products: CO2 (molecule.C00011), S-Adenosylmethioninamine (molecule.C01137).

## Enriched Pathways

- `ecocyc.BSUBPOLYAMSYN-PWY` spermidine biosynthesis I (EcoCyc)
- `ecocyc.PWY0-1303` aminopropylcadaverine biosynthesis (EcoCyc)

## Annotation

This reaction is involved in the spermidine biosynthesis pathway.

## Pathways

- `ecocyc.BSUBPOLYAMSYN-PWY` spermidine biosynthesis I (EcoCyc)
- `ecocyc.PWY0-1303` aminopropylcadaverine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (25)

- `activates` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C14819|molecule.C14819]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD-1484|molecule.ecocyc.CPD-1484]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.LI|molecule.ecocyc.LI_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.SAMDECARB-CPLX|complex.ecocyc.SAMDECARB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01137|molecule.C01137]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01137|molecule.C01137]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.BOROHYDRIDE|molecule.ecocyc.BOROHYDRIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1396|molecule.ecocyc.CPD0-1396]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1397|molecule.ecocyc.CPD0-1397]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1398|molecule.ecocyc.CPD0-1398]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1399|molecule.ecocyc.CPD0-1399]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1401|molecule.ecocyc.CPD0-1401]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1402|molecule.ecocyc.CPD0-1402]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1404|molecule.ecocyc.CPD0-1404]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1406|molecule.ecocyc.CPD0-1406]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHENYLHYDRAZINE|molecule.ecocyc.PHENYLHYDRAZINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:SAMDECARB-RXN`

## Notes

S-ADENOSYLMETHIONINE + PROTON -> CARBON-DIOXIDE + S-ADENOSYLMETHIONINAMINE; direction=PHYSIOL-LEFT-TO-RIGHT

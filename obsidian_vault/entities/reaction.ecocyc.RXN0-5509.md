---
entity_id: "reaction.ecocyc.RXN0-5509"
entity_type: "reaction"
name: "RXN0-5509"
source_database: "EcoCyc"
source_id: "RXN0-5509"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5509

`reaction.ecocyc.RXN0-5509`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5509`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction depends on the presence of the ribosome. Only mRNA that is actively translated is being cleaved. EcoCyc reaction equation: mRNA-Holder + WATER -> mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction depends on the presence of the ribosome. Only mRNA that is actively translated is being cleaved.

## Biological Role

Catalyzed by CP4-57 prophage; RNase LS, toxin of the RnlAB toxin-antitoxin system (complex.ecocyc.CPLX0-8095), ghoS (protein.P0AF61), relE (protein.P0C077), higB (protein.P64578), hicA (protein.P76106), mqsR (protein.Q46865), yafQ (protein.Q47149), yafO (protein.Q47157). Substrates: H2O (molecule.C00001), an mRNA (molecule.ecocyc.mRNA-Holder).

## Annotation

This reaction depends on the presence of the ribosome. Only mRNA that is actively translated is being cleaved.

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8095|complex.ecocyc.CPLX0-8095]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AF61|protein.P0AF61]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0C077|protein.P0C077]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P64578|protein.P64578]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76106|protein.P76106]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q46865|protein.Q46865]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q47149|protein.Q47149]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q47157|protein.Q47157]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.mRNA-Holder|molecule.ecocyc.mRNA-Holder]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5509`

## Notes

mRNA-Holder + WATER -> mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT

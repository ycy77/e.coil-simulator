---
entity_id: "reaction.ecocyc.TRANS-RXN-371"
entity_type: "reaction"
name: "export of 2,4-dinitrophenyl-S-glutathione"
source_database: "EcoCyc"
source_id: "TRANS-RXN-371"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# export of 2,4-dinitrophenyl-S-glutathione

`reaction.ecocyc.TRANS-RXN-371`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-371`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

The glutathione S-conjugates, 2,4-dinitrophenyl-S-glutathione and bimane-S-glutathione, are transported out of E. coli K-12; transport is inhibited by vanadate and by fluoride ion . 2,4-dinitrophenyl-S-glutathione transport is inhibited by probenecid and by the uncouplers, carbonyl cyanide p-trifluoromethoxyphenylhydrazone and 2,4-dinitrophenol . The transport protein responsible for export is not known but potential candidates include the ABC-6-CPLX and the putative ABC export complex, MdlAB (see G6248 and EG11622). EcoCyc reaction equation: S-24-DINITROPHENYLGLUTATHIONE + ATP + WATER -> S-24-DINITROPHENYLGLUTATHIONE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. The glutathione S-conjugates, 2,4-dinitrophenyl-S-glutathione and bimane-S-glutathione, are transported out of E. coli K-12; transport is inhibited by vanadate and by fluoride ion . 2,4-dinitrophenyl-S-glutathione transport is inhibited by probenecid and by the uncouplers, carbonyl cyanide p-trifluoromethoxyphenylhydrazone and 2,4-dinitrophenol . The transport protein responsible for export is not known but potential candidates include the ABC-6-CPLX and the putative ABC export complex, MdlAB (see G6248 and EG11622).

## Biological Role

Substrates: H2O (molecule.C00001), ATP (molecule.C00002), 2,4-dinitrophenyl-S-glutathione (molecule.ecocyc.S-24-DINITROPHENYLGLUTATHIONE). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi), 2,4-dinitrophenyl-S-glutathione (molecule.ecocyc.S-24-DINITROPHENYLGLUTATHIONE).

## Annotation

The glutathione S-conjugates, 2,4-dinitrophenyl-S-glutathione and bimane-S-glutathione, are transported out of E. coli K-12; transport is inhibited by vanadate and by fluoride ion . 2,4-dinitrophenyl-S-glutathione transport is inhibited by probenecid and by the uncouplers, carbonyl cyanide p-trifluoromethoxyphenylhydrazone and 2,4-dinitrophenol . The transport protein responsible for export is not known but potential candidates include the ABC-6-CPLX and the putative ABC export complex, MdlAB (see G6248 and EG11622).

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.S-24-DINITROPHENYLGLUTATHIONE|molecule.ecocyc.S-24-DINITROPHENYLGLUTATHIONE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.S-24-DINITROPHENYLGLUTATHIONE|molecule.ecocyc.S-24-DINITROPHENYLGLUTATHIONE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-371`

## Notes

S-24-DINITROPHENYLGLUTATHIONE + ATP + WATER -> S-24-DINITROPHENYLGLUTATHIONE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

---
entity_id: "reaction.ecocyc.RXN0-7007"
entity_type: "reaction"
name: "RXN0-7007"
source_database: "EcoCyc"
source_id: "RXN0-7007"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7007

`reaction.ecocyc.RXN0-7007`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7007`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + tRNA-adenine-37 + Reduced-2Fe-2S-Ferredoxins -> ADENOSYL-HOMO-CYS + MET + CH33ADO + tRNA-2methyladenine-37 + Oxidized-2Fe-2S-Ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + tRNA-adenine-37 + Reduced-2Fe-2S-Ferredoxins -> ADENOSYL-HOMO-CYS + MET + CH33ADO + tRNA-2methyladenine-37 + Oxidized-2Fe-2S-Ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rlmN (protein.P36979). Substrates: S-Adenosyl-L-methionine (molecule.C00019), an adenine37 in tRNA (molecule.ecocyc.tRNA-adenine-37). Products: S-Adenosyl-L-homocysteine (molecule.C00021), L-Methionine (molecule.C00073), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO), a 2-methyladenine37 in tRNA (molecule.ecocyc.tRNA-2methyladenine-37).

## Annotation

S-ADENOSYLMETHIONINE + tRNA-adenine-37 + Reduced-2Fe-2S-Ferredoxins -> ADENOSYL-HOMO-CYS + MET + CH33ADO + tRNA-2methyladenine-37 + Oxidized-2Fe-2S-Ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P36979|protein.P36979]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.tRNA-2methyladenine-37|molecule.ecocyc.tRNA-2methyladenine-37]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-adenine-37|molecule.ecocyc.tRNA-adenine-37]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7007`

## Notes

S-ADENOSYLMETHIONINE + tRNA-adenine-37 + Reduced-2Fe-2S-Ferredoxins -> ADENOSYL-HOMO-CYS + MET + CH33ADO + tRNA-2methyladenine-37 + Oxidized-2Fe-2S-Ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT

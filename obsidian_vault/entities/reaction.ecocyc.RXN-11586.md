---
entity_id: "reaction.ecocyc.RXN-11586"
entity_type: "reaction"
name: "RXN-11586"
source_database: "EcoCyc"
source_id: "RXN-11586"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "YgfB"
  - "RlmN/YgfB"
  - "methyltransferase YfgB/RlmN"
  - "S-adenosyl-L-methionine:23S rRNA (adenine<sup>2503</sup>-C<sup>2</sup>)-methyltransferase"
---

# RXN-11586

`reaction.ecocyc.RXN-11586`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11586`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 23S-rRNA-adenine-2503 + Reduced-2Fe-2S-Ferredoxins -> ADENOSYL-HOMO-CYS + MET + CH33ADO + 23S-rRNA-2-methyladenine2503 + Oxidized-2Fe-2S-Ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 23S-rRNA-adenine-2503 + Reduced-2Fe-2S-Ferredoxins -> ADENOSYL-HOMO-CYS + MET + CH33ADO + 23S-rRNA-2-methyladenine2503 + Oxidized-2Fe-2S-Ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rlmN (protein.P36979). Substrates: S-Adenosyl-L-methionine (molecule.C00019), adenine2503 in 23S rRNA (molecule.ecocyc.23S-rRNA-adenine-2503). Products: S-Adenosyl-L-homocysteine (molecule.C00021), L-Methionine (molecule.C00073), a 2-methyladenine2503 in 23S rRNA (molecule.ecocyc.23S-rRNA-2-methyladenine2503), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO).

## Annotation

S-ADENOSYLMETHIONINE + 23S-rRNA-adenine-2503 + Reduced-2Fe-2S-Ferredoxins -> ADENOSYL-HOMO-CYS + MET + CH33ADO + 23S-rRNA-2-methyladenine2503 + Oxidized-2Fe-2S-Ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P36979|protein.P36979]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-2-methyladenine2503|molecule.ecocyc.23S-rRNA-2-methyladenine2503]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-adenine-2503|molecule.ecocyc.23S-rRNA-adenine-2503]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11586`

## Notes

S-ADENOSYLMETHIONINE + 23S-rRNA-adenine-2503 + Reduced-2Fe-2S-Ferredoxins -> ADENOSYL-HOMO-CYS + MET + CH33ADO + 23S-rRNA-2-methyladenine2503 + Oxidized-2Fe-2S-Ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT

---
entity_id: "reaction.ecocyc.RXN0-2601"
entity_type: "reaction"
name: "RXN0-2601"
source_database: "EcoCyc"
source_id: "RXN0-2601"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2601

`reaction.ecocyc.RXN0-2601`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2601`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Excision of the nucleobase lesion is a two-step process and involves formation of an enzyme-substrate Schiff base intermediate; subsequent DNA strand nicking occurs via a β-elimination leaving a 3'-terminal α,β-unsaturated aldehyde and a 5'-terminal phosphate. This reaction is catalysed by the Nth (HhH) family of bifunctional DNA glycosylases. EcoCyc reaction equation: Damaged-DNA-Pyrimidine + WATER -> a-DNA-3-alpha-beta-unsaturated-aldehyde + 5-Phospho-terminated-DNAs + Modified-Bases + PROTON; direction=LEFT-TO-RIGHT. Excision of the nucleobase lesion is a two-step process and involves formation of an enzyme-substrate Schiff base intermediate; subsequent DNA strand nicking occurs via a β-elimination leaving a 3'-terminal α,β-unsaturated aldehyde and a 5'-terminal phosphate. This reaction is catalysed by the Nth (HhH) family of bifunctional DNA glycosylases.

## Biological Role

Catalyzed by nth (protein.P0AB83). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), a modified nucleobase (molecule.ecocyc.Modified-Bases), a [DNA]-3'-α,β-unsaturated aldehyde (molecule.ecocyc.a-DNA-3-alpha-beta-unsaturated-aldehyde).

## Annotation

Excision of the nucleobase lesion is a two-step process and involves formation of an enzyme-substrate Schiff base intermediate; subsequent DNA strand nicking occurs via a β-elimination leaving a 3'-terminal α,β-unsaturated aldehyde and a 5'-terminal phosphate. This reaction is catalysed by the Nth (HhH) family of bifunctional DNA glycosylases.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AB83|protein.P0AB83]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Modified-Bases|molecule.ecocyc.Modified-Bases]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.a-DNA-3-alpha-beta-unsaturated-aldehyde|molecule.ecocyc.a-DNA-3-alpha-beta-unsaturated-aldehyde]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00533|molecule.C00533]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-2601`

## Notes

Damaged-DNA-Pyrimidine + WATER -> a-DNA-3-alpha-beta-unsaturated-aldehyde + 5-Phospho-terminated-DNAs + Modified-Bases + PROTON; direction=LEFT-TO-RIGHT

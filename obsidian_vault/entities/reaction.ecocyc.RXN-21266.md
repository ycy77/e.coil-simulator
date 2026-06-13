---
entity_id: "reaction.ecocyc.RXN-21266"
entity_type: "reaction"
name: "RXN-21266"
source_database: "EcoCyc"
source_id: "RXN-21266"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21266

`reaction.ecocyc.RXN-21266`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21266`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Excision of the nucleobase lesion is a two-step process and involves formation of an enzyme-substrate Schiff base intermediate; subsequent DNA strand nicking occurs via a β,δ-elimination leaving a 3'-terminal phosphate and a 5'-terminal phosphate. This reaction is catalysed by the Fpg (MutM) family of bifunctional DNA glycosylases. EcoCyc reaction equation: a-purine-base-lesion-in-DNA + WATER -> 3-Prime-Phosphate-Terminated-DNAs + 5-Phospho-terminated-DNAs + CPD-21221 + Modified-Bases; direction=PHYSIOL-LEFT-TO-RIGHT. Excision of the nucleobase lesion is a two-step process and involves formation of an enzyme-substrate Schiff base intermediate; subsequent DNA strand nicking occurs via a β,δ-elimination leaving a 3'-terminal phosphate and a 5'-terminal phosphate. This reaction is catalysed by the Fpg (MutM) family of bifunctional DNA glycosylases.

## Biological Role

Catalyzed by mutM (protein.P05523). Substrates: H2O (molecule.C00001). Products: 4-oxo-2-pentenal (molecule.ecocyc.CPD-21221), a modified nucleobase (molecule.ecocyc.Modified-Bases).

## Annotation

Excision of the nucleobase lesion is a two-step process and involves formation of an enzyme-substrate Schiff base intermediate; subsequent DNA strand nicking occurs via a β,δ-elimination leaving a 3'-terminal phosphate and a 5'-terminal phosphate. This reaction is catalysed by the Fpg (MutM) family of bifunctional DNA glycosylases.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P05523|protein.P05523]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-21221|molecule.ecocyc.CPD-21221]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Modified-Bases|molecule.ecocyc.Modified-Bases]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21266`

## Notes

a-purine-base-lesion-in-DNA + WATER -> 3-Prime-Phosphate-Terminated-DNAs + 5-Phospho-terminated-DNAs + CPD-21221 + Modified-Bases; direction=PHYSIOL-LEFT-TO-RIGHT

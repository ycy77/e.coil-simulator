---
entity_id: "reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERVAL-RXN"
entity_type: "reaction"
name: "BRANCHED-CHAINAMINOTRANSFERVAL-RXN"
source_database: "EcoCyc"
source_id: "BRANCHED-CHAINAMINOTRANSFERVAL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# BRANCHED-CHAINAMINOTRANSFERVAL-RXN

`reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERVAL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BRANCHED-CHAINAMINOTRANSFERVAL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

VAL + 2-KETOGLUTARATE -> 2-KETO-ISOVALERATE + GLT; direction=REVERSIBLE EcoCyc reaction equation: VAL + 2-KETOGLUTARATE -> 2-KETO-ISOVALERATE + GLT; direction=REVERSIBLE.

## Biological Role

Catalyzed by branched-chain-amino-acid aminotransferase (complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX). Substrates: 2-Oxoglutarate (molecule.C00026), L-Valine (molecule.C00183). Products: L-Glutamate (molecule.C00025), 3-Methyl-2-oxobutanoic acid (molecule.C00141).

## Enriched Pathways

- `ecocyc.VALSYN-PWY` L-valine biosynthesis (EcoCyc)

## Annotation

VAL + 2-KETOGLUTARATE -> 2-KETO-ISOVALERATE + GLT; direction=REVERSIBLE

## Pathways

- `ecocyc.VALSYN-PWY` L-valine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX|complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00141|molecule.C00141]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:BRANCHED-CHAINAMINOTRANSFERVAL-RXN`

## Notes

VAL + 2-KETOGLUTARATE -> 2-KETO-ISOVALERATE + GLT; direction=REVERSIBLE

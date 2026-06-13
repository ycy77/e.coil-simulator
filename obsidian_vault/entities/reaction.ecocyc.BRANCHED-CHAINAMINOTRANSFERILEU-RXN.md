---
entity_id: "reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERILEU-RXN"
entity_type: "reaction"
name: "BRANCHED-CHAINAMINOTRANSFERILEU-RXN"
source_database: "EcoCyc"
source_id: "BRANCHED-CHAINAMINOTRANSFERILEU-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Transaminase B"
---

# BRANCHED-CHAINAMINOTRANSFERILEU-RXN

`reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERILEU-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BRANCHED-CHAINAMINOTRANSFERILEU-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The final reaction in the synthesis of L-isoleucine. Also acts on L-leucine and L-valine. EcoCyc reaction equation: ILE + 2-KETOGLUTARATE -> 2-KETO-3-METHYL-VALERATE + GLT; direction=REVERSIBLE. The final reaction in the synthesis of L-isoleucine. Also acts on L-leucine and L-valine.

## Biological Role

Catalyzed by branched-chain-amino-acid aminotransferase (complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX). Substrates: 2-Oxoglutarate (molecule.C00026), L-Isoleucine (molecule.C00407). Products: L-Glutamate (molecule.C00025), (S)-3-Methyl-2-oxopentanoic acid (molecule.C00671).

## Enriched Pathways

- `ecocyc.ILEUSYN-PWY` L-isoleucine biosynthesis I (from threonine) (EcoCyc)

## Annotation

The final reaction in the synthesis of L-isoleucine. Also acts on L-leucine and L-valine.

## Pathways

- `ecocyc.ILEUSYN-PWY` L-isoleucine biosynthesis I (from threonine) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX|complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00671|molecule.C00671]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00407|molecule.C00407]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:BRANCHED-CHAINAMINOTRANSFERILEU-RXN`

## Notes

ILE + 2-KETOGLUTARATE -> 2-KETO-3-METHYL-VALERATE + GLT; direction=REVERSIBLE

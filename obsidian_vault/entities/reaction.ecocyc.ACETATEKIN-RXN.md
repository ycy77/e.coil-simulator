---
entity_id: "reaction.ecocyc.ACETATEKIN-RXN"
entity_type: "reaction"
name: "ACETATEKIN-RXN"
source_database: "EcoCyc"
source_id: "ACETATEKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Acetokinase"
---

# ACETATEKIN-RXN

`reaction.ecocyc.ACETATEKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACETATEKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Involved in the activation of acetate to acetyl-CoA and utilization of acetate. During anaerobic growth it is also involved in the generation of most of the ATP formed catabolically. Requires MG+2 for activity. While purified enzyme from Escherichia coli is specific for acetate , others have found that the enzyme can also use propanoate as a substrate, but more slowly . Acetate can be converted into the key metabolic intermediate acetyl-CoA by coupling acetate kinase with EC 2.3.1.8, phosphate acetyltransferase. Both this enzyme and EC 2.7.2.15, propionate kinase, play important roles in the production of propanoate . EcoCyc reaction equation: ACET + ATP -> ACETYL-P + ADP; direction=REVERSIBLE. Involved in the activation of acetate to acetyl-CoA and utilization of acetate. During anaerobic growth it is also involved in the generation of most of the ATP formed catabolically. Requires MG+2 for activity. While purified enzyme from Escherichia coli is specific for acetate , others have found that the enzyme can also use propanoate as a substrate, but more slowly . Acetate can be converted into the key metabolic intermediate acetyl-CoA by coupling acetate kinase with EC 2.3.1.8, phosphate acetyltransferase. Both this enzyme and EC 2.7.2.15, propionate kinase, play important roles in the production of propanoate .

## Biological Role

Catalyzed by ackA (protein.P0A6A3), purT (protein.P33221). Substrates: ATP (molecule.C00002), Acetate (molecule.C00033). Products: ADP (molecule.C00008), Acetyl phosphate (molecule.C00227).

## Enriched Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY-5485` pyruvate fermentation to acetate IV (EcoCyc)
- `ecocyc.PWY0-1312` acetate and ATP formation from acetyl-CoA I (EcoCyc)
- `ecocyc.PWY0-1477` ethanolamine utilization (EcoCyc)

## Annotation

Involved in the activation of acetate to acetyl-CoA and utilization of acetate. During anaerobic growth it is also involved in the generation of most of the ATP formed catabolically. Requires MG+2 for activity. While purified enzyme from Escherichia coli is specific for acetate , others have found that the enzyme can also use propanoate as a substrate, but more slowly . Acetate can be converted into the key metabolic intermediate acetyl-CoA by coupling acetate kinase with EC 2.3.1.8, phosphate acetyltransferase. Both this enzyme and EC 2.7.2.15, propionate kinase, play important roles in the production of propanoate .

## Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY-5485` pyruvate fermentation to acetate IV (EcoCyc)
- `ecocyc.PWY0-1312` acetate and ATP formation from acetyl-CoA I (EcoCyc)
- `ecocyc.PWY0-1477` ethanolamine utilization (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A6A3|protein.P0A6A3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P33221|protein.P33221]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00227|molecule.C00227]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ACETATEKIN-RXN`

## Notes

ACET + ATP -> ACETYL-P + ADP; direction=REVERSIBLE

---
entity_id: "reaction.ecocyc.GLURS-RXN"
entity_type: "reaction"
name: "GLURS-RXN"
source_database: "EcoCyc"
source_id: "GLURS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "GLUTAMYL-TRNA SYNTHETASE"
  - "Glutamic acid translase"
---

# GLURS-RXN

`reaction.ecocyc.GLURS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLURS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction charges tRNA(Glu) for both protein and δ-aminolevulinic acid synthesis (ALA). ALA is the first committed tetrapyrrole precursor of heme. EcoCyc reaction equation: GLT-tRNAs + GLT + ATP -> Charged-GLT-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction charges tRNA(Glu) for both protein and δ-aminolevulinic acid synthesis (ALA). ALA is the first committed tetrapyrrole precursor of heme.

## Biological Role

Catalyzed by gltX (protein.P04805). Substrates: ATP (molecule.C00002), L-Glutamate (molecule.C00025). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.PWY-5188` uroporphyrinogen-III I (from glutamate) (EcoCyc)
- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

This reaction charges tRNA(Glu) for both protein and δ-aminolevulinic acid synthesis (ALA). ALA is the first committed tetrapyrrole precursor of heme.

## Pathways

- `ecocyc.PWY-5188` uroporphyrinogen-III I (from glutamate) (EcoCyc)
- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P04805|protein.P04805]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1883|molecule.ecocyc.CPD0-1883]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1884|molecule.ecocyc.CPD0-1884]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLURS-RXN`

## Notes

GLT-tRNAs + GLT + ATP -> Charged-GLT-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

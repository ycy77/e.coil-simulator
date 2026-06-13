---
entity_id: "molecule.C02350"
entity_type: "small_molecule"
name: "(S)-Allantoin"
source_database: "KEGG"
source_id: "C02350"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(S)-Allantoin"
  - "(S)(+)-Allantoin"
---

# (S)-Allantoin

`molecule.C02350`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02350`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (S)-Allantoin; (S)(+)-Allantoin EcoCyc common name: (S)-(+)-allantoin. S-ALLANTOIN is the only enantiomer of allantoin that is formed in living cells. In vitro, racemic allantoin is formed by non-enzymatic decomposition of 5-HYDROXYISOURATE .

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: (S)-Allantoin; (S)(+)-Allantoin

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-444|reaction.ecocyc.TRANS-RXN0-444]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ALLANTOINASE-RXN|reaction.ecocyc.ALLANTOINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-444|reaction.ecocyc.TRANS-RXN0-444]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02350`

## Notes

Included because it appears in at least one E. coli KEGG pathway.

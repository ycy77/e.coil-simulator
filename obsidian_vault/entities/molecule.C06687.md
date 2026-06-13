---
entity_id: "molecule.C06687"
entity_type: "small_molecule"
name: "Norfloxacin"
source_database: "KEGG"
source_id: "C06687"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Norfloxacin"
---

# Norfloxacin

`molecule.C06687`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06687`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Norfloxacin Norfloxacin is a second-generation fluoroquinolone antibiotic used to treat urinary tract infections, gynecological infections, inflammation of the prostate gland, gonorrhea and bladder infection. Norfloxacin was patented in 1979 by the pharmaceutical arm of the Japanese company Kyorin Seiyaku Kabushiki Kaisha and approved in Japan for medical use in 1983. It was approved by the FDA in 1986. Despite the substantial increase in antibacterial activity of norfloxacin relative to early fluoroquinolones such as CPD-21025, it did not become a widely used antibiotic, as much more active derivatives such as CPD-12843 reached the market soon after its introduction.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Norfloxacin

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-347|reaction.ecocyc.TRANS-RXN-347]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-347|reaction.ecocyc.TRANS-RXN-347]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P37340|protein.P37340]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C06687`

## Notes

Included because it appears in at least one E. coli KEGG pathway.

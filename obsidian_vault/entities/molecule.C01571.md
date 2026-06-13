---
entity_id: "molecule.C01571"
entity_type: "small_molecule"
name: "Decanoic acid"
source_database: "KEGG"
source_id: "C01571"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Decanoic acid"
  - "Decanoate"
  - "Decylic acid"
  - "n-Capric acid"
---

# Decanoic acid

`molecule.C01571`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01571`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Decanoic acid; Decanoate; Decylic acid; n-Capric acid EcoCyc common name: decanoate. The fatty acid CPD-3617 is often found in the cell activated by coenzyme A as CPD-10267 or attached to acyl-carrier protein, in the form of Decanoyl-ACPs "decanoyl-[acp].

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Annotation

KEGG compound: Decanoic acid; Decanoate; Decylic acid; n-Capric acid

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-9628|reaction.ecocyc.RXN-9628]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-356|reaction.ecocyc.TRANS-RXN-356]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-356|reaction.ecocyc.TRANS-RXN-356]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.TRANS-CPLX-201|complex.ecocyc.TRANS-CPLX-201]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C01571`

## Notes

Included because it appears in at least one E. coli KEGG pathway.

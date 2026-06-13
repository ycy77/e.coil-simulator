---
entity_id: "molecule.C00334"
entity_type: "small_molecule"
name: "4-Aminobutanoate"
source_database: "KEGG"
source_id: "C00334"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "4-Aminobutanoate"
  - "4-Aminobutanoic acid"
  - "4-Aminobutyrate"
  - "4-Aminobutyric acid"
  - "gamma-Aminobutyric acid"
  - "GABA"
---

# 4-Aminobutanoate

`molecule.C00334`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00334`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 4-Aminobutanoate; 4-Aminobutanoic acid; 4-Aminobutyrate; 4-Aminobutyric acid; gamma-Aminobutyric acid; GABA γ-aminobutyrate (GABA) is a four-carbon non-protein amino acid conserved from bacteria to plants and vertebrates. GABA was originally discovered in plants in 1949 , but interest shifted to animals when it was found that GABA occurs at high levels in the brain, as a neurotransmitter. In plants and in animals, GABA is mainly metabolized via a short pathway composed of three enzymes, called the GABA shunt because it bypasses two steps of the TCA.

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

KEGG compound: 4-Aminobutanoate; 4-Aminobutanoic acid; 4-Aminobutyrate; 4-Aminobutyric acid; gamma-Aminobutyric acid; GABA

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (14)

- `is_component_of` --> [[complex.ecocyc.CPLX0-9318|complex.ecocyc.CPLX0-9318]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00261|reaction.R00261]] `KEGG` `database` - C00025 <=> C00334 + C00011
- `is_product_of` --> [[reaction.ecocyc.AMINOBUTDEHYDROG-RXN|reaction.ecocyc.AMINOBUTDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUTDECARBOX-RXN|reaction.ecocyc.GLUTDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-3942|reaction.ecocyc.RXN0-3942]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-1549|reaction.ecocyc.TRANS-RXN-1549]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-261|reaction.ecocyc.TRANS-RXN-261]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-57|reaction.ecocyc.TRANS-RXN-57]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GABATRANSAM-RXN|reaction.ecocyc.GABATRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-24786|reaction.ecocyc.RXN-24786]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7412|reaction.ecocyc.RXN0-7412]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-1549|reaction.ecocyc.TRANS-RXN-1549]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-261|reaction.ecocyc.TRANS-RXN-261]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-57|reaction.ecocyc.TRANS-RXN-57]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (2)

- `transports` <-- [[protein.P25527|protein.P25527]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P63235|protein.P63235]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00334`

## Notes

Included because it appears in at least one E. coli KEGG pathway.

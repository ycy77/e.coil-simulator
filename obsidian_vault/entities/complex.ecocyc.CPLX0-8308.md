---
entity_id: "complex.ecocyc.CPLX0-8308"
entity_type: "complex"
name: "2-(all-trans-polyprenyl)phenol 6-hydroxylase (prephenate)"
source_database: "EcoCyc"
source_id: "CPLX0-8308"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ubiquinone hydroxylase UbiUV"
---

# 2-(all-trans-polyprenyl)phenol 6-hydroxylase (prephenate)

`complex.ecocyc.CPLX0-8308`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8308`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P45475|protein.P45475]], [[protein.P45527|protein.P45527]]

## Enriched Summary

UbiU and UbiV form a heterodimer that functions in the three hydroxylation reactions in the oxygen-independent pathway for ubiquinone (UQ) biosynthesis. Deletion of either gene result in mutants that are deficient in ubiquinone-8 biosynthesis under anaerobic growth conditions . UbiUV-dependent UQ synthesis is essential for nitrate respiration and uracil biosynthesis under anaerobiosis . The source of oxygen for the hydroxylation reaction was found to be PREPHENATE. The reaction involves an electron acceptor whose identity remains unknown as of 2024. Both UbiV and UbiU contain a 4Fe-4S iron-sulfur cluster that is essential for activity and may serve as part of an electron transfer chain from the substrate to the unidentified electron acceptor . UbiU and UbiV form a heterodimer that functions in the three hydroxylation reactions in the oxygen-independent pathway for ubiquinone (UQ) biosynthesis. Deletion of either gene result in mutants that are deficient in ubiquinone-8 biosynthesis under anaerobic growth conditions . UbiUV-dependent UQ synthesis is essential for nitrate respiration and uracil biosynthesis under anaerobiosis . The source of oxygen for the hydroxylation reaction was found to be PREPHENATE. The reaction involves an electron acceptor whose identity remains unknown as of 2024...

## Biological Role

Catalyzes RXN-24716 (reaction.ecocyc.RXN-24716), RXN-24717 (reaction.ecocyc.RXN-24717), RXN-24718 (reaction.ecocyc.RXN-24718), RXN-24918 (reaction.ecocyc.RXN-24918). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

UbiU and UbiV form a heterodimer that functions in the three hydroxylation reactions in the oxygen-independent pathway for ubiquinone (UQ) biosynthesis. Deletion of either gene result in mutants that are deficient in ubiquinone-8 biosynthesis under anaerobic growth conditions . UbiUV-dependent UQ synthesis is essential for nitrate respiration and uracil biosynthesis under anaerobiosis . The source of oxygen for the hydroxylation reaction was found to be PREPHENATE. The reaction involves an electron acceptor whose identity remains unknown as of 2024. Both UbiV and UbiU contain a 4Fe-4S iron-sulfur cluster that is essential for activity and may serve as part of an electron transfer chain from the substrate to the unidentified electron acceptor .

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.RXN-24716|reaction.ecocyc.RXN-24716]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24717|reaction.ecocyc.RXN-24717]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24718|reaction.ecocyc.RXN-24718]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24918|reaction.ecocyc.RXN-24918]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P45475|protein.P45475]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P45527|protein.P45527]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-8308`
- `QSPROTEOME:QS00196145`

## Notes

1*protein.P45475|1*protein.P45527

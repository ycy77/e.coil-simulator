---
entity_id: "complex.ecocyc.CPLX0-7848"
entity_type: "complex"
name: "L-ascorbate-6-phosphate lactonase"
source_database: "EcoCyc"
source_id: "CPLX0-7848"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-ascorbate-6-phosphate lactonase

`complex.ecocyc.CPLX0-7848`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7848`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P39300|protein.P39300]]

## Enriched Summary

UlaG is required for the ability to utilize L-ascorbate as the sole carbon source under anaerobic growth conditions. The enzyme was suggested to be a cytoplasmic L-ascorbate 6-phosphate lactonase , and its catalytic activity has recently been shown . Phosphodiesterase activity of UlaG was discovered in a high-throughput screen of purified proteins . Crystal structures of the UlaG apoenzyme and the Mn2+-bound holoenzyme have been solved at 2.6 Å resolution . Phylogenetic analysis of the UlaG-like protein family indicates that it has a common evolutionary origin with RNA processing and metabolizing metallo-β-lactamases . Expression of ulaG is negatively regulated by UlaR . UlaG is required for the ability to utilize L-ascorbate as the sole carbon source under anaerobic growth conditions. The enzyme was suggested to be a cytoplasmic L-ascorbate 6-phosphate lactonase , and its catalytic activity has recently been shown . Phosphodiesterase activity of UlaG was discovered in a high-throughput screen of purified proteins . Crystal structures of the UlaG apoenzyme and the Mn2+-bound holoenzyme have been solved at 2.6 Å resolution . Phylogenetic analysis of the UlaG-like protein family indicates that it has a common evolutionary origin with RNA processing and metabolizing metallo-β-lactamases . Expression of ulaG is negatively regulated by UlaR .

## Biological Role

Catalyzes RXN0-5214 (reaction.ecocyc.RXN0-5214). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

UlaG is required for the ability to utilize L-ascorbate as the sole carbon source under anaerobic growth conditions. The enzyme was suggested to be a cytoplasmic L-ascorbate 6-phosphate lactonase , and its catalytic activity has recently been shown . Phosphodiesterase activity of UlaG was discovered in a high-throughput screen of purified proteins . Crystal structures of the UlaG apoenzyme and the Mn2+-bound holoenzyme have been solved at 2.6 Å resolution . Phylogenetic analysis of the UlaG-like protein family indicates that it has a common evolutionary origin with RNA processing and metabolizing metallo-β-lactamases . Expression of ulaG is negatively regulated by UlaR .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5214|reaction.ecocyc.RXN0-5214]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P39300|protein.P39300]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-7848`
- `QSPROTEOME:QS00195607`

## Notes

6*protein.P39300

---
entity_id: "protein.P18843"
entity_type: "protein"
name: "nadE"
source_database: "UniProt"
source_id: "P18843"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nadE efg ntrL b1740 JW1729"
---

# nadE

`protein.P18843`

## Static

- Type: `protein`
- Source: `UniProt:P18843`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent amidation of deamido-NAD to form NAD. Uses ammonia as a nitrogen source. {ECO:0000255|HAMAP-Rule:MF_00193, ECO:0000269|PubMed:8195100}. NAD+ synthetase is an essential enzyme involved in both the de novo biosynthesis and salvage of NAD+, catalyzing the final step of both pathways. The enzyme shows a strong preference for ammonia over glutamine as the amino group donor and may even have no glutamine-dependent NAD+ synthetase activity at all . The enzyme contains a P-loop-like pyrophosphatase motif . Crystal structures of the enzyme alone and in complex with substrates and the reaction product NAD+ have been solved. The catalytic cycle appears to involve significant structural reorganization . nadE is essential for growth . In the presence of a heterologous NAD+ transporter, a ΔnadE mutant is able to grow with externally supplied NAD+ . Expression of nadE is posttranscriptionally regulated by the small RNA CyaR . Efg: "essential for growth" NadE: "NAD biosynthesis E" Reviews:

## Biological Role

Catalyzes deamido-NAD+:ammonia ligase (AMP-forming) (reaction.R00189). Component of NH3-dependent NAD+ synthetase (complex.ecocyc.NAD-SYNTH-CPLX).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the ATP-dependent amidation of deamido-NAD to form NAD. Uses ammonia as a nitrogen source. {ECO:0000255|HAMAP-Rule:MF_00193, ECO:0000269|PubMed:8195100}.

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00189|reaction.R00189]] `KEGG` `database` - via EC:6.3.1.5
- `is_component_of` --> [[complex.ecocyc.NAD-SYNTH-CPLX|complex.ecocyc.NAD-SYNTH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1740|gene.b1740]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P18843`
- `KEGG:ecj:JW1729;eco:b1740;ecoc:C3026_09940;`
- `GeneID:946946;`
- `GO:GO:0000287; GO:0003952; GO:0004359; GO:0005524; GO:0005829; GO:0006974; GO:0008795; GO:0034355; GO:0034628; GO:0042803`
- `EC:6.3.1.5`

## Notes

NH(3)-dependent NAD(+) synthetase (EC 6.3.1.5) (Nicotinamide adenine dinucleotide synthetase) (NADS) (Nitrogen regulatory protein)

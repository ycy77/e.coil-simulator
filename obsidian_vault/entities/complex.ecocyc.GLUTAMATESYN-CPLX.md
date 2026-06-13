---
entity_id: "complex.ecocyc.GLUTAMATESYN-CPLX"
entity_type: "complex"
name: "glutamate synthase"
source_database: "EcoCyc"
source_id: "GLUTAMATESYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "NADPH-GOGAT"
---

# glutamate synthase

`complex.ecocyc.GLUTAMATESYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLUTAMATESYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.GLUTAMATESYN-DIMER|complex.ecocyc.GLUTAMATESYN-DIMER]]

## Enriched Summary

Glutamate synthase catalyzes the single-step conversion of L-glutamine and alpha-ketoglutarate into two molecules of L-glutamate. In doing so, it simultaneously operates as the major source of L-glutamate for the cell and as a key step in ammonia assimilation during nitrogen-limited growth. Glutamate synthase catalyzes the production of L-glutamate from L-glutamine and alpha-ketoglutarate . In addition to L-glutamine, glutamate synthase can also use ammonia as a nitrogen source for the generation of L-glutamate from alpha-ketoglutarate. The ammonia-dependent reaction does not require flavin or iron like the L-glutamine-dependent reaction, but is also much slower than that reaction, with about 5-7% of its activity . Both the L-glutamine- and ammonia-dependent reactions are reversible, at about 10% of the rate of the forward reaction . Despite this similarity, the two reactions appear to occur by different mechanisms. In the L-glutamine-dependent reaction, the NADPH reduces the enzyme itself, most likely at the flavin cofactor, and then the enzyme is oxidized again during the reaction of L-glutamine and alpha-ketoglutarate to yield two L-glutamates. In this mode, hydrogen from NADPH ends up as a component of water...

## Biological Role

Catalyzes GLUTAMATESYN-RXN (reaction.ecocyc.GLUTAMATESYN-RXN), GLUTDEHYD-RXN (reaction.ecocyc.GLUTDEHYD-RXN). Bound by FAD (molecule.C00016), an iron-sulfur cluster (molecule.ecocyc.FeS-Centers).

## Annotation

Glutamate synthase catalyzes the single-step conversion of L-glutamine and alpha-ketoglutarate into two molecules of L-glutamate. In doing so, it simultaneously operates as the major source of L-glutamate for the cell and as a key step in ammonia assimilation during nitrogen-limited growth. Glutamate synthase catalyzes the production of L-glutamate from L-glutamine and alpha-ketoglutarate . In addition to L-glutamine, glutamate synthase can also use ammonia as a nitrogen source for the generation of L-glutamate from alpha-ketoglutarate. The ammonia-dependent reaction does not require flavin or iron like the L-glutamine-dependent reaction, but is also much slower than that reaction, with about 5-7% of its activity . Both the L-glutamine- and ammonia-dependent reactions are reversible, at about 10% of the rate of the forward reaction . Despite this similarity, the two reactions appear to occur by different mechanisms. In the L-glutamine-dependent reaction, the NADPH reduces the enzyme itself, most likely at the flavin cofactor, and then the enzyme is oxidized again during the reaction of L-glutamine and alpha-ketoglutarate to yield two L-glutamates. In this mode, hydrogen from NADPH ends up as a component of water. In the ammonia-dependent reaction, the enzyme is neither reduced nor oxidized, and hydrogen from NADPH ends up in the single L-glutamate that is produced from alpha-ketoglutarate . Glutamate synthase is a tetramer of dimers, with each dimer having one large and one small subunit (GltB and GltD, respectively) . The ammonia-dependent activity can be catalyzed very slowly by just the small subunit in the absence of the full complex . Ligand-binding interactions with glutamate synthase have been examined . The gltBDF operon that codes for both components of glutama

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GLUTAMATESYN-RXN|reaction.ecocyc.GLUTAMATESYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GLUTDEHYD-RXN|reaction.ecocyc.GLUTDEHYD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.FeS-Centers|molecule.ecocyc.FeS-Centers]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.GLUTAMATESYN-DIMER|complex.ecocyc.GLUTAMATESYN-DIMER]] `EcoCyc` `database` - EcoCyc component coefficient=4
- `is_component_of` <-- [[protein.P09831|protein.P09831]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4
- `is_component_of` <-- [[protein.P09832|protein.P09832]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:GLUTAMATESYN-CPLX`

## Notes

4*complex.ecocyc.GLUTAMATESYN-DIMER

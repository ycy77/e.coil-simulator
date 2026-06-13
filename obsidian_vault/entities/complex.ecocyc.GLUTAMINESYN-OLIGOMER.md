---
entity_id: "complex.ecocyc.GLUTAMINESYN-OLIGOMER"
entity_type: "complex"
name: "glutamine synthetase"
source_database: "EcoCyc"
source_id: "GLUTAMINESYN-OLIGOMER"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutamine synthetase

`complex.ecocyc.GLUTAMINESYN-OLIGOMER`

## Static

- Type: `complex`
- Source: `EcoCyc:GLUTAMINESYN-OLIGOMER`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A9C5|protein.P0A9C5]]

## Enriched Summary

Glutamine synthetase catalyzes the lone reaction in the glutamine biosynthesis pathway, combining L-glutamate and ammonia to generate L-glutamine. The enzyme is a 12-mer of identical subunits arranged as two doughnuts, each composed of six monomers . The reaction mechanism of glutamine synthetase has been the subject of many studies. Kinetic analyses suggest that following random substrate binding, the generation of glutamine proceeds by a two-step mechanism. In the first step the enzyme uses ATP to phosphorylate L-glutanate, forming L-GLUTAMATE-5-P, which remains bound to the active site. In the second step ammonia binds and reacts with L-GLUTAMATE-5-P to yield glutamine, which is released from the active site . Glutamate binding appears to occur at a lysine, and is partially antagonized by ATP binding . It has been observed that in a EG10768 mutant, which is blocked in L-proline biosynthesis, many single mutations occurred in EG10383 that resulted in leaking of L-GLUTAMATE-5-P into the intracellular milieu, enabling proline biosynthesis . Molecular basis of GlnA inhibition by phosphorylated molecules and amino acids. Regulation of this enzyme's activity has been clarified by structural studies. Kinetic analyses had suggested that a number of small molecules (e.g. individual amino acids, a sugar amine, nucleotides) bind to the enzyme from a wide range of organisms including E...

## Biological Role

Catalyzes GLUTAMINESYN-RXN (reaction.ecocyc.GLUTAMINESYN-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

Glutamine synthetase catalyzes the lone reaction in the glutamine biosynthesis pathway, combining L-glutamate and ammonia to generate L-glutamine. The enzyme is a 12-mer of identical subunits arranged as two doughnuts, each composed of six monomers . The reaction mechanism of glutamine synthetase has been the subject of many studies. Kinetic analyses suggest that following random substrate binding, the generation of glutamine proceeds by a two-step mechanism. In the first step the enzyme uses ATP to phosphorylate L-glutanate, forming L-GLUTAMATE-5-P, which remains bound to the active site. In the second step ammonia binds and reacts with L-GLUTAMATE-5-P to yield glutamine, which is released from the active site . Glutamate binding appears to occur at a lysine, and is partially antagonized by ATP binding . It has been observed that in a EG10768 mutant, which is blocked in L-proline biosynthesis, many single mutations occurred in EG10383 that resulted in leaking of L-GLUTAMATE-5-P into the intracellular milieu, enabling proline biosynthesis . Molecular basis of GlnA inhibition by phosphorylated molecules and amino acids. Regulation of this enzyme's activity has been clarified by structural studies. Kinetic analyses had suggested that a number of small molecules (e.g. individual amino acids, a sugar amine, nucleotides) bind to the enzyme from a wide range of organisms including E. coli and cumulatively cause feedback inhibition through action at a site distinct from that of the two substrates. X-ray crystallographic analyses of this enzyme complexed with L-alanine, L-serine, glycine, GDP, ADP and AMP have been performed and indicate that the amino acids all bind to the glutamate substrate site and that the nucleotides all bind to the ATP site. This, combined with the lack

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUTAMINESYN-RXN|reaction.ecocyc.GLUTAMINESYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A9C5|protein.P0A9C5]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12

## External IDs

- `EcoCyc:GLUTAMINESYN-OLIGOMER`

## Notes

12*protein.P0A9C5

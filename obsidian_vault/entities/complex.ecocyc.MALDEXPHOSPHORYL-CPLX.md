---
entity_id: "complex.ecocyc.MALDEXPHOSPHORYL-CPLX"
entity_type: "complex"
name: "maltodextrin phosphorylase"
source_database: "EcoCyc"
source_id: "MALDEXPHOSPHORYL-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# maltodextrin phosphorylase

`complex.ecocyc.MALDEXPHOSPHORYL-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:MALDEXPHOSPHORYL-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00490|protein.P00490]]

## Enriched Summary

Maltodextrin phosphorylase (MalP) is one of two distinct α-glucan phosphorylases in E. coli. While GLYCOPHOSPHORYL-CPLX (GlgP) acts directly on glycogen, MalP has high affinity for short, linear α-1,4 linked oligoglucosides and thus appears to act on soluble maltooligosaccharides . Experiments with the purified enzyme showed that the shortest maltodextrin which can be readily phosphorylyzed is maltopentaose, while the minimum length of the substrate for elongation of the oligosaccharide chain is maltotetraose . However, analysis of the maltodextrin degradation products in a malQ malZ mutant strain showed the production of maltotriose, implying that maltotetraose is a substrate of maltodextrin phosphorylase . The reaction mechanism and involvement of PLP in catalysis has been studied . Site-directed mutagenesis of active-site residues and their effect on catalytic activity and kinetic properties of the enzyme has been reported . Kinetic studies of the forward (phosphorylase) and reverse (synthesis) reactions indicated that the enzyme has different binding sites for the terminal glucose residue of the oligoglucoside and glucose-1-phosphate...

## Biological Role

Catalyzes RXN-14284 (reaction.ecocyc.RXN-14284), RXN-14285 (reaction.ecocyc.RXN-14285), RXN-14286 (reaction.ecocyc.RXN-14286), RXN-21092 (reaction.ecocyc.RXN-21092), RXN0-5182 (reaction.ecocyc.RXN0-5182). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Maltodextrin phosphorylase (MalP) is one of two distinct α-glucan phosphorylases in E. coli. While GLYCOPHOSPHORYL-CPLX (GlgP) acts directly on glycogen, MalP has high affinity for short, linear α-1,4 linked oligoglucosides and thus appears to act on soluble maltooligosaccharides . Experiments with the purified enzyme showed that the shortest maltodextrin which can be readily phosphorylyzed is maltopentaose, while the minimum length of the substrate for elongation of the oligosaccharide chain is maltotetraose . However, analysis of the maltodextrin degradation products in a malQ malZ mutant strain showed the production of maltotriose, implying that maltotetraose is a substrate of maltodextrin phosphorylase . The reaction mechanism and involvement of PLP in catalysis has been studied . Site-directed mutagenesis of active-site residues and their effect on catalytic activity and kinetic properties of the enzyme has been reported . Kinetic studies of the forward (phosphorylase) and reverse (synthesis) reactions indicated that the enzyme has different binding sites for the terminal glucose residue of the oligoglucoside and glucose-1-phosphate . Various crystal structures of maltodextrin phosphorylase have been solved, providing insight into the lack of allosteric control of the enzyme, substrate specificity and the catalytic mechanism, and supporting results from site-directed mutagenesis experiments . A malP mutant grown on maltose or maltodextrin contains increased levels of glycogen . The structure and side chain distribution of the glycogen-like polysaccharides produced by a glgA malP double mutant have been analyzed . Reviews:

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.RXN-14284|reaction.ecocyc.RXN-14284]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14285|reaction.ecocyc.RXN-14285]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14286|reaction.ecocyc.RXN-14286]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-21092|reaction.ecocyc.RXN-21092]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5182|reaction.ecocyc.RXN0-5182]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00490|protein.P00490]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:MALDEXPHOSPHORYL-CPLX`
- `QSPROTEOME:QS00181523`

## Notes

2*protein.P00490

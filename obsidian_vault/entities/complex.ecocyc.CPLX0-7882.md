---
entity_id: "complex.ecocyc.CPLX0-7882"
entity_type: "complex"
name: "1,4-dihydroxy-2-naphthoyl-CoA synthase"
source_database: "EcoCyc"
source_id: "CPLX0-7882"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 1,4-dihydroxy-2-naphthoyl-CoA synthase

`complex.ecocyc.CPLX0-7882`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7882`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ABU0|protein.P0ABU0]]

## Enriched Summary

1,4-Dihydroxy-2-naphthoyl-CoA synthase catalyzes a major step in menaquinone biosynthesis, formation of the bicyclic ring system by an intramolecular Claisen condensation . The enzyme requires a bound bicarbonate ion for full activity, and the crystal structure of the Salmonella enterica ortholog contains a bicarbonate ion. Both the S. enterica and the E. coli enzymes contain a glycine residue in the position corresponding to the essential active site Asp185 residue of the Mycobacterium tuberculosis enzyme, and the bicarbonate ion is found close to this Gly156 residue. Site-directed mutagenesis showed that Gly156 is essential for catalytic activity . Asp163 interacts with the C1 hydroxyl group of DHNA-CoA; a D163A mutation abolishes activity as well as ligand binding . A Y97F mutant lacks catalytic activity . Reaction mechanisms have been proposed . A crystal structure of MenB with bound O-succinylbenzoyl-aminoCoA (OSB-NCoA), a stable substrate analog, has been solved at 2 Å resolution. The structure reveals the position of all active site residues and supports a mechanism involving the direct participation of the two conserved Tyr residues Y97 and Y258 in the intramolecular transfer of the substrate proton to the benzylic carboxylate of the substrate...

## Biological Role

Catalyzes NAPHTHOATE-SYN-RXN (reaction.ecocyc.NAPHTHOATE-SYN-RXN). Bound by HCO3- (molecule.C00288).

## Annotation

1,4-Dihydroxy-2-naphthoyl-CoA synthase catalyzes a major step in menaquinone biosynthesis, formation of the bicyclic ring system by an intramolecular Claisen condensation . The enzyme requires a bound bicarbonate ion for full activity, and the crystal structure of the Salmonella enterica ortholog contains a bicarbonate ion. Both the S. enterica and the E. coli enzymes contain a glycine residue in the position corresponding to the essential active site Asp185 residue of the Mycobacterium tuberculosis enzyme, and the bicarbonate ion is found close to this Gly156 residue. Site-directed mutagenesis showed that Gly156 is essential for catalytic activity . Asp163 interacts with the C1 hydroxyl group of DHNA-CoA; a D163A mutation abolishes activity as well as ligand binding . A Y97F mutant lacks catalytic activity . Reaction mechanisms have been proposed . A crystal structure of MenB with bound O-succinylbenzoyl-aminoCoA (OSB-NCoA), a stable substrate analog, has been solved at 2 Å resolution. The structure reveals the position of all active site residues and supports a mechanism involving the direct participation of the two conserved Tyr residues Y97 and Y258 in the intramolecular transfer of the substrate proton to the benzylic carboxylate of the substrate .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.NAPHTHOATE-SYN-RXN|reaction.ecocyc.NAPHTHOATE-SYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0ABU0|protein.P0ABU0]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-7882`
- `QSPROTEOME:QS00181729`

## Notes

6*protein.P0ABU0

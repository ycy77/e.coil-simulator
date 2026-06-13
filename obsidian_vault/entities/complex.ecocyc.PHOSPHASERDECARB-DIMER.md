---
entity_id: "complex.ecocyc.PHOSPHASERDECARB-DIMER"
entity_type: "complex"
name: "phosphatidylserine decarboxylase"
source_database: "EcoCyc"
source_id: "PHOSPHASERDECARB-DIMER"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# phosphatidylserine decarboxylase

`complex.ecocyc.PHOSPHASERDECARB-DIMER`

## Static

- Type: `complex`
- Source: `EcoCyc:PHOSPHASERDECARB-DIMER`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A8K1|protein.P0A8K1]], [[protein.P0A8K1|protein.P0A8K1]]

## Enriched Summary

Phosphatidylserine decarboxylase catalyzes the formation of phosphatidylethanolamine, the most abundant phospholipid in E. coli membranes. Phosphatidylserine decarboxylase is one of a small class of enzymes that use a covalently bound pyruvoyl prosthetic group. The pyruvoyl group is thought to act analogously to pyridoxal phosphate cofactor by forming a Schiff base between its carbonyl residue and the amino group of the substrate and then serving as an electron sink to facilitate the decarboxylation. The pyruvoyl group is essential for catalytic activity and can be inactivated by carbonyl reagents . E. coli encodes two more members of this class of enzymes, CPLX0-2901 and SAMDECARB-CPLX. Pyruvoyl-containing enzymes are expressed as proenzymes, so-called "zymogens", which undergo a post-translational self-maturation/cleavage called serinolysis . In phosphatidylserine decarboxylase, the hydroxyl group of the Ser254 residue is essential for the cleavage of the peptide bond between Gly253 and Ser254, and for subsequent conversion of Ser254 into the pyruvoyl prosthetic group at the amino terminus of the α subunit . Asp90, Asp142 and His144 also play a role in the auto-cleavage reaction . Crystal structures of the apo- and phosphatidylethanolamine-bound C-terminally truncated enzyme have been solved . Psd froms a homodimer from two α/β monomers...

## Biological Role

Catalyzes PHOSPHASERDECARB-RXN (reaction.ecocyc.PHOSPHASERDECARB-RXN). Bound by a pyruvoyl cofactor (molecule.ecocyc.CPD0-2654).

## Annotation

Phosphatidylserine decarboxylase catalyzes the formation of phosphatidylethanolamine, the most abundant phospholipid in E. coli membranes. Phosphatidylserine decarboxylase is one of a small class of enzymes that use a covalently bound pyruvoyl prosthetic group. The pyruvoyl group is thought to act analogously to pyridoxal phosphate cofactor by forming a Schiff base between its carbonyl residue and the amino group of the substrate and then serving as an electron sink to facilitate the decarboxylation. The pyruvoyl group is essential for catalytic activity and can be inactivated by carbonyl reagents . E. coli encodes two more members of this class of enzymes, CPLX0-2901 and SAMDECARB-CPLX. Pyruvoyl-containing enzymes are expressed as proenzymes, so-called "zymogens", which undergo a post-translational self-maturation/cleavage called serinolysis . In phosphatidylserine decarboxylase, the hydroxyl group of the Ser254 residue is essential for the cleavage of the peptide bond between Gly253 and Ser254, and for subsequent conversion of Ser254 into the pyruvoyl prosthetic group at the amino terminus of the α subunit . Asp90, Asp142 and His144 also play a role in the auto-cleavage reaction . Crystal structures of the apo- and phosphatidylethanolamine-bound C-terminally truncated enzyme have been solved . Psd froms a homodimer from two α/β monomers. A hydrophobic N-terminal helical region within the β chain forms a positively charged pocket surrounding the active site . Higher-resolution structures allowed the identification of interaction sites with the diacyl chains of the phospholipid molecule . Site-directed mutagenesis of conserved residues within the active site pocket showed that Tyr137 and His144 are involved in catalysis ; the second and third N-terminal helices are requ

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PHOSPHASERDECARB-RXN|reaction.ecocyc.PHOSPHASERDECARB-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD0-2654|molecule.ecocyc.CPD0-2654]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A8K1|protein.P0A8K1]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PHOSPHASERDECARB-DIMER`

## Notes

2*protein.P0A8K1|2*protein.P0A8K1

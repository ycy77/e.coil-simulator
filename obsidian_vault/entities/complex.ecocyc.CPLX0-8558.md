---
entity_id: "complex.ecocyc.CPLX0-8558"
entity_type: "complex"
name: "sulfur carrier protein ThiS adenylyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-8558"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sulfur carrier protein ThiS adenylyltransferase

`complex.ecocyc.CPLX0-8558`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8558`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P30138|protein.P30138]]

## Enriched Summary

ThiF participates in the synthesis of the thiazole moiety of thiamine, catalyzing the transfer of an adenyl group to the C-terminal glycine of THIS-MONOMER ThiS . Crystal structures of ThiF alone and in complex with ATP have been solved. ThiF forms a homodimer, and a crossover loop (which contains the C184 residue) links the two subdomains of each monomer. Both monomers contribute to each ATP binding site . The crystal structure of the ThiS-ThiF protein complex shows a dimer of heterodimers, where the dimer interface is provided by ThiF. The ThiS C-terminus is located near the active site, distant from the C184 residue of ThiF . A covalently linked protein-protein conjugate between C184 of ThiF and the C-terminal glycine of ThiS was identified; the C184 residue is essential for ThiF function, but not for the thiocarboxylate modification of ThiS . A thiF mutant requires thiazole for growth . The C184S mutant of thiF does not complement the thiazole auxotrophy of the mutant . Reviews: ThiF participates in the synthesis of the thiazole moiety of thiamine, catalyzing the transfer of an adenyl group to the C-terminal glycine of THIS-MONOMER ThiS . Crystal structures of ThiF alone and in complex with ATP have been solved. ThiF forms a homodimer, and a crossover loop (which contains the C184 residue) links the two subdomains of each monomer...

## Biological Role

Catalyzes RXN-9789 (reaction.ecocyc.RXN-9789). Bound by Magnesium cation (molecule.C00305).

## Annotation

ThiF participates in the synthesis of the thiazole moiety of thiamine, catalyzing the transfer of an adenyl group to the C-terminal glycine of THIS-MONOMER ThiS . Crystal structures of ThiF alone and in complex with ATP have been solved. ThiF forms a homodimer, and a crossover loop (which contains the C184 residue) links the two subdomains of each monomer. Both monomers contribute to each ATP binding site . The crystal structure of the ThiS-ThiF protein complex shows a dimer of heterodimers, where the dimer interface is provided by ThiF. The ThiS C-terminus is located near the active site, distant from the C184 residue of ThiF . A covalently linked protein-protein conjugate between C184 of ThiF and the C-terminal glycine of ThiS was identified; the C184 residue is essential for ThiF function, but not for the thiocarboxylate modification of ThiS . A thiF mutant requires thiazole for growth . The C184S mutant of thiF does not complement the thiazole auxotrophy of the mutant . Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-9789|reaction.ecocyc.RXN-9789]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P30138|protein.P30138]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8558`
- `QSPROTEOME:QS00198601`

## Notes

2*protein.P30138

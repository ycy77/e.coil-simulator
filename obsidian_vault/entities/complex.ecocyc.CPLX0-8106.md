---
entity_id: "complex.ecocyc.CPLX0-8106"
entity_type: "complex"
name: "nucleoside triphosphate pyrophosphatase YhdE"
source_database: "EcoCyc"
source_id: "CPLX0-8106"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# nucleoside triphosphate pyrophosphatase YhdE

`complex.ecocyc.CPLX0-8106`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8106`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P25536|protein.P25536]]

## Enriched Summary

YhdE is a nucleoside triphosphate pyrophosphatase that preferentially hydrolyzes UTP, dTTP, and the naturally occurring modified nucleotides 5-methyl-UTP (m5UTP), 5-methyl-CTP (m5CTP) and pseudo-UTP (Ψ). The authors suggest tat the in vivo function of YhdE may be to monitor the ribonucleotide pool and prevent unspecific incorporation of modified bases into cellular RNAs . YhdE exists as a mixture of dimers and tetramers in solution . Crystal structures with open or closed conformations of the active site have been solved . Molecular dynamics simulations and free energy calculations suggest that the open state favors dTTP binding, while the closed state favors catalysis. Cooperativity is induced by dimerization and dTTP binding, involving a direct allosteric communication network . Nucleotide hydrolysis appears to follow a two-step pathway, with a water molecule attacking the α P-O bond of the substrate, followed by the release of pyrophosphate . A nucleotide binding loop was identified by combined sequence and structural alignment with other enzymes of the Maf/HAM1 superfamily and confirmed by kinetic analysis of mutant enzymes . Mutations in predicted active site residues reduce the catalytic activity. The unprotonated Asp70 residue is proposed to function as a general base that produces a nucleophilic hydroxide ion which attacks the α-phosphate of the substrate...

## Biological Role

Catalyzes RXN-14139 (reaction.ecocyc.RXN-14139), RXN0-5107 (reaction.ecocyc.RXN0-5107). Bound by Magnesium cation (molecule.C00305).

## Annotation

YhdE is a nucleoside triphosphate pyrophosphatase that preferentially hydrolyzes UTP, dTTP, and the naturally occurring modified nucleotides 5-methyl-UTP (m5UTP), 5-methyl-CTP (m5CTP) and pseudo-UTP (Ψ). The authors suggest tat the in vivo function of YhdE may be to monitor the ribonucleotide pool and prevent unspecific incorporation of modified bases into cellular RNAs . YhdE exists as a mixture of dimers and tetramers in solution . Crystal structures with open or closed conformations of the active site have been solved . Molecular dynamics simulations and free energy calculations suggest that the open state favors dTTP binding, while the closed state favors catalysis. Cooperativity is induced by dimerization and dTTP binding, involving a direct allosteric communication network . Nucleotide hydrolysis appears to follow a two-step pathway, with a water molecule attacking the α P-O bond of the substrate, followed by the release of pyrophosphate . A nucleotide binding loop was identified by combined sequence and structural alignment with other enzymes of the Maf/HAM1 superfamily and confirmed by kinetic analysis of mutant enzymes . Mutations in predicted active site residues reduce the catalytic activity. The unprotonated Asp70 residue is proposed to function as a general base that produces a nucleophilic hydroxide ion which attacks the α-phosphate of the substrate . An E33A mutant has very low catalytic activity . Overexpression of YhdE increases the intracellular concentration of dTMP and UMP . A yhdE null mutant shows increased growth especially under very high salt concentrations. Cells appear to be shorter and rounder than wild type . ΔyhdE shows aggravating genetic interactions with a set of DNA recombination genes .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-14139|reaction.ecocyc.RXN-14139]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5107|reaction.ecocyc.RXN0-5107]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P25536|protein.P25536]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8106`
- `QSPROTEOME:QS00196911`

## Notes

2*protein.P25536

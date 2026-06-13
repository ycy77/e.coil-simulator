---
entity_id: "complex.ecocyc.CPLX-7524"
entity_type: "complex"
name: "allantoate amidohydrolase"
source_database: "EcoCyc"
source_id: "CPLX-7524"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# allantoate amidohydrolase

`complex.ecocyc.CPLX-7524`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-7524`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77425|protein.P77425]]

## Enriched Summary

E. coli is able to utilize allantoin as a sole nitrogen source under anaerobic conditions . Following S-ALLANTOIN ring opening, allantoate amidohydrolase converts ALLANTOATE to CPD0-2298, liberating one molecule each of AMMONIA and CARBON-DIOXIDE . Before the identification of G6284-MONOMER, allantoate amidohydrolase was thought to catalyze both hydrolysis reactions of the allantoin degradation pathway, generating CPD-1091 directly . The crystal structure of allantoate amidohydrolase has been solved at 2.25 Å resolution. It exists as a homodimer in solution and the crystal, with each polypeptide chain folded into two domains - a large catalytic domain containing two metal ions, sulfate, and substrate binding sites, and a smaller dimerization domain. Due to the overall similarity of the protein to the di-zinc-dependent metallopeptidases, the metal ions were thought to be zinc. The sulfate ion may be an allosteric effector. A reaction mechanism was proposed . A crystal structure of the catalytically inactive E126A mutant in complex with allantoate shows a large movement of the catalytic domain into a closed conformation . Allantoate amidohydrolase activity is induced by growth on allantoin as the sole source of nitrogen . E. coli is able to utilize allantoin as a sole nitrogen source under anaerobic conditions...

## Biological Role

Catalyzes ALLANTOATE-DEIMINASE-RXN (reaction.ecocyc.ALLANTOATE-DEIMINASE-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

E. coli is able to utilize allantoin as a sole nitrogen source under anaerobic conditions . Following S-ALLANTOIN ring opening, allantoate amidohydrolase converts ALLANTOATE to CPD0-2298, liberating one molecule each of AMMONIA and CARBON-DIOXIDE . Before the identification of G6284-MONOMER, allantoate amidohydrolase was thought to catalyze both hydrolysis reactions of the allantoin degradation pathway, generating CPD-1091 directly . The crystal structure of allantoate amidohydrolase has been solved at 2.25 Å resolution. It exists as a homodimer in solution and the crystal, with each polypeptide chain folded into two domains - a large catalytic domain containing two metal ions, sulfate, and substrate binding sites, and a smaller dimerization domain. Due to the overall similarity of the protein to the di-zinc-dependent metallopeptidases, the metal ions were thought to be zinc. The sulfate ion may be an allosteric effector. A reaction mechanism was proposed . A crystal structure of the catalytically inactive E126A mutant in complex with allantoate shows a large movement of the catalytic domain into a closed conformation . Allantoate amidohydrolase activity is induced by growth on allantoin as the sole source of nitrogen .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ALLANTOATE-DEIMINASE-RXN|reaction.ecocyc.ALLANTOATE-DEIMINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P77425|protein.P77425]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX-7524`
- `QSPROTEOME:QS00183063`

## Notes

2*protein.P77425

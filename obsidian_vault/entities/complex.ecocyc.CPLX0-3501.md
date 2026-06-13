---
entity_id: "complex.ecocyc.CPLX0-3501"
entity_type: "complex"
name: "7-cyano-7-deazaguanine reductase"
source_database: "EcoCyc"
source_id: "CPLX0-3501"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 7-cyano-7-deazaguanine reductase

`complex.ecocyc.CPLX0-3501`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3501`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.Q46920|protein.Q46920]]

## Enriched Summary

Queuosine is one of the most complex tRNA modifications, occurring at the wobble position of the GUN anticodon in the Asn, Asp, Tyr, and His tRNAs. As part of PWY-6700, QueF catalyzes the NADPH-dependent four-electron reduction of a nitrile, 7-CYANO-7-DEAZAGUANINE, to an amine, 7-AMINOMETHYL-7-DEAZAGUANINE . QueF has sequence similarity to GTP cyclohydrolase I (FolE), but is missing characteristic zinc-binding and catalytic residues of that enzyme. Both QueF and FolE belong to the tunneling-fold structural superfamily; gel filtration experiments are consistent with a dimeric form of QueF . The essential role in catalysis of the proposed active site residues Cys190 and Asp197 were confirmed by analysis of site-directed mutants . The reaction mechanism involves formation of a covalent thioimide bond between QueF and preQ0, with half of-the-sites reactivity in the QueF homodimer. The two-step reduction is rate-limiting and involves transfer of the pro-4-R-hydrogen of NADPH . The conserved Glu89 and Phe228 active site residues are involved in sequestration of the imine reaction intermediate . Queuosine is one of the most complex tRNA modifications, occurring at the wobble position of the GUN anticodon in the Asn, Asp, Tyr, and His tRNAs...

## Biological Role

Catalyzes RXN0-4022 (reaction.ecocyc.RXN0-4022).

## Annotation

Queuosine is one of the most complex tRNA modifications, occurring at the wobble position of the GUN anticodon in the Asn, Asp, Tyr, and His tRNAs. As part of PWY-6700, QueF catalyzes the NADPH-dependent four-electron reduction of a nitrile, 7-CYANO-7-DEAZAGUANINE, to an amine, 7-AMINOMETHYL-7-DEAZAGUANINE . QueF has sequence similarity to GTP cyclohydrolase I (FolE), but is missing characteristic zinc-binding and catalytic residues of that enzyme. Both QueF and FolE belong to the tunneling-fold structural superfamily; gel filtration experiments are consistent with a dimeric form of QueF . The essential role in catalysis of the proposed active site residues Cys190 and Asp197 were confirmed by analysis of site-directed mutants . The reaction mechanism involves formation of a covalent thioimide bond between QueF and preQ0, with half of-the-sites reactivity in the QueF homodimer. The two-step reduction is rate-limiting and involves transfer of the pro-4-R-hydrogen of NADPH . The conserved Glu89 and Phe228 active site residues are involved in sequestration of the imine reaction intermediate .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4022|reaction.ecocyc.RXN0-4022]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.Q46920|protein.Q46920]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3501`
- `QSPROTEOME:QS00203703`

## Notes

2*protein.Q46920

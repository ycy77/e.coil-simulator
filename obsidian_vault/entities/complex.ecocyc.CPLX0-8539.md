---
entity_id: "complex.ecocyc.CPLX0-8539"
entity_type: "complex"
name: "metalloprotease TldDE"
source_database: "EcoCyc"
source_id: "CPLX0-8539"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# metalloprotease TldDE

`complex.ecocyc.CPLX0-8539`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8539`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AGG8|protein.P0AGG8]], [[protein.P0AFK0|protein.P0AFK0]]

## Enriched Summary

TldD and TldE form a stable heterodimeric complex with promiscuous metallopeptidase activity, catalyzing the cleavage of an amide bond. Both TldD and TldE can form homo- and heterodimeric complexes, but only the TldDE heterodimer appears to be active . TldD and TldE are both required for in vitro proteolytic processing of the microcin B17 precursor protein, McbA, which is encoded in the microcin biosynthetic gene cluster on the MccB17 plasmid and not present in TAX-511145. The processing involves cleavage of the N-terminal leader sequence and is a prerequisite for the biological activity and export of the peptide ). TldDE are also involved in degradation of the F plasmid encoded LetD inhibitor, LetA/CcdA, even though neither inhibitor gene is present in TAX-511145 . Crystal structures of the enzyme alone and in complexes with substrates and inhibitors have been solved. The TldD and TldE subunits share a similar fold; insertions in the C-terminal domain of TldD provide additional structural elements. Co-crystallization with peptide substrates showed them interacting with the active site cleft in an extended conformation. A catalytic mechanism was proposed . TldD and TldE form a stable heterodimeric complex with promiscuous metallopeptidase activity, catalyzing the cleavage of an amide bond...

## Biological Role

Catalyzes RXN-21204 (reaction.ecocyc.RXN-21204). Bound by Zinc cation (molecule.C00038), Fe2+ (molecule.C14818).

## Annotation

TldD and TldE form a stable heterodimeric complex with promiscuous metallopeptidase activity, catalyzing the cleavage of an amide bond. Both TldD and TldE can form homo- and heterodimeric complexes, but only the TldDE heterodimer appears to be active . TldD and TldE are both required for in vitro proteolytic processing of the microcin B17 precursor protein, McbA, which is encoded in the microcin biosynthetic gene cluster on the MccB17 plasmid and not present in TAX-511145. The processing involves cleavage of the N-terminal leader sequence and is a prerequisite for the biological activity and export of the peptide ). TldDE are also involved in degradation of the F plasmid encoded LetD inhibitor, LetA/CcdA, even though neither inhibitor gene is present in TAX-511145 . Crystal structures of the enzyme alone and in complexes with substrates and inhibitors have been solved. The TldD and TldE subunits share a similar fold; insertions in the C-terminal domain of TldD provide additional structural elements. Co-crystallization with peptide substrates showed them interacting with the active site cleft in an extended conformation. A catalytic mechanism was proposed .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-21204|reaction.ecocyc.RXN-21204]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AFK0|protein.P0AFK0]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AGG8|protein.P0AGG8]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-8539`
- `PDB:5NJF`
- `PDB:5NJC`
- `PDB:5NJB`
- `PDB:5NJA`
- `PDB:5NJ9`
- `PDB:5NJ5`
- `QSPROTEOME:QS00049467`

## Notes

1*protein.P0AGG8|1*protein.P0AFK0

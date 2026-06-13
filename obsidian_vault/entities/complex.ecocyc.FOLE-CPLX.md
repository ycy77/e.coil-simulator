---
entity_id: "complex.ecocyc.FOLE-CPLX"
entity_type: "complex"
name: "GTP cyclohydrolase 1"
source_database: "EcoCyc"
source_id: "FOLE-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# GTP cyclohydrolase 1

`complex.ecocyc.FOLE-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:FOLE-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6T5|protein.P0A6T5]]

## Enriched Summary

GTP cyclohydrolase I is an allosteric enzyme that catalyzes the first step in the biosynthesis of tetrahydrofolate and the modified base queuosine . The enzymatic reaction has a complex mechanism and appears to encompass four steps, with the intermediates being enzyme-bound. Detailed studies of the kinetics and reaction mechanism of the enzyme have been performed . Crystal structures and electron microscope observations of GTP cyclohydrolase I have shown a homodecamer that forms a torus . The active site appears to be located between dimers, and the active enzyme is composed of a pentamer of five dimers . A catalytically active zinc ion is coordinated by C110, C181, and H113 . Each polypeptide seems to contain one GTP binding site . FolE is sensitive to oxidative stress . A folE deletion mutant lacks the queuosine ribonucleoside in tRNAs, indicating that folE is required for preQ0 biosynthesis from GTP . folE gene expression is repressed by MetJ . Translation of FolE is repressed by the small RNA SgrS; overexpression of FolE exacerbates the effects of glucose-phosphate stress in a ppsA mutant . FolE: GTP cyclohydrolase I is an allosteric enzyme that catalyzes the first step in the biosynthesis of tetrahydrofolate and the modified base queuosine . The enzymatic reaction has a complex mechanism and appears to encompass four steps, with the intermediates being enzyme-bound...

## Biological Role

Catalyzes GTP-CYCLOHYDRO-I-RXN (reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN). Bound by Zinc cation (molecule.C00038).

## Annotation

GTP cyclohydrolase I is an allosteric enzyme that catalyzes the first step in the biosynthesis of tetrahydrofolate and the modified base queuosine . The enzymatic reaction has a complex mechanism and appears to encompass four steps, with the intermediates being enzyme-bound. Detailed studies of the kinetics and reaction mechanism of the enzyme have been performed . Crystal structures and electron microscope observations of GTP cyclohydrolase I have shown a homodecamer that forms a torus . The active site appears to be located between dimers, and the active enzyme is composed of a pentamer of five dimers . A catalytically active zinc ion is coordinated by C110, C181, and H113 . Each polypeptide seems to contain one GTP binding site . FolE is sensitive to oxidative stress . A folE deletion mutant lacks the queuosine ribonucleoside in tRNAs, indicating that folE is required for preQ0 biosynthesis from GTP . folE gene expression is repressed by MetJ . Translation of FolE is repressed by the small RNA SgrS; overexpression of FolE exacerbates the effects of glucose-phosphate stress in a ppsA mutant . FolE:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN|reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A6T5|protein.P0A6T5]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## External IDs

- `EcoCyc:FOLE-CPLX`
- `QSPROTEOME:QS00182709`

## Notes

10*protein.P0A6T5

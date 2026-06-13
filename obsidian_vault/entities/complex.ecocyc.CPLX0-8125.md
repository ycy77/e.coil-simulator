---
entity_id: "complex.ecocyc.CPLX0-8125"
entity_type: "complex"
name: "cellulose synthase"
source_database: "EcoCyc"
source_id: "CPLX0-8125"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cellulose synthase

`complex.ecocyc.CPLX0-8125`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8125`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P37652|protein.P37652]], [[protein.P37653|protein.P37653]]

## Enriched Summary

Inverted membrane vesicles containing coexpressed BcsA and BcsB show C-DI-GMP (c-di-GMP) and Mg2+-dependent cellulose synthase activity . Crystal structures of the BcsA-BcsB complex from Rhodobacter sphaeroides have provided insight into the function and regulation of cellulose synthase: BcsA forms a cellulose-conducting channel in the cytoplasmic membrane and BcsB is a membrane-anchored periplasmic protein ; binding of c-di-GMP releases the enzyme from an autoinhibited state . The physical interactions between the diguanylate cyclase EG11257-MONOMER DgcC, the c-di-GMP phosphodiesterase EG12256-MONOMER PdeK, and the BcsB subunit of cellulose synthase create a local microenvironment where the c-di-GMP signal is produced and degraded in proximity to its regulatory target, the catalytic subunit of cellulose synthase BcsA, resulting in local c-di-GMP signaling . In the cellulose producing strain E. coli 1094, the inner membrane and cytosolic Bcs proteins - BcsA, BcsB, BscQ, BcsG, BcsE, BcsR and BcsF - organize in a multisubunit, stable macrocomplex; two-hybrid assays identified multiple direct interactions between the subunits and a low resolution structure has been obtained (see also ). Review: Inverted membrane vesicles containing coexpressed BcsA and BcsB show C-DI-GMP (c-di-GMP) and Mg2+-dependent cellulose synthase activity...

## Biological Role

Catalyzes CELLULOSE-SYNTHASE-UDP-FORMING-RXN (reaction.ecocyc.CELLULOSE-SYNTHASE-UDP-FORMING-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Inverted membrane vesicles containing coexpressed BcsA and BcsB show C-DI-GMP (c-di-GMP) and Mg2+-dependent cellulose synthase activity . Crystal structures of the BcsA-BcsB complex from Rhodobacter sphaeroides have provided insight into the function and regulation of cellulose synthase: BcsA forms a cellulose-conducting channel in the cytoplasmic membrane and BcsB is a membrane-anchored periplasmic protein ; binding of c-di-GMP releases the enzyme from an autoinhibited state . The physical interactions between the diguanylate cyclase EG11257-MONOMER DgcC, the c-di-GMP phosphodiesterase EG12256-MONOMER PdeK, and the BcsB subunit of cellulose synthase create a local microenvironment where the c-di-GMP signal is produced and degraded in proximity to its regulatory target, the catalytic subunit of cellulose synthase BcsA, resulting in local c-di-GMP signaling . In the cellulose producing strain E. coli 1094, the inner membrane and cytosolic Bcs proteins - BcsA, BcsB, BscQ, BcsG, BcsE, BcsR and BcsF - organize in a multisubunit, stable macrocomplex; two-hybrid assays identified multiple direct interactions between the subunits and a low resolution structure has been obtained (see also ). Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.CELLULOSE-SYNTHASE-UDP-FORMING-RXN|reaction.ecocyc.CELLULOSE-SYNTHASE-UDP-FORMING-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P37652|protein.P37652]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P37653|protein.P37653]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-8125`
- `PDB:7LBY`
- `QSPROTEOME:QS00049459`

## Notes

protein.P37652|protein.P37653

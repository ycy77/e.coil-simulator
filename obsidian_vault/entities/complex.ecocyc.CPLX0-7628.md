---
entity_id: "complex.ecocyc.CPLX0-7628"
entity_type: "complex"
name: "lipopolysaccharide transport system - outer membrane assembly complex"
source_database: "EcoCyc"
source_id: "CPLX0-7628"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# lipopolysaccharide transport system - outer membrane assembly complex

`complex.ecocyc.CPLX0-7628`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7628`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P31554|protein.P31554]], [[protein.P0ADC1|protein.P0ADC1]]

## Enriched Summary

LptD and LptE form a 'plug and barrel' type complex in the outer membrane that is responsible for transporting lipopolysaccharide (LPS) from the periplasm to the cell surface. lptD and lptE are essential . Upon depletion of LptD and LptE, cells exhibit increased outer membrane (OM) density, increases in LPS components within the cell, and phospholipids located in the outer leaflet of the OM . Eventually, cell growth stops and death occurs . After depletion of LptD or LptE, de novo synthesized LPS does not reach the outer membrane . LptD and LptE physically interact within the outer membrane . LptD and LptE interact at the CPLX0-3933 "Bam complex" during biogenesis of the LptDE complex . MONOMER0-2693 Lipoprotein LptM interacts with LptDE and promotes its efficient assembly at the BAM complex . Overexpressed LptD and LptE purify as a stable complex in a 1:1 stoichiometry . LptM stably associates with LptDE forming a 1:1:1 heterotrimeric complex . LptDE is implicated in a trafficking pathway for surface exposed lipoproteins, including LptM . LptD interacts with LptE through the C-terminal transmembrane domain of LptD . LptD and LptE interact via an extensive interface involving multiple regions of LptE . LptE is located within the lumen of the LptD β-barrel...

## Biological Role

Component of lipopolysaccharide transport system (complex.ecocyc.CPLX0-7992).

## Annotation

LptD and LptE form a 'plug and barrel' type complex in the outer membrane that is responsible for transporting lipopolysaccharide (LPS) from the periplasm to the cell surface. lptD and lptE are essential . Upon depletion of LptD and LptE, cells exhibit increased outer membrane (OM) density, increases in LPS components within the cell, and phospholipids located in the outer leaflet of the OM . Eventually, cell growth stops and death occurs . After depletion of LptD or LptE, de novo synthesized LPS does not reach the outer membrane . LptD and LptE physically interact within the outer membrane . LptD and LptE interact at the CPLX0-3933 "Bam complex" during biogenesis of the LptDE complex . MONOMER0-2693 Lipoprotein LptM interacts with LptDE and promotes its efficient assembly at the BAM complex . Overexpressed LptD and LptE purify as a stable complex in a 1:1 stoichiometry . LptM stably associates with LptDE forming a 1:1:1 heterotrimeric complex . LptDE is implicated in a trafficking pathway for surface exposed lipoproteins, including LptM . LptD interacts with LptE through the C-terminal transmembrane domain of LptD . LptD and LptE interact via an extensive interface involving multiple regions of LptE . LptE is located within the lumen of the LptD β-barrel . A ten residue region of LptD (residues 529 - 538), which forms part of an extracellular loop, interacts with LptE and deletion of this region compromises assembly of the complex in vivo and is associated with defects in the outer membrane . LptM binds to sites in both LptD and LptE that are important in coordinating LPS insertion into the outer membrane .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7992|complex.ecocyc.CPLX0-7992]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P0ADC1|protein.P0ADC1]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P31554|protein.P31554]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-7628`
- `PDB:4RHB`
- `QSPROTEOME:QS00178301`

## Notes

1*protein.P31554|1*protein.P0ADC1

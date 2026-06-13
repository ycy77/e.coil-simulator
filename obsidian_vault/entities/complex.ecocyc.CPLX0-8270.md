---
entity_id: "complex.ecocyc.CPLX0-8270"
entity_type: "complex"
name: "sensor histidine kinase CpxA"
source_database: "EcoCyc"
source_id: "CPLX0-8270"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sensor histidine kinase CpxA

`complex.ecocyc.CPLX0-8270`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8270`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AE82|protein.P0AE82]]

## Enriched Summary

CpxA is the sensor kinase of the CpxAR two-component signal transduction system - an envelope stress response system which responds to disruptions in inner membrane homeostasis (see ). CpxA is an inner membrane protein with both cytoplasmic and periplasmic domains . The purified cytoplasmic domain of CpxA (MBP-CpxA) has autokinase, CpxR kinase and phospho-CpxR phosphatase activity in vitro; alterations in the kinase:phosphatase ratio may regulate output of the Cpx pathway in vivo . The periplasmic protein G7816-MONOMER "CpxP" binds to CpxA and inhibits the autokinase activity of CpxA (see also ). CpxA interacts directly with CpxP in vivo and this interaction is disrupted by high salt concentration (300mM NaCl) and the presence of misfolded P pilus subunit (from uropathogenic E. coli), PapE . CpxA function is influenced by lipid environment in vitro . CpxA physically interacts with the outer membrane sensor lipoprotein EG12137-MONOMER "NlpE"; this interaction may function as a trigger to activate the Cpx pathway in response to envelope stress (see also ). The model cationic antimicrobial peptide, protamine, directly activates CpxA kinase activity in vitro . The purified, periplasmic sensor domain of CpxA (CpxA31-163) is a dimer of Per-Arnt-Sim (PAS)-like domains; PAS-sensor domain dimerization is implicated in the regulation of sensor kinase activity...

## Biological Role

Catalyzes 2.7.13.2-RXN (reaction.ecocyc.2.7.13.2-RXN), RXN0-7299 (reaction.ecocyc.RXN0-7299).

## Annotation

CpxA is the sensor kinase of the CpxAR two-component signal transduction system - an envelope stress response system which responds to disruptions in inner membrane homeostasis (see ). CpxA is an inner membrane protein with both cytoplasmic and periplasmic domains . The purified cytoplasmic domain of CpxA (MBP-CpxA) has autokinase, CpxR kinase and phospho-CpxR phosphatase activity in vitro; alterations in the kinase:phosphatase ratio may regulate output of the Cpx pathway in vivo . The periplasmic protein G7816-MONOMER "CpxP" binds to CpxA and inhibits the autokinase activity of CpxA (see also ). CpxA interacts directly with CpxP in vivo and this interaction is disrupted by high salt concentration (300mM NaCl) and the presence of misfolded P pilus subunit (from uropathogenic E. coli), PapE . CpxA function is influenced by lipid environment in vitro . CpxA physically interacts with the outer membrane sensor lipoprotein EG12137-MONOMER "NlpE"; this interaction may function as a trigger to activate the Cpx pathway in response to envelope stress (see also ). The model cationic antimicrobial peptide, protamine, directly activates CpxA kinase activity in vitro . The purified, periplasmic sensor domain of CpxA (CpxA31-163) is a dimer of Per-Arnt-Sim (PAS)-like domains; PAS-sensor domain dimerization is implicated in the regulation of sensor kinase activity . CpxA autophosphorylates at the tele nitrogen atom (Nε2) of His-248 via a trans mechanism (ie. ATP binds to one subunit of the dimer and its γ-phosphate is transferred to His-248 in the second subunit) (see also ). CpxA and ArcA interact physically and specifically after aminoglycoside treatment of cells; expression of cpxA does not change significantly in response to aminoglycoside treatment; CpxA does not appear to cross-

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.2-RXN|reaction.ecocyc.2.7.13.2-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7299|reaction.ecocyc.RXN0-7299]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AE82|protein.P0AE82]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8270`
- `QSPROTEOME:QS00195915`

## Notes

2*protein.P0AE82

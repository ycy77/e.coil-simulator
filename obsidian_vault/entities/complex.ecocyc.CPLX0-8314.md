---
entity_id: "complex.ecocyc.CPLX0-8314"
entity_type: "complex"
name: "sensor histidine kinase EvgS"
source_database: "EcoCyc"
source_id: "CPLX0-8314"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCO-PM-BAC-ACT"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sensor histidine kinase EvgS

`complex.ecocyc.CPLX0-8314`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8314`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCO-PM-BAC-ACT
- Complex type: `regulatory`
- Components: [[protein.P30855|protein.P30855]]

## Enriched Summary

evgS encodes the sensor histidine kinase of the EvgS/EvgA two component system which is associated with acid and drug resistance in E. coli K-12. EvgS is a tripartite sensor kinase; the protein contains a single predicted transmembrane domain, a large periplasmic region containing two Venus flytrap (VFT) domains, and a multi-domain cytoplasmic region with PAS (Per-Arnt-Sim), HK (histidine kinase), R (receiver) and HPt (histidine phosphotransfer) domains . EvgS is a hybrid (tripartite) sensor kinase and signal transduction is believed to proceed via a multi-step His-Asp-His phosphorelay; a conserved histidine (His-721) in the HK domain is the site of autophosphorylation and phosphotransfer proceeds from phospho-His-721 to His-1127 in the HPt domain via an aspartate residue (Asp-1009) in the receiver domain (see ). The purified cytoplasmic domain of EvgS autophosphorylates in the presence of γ33-ATP and transfers a labeled phosphate to its cognate response regulator EvgA in vitro (see also ). EvgS activation occus under mild acidic conditions (pH 5-6) in the presence of high concentrations of alkali metals (approx. 150mM Na+ or K+) . Oxidized ubiquinone-0 is a strong inhibitor of EvgS kinase activity in vitro . INDOLE Indole inhibits EvgS-dependent induction of a G6791 ydeP-lacZ reporter; indole does not inhibit autophosphorylation of EvgS in vitro...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Annotation

evgS encodes the sensor histidine kinase of the EvgS/EvgA two component system which is associated with acid and drug resistance in E. coli K-12. EvgS is a tripartite sensor kinase; the protein contains a single predicted transmembrane domain, a large periplasmic region containing two Venus flytrap (VFT) domains, and a multi-domain cytoplasmic region with PAS (Per-Arnt-Sim), HK (histidine kinase), R (receiver) and HPt (histidine phosphotransfer) domains . EvgS is a hybrid (tripartite) sensor kinase and signal transduction is believed to proceed via a multi-step His-Asp-His phosphorelay; a conserved histidine (His-721) in the HK domain is the site of autophosphorylation and phosphotransfer proceeds from phospho-His-721 to His-1127 in the HPt domain via an aspartate residue (Asp-1009) in the receiver domain (see ). The purified cytoplasmic domain of EvgS autophosphorylates in the presence of γ33-ATP and transfers a labeled phosphate to its cognate response regulator EvgA in vitro (see also ). EvgS activation occus under mild acidic conditions (pH 5-6) in the presence of high concentrations of alkali metals (approx. 150mM Na+ or K+) . Oxidized ubiquinone-0 is a strong inhibitor of EvgS kinase activity in vitro . INDOLE Indole inhibits EvgS-dependent induction of a G6791 ydeP-lacZ reporter; indole does not inhibit autophosphorylation of EvgS in vitro . EvgS activation in vivo requires aerobic conditions and ubiquinone EvgS is predicted to be active as a homodimer; modelling indicates that detection of a signal in the periplasm may lead to weakening of the dimer interface in the cytoplasmic PAS domain and activation of the autokinase activity . evgS1 and evgS4 'linker mutations' result in constitutive expression of emrKY and increased resistance to sodium deoxycholate (furth

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P30855|protein.P30855]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8314`
- `QSPROTEOME:QS00195645`

## Notes

2*protein.P30855

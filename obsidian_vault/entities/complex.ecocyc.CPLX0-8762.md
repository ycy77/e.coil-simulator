---
entity_id: "complex.ecocyc.CPLX0-8762"
entity_type: "complex"
name: "hydrogenase 2"
source_database: "EcoCyc"
source_id: "CPLX0-8762"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "HYD2"
  - "hydrogen:menaquinone oxidoreductase 2"
---

# hydrogenase 2

`complex.ecocyc.CPLX0-8762`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8762`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.FORMHYDROG2-CPLX|complex.ecocyc.FORMHYDROG2-CPLX]]

## Enriched Summary

Hydrogenase 2 is a membrane-bound, [Ni-Fe] enzyme produced under anaerobic conditions. Hydrogenase 2 is a respiratory enzyme which couples hydrogen oxidation in the periplasm to reduction of the inner membrane quinone pool . Hydrogenase 2 participates in H(2) dependent reduction of fumarate, dimethyl sulfoxide and trimethylamine N-oxide (and see . Hydrogenase 2 is an oxygen sensitive enzyme - it is unable to catalyse H(2) oxidation under aerobic conditions . Hydrogenase 2 functions optimally at redox potentials lower than -100 to -150 mV . Hydrogenase 2 is capable of bidirectional catalysis in vitro and in vivo . Hydrogenase 2 can function as an H(2) evolving enzyme (i.e. as a proton reductant) during fermentative growth with glycerol; this endergonic reaction is driven by the membrane proton gradient and probably functions to prevent over reduction of the quinone pool (see also ). Hydrogenase 2 uses menaquinone/demethylmenaquinone to couple hydrogen oxidation to fumarate reduction during anaerobic respiratory growth with glycerol and fumarate and also during H(2) evolution during fermentation with glycerol; hydrogenase 2 can rapidly switch between H(2) evolution and H(2) oxidation modes in vivo . Trypsin treatment of membranes releases an active, soluble fragment of hydrogenase 2 which consists of the large and small subunits...

## Biological Role

Catalyzes RXN0-7399 (reaction.ecocyc.RXN0-7399). Bound by NiFe(CO)(CN)2 cofactor (molecule.ecocyc.CPD-24862), an iron-sulfur cluster (molecule.ecocyc.FeS-Centers).

## Annotation

Hydrogenase 2 is a membrane-bound, [Ni-Fe] enzyme produced under anaerobic conditions. Hydrogenase 2 is a respiratory enzyme which couples hydrogen oxidation in the periplasm to reduction of the inner membrane quinone pool . Hydrogenase 2 participates in H(2) dependent reduction of fumarate, dimethyl sulfoxide and trimethylamine N-oxide (and see . Hydrogenase 2 is an oxygen sensitive enzyme - it is unable to catalyse H(2) oxidation under aerobic conditions . Hydrogenase 2 functions optimally at redox potentials lower than -100 to -150 mV . Hydrogenase 2 is capable of bidirectional catalysis in vitro and in vivo . Hydrogenase 2 can function as an H(2) evolving enzyme (i.e. as a proton reductant) during fermentative growth with glycerol; this endergonic reaction is driven by the membrane proton gradient and probably functions to prevent over reduction of the quinone pool (see also ). Hydrogenase 2 uses menaquinone/demethylmenaquinone to couple hydrogen oxidation to fumarate reduction during anaerobic respiratory growth with glycerol and fumarate and also during H(2) evolution during fermentation with glycerol; hydrogenase 2 can rapidly switch between H(2) evolution and H(2) oxidation modes in vivo . Trypsin treatment of membranes releases an active, soluble fragment of hydrogenase 2 which consists of the large and small subunits . Hydrogenase 2 is encoded within the hyb operon (hybGFEDCBAO); the complete enzyme complex is thought to consist of the HybA, HybB, HybC and HybO subunits . HybOC forms the core catalytic dimer anchored to the membrane via a hydrophobic helix at the C-terminus of HybO; HybA (a ferredoxin type protein) and HybB (an integral membrane protein) are essential for shuttling electrons to the quinone pool . HybC and HybO are coordinately assembled and pr

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7399|reaction.ecocyc.RXN0-7399]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (7)

- `binds` <-- [[molecule.ecocyc.CPD-24862|molecule.ecocyc.CPD-24862]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.FeS-Centers|molecule.ecocyc.FeS-Centers]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.FORMHYDROG2-CPLX|complex.ecocyc.FORMHYDROG2-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `is_component_of` <-- [[protein.P0AAJ8|protein.P0AAJ8]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0ACE0|protein.P0ACE0]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P37180|protein.P37180]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P69741|protein.P69741]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8762`
- `QSPROTEOME:QS00195953`

## Notes

2*complex.ecocyc.FORMHYDROG2-CPLX

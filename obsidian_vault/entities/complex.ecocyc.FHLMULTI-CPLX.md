---
entity_id: "complex.ecocyc.FHLMULTI-CPLX"
entity_type: "complex"
name: "formate hydrogenlyase complex"
source_database: "EcoCyc"
source_id: "FHLMULTI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "FHL"
---

# formate hydrogenlyase complex

`complex.ecocyc.FHLMULTI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:FHLMULTI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07658|protein.P07658]], [[complex.ecocyc.HYDROG3-CPLX|complex.ecocyc.HYDROG3-CPLX]]

## Enriched Summary

Formate hydrogenlyase (FHL) is a membrane associated, multisubunit complex that links formate oxidation to the reduction of protons and releases carbon dioxide and dihydrogen; FHL is responsible for the majority of H2 production that occurs during glucose fermentation. The complex consists of a cytoplasmic formate dehydrogenase (FdhF) plus a group 4 [NiFe] hydrogenases (HycBCDEFG or HYDROG3-CPLX); HycC and HycD are integral membrane proteins; HycE and HycG are the large and small subunits respectively, of hydrogenase 3 and HycB and HycF are iron-sulfur proteins. Electrons flow from the site of formate oxidation in FdhF to the site of H2 production in HycE via the iron-sulfur proteins HycB, HycF and HycG (reviewed in and see also ). Isolation of FHL using affinity chromatography indicates the presence of a core complex containing HycE, HycB, HycF, HycG and (loosely associated) FdhF which has formate hydrogenlyase activity in vitro; a larger complex containing the membrane associated subunits HycC and HycD is isolated in the presence of detergent...

## Biological Role

Catalyzes FHLMULTI-RXN (reaction.ecocyc.FHLMULTI-RXN). Bound by bis(guanylyl molybdopterin) cofactor (molecule.ecocyc.CPD-15873), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

Formate hydrogenlyase (FHL) is a membrane associated, multisubunit complex that links formate oxidation to the reduction of protons and releases carbon dioxide and dihydrogen; FHL is responsible for the majority of H2 production that occurs during glucose fermentation. The complex consists of a cytoplasmic formate dehydrogenase (FdhF) plus a group 4 [NiFe] hydrogenases (HycBCDEFG or HYDROG3-CPLX); HycC and HycD are integral membrane proteins; HycE and HycG are the large and small subunits respectively, of hydrogenase 3 and HycB and HycF are iron-sulfur proteins. Electrons flow from the site of formate oxidation in FdhF to the site of H2 production in HycE via the iron-sulfur proteins HycB, HycF and HycG (reviewed in and see also ). Isolation of FHL using affinity chromatography indicates the presence of a core complex containing HycE, HycB, HycF, HycG and (loosely associated) FdhF which has formate hydrogenlyase activity in vitro; a larger complex containing the membrane associated subunits HycC and HycD is isolated in the presence of detergent . Cryo-EM structures of FHL, purified aerobically and anaerobically, have been reported; the complex has an L-shaped structure with membrane-embedded (HycC and HycD) and cytoplasmic (HycB, HycE, HycF, HycG and FdhF) regions; formate oxidation occurs at the CPD-15873 (bis-MGD) active site in FdhF, and electrons are transferred to the site of proton reduction in HycE via a relay of eight [4Fe-4S] clusters . Formate oxidation in an anaerobically grown fermenting E. coli strain lacking hydrogenase 1 and hydrogenase 2 enzymes generates membrane potential . Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.FHLMULTI-RXN|reaction.ecocyc.FHLMULTI-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (10)

- `binds` <-- [[molecule.ecocyc.CPD-15873|molecule.ecocyc.CPD-15873]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.HYDROG3-CPLX|complex.ecocyc.HYDROG3-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P07658|protein.P07658]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AAK1|protein.P0AAK1]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P16429|protein.P16429]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P16430|protein.P16430]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P16431|protein.P16431]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P16432|protein.P16432]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P16433|protein.P16433]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:FHLMULTI-CPLX`
- `PDB:7Z0T`

## Notes

1*protein.P07658|1*complex.ecocyc.HYDROG3-CPLX

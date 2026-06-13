---
entity_id: "complex.ecocyc.CPLX0-7964"
entity_type: "complex"
name: "outer membrane channel TolC"
source_database: "EcoCyc"
source_id: "CPLX0-7964"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# outer membrane channel TolC

`complex.ecocyc.CPLX0-7964`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7964`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P02930|protein.P02930]]

## Enriched Summary

TolC is the common outer membrane channel of efflux systems which pump out a large variety of toxic exogenous compounds (antibiotics, dyes detergents, bile compounds, organic solvents) and some intracellular metabolites (enterobactin, porphyrinogens/porphyrins); TolC is also the site of colicin E1 entry and the receptor for bacteriophage TLS. TolC is an outer membrane protein . Purified TolC is trimeric and consists of an outer membrane β-barrel contiguous with an α-helical barrel that extends into the periplasm; the molecule forms a single pore which is open to the outside of the cell but tapers to a virtual close at the periplasmic entrance; aspartate residues located at the periplasmic constriction are implicated in high affinity ligand binding . The TolC periplasmic entrance must be opened to allow substrate efflux (see ); TolC transitions to the open state by realigning or 'untwisting' of the entrance helices...

## Biological Role

Component of multidrug efflux pump EmrAB-TolC (complex.ecocyc.CPLX0-2121), multidrug efflux pump AcrEF-TolC (complex.ecocyc.CPLX0-2141), tripartite efflux pump EmrKY-TolC (complex.ecocyc.CPLX0-2161), multidrug efflux pump AcrAD-TolC (complex.ecocyc.CPLX0-3932), ABC-type tripartite efflux pump (complex.ecocyc.TRANS-200-CPLX), multidrug efflux pump AcrAB-TolC (complex.ecocyc.TRANS-CPLX-201), multidrug efflux pump MdtABC-TolC (complex.ecocyc.TRANS-CPLX-202), multidrug efflux pump MdtEF-TolC (complex.ecocyc.TRANS-CPLX-204).

## Annotation

TolC is the common outer membrane channel of efflux systems which pump out a large variety of toxic exogenous compounds (antibiotics, dyes detergents, bile compounds, organic solvents) and some intracellular metabolites (enterobactin, porphyrinogens/porphyrins); TolC is also the site of colicin E1 entry and the receptor for bacteriophage TLS. TolC is an outer membrane protein . Purified TolC is trimeric and consists of an outer membrane β-barrel contiguous with an α-helical barrel that extends into the periplasm; the molecule forms a single pore which is open to the outside of the cell but tapers to a virtual close at the periplasmic entrance; aspartate residues located at the periplasmic constriction are implicated in high affinity ligand binding . The TolC periplasmic entrance must be opened to allow substrate efflux (see ); TolC transitions to the open state by realigning or 'untwisting' of the entrance helices . Cryo-EM structures of the AcrAB-TolC complex (with and without ligand) show that trimeric TolC interacts in a tip-to-tip manner with hexameric AcrA; TolC adopts a closed state in the 'apo' complex and a fully opened state (through an 'iris-like dilation' of the periplasmic end) in the ligand-bound complex; the structures suggest that upon ligand binding, conformational change in AcrB is communicated through AcrA to TolC and this allosteric effect both seals and opens the export channel . Mutations at the tolC locus make the cell resistant to colicin E1 and sensitive to acriflavine and deoxycholate (see and references within). TolC is the channel for colicin E1 (see also ); TolC is the receptor for bacteriophage TLS . TolC is required for the function of the AcrAB efflux pump and its homologs AcrEF and MdtEF , the EmrAB efflux pump (see ), the EmrAB homolog,

## Outgoing Edges (8)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2121|complex.ecocyc.CPLX0-2121]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-2141|complex.ecocyc.CPLX0-2141]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-2161|complex.ecocyc.CPLX0-2161]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-3932|complex.ecocyc.CPLX0-3932]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.TRANS-200-CPLX|complex.ecocyc.TRANS-200-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.TRANS-CPLX-201|complex.ecocyc.TRANS-CPLX-201]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.TRANS-CPLX-202|complex.ecocyc.TRANS-CPLX-202]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.TRANS-CPLX-204|complex.ecocyc.TRANS-CPLX-204]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P02930|protein.P02930]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-7964`
- `QSPROTEOME:QS00093450`

## Notes

3*protein.P02930

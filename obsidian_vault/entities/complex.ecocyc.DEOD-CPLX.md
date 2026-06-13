---
entity_id: "complex.ecocyc.DEOD-CPLX"
entity_type: "complex"
name: "purine nucleoside phosphorylase"
source_database: "EcoCyc"
source_id: "DEOD-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# purine nucleoside phosphorylase

`complex.ecocyc.DEOD-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DEOD-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `structural`
- Components: [[protein.P0ABP8|protein.P0ABP8]]

## Enriched Summary

DeoD (also called PNP-I) is one of the two purine nuceloside phosphorylases (PNPs) in E. coli. PNPs use orthophosphate to cleave the N-glycosidic bond of the β-(deoxy)ribonucleosides to produce α-(deoxy)ribose1-phosphate and the free purine base. The bases can be utilized as precursors in the synthesis of nucleotides in the purine and pyrimidine salvage pathways as well as a nitrogen source. The pentose-1-phosphate formed serves as a carbon source. The other PNP, PNP-II XANTHOSINEPHOSPHORY-CPLX, differs in substrate specificity. DeoD is a homohexamer and has broader substrate specificity but cannot act on xanthosine . The homohexameric configuration is necessary for structural stability and catalytic activity . Additionally, DeoD can catalyze a phosphate-dependent transfer of the pentose moiety from one purine base to another . Phosphate stimulates the ribosyl transferase activity, and kinetic studies show strong negative cooperativity in binding of phosphate to the enzyme . The reaction mechanism has been explored . The enzyme is inhibited by Cu2+ and Zn2+ . Reports differ on whether () or not () Ni2+ and SO42- inhibit the enzyme. The substrate recognition mechanism of the enzyme has been investigated using a variety of natural purine analogs and a Ser90Ala mutant...

## Biological Role

Catalyzes ADENPHOSPHOR-RXN (reaction.ecocyc.ADENPHOSPHOR-RXN), DEOXYADENPHOSPHOR-RXN (reaction.ecocyc.DEOXYADENPHOSPHOR-RXN), DEOXYGUANPHOSPHOR-RXN (reaction.ecocyc.DEOXYGUANPHOSPHOR-RXN), DEOXYINOPHOSPHOR-RXN (reaction.ecocyc.DEOXYINOPHOSPHOR-RXN), INOPHOSPHOR-RXN (reaction.ecocyc.INOPHOSPHOR-RXN), PNP-RXN (reaction.ecocyc.PNP-RXN), RXN0-5199 (reaction.ecocyc.RXN0-5199).

## Annotation

DeoD (also called PNP-I) is one of the two purine nuceloside phosphorylases (PNPs) in E. coli. PNPs use orthophosphate to cleave the N-glycosidic bond of the β-(deoxy)ribonucleosides to produce α-(deoxy)ribose1-phosphate and the free purine base. The bases can be utilized as precursors in the synthesis of nucleotides in the purine and pyrimidine salvage pathways as well as a nitrogen source. The pentose-1-phosphate formed serves as a carbon source. The other PNP, PNP-II XANTHOSINEPHOSPHORY-CPLX, differs in substrate specificity. DeoD is a homohexamer and has broader substrate specificity but cannot act on xanthosine . The homohexameric configuration is necessary for structural stability and catalytic activity . Additionally, DeoD can catalyze a phosphate-dependent transfer of the pentose moiety from one purine base to another . Phosphate stimulates the ribosyl transferase activity, and kinetic studies show strong negative cooperativity in binding of phosphate to the enzyme . The reaction mechanism has been explored . The enzyme is inhibited by Cu2+ and Zn2+ . Reports differ on whether () or not () Ni2+ and SO42- inhibit the enzyme. The substrate recognition mechanism of the enzyme has been investigated using a variety of natural purine analogs and a Ser90Ala mutant . Crystal structures of DeoD have been determined for wild-type and mutant enzymes and their complexes with substrate analogs. The catalytic mechanisms and substrate specificities of the enzymes were analyzed . A phosphate binding site was also demonstrated . In an extension of the crystallographic work, hydrogen/deuterium exchange mass spectrometry data and molecular dynamics simulations revealed steps in the allosteric communication between neighboring monomer active sites. Both wild-type and an Arg24Ala mu

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.ADENPHOSPHOR-RXN|reaction.ecocyc.ADENPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DEOXYADENPHOSPHOR-RXN|reaction.ecocyc.DEOXYADENPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DEOXYGUANPHOSPHOR-RXN|reaction.ecocyc.DEOXYGUANPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DEOXYINOPHOSPHOR-RXN|reaction.ecocyc.DEOXYINOPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.INOPHOSPHOR-RXN|reaction.ecocyc.INOPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PNP-RXN|reaction.ecocyc.PNP-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5199|reaction.ecocyc.RXN0-5199]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ABP8|protein.P0ABP8]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:DEOD-CPLX`
- `QSPROTEOME:QS00200457`

## Notes

6*protein.P0ABP8

---
entity_id: "complex.ecocyc.DIMESULFREDUCT-CPLX"
entity_type: "complex"
name: "dimethyl sulfoxide reductase"
source_database: "EcoCyc"
source_id: "DIMESULFREDUCT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "DMSO/TMAO reductase"
  - "menaquinol:dimethyl sulfoxide oxidoreductase"
---

# dimethyl sulfoxide reductase

`complex.ecocyc.DIMESULFREDUCT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DIMESULFREDUCT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[protein.P18775|protein.P18775]], [[protein.P18776|protein.P18776]], [[protein.P18777|protein.P18777]]

## Enriched Summary

Dimethyl sulfoxide (DMSO) reductase is a membrane-associated Fe-S molybdoenzyme which catalyses the reduction of DMSO to dimethyl sulfide. The enzyme functions as a terminal reductase during anaerobic respiration on DMSO . Purified DMSO reductase has broad substrate specificity - it is active on hydroxylamine and chlorate plus a range of amine-N-oxides (including trimethylamine N-oxide) and methyl-sulfoxides . DMSO reductase is a member of the complex iron sulfur molybdoenzyme (CISM) family . The enzyme complex contains three non-identical subunits - a catalytic subunit (DmsA) with a molybdo-bis(pyranopterin guanine dinucleotide) (Mo-bisPGD) cofactor and a [4Fe-4S] cluster (known as FS0), an electron transfer subunit (DmsB) containing four [4Fe-4S] clusters (FS1-FS4) and a membrane anchor subunit (DmsC) containing the quinone-binding site . Electron transfer is believed to occur from the menaquinol binding site in DmsC, via the Fe-S clusters in DmsB to the site of DMSO reduction in DmsA . Early experiments suggested that the DmsAB subunits were located on the cytoplasmic face of the inner membrane however later work showed they were present at the the periplasmic face of the inner membrane . DmsC is the integral membrane subunit - it is required for membrane localization of the complex...

## Biological Role

Catalyzes DIMESULFREDUCT-RXN (reaction.ecocyc.DIMESULFREDUCT-RXN). Bound by bis(guanylyl molybdopterin) cofactor (molecule.ecocyc.CPD-15873), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

Dimethyl sulfoxide (DMSO) reductase is a membrane-associated Fe-S molybdoenzyme which catalyses the reduction of DMSO to dimethyl sulfide. The enzyme functions as a terminal reductase during anaerobic respiration on DMSO . Purified DMSO reductase has broad substrate specificity - it is active on hydroxylamine and chlorate plus a range of amine-N-oxides (including trimethylamine N-oxide) and methyl-sulfoxides . DMSO reductase is a member of the complex iron sulfur molybdoenzyme (CISM) family . The enzyme complex contains three non-identical subunits - a catalytic subunit (DmsA) with a molybdo-bis(pyranopterin guanine dinucleotide) (Mo-bisPGD) cofactor and a [4Fe-4S] cluster (known as FS0), an electron transfer subunit (DmsB) containing four [4Fe-4S] clusters (FS1-FS4) and a membrane anchor subunit (DmsC) containing the quinone-binding site . Electron transfer is believed to occur from the menaquinol binding site in DmsC, via the Fe-S clusters in DmsB to the site of DMSO reduction in DmsA . Early experiments suggested that the DmsAB subunits were located on the cytoplasmic face of the inner membrane however later work showed they were present at the the periplasmic face of the inner membrane . DmsC is the integral membrane subunit - it is required for membrane localization of the complex . Insertion of the molybdenum cofactor and targeting of the enzyme to the inner membrane requires the redox enzyme maturation protein (REMP), G6849-MONOMER DmsD (reviewed in ). The enzyme functions anaerobically in the absence of nitrate (a preferred terminal electron acceptor). Anaerobiosis stimulates its expression 100-fold, an effect controlled by the Fnr regulatory protein . Please note: analysis of DMSO reductase has largely been done using E. coli HB101. Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DIMESULFREDUCT-RXN|reaction.ecocyc.DIMESULFREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `binds` <-- [[molecule.ecocyc.CPD-15873|molecule.ecocyc.CPD-15873]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P18775|protein.P18775]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P18776|protein.P18776]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P18777|protein.P18777]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:DIMESULFREDUCT-CPLX`
- `QSPROTEOME:QS00178299`

## Notes

1*protein.P18775|1*protein.P18776|1*protein.P18777

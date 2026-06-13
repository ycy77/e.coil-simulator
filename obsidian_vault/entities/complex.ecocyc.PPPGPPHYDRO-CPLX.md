---
entity_id: "complex.ecocyc.PPPGPPHYDRO-CPLX"
entity_type: "complex"
name: "guanosine-5'-triphosphate,3'-diphosphate phosphatase"
source_database: "EcoCyc"
source_id: "PPPGPPHYDRO-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# guanosine-5'-triphosphate,3'-diphosphate phosphatase

`complex.ecocyc.PPPGPPHYDRO-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PPPGPPHYDRO-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P25552|protein.P25552]]

## Enriched Summary

Guanosine 5'-triphosphate, 3'-diphosphate (pppGpp) pyrophosphatase catalyzes the conversion of pppGpp to ppGpp. The enzyme requires Mg+2 and a monovalent cation. NH4+ is preferred over K+ . Gpp also has long chain exopolyphosphatase activity (E.C.3.6.1.11). The enzyme preferred polyphosphate as substrate, with a Km for polyphosphate of 0.5 nM as compared with 0.13 mM for pppGpp . Gpp hydrolyzes the 5' phosphate from pppGpp to produce ppGpp. These two nucleotides have been implicated in the regulation of bacterial adjustments to stress, known as the stringent response (reviewed in Cashel et. al. (1996) "The Stringent Response", chapter 92, in ). This enzyme is homologous to the exopolyphosphatase PPX-MONOMER Ppx. Both enzymes belong to the large sugar kinase/actin/hsp70 superfamily. Although Ppx and Gpp have similar catalytic properties, they have different physiological roles . The native apparent molecular mass was determined by gel filtration chromatography. The apparent molecular mass of the subunit was determined by SDS-PAGE . Gpp: Guanosine 5'-triphosphate, 3'-diphosphate (pppGpp) pyrophosphatase catalyzes the conversion of pppGpp to ppGpp. The enzyme requires Mg+2 and a monovalent cation. NH4+ is preferred over K+ . Gpp also has long chain exopolyphosphatase activity (E.C.3.6.1.11). The enzyme preferred polyphosphate as substrate, with a Km for polyphosphate of 0...

## Biological Role

Catalyzes PPPGPPHYDRO-RXN (reaction.ecocyc.PPPGPPHYDRO-RXN). Bound by Magnesium cation (molecule.C00305), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

Guanosine 5'-triphosphate, 3'-diphosphate (pppGpp) pyrophosphatase catalyzes the conversion of pppGpp to ppGpp. The enzyme requires Mg+2 and a monovalent cation. NH4+ is preferred over K+ . Gpp also has long chain exopolyphosphatase activity (E.C.3.6.1.11). The enzyme preferred polyphosphate as substrate, with a Km for polyphosphate of 0.5 nM as compared with 0.13 mM for pppGpp . Gpp hydrolyzes the 5' phosphate from pppGpp to produce ppGpp. These two nucleotides have been implicated in the regulation of bacterial adjustments to stress, known as the stringent response (reviewed in Cashel et. al. (1996) "The Stringent Response", chapter 92, in ). This enzyme is homologous to the exopolyphosphatase PPX-MONOMER Ppx. Both enzymes belong to the large sugar kinase/actin/hsp70 superfamily. Although Ppx and Gpp have similar catalytic properties, they have different physiological roles . The native apparent molecular mass was determined by gel filtration chromatography. The apparent molecular mass of the subunit was determined by SDS-PAGE . Gpp:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PPPGPPHYDRO-RXN|reaction.ecocyc.PPPGPPHYDRO-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P25552|protein.P25552]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PPPGPPHYDRO-CPLX`
- `QSPROTEOME:QS00049750`

## Notes

2*protein.P25552

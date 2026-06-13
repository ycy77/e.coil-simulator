---
entity_id: "complex.ecocyc.NAP-CPLX"
entity_type: "complex"
name: "periplasmic nitrate reductase"
source_database: "EcoCyc"
source_id: "NAP-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Nap"
---

# periplasmic nitrate reductase

`complex.ecocyc.NAP-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:NAP-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PERI-BAC-GN
- Complex type: `regulatory`
- Components: [[protein.P0ABL3|protein.P0ABL3]], [[protein.P33937|protein.P33937]]

## Enriched Summary

E. coli K-12 contains three nitrate reductases. Two of them, NITRATREDUCTA-CPLX (NRA) and NITRATREDUCTZ-CPLX (NRZ), are membrane bound and biochemically similar. The third nitrate reductase, Nap, is located in the periplasm. It is induced by anaerobiosis through the mediation of the transcription factor Fnr and low concentrations of nitrate through the mediation of NARP-MONOMER NarP . Nap is not itself a coupling site for generating proton motive force; acting as a terminal electron acceptor, it does support anaerobic respiration of various carbon sources . The physiological role of Nap is that of mediating anaerobic respiration at the expense of low concentrations of nitrate. Owing to the periplasmic location of Nap, the cost of pumping nitrate into the cell is avoided. In addition, Nap has a significantly higher affinity for nitrate than NRA and is thus able to exploit the low concentrations of nitrate occuring in the natural environment of E. coli . Notably, several pathogenic bacterial species, such as TAX-727, only contain orthologs of the periplasmic nitrate reductase . During glucose fermentation in the absence of menaquinone, a very low level of Nap activity appears to substitute for the redox-balancing role of fumarate reductase, which is dependent on menaquinone . The nap operon encodes seven proteins...

## Biological Role

Catalyzes NITRATE-REDUCTASE-CYTOCHROME-RXN (reaction.ecocyc.NITRATE-REDUCTASE-CYTOCHROME-RXN). Bound by bis(guanylyl molybdopterin) cofactor (molecule.ecocyc.CPD-15873), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7), heme c (molecule.ecocyc.HEME_C).

## Annotation

E. coli K-12 contains three nitrate reductases. Two of them, NITRATREDUCTA-CPLX (NRA) and NITRATREDUCTZ-CPLX (NRZ), are membrane bound and biochemically similar. The third nitrate reductase, Nap, is located in the periplasm. It is induced by anaerobiosis through the mediation of the transcription factor Fnr and low concentrations of nitrate through the mediation of NARP-MONOMER NarP . Nap is not itself a coupling site for generating proton motive force; acting as a terminal electron acceptor, it does support anaerobic respiration of various carbon sources . The physiological role of Nap is that of mediating anaerobic respiration at the expense of low concentrations of nitrate. Owing to the periplasmic location of Nap, the cost of pumping nitrate into the cell is avoided. In addition, Nap has a significantly higher affinity for nitrate than NRA and is thus able to exploit the low concentrations of nitrate occuring in the natural environment of E. coli . Notably, several pathogenic bacterial species, such as TAX-727, only contain orthologs of the periplasmic nitrate reductase . During glucose fermentation in the absence of menaquinone, a very low level of Nap activity appears to substitute for the redox-balancing role of fumarate reductase, which is dependent on menaquinone . The nap operon encodes seven proteins. The catalytic portion of the protein, consisting of the periplasmic NAPA-MONOMER NapA and NAPB-MONOMER NapB polypeptides, receives its electrons from the membrane quinone pool in different paths depending on the quinone type present at the time. When menaquinol is present, it reduces the membrane-bound cytochrome NAPC-MONOMER NapC, which then transfers the electrons to NapB. Ubiquinol, on the other hand, is not able to reduce NapC directly. Instead, it reduces t

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.NITRATE-REDUCTASE-CYTOCHROME-RXN|reaction.ecocyc.NITRATE-REDUCTASE-CYTOCHROME-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `binds` <-- [[molecule.ecocyc.CPD-15873|molecule.ecocyc.CPD-15873]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.HEME_C|molecule.ecocyc.HEME_C]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0ABL3|protein.P0ABL3]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P33937|protein.P33937]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:NAP-CPLX`
- `QSPROTEOME:QS00185827`

## Notes

1*protein.P0ABL3|1*protein.P33937

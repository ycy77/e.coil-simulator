---
entity_id: "complex.ecocyc.CPLX0-8205"
entity_type: "complex"
name: "UTP—glucose-1-phosphate uridylyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-8205"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# UTP—glucose-1-phosphate uridylyltransferase

`complex.ecocyc.CPLX0-8205`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8205`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEP3|protein.P0AEP3]]

## Enriched Summary

UTP—glucose-1-phosphate uridylyltransferase (GalU) catalyzes the synthesis of UDP-D-glucose from UTP and α-D-glucose 1-phosphate . UDP-D-glucose is a central precursor for synthesis of cell envelope components, including LPS core , colanic acid and membrane-derived oligosaccharides (now known as CPD-16398 osmoregulated periplasmic glucans) , as well as for trehalose . In addition, GalU supplies the catalytic amount of UDP-glucose that is required for galactose utilization via the PWY-6317 "Leloir pathway" . The crystal structure of GalU was determined at 1.9 Å resolution, showing a tetramer in a dimer of dimers configuration . The interaction of GalU with its product UDP-glucose was modeled based on the crystal structure of the Corynebacterium glutamicum enzyme . A T20M R21H double mutant and a K202A mutant have lower enzymatic activity than wild type . G7093-MONOMER GalF is a protein with 58% sequence identity to GalU that has vestigial UTP:glucose-1-phosphate uridylyltransferase activity . It was initially suggested to be a subunit of a GalU/GalF protein complex involved in COLANSYN-PWY. In the uropathogenic E. coli strain VW187 (O7:K1), GalF has been shown to interact physically with GalU, as well as enhancing its thermal stability and increasing its enzymatic activity...

## Biological Role

Catalyzes GLUC1PURIDYLTRANS-RXN (reaction.ecocyc.GLUC1PURIDYLTRANS-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

UTP—glucose-1-phosphate uridylyltransferase (GalU) catalyzes the synthesis of UDP-D-glucose from UTP and α-D-glucose 1-phosphate . UDP-D-glucose is a central precursor for synthesis of cell envelope components, including LPS core , colanic acid and membrane-derived oligosaccharides (now known as CPD-16398 osmoregulated periplasmic glucans) , as well as for trehalose . In addition, GalU supplies the catalytic amount of UDP-glucose that is required for galactose utilization via the PWY-6317 "Leloir pathway" . The crystal structure of GalU was determined at 1.9 Å resolution, showing a tetramer in a dimer of dimers configuration . The interaction of GalU with its product UDP-glucose was modeled based on the crystal structure of the Corynebacterium glutamicum enzyme . A T20M R21H double mutant and a K202A mutant have lower enzymatic activity than wild type . G7093-MONOMER GalF is a protein with 58% sequence identity to GalU that has vestigial UTP:glucose-1-phosphate uridylyltransferase activity . It was initially suggested to be a subunit of a GalU/GalF protein complex involved in COLANSYN-PWY. In the uropathogenic E. coli strain VW187 (O7:K1), GalF has been shown to interact physically with GalU, as well as enhancing its thermal stability and increasing its enzymatic activity . galU mutants are unable to utilize galactose as the sole source of carbon , contain significantly reduced levels of glucoside in extracellular polysaccharides , lack membrane-derived oligosaccharides and colanic acid , don't accumulate trehalose , and are not susceptible to phage P1 infection . Deletion of galU, among other genes required for LPS biosynthesis, confers partial resistance to colicin N .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUC1PURIDYLTRANS-RXN|reaction.ecocyc.GLUC1PURIDYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AEP3|protein.P0AEP3]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8205`
- `QSPROTEOME:QS00181997`

## Notes

4*protein.P0AEP3

---
entity_id: "complex.ecocyc.CPLX0-8034"
entity_type: "complex"
name: "glucose-1-phosphate thymidylyltransferase 1"
source_database: "EcoCyc"
source_id: "CPLX0-8034"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glucose-1-phosphate thymidylyltransferase 1

`complex.ecocyc.CPLX0-8034`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8034`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37744|protein.P37744]]

## Enriched Summary

dTDP-glucose pyrophosphorylase is involved in the biosynthesis of dTDP-L-rhamnose. dTDP-L-rhamnose is a precursor of L-rhamnose which is an essential component of surface antigens such as the O-lipopolysaccharide. The enzyme catalyzes the formation of dTDP-glucose from dTTP and glucose-1-phosphate, as well as its pyrophosphorolysis. A divalent cation is essential for catalysis . dTDP-glucose pyrophosphorylase is encoded by the rfbA gene which is paralogous to rffH. The product of rffH is another dTDP-glucose pyrophosphorylase which catalyzes the same reaction, but functions in the enterobacterial common antigen biosynthesis pathway. There is 68% amino acid sequence identity between the two paralogs. Of the two enzymes, RfbA appears to be the major contributor to dTDP-glucose biosynthesis in vivo . The crystal structure of the homotetrameric molecule in complex with dDTP-glucose was refined at 1.9 Å resolution and shows conserved substrate and inhibitor binding modes . Mutant cells deficient in dTDP-glucose pyrophosphorylase activity lose viability faster, form longer filaments, lose thymidine nucleotides and dTDP-sugar pools at a faster rate than wild-type cells . For information on bacterial polysaccharide gene nomenclature see . dTDP-glucose pyrophosphorylase is involved in the biosynthesis of dTDP-L-rhamnose...

## Biological Role

Catalyzes DTDPGLUCOSEPP-RXN (reaction.ecocyc.DTDPGLUCOSEPP-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

dTDP-glucose pyrophosphorylase is involved in the biosynthesis of dTDP-L-rhamnose. dTDP-L-rhamnose is a precursor of L-rhamnose which is an essential component of surface antigens such as the O-lipopolysaccharide. The enzyme catalyzes the formation of dTDP-glucose from dTTP and glucose-1-phosphate, as well as its pyrophosphorolysis. A divalent cation is essential for catalysis . dTDP-glucose pyrophosphorylase is encoded by the rfbA gene which is paralogous to rffH. The product of rffH is another dTDP-glucose pyrophosphorylase which catalyzes the same reaction, but functions in the enterobacterial common antigen biosynthesis pathway. There is 68% amino acid sequence identity between the two paralogs. Of the two enzymes, RfbA appears to be the major contributor to dTDP-glucose biosynthesis in vivo . The crystal structure of the homotetrameric molecule in complex with dDTP-glucose was refined at 1.9 Å resolution and shows conserved substrate and inhibitor binding modes . Mutant cells deficient in dTDP-glucose pyrophosphorylase activity lose viability faster, form longer filaments, lose thymidine nucleotides and dTDP-sugar pools at a faster rate than wild-type cells . For information on bacterial polysaccharide gene nomenclature see .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DTDPGLUCOSEPP-RXN|reaction.ecocyc.DTDPGLUCOSEPP-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P37744|protein.P37744]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8034`
- `QSPROTEOME:QS00182761`

## Notes

4*protein.P37744

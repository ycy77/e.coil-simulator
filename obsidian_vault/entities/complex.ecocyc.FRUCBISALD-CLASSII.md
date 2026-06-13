---
entity_id: "complex.ecocyc.FRUCBISALD-CLASSII"
entity_type: "complex"
name: "fructose-bisphosphate aldolase class II"
source_database: "EcoCyc"
source_id: "FRUCBISALD-CLASSII"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# fructose-bisphosphate aldolase class II

`complex.ecocyc.FRUCBISALD-CLASSII`

## Static

- Type: `complex`
- Source: `EcoCyc:FRUCBISALD-CLASSII`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AB71|protein.P0AB71]]

## Enriched Summary

This enzyme catalyzes a reversible aldol cleavage/condensation reaction during glycolysis and gluconeogenesis in E. coli. In the glycolytic direction fructose 1,6-bisphosphate (FBP) is cleaved to produce glyceraldehyde 3-phosphate and dihydroxyacetone phosphate (glycerone phosphate). Two types of FBP aldolases have been distinguished, Class I and Class II. Class I FBP aldolases utilize an active site lysine residue to form a Schiff-base between the ε-amino group of lysine and the carbonyl group of the substrate. Class II FBP aldolases are dimeric and utilize a divalent metal ion in catalysis via a similar mechanism. The two also vary in subunit stoichiometry. The Class I enzymes of eukaryotes have been well studied . E. coli is one of a few organisms that expresses both classes of FBP aldolase . The Class I enzyme encoded by G7129 is induced by gluconeogenic substrates, whereas the Class II enzyme encoded by EG10282 is constitutive. When E. coli K-12 is grown on C-3 carbon sources both classes of aldolase are present, although the Class I enzyme is present only under these conditions. Therefore the Class I enzyme is most likely involved in gluconeogenesis and the Class II enzyme in glycolysis . The E. coli FRUCBISALD-CLASSII FbaA enzyme resembles the typical class II aldolase from yeast in size and amino acid composition, strongly suggesting that they are related...

## Biological Role

Catalyzes F16ALDOLASE-RXN (reaction.ecocyc.F16ALDOLASE-RXN), SEDOBISALDOL-RXN (reaction.ecocyc.SEDOBISALDOL-RXN). Bound by Zinc cation (molecule.C00038).

## Annotation

This enzyme catalyzes a reversible aldol cleavage/condensation reaction during glycolysis and gluconeogenesis in E. coli. In the glycolytic direction fructose 1,6-bisphosphate (FBP) is cleaved to produce glyceraldehyde 3-phosphate and dihydroxyacetone phosphate (glycerone phosphate). Two types of FBP aldolases have been distinguished, Class I and Class II. Class I FBP aldolases utilize an active site lysine residue to form a Schiff-base between the ε-amino group of lysine and the carbonyl group of the substrate. Class II FBP aldolases are dimeric and utilize a divalent metal ion in catalysis via a similar mechanism. The two also vary in subunit stoichiometry. The Class I enzymes of eukaryotes have been well studied . E. coli is one of a few organisms that expresses both classes of FBP aldolase . The Class I enzyme encoded by G7129 is induced by gluconeogenic substrates, whereas the Class II enzyme encoded by EG10282 is constitutive. When E. coli K-12 is grown on C-3 carbon sources both classes of aldolase are present, although the Class I enzyme is present only under these conditions. Therefore the Class I enzyme is most likely involved in gluconeogenesis and the Class II enzyme in glycolysis . The E. coli FRUCBISALD-CLASSII FbaA enzyme resembles the typical class II aldolase from yeast in size and amino acid composition, strongly suggesting that they are related. These aldolases are found both in the eukaryotic green algae and fungi, and in the prokaryotic cyanobacteria and other bacteria . A number of studies provided initial characterizations of the enzyme including mutant phenotypes , gene localization , its metabolic regulation , and evidence for its modification by phosphate and 2-mercaptoethanol . The enzyme has been cloned, overexpressed and purified in high yie

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.F16ALDOLASE-RXN|reaction.ecocyc.F16ALDOLASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SEDOBISALDOL-RXN|reaction.ecocyc.SEDOBISALDOL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AB71|protein.P0AB71]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:FRUCBISALD-CLASSII`
- `QSPROTEOME:QS00197293`

## Notes

2*protein.P0AB71

---
entity_id: "complex.ecocyc.6PFK-2-CPX"
entity_type: "complex"
name: "6-phosphofructokinase 2"
source_database: "EcoCyc"
source_id: "6PFK-2-CPX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "PFK II"
---

# 6-phosphofructokinase 2

`complex.ecocyc.6PFK-2-CPX`

## Static

- Type: `complex`
- Source: `EcoCyc:6PFK-2-CPX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P06999|protein.P06999]]

## Enriched Summary

Phosphofructokinase (Pfk) catalyzes the phosphorylation of fructose-6-phosphate on the C1 carbon during glycolysis. E. coli contains two Pfk isozymes, 6PFK-1-CPX "Pfk-1" and Pfk-2, which do not share sequence similarity . Only less than 5% of Pfk activity in the wild-type cells can be attributed to Pfk-2 . Pfk-2 is a member of the ribokinase family of sugar kinases. Pfk-2, unlike Pfk-1, does not show cooperative interaction with fructose-6-phosphate (F6P), inhibition by PEP or activation by ADP . MgATP2- is the true substrate of the enzyme . In a proteome-wide screen, Pfk-2 was found to bind citrate, glucose-6-phosphate, phosphoenolpyruvate, ATP and GTP near the active site, suggesting that the enzyme has a promiscuous active site . Pfk-2 can use tagatose-6-phosphate as a substrate ; this reaction is part of the GALACTITOLCAT-PWY pathway. Allosteric binding of MgATP2- to dimeric Pfk-2 leads to tetramerization and inhibition of enzymatic activity. Increased sugar-phosphate concentration reverts both effects , while K+ enhances allosteric inhibition by MgATP2- . The kinetics of allosteric inhibition by MgATP have been determined, and the interplay of substrate binding and allosteric binding of MgATP have been analyzed...

## Biological Role

Catalyzes 6PFRUCTPHOS-RXN (reaction.ecocyc.6PFRUCTPHOS-RXN), TAGAKIN-RXN (reaction.ecocyc.TAGAKIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Phosphofructokinase (Pfk) catalyzes the phosphorylation of fructose-6-phosphate on the C1 carbon during glycolysis. E. coli contains two Pfk isozymes, 6PFK-1-CPX "Pfk-1" and Pfk-2, which do not share sequence similarity . Only less than 5% of Pfk activity in the wild-type cells can be attributed to Pfk-2 . Pfk-2 is a member of the ribokinase family of sugar kinases. Pfk-2, unlike Pfk-1, does not show cooperative interaction with fructose-6-phosphate (F6P), inhibition by PEP or activation by ADP . MgATP2- is the true substrate of the enzyme . In a proteome-wide screen, Pfk-2 was found to bind citrate, glucose-6-phosphate, phosphoenolpyruvate, ATP and GTP near the active site, suggesting that the enzyme has a promiscuous active site . Pfk-2 can use tagatose-6-phosphate as a substrate ; this reaction is part of the GALACTITOLCAT-PWY pathway. Allosteric binding of MgATP2- to dimeric Pfk-2 leads to tetramerization and inhibition of enzymatic activity. Increased sugar-phosphate concentration reverts both effects , while K+ enhances allosteric inhibition by MgATP2- . The kinetics of allosteric inhibition by MgATP have been determined, and the interplay of substrate binding and allosteric binding of MgATP have been analyzed . Kinetic analysis of hybrid enzymes formed from combinations of mutants in the active site, the F6P binding site, or the allosteric ATP binding site suggest that catalytic turnover in each subunits is independent of the other and provide insight into the role of intersubunit interactions . The unphosphorylated form of the PTS system phosphocarrier protein PTSH-MONOMER HPr allosterically activates Pfk-2 . The dimeric state of Pfk-2 is essential for the stability and activity of the enzyme . Studies on the unfolding and folding pathways of monomeric, dimeric

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.6PFRUCTPHOS-RXN|reaction.ecocyc.6PFRUCTPHOS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TAGAKIN-RXN|reaction.ecocyc.TAGAKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P06999|protein.P06999]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:6PFK-2-CPX`
- `QSPROTEOME:QS00182741`

## Notes

2*protein.P06999

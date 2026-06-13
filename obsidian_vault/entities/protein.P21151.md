---
entity_id: "protein.P21151"
entity_type: "protein"
name: "fadA"
source_database: "UniProt"
source_id: "P21151"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fadA oldA b3845 JW5578"
---

# fadA

`protein.P21151`

## Static

- Type: `protein`
- Source: `UniProt:P21151`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the final step of fatty acid oxidation in which acetyl-CoA is released and the CoA ester of a fatty acid two carbons shorter is formed. Involved in the aerobic and anaerobic degradation of long-chain fatty acids. {ECO:0000269|PubMed:12535077, ECO:0000269|PubMed:368024, ECO:0000269|PubMed:8454629}. 3-ketoacyl-CoA thiolase (FadA) is involved in the degradation of fatty acids via the β-oxidation cycle. The enzyme acts on 3-oxoacyl-CoAs in the presence of a CoA acceptor to produce acetyl-CoA and an acyl-CoA shortened by two carbon atoms. FadA has broad chain-length specificity for substrates, but exhibits its highest activity with medium-chain substrates. FadA and FadB form a multifunctional enzyme complex (data from E. coli B in ). Overexpression of FadA and FadB can be utilized for the production of long-chain fatty acids in an engineered reversal of the β-oxidation cycle . In the reverse direction the enzyme acts on an acyl-CoA and acetyl-CoA, catalyzing a non-decarboxylative Claisen condensation reaction that forms a 3-oxo-acyl-CoA elongated by two carbons. The enzyme has a broad substrate range when working in the reverse reaction, and was shown to act on CINNAMOYL-COA and CPD-503, catalyzing two rounds of extension and resulting in formation of the styrylpyrones CPD-22601 and CPD-26560...

## Biological Role

Catalyzes acetyl-CoA:acetyl-CoA C-acetyltransferase (reaction.R00238), acyl-CoA:acetyl-CoA C-acyltransferase (reaction.R00391), succinyl-CoA:acetyl-CoA C-acyltransferase; (reaction.R00829), octanoyl-CoA:acetyl-CoA C-acyltransferase (reaction.R03778), R05506 (reaction.R05506), KETOACYLCOATHIOL-RXN (reaction.ecocyc.KETOACYLCOATHIOL-RXN), RXN-14394 (reaction.ecocyc.RXN-14394), RXN-17778 (reaction.ecocyc.RXN-17778), and 5 more. Component of trifunctional fatty acid oxidation complex (complex.ecocyc.FAO-CPLX).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00592` alpha-Linolenic acid metabolism (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco00984` Steroid degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the final step of fatty acid oxidation in which acetyl-CoA is released and the CoA ester of a fatty acid two carbons shorter is formed. Involved in the aerobic and anaerobic degradation of long-chain fatty acids. {ECO:0000269|PubMed:12535077, ECO:0000269|PubMed:368024, ECO:0000269|PubMed:8454629}.

## Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00592` alpha-Linolenic acid metabolism (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco00984` Steroid degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Outgoing Edges (14)

- `catalyzes` --> [[reaction.R00238|reaction.R00238]] `KEGG` `database` - via EC:2.3.1.16
- `catalyzes` --> [[reaction.R00391|reaction.R00391]] `KEGG` `database` - via EC:2.3.1.16
- `catalyzes` --> [[reaction.R00829|reaction.R00829]] `KEGG` `database` - via EC:2.3.1.16
- `catalyzes` --> [[reaction.R03778|reaction.R03778]] `KEGG` `database` - via EC:2.3.1.16
- `catalyzes` --> [[reaction.R05506|reaction.R05506]] `KEGG` `database` - via EC:2.3.1.16
- `catalyzes` --> [[reaction.ecocyc.KETOACYLCOATHIOL-RXN|reaction.ecocyc.KETOACYLCOATHIOL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14394|reaction.ecocyc.RXN-14394]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17778|reaction.ecocyc.RXN-17778]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17782|reaction.ecocyc.RXN-17782]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17787|reaction.ecocyc.RXN-17787]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17791|reaction.ecocyc.RXN-17791]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17795|reaction.ecocyc.RXN-17795]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17799|reaction.ecocyc.RXN-17799]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.FAO-CPLX|complex.ecocyc.FAO-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3845|gene.b3845]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21151`
- `KEGG:ecj:JW5578;eco:b3845;ecoc:C3026_20790;`
- `GeneID:948324;`
- `GO:GO:0003988; GO:0005737; GO:0006635; GO:0009062; GO:0010124; GO:0036125`
- `EC:2.3.1.16`

## Notes

3-ketoacyl-CoA thiolase FadA (EC 2.3.1.16) (Acetyl-CoA acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex subunit beta)

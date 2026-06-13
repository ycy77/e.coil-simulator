---
entity_id: "protein.P76503"
entity_type: "protein"
name: "fadI"
source_database: "UniProt"
source_id: "P76503"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fadI yfcY b2342 JW2339"
---

# fadI

`protein.P76503`

## Static

- Type: `protein`
- Source: `UniProt:P76503`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Catalyzes the final step of fatty acid oxidation in which acetyl-CoA is released and the CoA ester of a fatty acid two carbons shorter is formed. Strongly involved in the anaerobic degradation of long and medium-chain fatty acids in the presence of nitrate and weakly involved in the aerobic degradation of long-chain fatty acids. {ECO:0000269|PubMed:12270828, ECO:0000269|PubMed:12535077}. During anaerobic β-oxidation of fatty acids, G7213 FadI, G7212 FadJ, and EG12357 FadK serve functions parallel to those of EG10278 FadA, EG10279 FadB, and EG11530 FadD in the aerobic pathway . FadI and FadJ also exhibit partial functional redundancy with FadA and FadB under aerobic conditions; the two complexes are proposed to increase efficiency of β-oxidation by favoring substrates of different chain length . A strain producing FadI and FadJ from a plasmid exhibits thiolase activity with β-ketoacyl-CoAs of 6 to 12 carbon units, but not with acetoacetyl-CoA . It has been shown that the β-oxidation enzymes can be induced to work in the reverse direction, a phenomenon that is being utilized for metabolic engineering . In the reverse direction FadI acts on an acyl-CoA and acetyl-CoA, catalyzing a non-decarboxylative Claisen condensation reaction that forms a 3-oxo-acyl-CoA elongated by two carbons...

## Biological Role

Catalyzes acetyl-CoA:acetyl-CoA C-acetyltransferase (reaction.R00238), acyl-CoA:acetyl-CoA C-acyltransferase (reaction.R00391), succinyl-CoA:acetyl-CoA C-acyltransferase; (reaction.R00829), octanoyl-CoA:acetyl-CoA C-acyltransferase (reaction.R03778), R05506 (reaction.R05506), KETOACYLCOATHIOL-RXN (reaction.ecocyc.KETOACYLCOATHIOL-RXN), RXN-14394 (reaction.ecocyc.RXN-14394), RXN-17778 (reaction.ecocyc.RXN-17778), and 5 more. Component of anaerobic fatty acid β-oxidation complex (complex.ecocyc.CPLX0-1668).

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

FUNCTION: Catalyzes the final step of fatty acid oxidation in which acetyl-CoA is released and the CoA ester of a fatty acid two carbons shorter is formed. Strongly involved in the anaerobic degradation of long and medium-chain fatty acids in the presence of nitrate and weakly involved in the aerobic degradation of long-chain fatty acids. {ECO:0000269|PubMed:12270828, ECO:0000269|PubMed:12535077}.

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
- `is_component_of` --> [[complex.ecocyc.CPLX0-1668|complex.ecocyc.CPLX0-1668]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2342|gene.b2342]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76503`
- `KEGG:ecj:JW2339;eco:b2342;ecoc:C3026_13035;`
- `GeneID:948823;`
- `GO:GO:0003857; GO:0003985; GO:0003988; GO:0004300; GO:0005737; GO:0005829; GO:0006635; GO:0033542; GO:0036125`
- `EC:2.3.1.16`

## Notes

3-ketoacyl-CoA thiolase FadI (EC 2.3.1.16) (ACSs) (Acetyl-CoA acyltransferase) (Acyl-CoA ligase) (Beta-ketothiolase) (Fatty acid oxidation complex subunit beta)

---
entity_id: "complex.ecocyc.CPLX0-8158"
entity_type: "complex"
name: "D-lactate dehydrogenase"
source_database: "EcoCyc"
source_id: "CPLX0-8158"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# D-lactate dehydrogenase

`complex.ecocyc.CPLX0-8158`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8158`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P52643|protein.P52643]]

## Enriched Summary

LdhA is a soluble NAD-linked lactate dehydrogenase (LDH) that is specific for the production of D-lactate . LdhA is a homotetramer and shows positive homotropic cooperativity under higher pH conditions . E. coli contains two other lactate dehydrogenases: DLACTDEHYDROGFAD-MONOMER and L-LACTDEHYDROGFMN-MONOMER. Both are membrane-associated flavoproteins required for aerobic growth on lactate. The enzyme is present under aerobic conditions but is induced when E. coli is grown on a variety of sugars under anaerobic conditions at acidic pH . Unlike most of the genes involved in anaerobic respiration, ldhA is not activated by Fnr; rather the ArcAB system and several genes involved in the control of carbohydrate metabolism (csrAB and mlc) appear to regulate expression . Several metabolic genes, including ldhA, were found upregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 . The expression of ldhA is negatively affected by the transcriptional regulator ArcA . Reports disagree on whether or not expression is induced by heat shock. However, ldhA belongs to the σ32 regulon . E. coli carrying ldhA mutations show no observable growth defect and can still ferment sugars to a variety of products other than lactate...

## Biological Role

Catalyzes DLACTDEHYDROGNAD-RXN (reaction.ecocyc.DLACTDEHYDROGNAD-RXN).

## Annotation

LdhA is a soluble NAD-linked lactate dehydrogenase (LDH) that is specific for the production of D-lactate . LdhA is a homotetramer and shows positive homotropic cooperativity under higher pH conditions . E. coli contains two other lactate dehydrogenases: DLACTDEHYDROGFAD-MONOMER and L-LACTDEHYDROGFMN-MONOMER. Both are membrane-associated flavoproteins required for aerobic growth on lactate. The enzyme is present under aerobic conditions but is induced when E. coli is grown on a variety of sugars under anaerobic conditions at acidic pH . Unlike most of the genes involved in anaerobic respiration, ldhA is not activated by Fnr; rather the ArcAB system and several genes involved in the control of carbohydrate metabolism (csrAB and mlc) appear to regulate expression . Several metabolic genes, including ldhA, were found upregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 . The expression of ldhA is negatively affected by the transcriptional regulator ArcA . Reports disagree on whether or not expression is induced by heat shock. However, ldhA belongs to the σ32 regulon . E. coli carrying ldhA mutations show no observable growth defect and can still ferment sugars to a variety of products other than lactate . The ldhA gene is a frequent target for mutations in metabolic engineering, most often to eliminate production of undesirable fermentation side products, but also to specifically produce D-lactate, e.g. . The enzyme can be acetylated on several L-lysine residues, including K9, K70, K154, and K248. A K9R mutation improves lactate production 1.74 fold as compared with the wild type, while a K154Q-K248Q double mutation inhibits lactate accumulation .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DLACTDEHYDROGNAD-RXN|reaction.ecocyc.DLACTDEHYDROGNAD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P52643|protein.P52643]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8158`
- `QSPROTEOME:QS00181761`

## Notes

4*protein.P52643

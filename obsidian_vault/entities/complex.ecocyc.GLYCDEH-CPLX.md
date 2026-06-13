---
entity_id: "complex.ecocyc.GLYCDEH-CPLX"
entity_type: "complex"
name: "L-1,2-propanediol dehydrogenase / glycerol dehydrogenase"
source_database: "EcoCyc"
source_id: "GLYCDEH-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-1,2-propanediol dehydrogenase / glycerol dehydrogenase

`complex.ecocyc.GLYCDEH-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLYCDEH-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9S5|protein.P0A9S5]]

## Enriched Summary

The physiological function of the GldA enzyme has long been unclear. The enzyme was independently isolated as an EC-1.1.1.6, and an EC-1.1.1.75. At that time, 1-AMINO-PROPAN-2-OL (the product of the latter activity) was thought to be an intermediate for the biosynthesis of vitamin B12, and although E. coli is unable to synthesize vitamin B12 de novo, enzymes catalyzing the synthesis of this compound were sought . It was later confirmed that GldA catalyzes both activities . The primary in vivo role of GldA was proposed to be the removal of DIHYDROXYACETONE by converting it to GLYCEROL . However, a dual role in the fermentation of glycerol has also been established . Glycerol dissimilation in E. coli can be accomplished by two different pathways in E. coli. The PWY0-381 pathway, which was characterized first, requires the presence of a terminal electron acceptor and utilizes an ATP-dependent kinase of the Glp system, which phosphorylates glycerol to glycerol-3-phosphate. However, upon inactivation of the kinase and selection for growth on glycerol , it was found that GldA was able to support glycerol fermentation (see GLYCEROLMETAB-PWY). GldA is involved in glycerol fermentation both as a glycerol dehydrogenase, producing dihydroxyacetone, and as a ENZRXN0-6324, regenerating NAD+ by producing PROPANE-1-2-DIOL from ACETOL...

## Biological Role

Catalyzes AMINOPROPDEHYDROG-RXN (reaction.ecocyc.AMINOPROPDEHYDROG-RXN), GLYCDEH-RXN (reaction.ecocyc.GLYCDEH-RXN), RXN-8632 (reaction.ecocyc.RXN-8632).

## Annotation

The physiological function of the GldA enzyme has long been unclear. The enzyme was independently isolated as an EC-1.1.1.6, and an EC-1.1.1.75. At that time, 1-AMINO-PROPAN-2-OL (the product of the latter activity) was thought to be an intermediate for the biosynthesis of vitamin B12, and although E. coli is unable to synthesize vitamin B12 de novo, enzymes catalyzing the synthesis of this compound were sought . It was later confirmed that GldA catalyzes both activities . The primary in vivo role of GldA was proposed to be the removal of DIHYDROXYACETONE by converting it to GLYCEROL . However, a dual role in the fermentation of glycerol has also been established . Glycerol dissimilation in E. coli can be accomplished by two different pathways in E. coli. The PWY0-381 pathway, which was characterized first, requires the presence of a terminal electron acceptor and utilizes an ATP-dependent kinase of the Glp system, which phosphorylates glycerol to glycerol-3-phosphate. However, upon inactivation of the kinase and selection for growth on glycerol , it was found that GldA was able to support glycerol fermentation (see GLYCEROLMETAB-PWY). GldA is involved in glycerol fermentation both as a glycerol dehydrogenase, producing dihydroxyacetone, and as a ENZRXN0-6324, regenerating NAD+ by producing PROPANE-1-2-DIOL from ACETOL . Different studies have reported that GldA is able to act on a large number of additional C2-C4 alcohols, including GLYCOL, 3-AMINO-12-PROPANEDIOL, CPD0-1951, CPD0-1953, CPD-12010, CPD-12276, and 2-3-Butanediols "2,3-butanediol" . A broad survey of aldehyde reductases showed that GldA was one of several endogenous aldehyde reductases that contribute to the degradation of desired aldehyde end products of metabolic engineering . A later study focused on Gl

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.AMINOPROPDEHYDROG-RXN|reaction.ecocyc.AMINOPROPDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GLYCDEH-RXN|reaction.ecocyc.GLYCDEH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-8632|reaction.ecocyc.RXN-8632]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9S5|protein.P0A9S5]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## External IDs

- `EcoCyc:GLYCDEH-CPLX`
- `QSPROTEOME:QS00181573`

## Notes

8*protein.P0A9S5

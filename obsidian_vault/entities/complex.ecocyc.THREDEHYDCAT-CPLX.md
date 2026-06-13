---
entity_id: "complex.ecocyc.THREDEHYDCAT-CPLX"
entity_type: "complex"
name: "catabolic threonine dehydratase"
source_database: "EcoCyc"
source_id: "THREDEHYDCAT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "biodegradative L-threonine dehydrase"
---

# catabolic threonine dehydratase

`complex.ecocyc.THREDEHYDCAT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:THREDEHYDCAT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AGF6|protein.P0AGF6]]

## Enriched Summary

Catabolic threonine dehydratase (TdcB) carries out the first step in threonine degradation and is one of several enzymes carrying out the first step in serine degradation. It is only expressed during anaerobic growth in the absence of glucose. Although the conversion of threonine into oxobutanoate is also the first step in the synthesis of isoleucine from threonine, TdcB is not expected to play a major role in that biosynthetic pathway due to this limited expression profile. TdcB catalyzes the conversion of L-threonine into 2-oxobutanoate and ammonia . Most of the enzyme appears to wait in an inactive state until it meets L-threonine, at which point the reaction proceeds via dehydration and alpha-beta elimination . TdcB also catalyzes the conversion of L-serine into pyruvate and ammonia . TdcB abundance is regulated by a number of inputs, most of them involved in ensuring that it is only expressed during anaerobic growth in the absence of glucose . Following a transition from aerobic to anaerobic growth, cAMP levels rise dramatically. This, in turn, leads to increased expression of tdcB and consequently high levels of catabolic threanine deaminase . tdcB is subject to countervailing catabolite repression by glucose, gluconate, glycerol, and pyruvate . Synthesis of TdcB is similarly blocked by oxygen, and does not occur at concentrations of 6 µM or above...

## Biological Role

Catalyzes 4.3.1.17-RXN (reaction.ecocyc.4.3.1.17-RXN), THREDEHYD-RXN (reaction.ecocyc.THREDEHYD-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Catabolic threonine dehydratase (TdcB) carries out the first step in threonine degradation and is one of several enzymes carrying out the first step in serine degradation. It is only expressed during anaerobic growth in the absence of glucose. Although the conversion of threonine into oxobutanoate is also the first step in the synthesis of isoleucine from threonine, TdcB is not expected to play a major role in that biosynthetic pathway due to this limited expression profile. TdcB catalyzes the conversion of L-threonine into 2-oxobutanoate and ammonia . Most of the enzyme appears to wait in an inactive state until it meets L-threonine, at which point the reaction proceeds via dehydration and alpha-beta elimination . TdcB also catalyzes the conversion of L-serine into pyruvate and ammonia . TdcB abundance is regulated by a number of inputs, most of them involved in ensuring that it is only expressed during anaerobic growth in the absence of glucose . Following a transition from aerobic to anaerobic growth, cAMP levels rise dramatically. This, in turn, leads to increased expression of tdcB and consequently high levels of catabolic threanine deaminase . tdcB is subject to countervailing catabolite repression by glucose, gluconate, glycerol, and pyruvate . Synthesis of TdcB is similarly blocked by oxygen, and does not occur at concentrations of 6 µM or above . Although they are less clearly involved with TdcB's apparent role as an anaerobic, non-glucose growth enzyme, leucine, serine, threonine, valine, DNA gyrase inhibitors and mutations in gyrB are all numbered among inducers of TdcB . The primary regulators of TdcB's enzymatic activity operate by moving TdcB back and forth along an oligomerization axis. AMP promotes formation of the active tetrameric form of the enzyme. C

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.4.3.1.17-RXN|reaction.ecocyc.4.3.1.17-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.THREDEHYD-RXN|reaction.ecocyc.THREDEHYD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AGF6|protein.P0AGF6]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:THREDEHYDCAT-CPLX`
- `QSPROTEOME:QS00203717`

## Notes

4*protein.P0AGF6

---
entity_id: "molecule.ecocyc.NADH-P-OR-NOP"
entity_type: "small_molecule"
name: "NAD(P)H"
source_database: "EcoCyc"
source_id: "NADH-P-OR-NOP"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "β-NAD(P)H"
---

# NAD(P)H

`molecule.ecocyc.NADH-P-OR-NOP`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:NADH-P-OR-NOP`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

NADH-P-OR-NOP is a class of compounds including the instances NADH and NADPH. NAD-P-OR-NOP is a class of compounds including the instances NAD and NADP. NAD and NADP are dinucleotides containing one NIACINAMIDE base and one ADENINE base. Each nucleotide is connected to a ribose sugar at position 1, and the two riboses are connected at their 5 position via a diphosphate. The only difference between the two is that in NADP there is an additional phosphate group at the 2' position of the ribose that carries the adenine moiety. These molecules are biological carriers of reductive equivalents (i.e. high potential electrons). They are often referred to as coenzymes, although in most of their reactions they function as cosubstrates rather than true coenzymes. The most common function of NAD is to accept two electrons and a proton (a hydride ion) from a substrate that is being oxidized. This reduction converts NAD to NADH, the reduced form. NADH then diffuses or is transported to a terminal oxidase, where the electrons are passed on, regenerating the oxidized form. NADPH, on the other hand, is mostly involved in biosynthetic reactions, where it serves as an electron donor. NADPH is formed by reduction of NADP, which occurs by different mechanisms in different types of organisms. In photosynthetic organisms NADP is reduced by CPLX-84...

## Biological Role

Consumed as substrate in 14 reaction(s). Produced in 22 reaction(s). Binds thiC (protein.P30136).

## Annotation

NADH-P-OR-NOP is a class of compounds including the instances NADH and NADPH. NAD-P-OR-NOP is a class of compounds including the instances NAD and NADP. NAD and NADP are dinucleotides containing one NIACINAMIDE base and one ADENINE base. Each nucleotide is connected to a ribose sugar at position 1, and the two riboses are connected at their 5 position via a diphosphate. The only difference between the two is that in NADP there is an additional phosphate group at the 2' position of the ribose that carries the adenine moiety. These molecules are biological carriers of reductive equivalents (i.e. high potential electrons). They are often referred to as coenzymes, although in most of their reactions they function as cosubstrates rather than true coenzymes. The most common function of NAD is to accept two electrons and a proton (a hydride ion) from a substrate that is being oxidized. This reduction converts NAD to NADH, the reduced form. NADH then diffuses or is transported to a terminal oxidase, where the electrons are passed on, regenerating the oxidized form. NADPH, on the other hand, is mostly involved in biosynthetic reactions, where it serves as an electron donor. NADPH is formed by reduction of NADP, which occurs by different mechanisms in different types of organisms. In photosynthetic organisms NADP is reduced by CPLX-84. In heterotrophic organisms it is reduced by central metabolism processes such as the pentose phosphate pathway (see OXIDATIVEPENT-PWY).

## Outgoing Edges (37)

- `binds` --> [[protein.P30136|protein.P30136]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.ecocyc.1.1.1.264-RXN|reaction.ecocyc.1.1.1.264-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.1.5.1.20-RXN|reaction.ecocyc.1.5.1.20-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.1.5.1.34-RXN|reaction.ecocyc.1.5.1.34-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.FMNREDUCT-RXN|reaction.ecocyc.FMNREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUCONATE-5-DEHYDROGENASE-RXN|reaction.ecocyc.GLUCONATE-5-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLYC3PDEHYDROGBIOSYN-RXN|reaction.ecocyc.GLYC3PDEHYDROGBIOSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.HOMOSERDEHYDROG-RXN|reaction.ecocyc.HOMOSERDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PYRROLINECARBREDUCT-RXN|reaction.ecocyc.PYRROLINECARBREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.QUINATE-5-DEHYDROGENASE-RXN|reaction.ecocyc.QUINATE-5-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.R165-RXN|reaction.ecocyc.R165-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-11174|reaction.ecocyc.RXN-11174]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12445|reaction.ecocyc.RXN-12445]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-13853|reaction.ecocyc.RXN-13853]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14014|reaction.ecocyc.RXN-14014]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14641|reaction.ecocyc.RXN-14641]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15892|reaction.ecocyc.RXN-15892]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16333|reaction.ecocyc.RXN-16333]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-2962|reaction.ecocyc.RXN-2962]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-7632|reaction.ecocyc.RXN-7632]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-3922|reaction.ecocyc.RXN0-3922]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5455|reaction.ecocyc.RXN0-5455]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TSA-REDUCT-RXN|reaction.ecocyc.TSA-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.FAD-RED-RXN|reaction.ecocyc.FAD-RED-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.FMN-RED-RXN|reaction.ecocyc.FMN-RED-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.NQOR-RXN|reaction.ecocyc.NQOR-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.R621-RXN|reaction.ecocyc.R621-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10745|reaction.ecocyc.RXN-10745]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10745-1|reaction.ecocyc.RXN-10745-1]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18258|reaction.ecocyc.RXN-18258]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18376|reaction.ecocyc.RXN-18376]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-24132|reaction.ecocyc.RXN-24132]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-5921|reaction.ecocyc.RXN-5921]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-3381|reaction.ecocyc.RXN0-3381]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7386|reaction.ecocyc.RXN0-7386]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7427|reaction.ecocyc.RXN0-7427]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7453|reaction.ecocyc.RXN0-7453]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:NADH-P-OR-NOP`
- `SEED:cpd27640`
- `METANETX:MNXM162231`
- `CHEBI:13392`

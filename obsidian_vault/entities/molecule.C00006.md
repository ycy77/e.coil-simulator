---
entity_id: "molecule.C00006"
entity_type: "small_molecule"
name: "NADP+"
source_database: "KEGG"
source_id: "C00006"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "NADP+"
  - "NADP"
  - "Nicotinamide adenine dinucleotide phosphate"
  - "beta-Nicotinamide adenine dinucleotide phosphate"
  - "TPN"
  - "Triphosphopyridine nucleotide"
  - "beta-NADP+"
---

# NADP+

`molecule.C00006`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00006`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: NADP+; NADP; Nicotinamide adenine dinucleotide phosphate; beta-Nicotinamide adenine dinucleotide phosphate; TPN; Triphosphopyridine nucleotide; beta-NADP+ NAD and NADP are dinucleotides containing one NIACINAMIDE base and one ADENINE base. Each nucleotide is connected to a ribose sugar at position 1, and the two riboses are connected at their 5 position via a diphosphate. The only difference between the two is that in NADP there is an additional phosphate group at the 2' position of the ribose that carries the adenine moiety. These molecules are biological carriers of reductive equivalents (i.e. high potential electrons). Most of the time they function as cosubstrates, and in some cases they function as Cofactors cofactors. They are often referred to by the obsolete term "coenzymes". The most common function of NAD is to accept two electrons and a proton (a hydride ion) from a substrate that is being oxidized. This reduction converts NAD to NADH, the reduced form. NADH then diffuses or is transported to a terminal oxidase, where the electrons are passed on, regenerating the oxidized form. NADPH, on the other hand, is mostly involved in biosynthetic reactions, where it serves as an electron donor. NADPH is formed by reduction of NADP, which occurs by different mechanisms in different types of organisms. In photosynthetic organisms NADP is reduced by CPLX-84...

## Biological Role

Consumed as substrate in 139 reaction(s). Produced in 20 reaction(s). Binds ADP-L-glycero-D-mannoheptose 6-epimerase (complex.ecocyc.CPLX0-3681), GDP-mannose 4,6-dehydratase (complex.ecocyc.GDPMANDEHYDRA-CPLX).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Annotation

KEGG compound: NADP+; NADP; Nicotinamide adenine dinucleotide phosphate; beta-Nicotinamide adenine dinucleotide phosphate; TPN; Triphosphopyridine nucleotide; beta-NADP+

## Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Outgoing Edges (172)

- `binds` --> [[complex.ecocyc.CPLX0-3681|complex.ecocyc.CPLX0-3681]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.GDPMANDEHYDRA-CPLX|complex.ecocyc.GDPMANDEHYDRA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.R00104|reaction.R00104]] `KEGG` `database` - C00002 + C00003 <=> C00008 + C00006
- `is_product_of` --> [[reaction.R00112|reaction.R00112]] `KEGG` `database` - C00005 + C00003 <=> C00006 + C00004
- `is_product_of` --> [[reaction.R02364|reaction.R02364]] `KEGG` `database` - 2 C15602 + C00005 + C00080 <=> 2 C05309 + C00006
- `is_product_of` --> [[reaction.R05725|reaction.R05725]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00005 + C00080 <=> 2 C00244 + C00006
- `is_product_of` --> [[reaction.R07763|reaction.R07763]] `KEGG` `database` - C16219 + C00005 + C00080 <=> C16220 + C00006
- `is_product_of` --> [[reaction.R11911|reaction.R11911]] `KEGG` `database` - C00318 + C00005 + C00080 + C00007 <=> C21761 + C00565 + C00006 + C00001
- `is_product_of` --> [[reaction.ecocyc.2-OCTAPRENYL-6-METHOXYPHENOL-HYDROX-RXN|reaction.ecocyc.2-OCTAPRENYL-6-METHOXYPHENOL-HYDROX-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.2-OCTAPRENYLPHENOL-HYDROX-RXN|reaction.ecocyc.2-OCTAPRENYLPHENOL-HYDROX-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.NAD-KIN-RXN|reaction.ecocyc.NAD-KIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PYRNUTRANSHYDROGEN-RXN|reaction.ecocyc.PYRNUTRANSHYDROGEN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.QOR-RXN|reaction.ecocyc.QOR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-11319|reaction.ecocyc.RXN-11319]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-2042|reaction.ecocyc.RXN0-2042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-271|reaction.ecocyc.RXN0-271]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5387|reaction.ecocyc.RXN0-5387]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6676|reaction.ecocyc.RXN0-6676]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6677|reaction.ecocyc.RXN0-6677]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7000|reaction.ecocyc.RXN0-7000]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7385|reaction.ecocyc.RXN0-7385]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-277|reaction.ecocyc.TRANS-RXN0-277]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00114|reaction.R00114]] `KEGG` `database` - 2 C00025 + C00006 <=> C00064 + C00026 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00115|reaction.R00115]] `KEGG` `database` - 2 C00051 + C00006 <=> C00127 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00146|reaction.R00146]] `KEGG` `database` - C05167 + C00001 + C00006 <=> C00161 + C00014 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00216|reaction.R00216]] `KEGG` `database` - C00149 + C00006 <=> C00022 + C00011 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00248|reaction.R00248]] `KEGG` `database` - C00025 + C00006 + C00001 <=> C00026 + C00014 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00267|reaction.R00267]] `KEGG` `database` - C00311 + C00006 <=> C00026 + C00011 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00465|reaction.R00465]] `KEGG` `database` - C00160 + C00006 <=> C00048 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00625|reaction.R00625]] `KEGG` `database` - C00226 + C00006 <=> C00071 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00708|reaction.R00708]] `KEGG` `database` - C03912 + C00006 + 2 C00001 <=> C00025 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00714|reaction.R00714]] `KEGG` `database` - C00232 + C00006 + C00001 <=> C00042 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00746|reaction.R00746]] `KEGG` `database` - C00469 + C00006 <=> C00084 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00835|reaction.R00835]] `KEGG` `database` - C00092 + C00006 <=> C01236 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00844|reaction.R00844]] `KEGG` `database` - C00093 + C00006 <=> C00111 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R01134|reaction.R01134]] `KEGG` `database` - C00130 + C00014 + C00006 <=> C00144 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R01528|reaction.R01528]] `KEGG` `database` - C00345 + C00006 <=> C00199 + C00011 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R01739|reaction.R01739]] `KEGG` `database` - C00257 + C00006 <=> C06473 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R01740|reaction.R01740]] `KEGG` `database` - C00257 + C00006 <=> C01062 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R01747|reaction.R01747]] `KEGG` `database` - C00258 + C00006 <=> C01146 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R01899|reaction.R01899]] `KEGG` `database` - C00311 + C00006 <=> C05379 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R03192|reaction.R03192]] `KEGG` `database` - C01050 + C00006 <=> C04631 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R03443|reaction.R03443]] `KEGG` `database` - C01250 + C00009 + C00006 <=> C04133 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R03458|reaction.R03458]] `KEGG` `database` - C04454 + C00006 <=> C01268 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R04430|reaction.R04430]] `KEGG` `database` - C05745 + C00006 <=> C04246 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R04439|reaction.R04439]] `KEGG` `database` - C04272 + C00006 <=> C06010 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R04440|reaction.R04440]] `KEGG` `database` - C04272 + C00006 <=> C04181 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R04725|reaction.R04725]] `KEGG` `database` - C05223 + C00006 <=> C05758 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R04959|reaction.R04959]] `KEGG` `database` - C05752 + C00006 <=> C05751 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R04962|reaction.R04962]] `KEGG` `database` - C05755 + C00006 <=> C05754 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R04964|reaction.R04964]] `KEGG` `database` - C05757 + C00006 <=> C05756 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R05231|reaction.R05231]] `KEGG` `database` - C06103 + C00006 <=> C06102 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R08878|reaction.R08878]] `KEGG` `database` - C15673 + C00006 <=> C02780 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R08879|reaction.R08879]] `KEGG` `database` - C01062 + C00006 <=> C02780 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R08880|reaction.R08880]] `KEGG` `database` - C00770 + C00006 <=> C15673 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R09820|reaction.R09820]] `KEGG` `database` - C19946 + C00006 + C00001 <=> C19945 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R10852|reaction.R10852]] `KEGG` `database` - C05519 + C00006 <=> C01888 + C00011 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R11485|reaction.R11485]] `KEGG` `database` - C02745 + C00006 <=> C02869 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R12620|reaction.R12620]] `KEGG` `database` - C00658 + C00006 <=> C22258 + C00005 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.168-RXN|reaction.ecocyc.1.1.1.168-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.215-RXN|reaction.ecocyc.1.1.1.215-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.271-RXN|reaction.ecocyc.1.1.1.271-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.274-RXN|reaction.ecocyc.1.1.1.274-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.283-RXN|reaction.ecocyc.1.1.1.283-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN|reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.25-DIOXOVALERATE-DEHYDROGENASE-RXN|reaction.ecocyc.25-DIOXOVALERATE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.3-OXOACYL-ACP-REDUCT-RXN|reaction.ecocyc.3-OXOACYL-ACP-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ACETOLACTREDUCTOISOM-RXN|reaction.ecocyc.ACETOLACTREDUCTOISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ACETOOHBUTREDUCTOISOM-RXN|reaction.ecocyc.ACETOOHBUTREDUCTOISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN|reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ALDEHYDE-DEHYDROGENASE-NADP_-RXN|reaction.ecocyc.ALDEHYDE-DEHYDROGENASE-NADP_-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN|reaction.ecocyc.ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DIENOYLCOAREDUCT-RXN|reaction.ecocyc.DIENOYLCOAREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN|reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DTDPDEHYRHAMREDUCT-RXN|reaction.ecocyc.DTDPDEHYRHAMREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DXPREDISOM-RXN|reaction.ecocyc.DXPREDISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ENOYL-ACP-REDUCT-NADPH-RXN|reaction.ecocyc.ENOYL-ACP-REDUCT-NADPH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.FCLREDUCT-RXN|reaction.ecocyc.FCLREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.FLAVONADPREDUCT-RXN|reaction.ecocyc.FLAVONADPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLU6PDEHYDROG-RXN|reaction.ecocyc.GLU6PDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTAMATESYN-RXN|reaction.ecocyc.GLUTAMATESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTATHIONE-REDUCT-NADPH-RXN|reaction.ecocyc.GLUTATHIONE-REDUCT-NADPH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTDEHYD-RXN|reaction.ecocyc.GLUTDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTRNAREDUCT-RXN|reaction.ecocyc.GLUTRNAREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUTSEMIALDEHYDROG-RXN|reaction.ecocyc.GLUTSEMIALDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLYOXYLATE-REDUCTASE-NADP_-RXN|reaction.ecocyc.GLYOXYLATE-REDUCTASE-NADP_-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GMP-REDUCT-RXN|reaction.ecocyc.GMP-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ISOCITDEH-RXN|reaction.ecocyc.ISOCITDEH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.L-IDONATE-2-DEHYDROGENASE-RXN|reaction.ecocyc.L-IDONATE-2-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MALATE-DEHYDROGENASE-NADP_-RXN|reaction.ecocyc.MALATE-DEHYDROGENASE-NADP_-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MALIC-NADP-RXN|reaction.ecocyc.MALIC-NADP-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.METHYLENETHFDEHYDROG-NADP-RXN|reaction.ecocyc.METHYLENETHFDEHYDROG-NADP-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.N-ACETYLGLUTPREDUCT-RXN|reaction.ecocyc.N-ACETYLGLUTPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.NADPH-DEHYDROGENASE-FLAVIN-RXN|reaction.ecocyc.NADPH-DEHYDROGENASE-FLAVIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PYRIDOXINE-4-DEHYDROGENASE-RXN|reaction.ecocyc.PYRIDOXINE-4-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.R303-RXN|reaction.ecocyc.R303-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RIBOFLAVINSYNREDUC-RXN|reaction.ecocyc.RIBOFLAVINSYNREDUC-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10655|reaction.ecocyc.RXN-10655]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10659|reaction.ecocyc.RXN-10659]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11476|reaction.ecocyc.RXN-11476]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11480|reaction.ecocyc.RXN-11480]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12444|reaction.ecocyc.RXN-12444]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15743|reaction.ecocyc.RXN-15743]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15744|reaction.ecocyc.RXN-15744]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16000|reaction.ecocyc.RXN-16000]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16001|reaction.ecocyc.RXN-16001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16003|reaction.ecocyc.RXN-16003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17897|reaction.ecocyc.RXN-17897]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19329|reaction.ecocyc.RXN-19329]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20084|reaction.ecocyc.RXN-20084]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20767|reaction.ecocyc.RXN-20767]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21503|reaction.ecocyc.RXN-21503]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23340|reaction.ecocyc.RXN-23340]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-24048|reaction.ecocyc.RXN-24048]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-24049|reaction.ecocyc.RXN-24049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-5822|reaction.ecocyc.RXN-5822]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8182|reaction.ecocyc.RXN-8182]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8772|reaction.ecocyc.RXN-8772]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8773|reaction.ecocyc.RXN-8773]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8974|reaction.ecocyc.RXN-8974]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9087|reaction.ecocyc.RXN-9087]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-924|reaction.ecocyc.RXN-924]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9514|reaction.ecocyc.RXN-9514]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9518|reaction.ecocyc.RXN-9518]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9524|reaction.ecocyc.RXN-9524]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9528|reaction.ecocyc.RXN-9528]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9532|reaction.ecocyc.RXN-9532]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9536|reaction.ecocyc.RXN-9536]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9540|reaction.ecocyc.RXN-9540]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9556|reaction.ecocyc.RXN-9556]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9951|reaction.ecocyc.RXN-9951]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9952|reaction.ecocyc.RXN-9952]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1281|reaction.ecocyc.RXN0-1281]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1941|reaction.ecocyc.RXN0-1941]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2142|reaction.ecocyc.RXN0-2142]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2201|reaction.ecocyc.RXN0-2201]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-300|reaction.ecocyc.RXN0-300]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-3962|reaction.ecocyc.RXN0-3962]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4022|reaction.ecocyc.RXN0-4022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4281|reaction.ecocyc.RXN0-4281]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5101|reaction.ecocyc.RXN0-5101]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5141|reaction.ecocyc.RXN0-5141]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5410|reaction.ecocyc.RXN0-5410]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6367|reaction.ecocyc.RXN0-6367]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6487|reaction.ecocyc.RXN0-6487]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6511|reaction.ecocyc.RXN0-6511]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6555|reaction.ecocyc.RXN0-6555]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6941|reaction.ecocyc.RXN0-6941]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7020|reaction.ecocyc.RXN0-7020]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7021|reaction.ecocyc.RXN0-7021]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7119|reaction.ecocyc.RXN0-7119]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7154|reaction.ecocyc.RXN0-7154]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7313|reaction.ecocyc.RXN0-7313]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXNMETA-12672|reaction.ecocyc.RXNMETA-12672]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SHIKIMATE-5-DEHYDROGENASE-RXN|reaction.ecocyc.SHIKIMATE-5-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SUCCSEMIALDDEHYDROG-RXN|reaction.ecocyc.SUCCSEMIALDDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SULFITE-REDUCT-RXN|reaction.ecocyc.SULFITE-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.THIOREDOXIN-REDUCT-NADPH-RXN|reaction.ecocyc.THIOREDOXIN-REDUCT-NADPH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANSENOYLCOARED-RXN|reaction.ecocyc.TRANSENOYLCOARED-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UDPNACETYLMURAMATEDEHYDROG-RXN|reaction.ecocyc.UDPNACETYLMURAMATEDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.YIAE1-RXN|reaction.ecocyc.YIAE1-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.1.1.1.271-RXN|reaction.ecocyc.1.1.1.271-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN|reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ACETOLACTREDUCTOISOM-RXN|reaction.ecocyc.ACETOLACTREDUCTOISOM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.FMNREDUCT-RXN|reaction.ecocyc.FMNREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.MALIC-NADP-RXN|reaction.ecocyc.MALIC-NADP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.NADPH-DEHYDROGENASE-FLAVIN-RXN|reaction.ecocyc.NADPH-DEHYDROGENASE-FLAVIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PHOSICITDEHASE-RXN|reaction.ecocyc.PHOSICITDEHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PYRROLINECARBREDUCT-RXN|reaction.ecocyc.PYRROLINECARBREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-14014|reaction.ecocyc.RXN-14014]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.SULFITE-REDUCT-RXN|reaction.ecocyc.SULFITE-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANSENOYLCOARED-RXN|reaction.ecocyc.TRANSENOYLCOARED-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.PYRNUTRANSHYDROGEN-CPLX|complex.ecocyc.PYRNUTRANSHYDROGEN-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00006`

## Notes

Included because it appears in at least one E. coli KEGG pathway.

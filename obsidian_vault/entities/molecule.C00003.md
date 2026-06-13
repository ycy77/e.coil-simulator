---
entity_id: "molecule.C00003"
entity_type: "small_molecule"
name: "NAD+"
source_database: "KEGG"
source_id: "C00003"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "NAD+"
  - "NAD"
  - "Nicotinamide adenine dinucleotide"
  - "DPN"
  - "Diphosphopyridine nucleotide"
  - "Nadide"
  - "beta-NAD+"
---

# NAD+

`molecule.C00003`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00003`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: NAD+; NAD; Nicotinamide adenine dinucleotide; DPN; Diphosphopyridine nucleotide; Nadide; beta-NAD+ NAD and NADP are dinucleotides containing one NIACINAMIDE base and one ADENINE base. Each nucleotide is connected to a ribose sugar at position 1, and the two riboses are connected at their 5 position via a diphosphate. The only difference between the two is that in NADP there is an additional phosphate group at the 2' position of the ribose that carries the adenine moiety. These molecules are biological carriers of reductive equivalents (i.e. high potential electrons). Most of the time they function as cosubstrates, and in some cases they function as Cofactors cofactors. They are often referred to by the obsolete term "coenzymes". The most common function of NAD is to accept two electrons and a proton (a hydride ion) from a substrate that is being oxidized. This reduction converts NAD to NADH, the reduced form. NADH then diffuses or is transported to a terminal oxidase, where the electrons are passed on, regenerating the oxidized form. NADPH, on the other hand, is mostly involved in biosynthetic reactions, where it serves as an electron donor. NADPH is formed by reduction of NADP, which occurs by different mechanisms in different types of organisms. In photosynthetic organisms NADP is reduced by CPLX-84...

## Biological Role

Consumed as substrate in 195 reaction(s). Produced in 29 reaction(s). Binds monoacetylchitobiose-6-phosphate hydrolase (complex.ecocyc.CPLX0-7979), erythronate-4-phosphate dehydrogenase (complex.ecocyc.CPLX0-8212), KpLE2 phage-like element; 2,7-anhydro-N-acetylneuraminate hydratase (complex.ecocyc.CPLX0-8544), protein-lysine deacetylase/desuccinylase/delipoylase (complex.ecocyc.CPLX0-8550), dTDP-glucose 4,6-dehydratase 1 (complex.ecocyc.DTDPGLUCDEHYDRAT-CPLX), UDP-glucose 4-epimerase (complex.ecocyc.UDPGLUCEPIM-CPLX), aroB (protein.P07639), rffG (protein.P27830).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Annotation

KEGG compound: NAD+; NAD; Nicotinamide adenine dinucleotide; DPN; Diphosphopyridine nucleotide; Nadide; beta-NAD+

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Outgoing Edges (244)

- `activates` --> [[reaction.ecocyc.ACETALD-DEHYDROG-RXN|reaction.ecocyc.ACETALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.ALCOHOL-DEHYDROG-RXN|reaction.ecocyc.ALCOHOL-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.ALPHAGALACTOSID-RXN|reaction.ecocyc.ALPHAGALACTOSID-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN0-7143|reaction.ecocyc.RXN0-7143]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `binds` --> [[complex.ecocyc.CPLX0-7979|complex.ecocyc.CPLX0-7979]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-8212|complex.ecocyc.CPLX0-8212]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-8544|complex.ecocyc.CPLX0-8544]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-8550|complex.ecocyc.CPLX0-8550]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.DTDPGLUCDEHYDRAT-CPLX|complex.ecocyc.DTDPGLUCDEHYDRAT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.UDPGLUCEPIM-CPLX|complex.ecocyc.UDPGLUCEPIM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P07639|protein.P07639]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P27830|protein.P27830]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.R00137|reaction.R00137]] `KEGG` `database` - C00002 + C00455 <=> C00013 + C00003
- `is_product_of` --> [[reaction.R00189|reaction.R00189]] `KEGG` `database` - C00002 + C00857 + C00014 <=> C00020 + C00013 + C00003
- `is_product_of` --> [[reaction.R00994|reaction.R00994]] `KEGG` `database` - C00109 + C00011 + C00004 + C00080 <=> C06032 + C00003
- `is_product_of` --> [[reaction.R05724|reaction.R05724]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00004 + C00080 <=> 2 C00244 + C00003
- `is_product_of` --> [[reaction.R07765|reaction.R07765]] `KEGG` `database` - C16221 + C00004 + C00080 <=> C04088 + C00003
- `is_product_of` --> [[reaction.R11945|reaction.R11945]] `KEGG` `database` - C00399 + C00004 + C00080 + 4 C00080 <=> C00390 + C00003 + 4 C00080
- `is_product_of` --> [[reaction.ecocyc.2.7.7.1-RXN|reaction.ecocyc.2.7.7.1-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.HCAMULTI-RXN|reaction.ecocyc.HCAMULTI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MHPHYDROXY-RXN|reaction.ecocyc.MHPHYDROXY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.NAD-SYNTH-GLN-RXN|reaction.ecocyc.NAD-SYNTH-GLN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.NAD-SYNTH-NH3-RXN|reaction.ecocyc.NAD-SYNTH-NH3-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.NADH-DEHYDROG-A-RXN|reaction.ecocyc.NADH-DEHYDROG-A-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.NADH-DEHYDROGENASE-QUINONE-RXN|reaction.ecocyc.NADH-DEHYDROGENASE-QUINONE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.R170-RXN|reaction.ecocyc.R170-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.R4-RXN|reaction.ecocyc.R4-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-10040|reaction.ecocyc.RXN-10040]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12072|reaction.ecocyc.RXN-12072]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12886|reaction.ecocyc.RXN-12886]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15607|reaction.ecocyc.RXN-15607]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-20691|reaction.ecocyc.RXN-20691]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-5822|reaction.ecocyc.RXN-5822]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5213|reaction.ecocyc.RXN0-5213]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5330|reaction.ecocyc.RXN0-5330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5388|reaction.ecocyc.RXN0-5388]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6444|reaction.ecocyc.RXN0-6444]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6450|reaction.ecocyc.RXN0-6450]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6722|reaction.ecocyc.RXN0-6722]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7123|reaction.ecocyc.RXN0-7123]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7363|reaction.ecocyc.RXN0-7363]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00094|reaction.R00094]] `KEGG` `database` - 2 C00051 + C00003 <=> C00127 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00103|reaction.R00103]] `KEGG` `database` - C00003 + C00001 <=> C00020 + C00455
- `is_substrate_of` --> [[reaction.R00104|reaction.R00104]] `KEGG` `database` - C00002 + C00003 <=> C00008 + C00006
- `is_substrate_of` --> [[reaction.R00112|reaction.R00112]] `KEGG` `database` - C00005 + C00003 <=> C00006 + C00004
- `is_substrate_of` --> [[reaction.R00143|reaction.R00143]] `KEGG` `database` - C00014 + C00003 + C00001 <=> C00192 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00145|reaction.R00145]] `KEGG` `database` - C05167 + C00001 + C00003 <=> C00161 + C00014 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00203|reaction.R00203]] `KEGG` `database` - C00546 + C00003 + C00001 <=> C00022 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00214|reaction.R00214]] `KEGG` `database` - C00149 + C00003 <=> C00022 + C00011 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00215|reaction.R00215]] `KEGG` `database` - C00497 + C00003 <=> C00022 + C00011 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00228|reaction.R00228]] `KEGG` `database` - C00084 + C00010 + C00003 <=> C00024 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00245|reaction.R00245]] `KEGG` `database` - C01165 + C00003 + C00001 <=> C00025 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00286|reaction.R00286]] `KEGG` `database` - C00029 + C00001 + 2 C00003 <=> C00167 + 2 C00004 + 2 C00080
- `is_substrate_of` --> [[reaction.R00342|reaction.R00342]] `KEGG` `database` - C00149 + C00003 <=> C00036 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00382|reaction.R00382]] `KEGG` `database` - C00003 + C00039(n) + C02128(m) <=> C00020 + C00455 + C00039(n+m)
- `is_substrate_of` --> [[reaction.R00519|reaction.R00519]] `KEGG` `database` - C00058 + C00003 <=> C00080 + C00011 + C00004
- `is_substrate_of` --> [[reaction.R00623|reaction.R00623]] `KEGG` `database` - C00226 + C00003 <=> C00071 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00624|reaction.R00624]] `KEGG` `database` - C01612 + C00003 <=> C01450 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00704|reaction.R00704]] `KEGG` `database` - C00256 + C00003 <=> C00022 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00707|reaction.R00707]] `KEGG` `database` - C03912 + C00003 + 2 C00001 <=> C00025 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00713|reaction.R00713]] `KEGG` `database` - C00232 + C00003 + C00001 <=> C00042 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00754|reaction.R00754]] `KEGG` `database` - C00469 + C00003 <=> C00084 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00758|reaction.R00758]] `KEGG` `database` - C00644 + C00003 <=> C00085 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00787|reaction.R00787]] `KEGG` `database` - C00014 + 3 C00003 + 2 C00001 <=> C00088 + 3 C00004 + 3 C00080
- `is_substrate_of` --> [[reaction.R00842|reaction.R00842]] `KEGG` `database` - C00093 + C00003 <=> C00111 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00977|reaction.R00977]] `KEGG` `database` - C00429 + C00003 <=> C00106 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R01158|reaction.R01158]] `KEGG` `database` - C00860 + 2 C00003 + C00001 <=> C00135 + 2 C00004 + 2 C00080
- `is_substrate_of` --> [[reaction.R01163|reaction.R01163]] `KEGG` `database` - C01929 + C00001 + C00003 <=> C00135 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R01542|reaction.R01542]] `KEGG` `database` - C00204 + C00003 <=> C04349 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R01728|reaction.R01728]] `KEGG` `database` - C00254 + C00003 <=> C01179 + C00011 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R01738|reaction.R01738]] `KEGG` `database` - C00257 + C00003 <=> C01062 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R01745|reaction.R01745]] `KEGG` `database` - C00258 + C00003 <=> C01146 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R01896|reaction.R01896]] `KEGG` `database` - C00379 + C00003 <=> C00310 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R02124|reaction.R02124]] `KEGG` `database` - C00473 + C00003 <=> C00376 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R02401|reaction.R02401]] `KEGG` `database` - C03273 + C00003 + C00001 <=> C00489 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R02792|reaction.R02792]] `KEGG` `database` - C00695 + C00003 <=> C04643 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R02878|reaction.R02878]] `KEGG` `database` - C00756 + C00003 <=> C01545 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R03191|reaction.R03191]] `KEGG` `database` - C01050 + C00003 <=> C04631 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R03431|reaction.R03431]] `KEGG` `database` - C04367 + C00003 <=> C01244 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R04426|reaction.R04426]] `KEGG` `database` - C04411 + C00003 <=> C04236 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R04429|reaction.R04429]] `KEGG` `database` - C05745 + C00003 <=> C04246 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R04724|reaction.R04724]] `KEGG` `database` - C05223 + C00003 <=> C05758 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R04958|reaction.R04958]] `KEGG` `database` - C05752 + C00003 <=> C05751 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R04961|reaction.R04961]] `KEGG` `database` - C05755 + C00003 <=> C05754 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R04966|reaction.R04966]] `KEGG` `database` - C05761 + C00003 <=> C05760 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R05233|reaction.R05233]] `KEGG` `database` - C06611 + C00003 <=> C06613 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R05234|reaction.R05234]] `KEGG` `database` - C06612 + C00003 <=> C16348 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R05305|reaction.R05305]] `KEGG` `database` - C06714 + C00003 <=> C06715 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R05837|reaction.R05837]] `KEGG` `database` - C06055 + C00003 <=> C11638 + C00004 + C00080 + C00011
- `is_substrate_of` --> [[reaction.R06180|reaction.R06180]] `KEGG` `database` - C00898 + C00003 <=> C03459 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R06917|reaction.R06917]] `KEGG` `database` - C14089 + C00003 <=> C14090 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R06927|reaction.R06927]] `KEGG` `database` - C02909 + C00003 <=> C14099 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R06941|reaction.R06941]] `KEGG` `database` - C14145 + C00003 <=> C02232 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R06983|reaction.R06983]] `KEGG` `database` - C14180 + C00003 <=> C01031 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R08198|reaction.R08198]] `KEGG` `database` - C02630 + C00003 <=> C00026 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R10221|reaction.R10221]] `KEGG` `database` - C00345 + C00003 <=> C00199 + C00011 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R10907|reaction.R10907]] `KEGG` `database` - C01172 + C00003 <=> C01236 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R11337|reaction.R11337]] `KEGG` `database` - C01087 + C00003 <=> C00026 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R12035|reaction.R12035]] `KEGG` `database` - C00108 + C04203 + 2 C00003 <=> C19459 + 2 C00004 + 2 C00080
- `is_substrate_of` --> [[reaction.R12146|reaction.R12146]] `KEGG` `database` - C15930 + C00003 <=> C00558 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.127-RXN|reaction.ecocyc.1.1.1.127-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.251-RXN|reaction.ecocyc.1.1.1.251-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.39-RXN|reaction.ecocyc.1.1.1.39-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.83-RXN|reaction.ecocyc.1.1.1.83-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.1.3.1.9-RXN|reaction.ecocyc.1.3.1.9-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.1.8.1.4-RXN|reaction.ecocyc.1.8.1.4-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.2OXOGLUTARATEDEH-RXN|reaction.ecocyc.2OXOGLUTARATEDEH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.3-ISOPROPYLMALDEHYDROG-RXN|reaction.ecocyc.3-ISOPROPYLMALDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.4-HYDROXYBUTYRATE-DEHYDROGENASE-RXN|reaction.ecocyc.4-HYDROXYBUTYRATE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.7-ALPHA-HYDROXYSTEROID-DEH-RXN|reaction.ecocyc.7-ALPHA-HYDROXYSTEROID-DEH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ACETALD-DEHYDROG-RXN|reaction.ecocyc.ACETALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ALCOHOL-DEHYDROG-GENERIC-RXN|reaction.ecocyc.ALCOHOL-DEHYDROG-GENERIC-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ALCOHOL-DEHYDROG-RXN|reaction.ecocyc.ALCOHOL-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ALTRO-OXIDOREDUCT-RXN|reaction.ecocyc.ALTRO-OXIDOREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.AMINOBUTDEHYDROG-RXN|reaction.ecocyc.AMINOBUTDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.AMINOPROPDEHYDROG-RXN|reaction.ecocyc.AMINOPROPDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.BADH-RXN|reaction.ecocyc.BADH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.D-ARABINITOL-4-DEHYDROGENASE-RXN|reaction.ecocyc.D-ARABINITOL-4-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.D-XYLULOSE-REDUCTASE-RXN|reaction.ecocyc.D-XYLULOSE-REDUCTASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DHBDEHYD-RXN|reaction.ecocyc.DHBDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DIHYDROURACIL-DEHYDROGENASE-NAD_-RXN|reaction.ecocyc.DIHYDROURACIL-DEHYDROGENASE-NAD_-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DIMETHUROPORDEHYDROG-RXN|reaction.ecocyc.DIMETHUROPORDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DLACTDEHYDROGNAD-RXN|reaction.ecocyc.DLACTDEHYDROGNAD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DNA-LIGASE-NAD_-RXN|reaction.ecocyc.DNA-LIGASE-NAD_-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ENOYL-ACP-REDUCT-NADH-RXN|reaction.ecocyc.ENOYL-ACP-REDUCT-NADH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ERYTH4PDEHYDROG-RXN|reaction.ecocyc.ERYTH4PDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ERYTHRON4PDEHYDROG-RXN|reaction.ecocyc.ERYTHRON4PDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.FERREDOXIN--NAD_-REDUCTASE-RXN|reaction.ecocyc.FERREDOXIN--NAD_-REDUCTASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GAPOXNPHOSPHN-RXN|reaction.ecocyc.GAPOXNPHOSPHN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GCVMULTI-RXN|reaction.ecocyc.GCVMULTI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLYCDEH-RXN|reaction.ecocyc.GLYCDEH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLYCOLALD-DEHYDROG-RXN|reaction.ecocyc.GLYCOLALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLYCOLALDREDUCT-RXN|reaction.ecocyc.GLYCOLALDREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLYCOLATE-REDUCTASE-RXN|reaction.ecocyc.GLYCOLATE-REDUCTASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HISTALDEHYD-RXN|reaction.ecocyc.HISTALDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HISTOLDEHYD-RXN|reaction.ecocyc.HISTOLDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.IMP-DEHYDROG-RXN|reaction.ecocyc.IMP-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.KDUD-RXN|reaction.ecocyc.KDUD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.KETOGLUTREDUCT-RXN|reaction.ecocyc.KETOGLUTREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.LACTALDDEHYDROG-RXN|reaction.ecocyc.LACTALDDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.LACTALDREDUCT-RXN|reaction.ecocyc.LACTALDREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MALATE-DEH-RXN|reaction.ecocyc.MALATE-DEH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MANNONOXIDOREDUCT-RXN|reaction.ecocyc.MANNONOXIDOREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MANNPDEHYDROG-RXN|reaction.ecocyc.MANNPDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.NAD-KIN-RXN|reaction.ecocyc.NAD-KIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.NADPYROPHOSPHAT-RXN|reaction.ecocyc.NADPYROPHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.OHACYL-COA-DEHYDROG-RXN|reaction.ecocyc.OHACYL-COA-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PGLYCDEHYDROG-RXN|reaction.ecocyc.PGLYCDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PHENDEHYD-RXN|reaction.ecocyc.PHENDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PHENPRODIOLDEHYDROG-RXN|reaction.ecocyc.PHENPRODIOLDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PREPHENATEDEHYDROG-RXN|reaction.ecocyc.PREPHENATEDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PYRNUTRANSHYDROGEN-RXN|reaction.ecocyc.PYRNUTRANSHYDROGEN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PYRROLINECARBDEHYDROG-RXN|reaction.ecocyc.PYRROLINECARBDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PYRUVDEH-RXN|reaction.ecocyc.PYRUVDEH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RIBITOL-2-DEHYDROGENASE-RXN|reaction.ecocyc.RIBITOL-2-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10657|reaction.ecocyc.RXN-10657]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10661|reaction.ecocyc.RXN-10661]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10715|reaction.ecocyc.RXN-10715]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11032|reaction.ecocyc.RXN-11032]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11478|reaction.ecocyc.RXN-11478]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11482|reaction.ecocyc.RXN-11482]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11662|reaction.ecocyc.RXN-11662]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12071|reaction.ecocyc.RXN-12071]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12107|reaction.ecocyc.RXN-12107]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12490|reaction.ecocyc.RXN-12490]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12570|reaction.ecocyc.RXN-12570]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13158|reaction.ecocyc.RXN-13158]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13179|reaction.ecocyc.RXN-13179]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13854|reaction.ecocyc.RXN-13854]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13859|reaction.ecocyc.RXN-13859]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14023|reaction.ecocyc.RXN-14023]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14116|reaction.ecocyc.RXN-14116]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14249|reaction.ecocyc.RXN-14249]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14393|reaction.ecocyc.RXN-14393]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15299|reaction.ecocyc.RXN-15299]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16701|reaction.ecocyc.RXN-16701]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16964|reaction.ecocyc.RXN-16964]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17777|reaction.ecocyc.RXN-17777]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17781|reaction.ecocyc.RXN-17781]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17786|reaction.ecocyc.RXN-17786]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17790|reaction.ecocyc.RXN-17790]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17794|reaction.ecocyc.RXN-17794]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17798|reaction.ecocyc.RXN-17798]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17920|reaction.ecocyc.RXN-17920]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19919|reaction.ecocyc.RXN-19919]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20676|reaction.ecocyc.RXN-20676]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20679|reaction.ecocyc.RXN-20679]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20680|reaction.ecocyc.RXN-20680]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20682|reaction.ecocyc.RXN-20682]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20706|reaction.ecocyc.RXN-20706]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22001|reaction.ecocyc.RXN-22001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22438|reaction.ecocyc.RXN-22438]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22964|reaction.ecocyc.RXN-22964]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23715|reaction.ecocyc.RXN-23715]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-25213|reaction.ecocyc.RXN-25213]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-25215|reaction.ecocyc.RXN-25215]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-7682|reaction.ecocyc.RXN-7682]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-7716|reaction.ecocyc.RXN-7716]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8001|reaction.ecocyc.RXN-8001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8506|reaction.ecocyc.RXN-8506]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8629|reaction.ecocyc.RXN-8629]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8632|reaction.ecocyc.RXN-8632]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9510|reaction.ecocyc.RXN-9510]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9558|reaction.ecocyc.RXN-9558]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9657|reaction.ecocyc.RXN-9657]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9658|reaction.ecocyc.RXN-9658]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9659|reaction.ecocyc.RXN-9659]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9660|reaction.ecocyc.RXN-9660]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9661|reaction.ecocyc.RXN-9661]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9662|reaction.ecocyc.RXN-9662]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9663|reaction.ecocyc.RXN-9663]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1132|reaction.ecocyc.RXN0-1132]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1861|reaction.ecocyc.RXN0-1861]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2044|reaction.ecocyc.RXN0-2044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2145|reaction.ecocyc.RXN0-2145]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-307|reaction.ecocyc.RXN0-307]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5229|reaction.ecocyc.RXN0-5229]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5248|reaction.ecocyc.RXN0-5248]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5289|reaction.ecocyc.RXN0-5289]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5375|reaction.ecocyc.RXN0-5375]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6445|reaction.ecocyc.RXN0-6445]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6565|reaction.ecocyc.RXN0-6565]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7024|reaction.ecocyc.RXN0-7024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-703|reaction.ecocyc.RXN0-703]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7078|reaction.ecocyc.RXN0-7078]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7101|reaction.ecocyc.RXN0-7101]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7318|reaction.ecocyc.RXN0-7318]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-901|reaction.ecocyc.RXN0-901]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SORB6PDEHYDROG-RXN|reaction.ecocyc.SORB6PDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SUCCGLUALDDEHYD-RXN|reaction.ecocyc.SUCCGLUALDDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN|reaction.ecocyc.SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TARTRATE-DEHYDROGENASE-RXN|reaction.ecocyc.TARTRATE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.THREODEHYD-RXN|reaction.ecocyc.THREODEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-277|reaction.ecocyc.TRANS-RXN0-277]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UDPMANNACADEHYDROG-RXN|reaction.ecocyc.UDPMANNACADEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UGD-RXN|reaction.ecocyc.UGD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.3-DEHYDROQUINATE-SYNTHASE-RXN|reaction.ecocyc.3-DEHYDROQUINATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.L-ASPARTATE-OXID-RXN|reaction.ecocyc.L-ASPARTATE-OXID-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN|reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.MANNONOXIDOREDUCT-RXN|reaction.ecocyc.MANNONOXIDOREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.NADH-DEHYDROG-A-RXN|reaction.ecocyc.NADH-DEHYDROG-A-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.NICOTINAMID-RXN|reaction.ecocyc.NICOTINAMID-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PYRUVDEH-RXN|reaction.ecocyc.PYRUVDEH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-13854|reaction.ecocyc.RXN-13854]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.PYRNUTRANSHYDROGEN-CPLX|complex.ecocyc.PYRNUTRANSHYDROGEN-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00003`

## Notes

Included because it appears in at least one E. coli KEGG pathway.

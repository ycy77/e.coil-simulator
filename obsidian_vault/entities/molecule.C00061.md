---
entity_id: "molecule.C00061"
entity_type: "small_molecule"
name: "FMN"
source_database: "KEGG"
source_id: "C00061"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "FMN"
  - "Riboflavin-5-phosphate"
  - "Flavin mononucleotide"
---

# FMN

`molecule.C00061`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00061`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: FMN; Riboflavin-5-phosphate; Flavin mononucleotide FMN is the principal form in which RIBOFLAVIN (vitamin B2) is found in cells and tissues. While it takes more energy to produce than the non-phosphorylated form of RIBOFLAVIN, it is more soluble. FMN is produced from riboflavin by the enzyme EC-2.7.1.26, and functions as prosthetic group of various oxidoreductases including NADH dehydrogenase. During the catalytic cycle, FMN cycles between the oxidized (FMN), semiquinone (FMNH) and reduced (FMNH2) forms, enabling it to take part in both one and two electron transfers. FMN is a stronger oxidizing agent than NAD.

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 13 reaction(s). Binds anaerobic glycerol-3-phosphate dehydrogenase (complex.ecocyc.ANGLYC3PDEHYDROG-CPLX), SoxR [2Fe-2S] reducing system (complex.ecocyc.CPLX0-10853), NADPH-dependent nitroreductase / NADPH-dependent quinone reductase (complex.ecocyc.CPLX0-244), quinone reductase (complex.ecocyc.CPLX0-3121), fused 4'-phosphopantothenoylcysteine decarboxylase and phosphopantothenoylcysteine synthetase (complex.ecocyc.CPLX0-341), NAD(P)H:quinone oxidoreductase (complex.ecocyc.CPLX0-7632), FMN dependent NADH:quinone oxidoreductase (complex.ecocyc.CPLX0-7693), protoporphyrinogen oxidase (complex.ecocyc.CPLX0-7811), and 12 more.

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Annotation

KEGG compound: FMN; Riboflavin-5-phosphate; Flavin mononucleotide

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Outgoing Edges (40)

- `binds` --> [[complex.ecocyc.ANGLYC3PDEHYDROG-CPLX|complex.ecocyc.ANGLYC3PDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-10853|complex.ecocyc.CPLX0-10853]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-244|complex.ecocyc.CPLX0-244]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-3121|complex.ecocyc.CPLX0-3121]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-341|complex.ecocyc.CPLX0-341]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-7632|complex.ecocyc.CPLX0-7632]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-7693|complex.ecocyc.CPLX0-7693]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-7811|complex.ecocyc.CPLX0-7811]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-7841|complex.ecocyc.CPLX0-7841]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-7939|complex.ecocyc.CPLX0-7939]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.DIHYDROPTERIREDUCT-CPLX|complex.ecocyc.DIHYDROPTERIREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.NADH-DHI-CPLX|complex.ecocyc.NADH-DHI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.NQOR-CPLX|complex.ecocyc.NQOR-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.PDXH-CPLX|complex.ecocyc.PDXH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.SULFITE-REDUCT-CPLX|complex.ecocyc.SULFITE-REDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P0A7E1|protein.P0A7E1]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P33232|protein.P33232]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P42593|protein.P42593]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P75898|protein.P75898]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P77258|protein.P77258]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.R00160|reaction.R00160]] `KEGG` `database` - C00016 + C00001 <=> C00020 + C00061
- `is_product_of` --> [[reaction.R00549|reaction.R00549]] `KEGG` `database` - C00002 + C00255 <=> C00008 + C00061
- `is_product_of` --> [[reaction.ecocyc.FMNREDUCT-RXN|reaction.ecocyc.FMNREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RIBOFLAVINKIN-RXN|reaction.ecocyc.RIBOFLAVINKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12444|reaction.ecocyc.RXN-12444]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12886|reaction.ecocyc.RXN-12886]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-13418|reaction.ecocyc.RXN-13418]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15341|reaction.ecocyc.RXN-15341]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-9510|reaction.ecocyc.RXN-9510]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-280|reaction.ecocyc.RXN0-280]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6444|reaction.ecocyc.RXN0-6444]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6973|reaction.ecocyc.RXN0-6973]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-595|reaction.ecocyc.TRANS-RXN0-595]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00161|reaction.R00161]] `KEGG` `database` - C00002 + C00061 <=> C00013 + C00016
- `is_substrate_of` --> [[reaction.R00548|reaction.R00548]] `KEGG` `database` - C00061 + C00001 <=> C00255 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.FADSYN-RXN|reaction.ecocyc.FADSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20706|reaction.ecocyc.RXN-20706]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5187|reaction.ecocyc.RXN0-5187]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-595|reaction.ecocyc.TRANS-RXN0-595]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[gene.b3041|gene.b3041]] `EcoCyc` `database` - EcoCyc regulation TYPES=Compound-Mediated-Translation-Regulation

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00061`

## Notes

Included because it appears in at least one E. coli KEGG pathway.

---
entity_id: "protein.P26281"
entity_type: "protein"
name: "folK"
source_database: "UniProt"
source_id: "P26281"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "folK b0142 JW0138"
---

# folK

`protein.P26281`

## Static

- Type: `protein`
- Source: `UniProt:P26281`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the transfer of pyrophosphate from adenosine triphosphate (ATP) to 6-hydroxymethyl-7,8-dihydropterin, an enzymatic step in folate biosynthesis pathway. {ECO:0000269|PubMed:1325970}. 6-hydroxymethyl-7,8-dihydropterin pyrophosphokinase (HPPK) catalyzes a reaction in the folate biosynthesis pathway, the transfer of pyrophosphate from ATP to 6-hydroxymethyl-7,8-dihydropterin . HPPK is essential in microorganisms, and the enzyme is not present in mammals; it is therefore a target for the development of antimicrobial drugs. Various crystal and solution structures of HPPK have been solved and have elucidated the reaction mechanism and kinetics. The protein undergoes conformational changes during the catalytic cycle. The enzyme binds ATP first, which then enables faster binding of 6-hydroxymethyl-7,8-dihydropterin (HMDP) . Mg2+ is important for binding of both ATP and HMDP . The roles in substrate binding and catalysis of several amino acid residues in the flexible loop 3 have been investigated by site-directed mutagenesis . Substrate site inhibitors have been synthesized and tested . Comparative genomics has suggested a functional association between 3-METHYL-2-OXOBUT-OHCH3XFER-CPLX PanB and FolK...

## Biological Role

Catalyzes H2PTERIDINEPYROPHOSPHOKIN-RXN (reaction.ecocyc.H2PTERIDINEPYROPHOSPHOKIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of pyrophosphate from adenosine triphosphate (ATP) to 6-hydroxymethyl-7,8-dihydropterin, an enzymatic step in folate biosynthesis pathway. {ECO:0000269|PubMed:1325970}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.H2PTERIDINEPYROPHOSPHOKIN-RXN|reaction.ecocyc.H2PTERIDINEPYROPHOSPHOKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0142|gene.b0142]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P26281`
- `KEGG:ecj:JW0138;eco:b0142;ecoc:C3026_00615;`
- `GeneID:948792;`
- `GO:GO:0000287; GO:0003848; GO:0005524; GO:0016301; GO:0046654; GO:0046656`
- `EC:2.7.6.3`

## Notes

2-amino-4-hydroxy-6-hydroxymethyldihydropteridine pyrophosphokinase (EC 2.7.6.3) (6-hydroxymethyl-7,8-dihydropterin pyrophosphokinase) (PPPK) (7,8-dihydro-6-hydroxymethylpterin-pyrophosphokinase) (HPPK)

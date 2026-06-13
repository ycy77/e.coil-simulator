---
entity_id: "protein.P77182"
entity_type: "protein"
name: "mnmC"
source_database: "UniProt"
source_id: "P77182"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mnmC yfcK b2324 JW5380"
---

# mnmC

`protein.P77182`

## Static

- Type: `protein`
- Source: `UniProt:P77182`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the last two steps in the biosynthesis of 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) at the wobble position (U34) in tRNA. Catalyzes the FAD-dependent demodification of cmnm(5)s(2)U34 to nm(5)s(2)U34, followed by the transfer of a methyl group from S-adenosyl-L-methionine to nm(5)s(2)U34, to form mnm(5)s(2)U34. {ECO:0000269|PubMed:15247431, ECO:0000269|PubMed:18186482}. The tRNAs specific for glutamate, lysine, and possibly glutamine contain the hypermodified nucleoside 5-methylaminomethyl-2-thiouridine (mnm5s2U) in position 34, the wobble position. The MnmC protein was shown to catalyze the formation of mnm5s2U from 5-carboxymethylaminomethyl-2-thiouridine (cmnm5s2U) in tRNA . Both the tRNA species and growth conditions modulate synthesis of the wobble base modifications . A tentative reaction mechanism has been proposed. The enzyme catalyzes two steps, an initial FAD-dependent demodification of cmnm5s2U to nm5s2U followed by the transfer of a methyl group from AdoMet to nm5s2U to produce mnm5s2U . The second reaction occurs faster than the first reaction, indicating that the enzyme is tuned to produce fully mnm5s2U-modified tRNA without accumulating the nm5s2U-modified tRNA intermediate . tRNAGlncmnm5s2UUG and tRNALeucmnm5UmAA are not substrates for the demodification activity of MnmC...

## Biological Role

Catalyzes S-adenosyl-L-methionine:tRNA 5-methylaminomethyl-2-thiouridine methyltransferase; (reaction.R00601), RXN0-5144 (reaction.ecocyc.RXN0-5144), RXN0-7081 (reaction.ecocyc.RXN0-7081). Bound by FAD (molecule.C00016).

## Annotation

FUNCTION: Catalyzes the last two steps in the biosynthesis of 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) at the wobble position (U34) in tRNA. Catalyzes the FAD-dependent demodification of cmnm(5)s(2)U34 to nm(5)s(2)U34, followed by the transfer of a methyl group from S-adenosyl-L-methionine to nm(5)s(2)U34, to form mnm(5)s(2)U34. {ECO:0000269|PubMed:15247431, ECO:0000269|PubMed:18186482}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00601|reaction.R00601]] `KEGG` `database` - via EC:2.1.1.61
- `catalyzes` --> [[reaction.ecocyc.RXN0-5144|reaction.ecocyc.RXN0-5144]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7081|reaction.ecocyc.RXN0-7081]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2324|gene.b2324]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77182`
- `KEGG:ecj:JW5380;eco:b2324;ecoc:C3026_12950;`
- `GeneID:946800;`
- `GO:GO:0002098; GO:0004808; GO:0005737; GO:0016645; GO:0030488; GO:0071949`
- `EC:1.5.-.-; 2.1.1.61`

## Notes

tRNA 5-methylaminomethyl-2-thiouridine biosynthesis bifunctional protein MnmC (tRNA mnm(5)s(2)U biosynthesis bifunctional protein) [Includes: tRNA (mnm(5)s(2)U34)-methyltransferase (EC 2.1.1.61); FAD-dependent cmnm(5)s(2)U34 oxidoreductase (EC 1.5.-.-)]

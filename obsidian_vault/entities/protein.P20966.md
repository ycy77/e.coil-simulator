---
entity_id: "protein.P20966"
entity_type: "protein"
name: "fruA"
source_database: "UniProt"
source_id: "P20966"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:3076173}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:3076173, ECO:0000305|PubMed:8626640}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fruA ptsF b2167 JW2154"
---

# fruA

`protein.P20966`

## Static

- Type: `protein`
- Source: `UniProt:P20966`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:3076173}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:3076173, ECO:0000305|PubMed:8626640}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FruAB PTS system is involved in fructose transport. {ECO:0000269|PubMed:3510127, ECO:0000269|PubMed:8626640, ECO:0000305|PubMed:3076173}. fruA expressed in trans restores the ability of a fruA transposon mutant to grow on 2.5mM fructose as carbon source and to phosphorylate fructose in vitro. FruA is predicted to be an inner membrane protein . FruA lacking the B' domain is able to transport fructose in vivo and to phosphorylate fructose in vitro. FruA lacking the B' domain shows less affinity for FruB in vitro. Loss of the B' domain mainly affects phosphoryl transfer between FruB which contains the pseudo-HPr domain and FruA . FruA containing a C112S amino acid substitution is unable to transport fructose in vivo or in vitro. The IIC domain of FruA is predicted to contain 9 transmembrane segments. FruA is likely to function as a homo-oligomer . This subunit contains PTS Enzyme IIB', IIB and IIC domains.

## Biological Role

Component of fructose-specific PTS enzyme II (complex.ecocyc.CPLX-158).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FruAB PTS system is involved in fructose transport. {ECO:0000269|PubMed:3510127, ECO:0000269|PubMed:8626640, ECO:0000305|PubMed:3076173}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-158|complex.ecocyc.CPLX-158]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2167|gene.b2167]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P20966`
- `KEGG:ecj:JW2154;eco:b2167;ecoc:C3026_12140;`
- `GeneID:946672;`
- `GO:GO:0005351; GO:0005886; GO:0009401; GO:0016301; GO:0022877; GO:0090563; GO:0090582; GO:1902495; GO:1990539`
- `EC:2.7.1.202`

## Notes

PTS system fructose-specific EIIB'BC component (EIIB'BC-Fru) [Includes: PTS system fructose-specific EIIB component (EC 2.7.1.202) (EIII-Fru) (Fructose-specific phosphotransferase enzyme IIB component); PTS system fructose-specific EIIC component (Fructose permease IIC component)]

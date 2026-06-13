---
entity_id: "protein.P19642"
entity_type: "protein"
name: "malX"
source_database: "UniProt"
source_id: "P19642"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "malX b1621 JW1613"
---

# malX

`protein.P19642`

## Static

- Type: `protein`
- Source: `UniProt:P19642`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in maltose transport. MalX can also recognize and transport glucose even though this sugar may not represent the natural substrate of the system. {ECO:0000269|PubMed:1856179}. The deduced amino acid sequence of MalX displays 35% identity with PTSG-MONOMER "PtsG" (Enzyme IIBCglc of the glucose PTS). The constitutive expression of chromosomal malX (through a malI::Tn10 mutation) restores growth on glucose in an E. coli ΔptsG ΔptsM strain provided cytoplasmic glucokinase (encoded by glk) is present. This suggests that the MalX protein can transport glucose via facilitated diffusion . Overexpression of malX from a plasmid restores growth on glucose in a ΔptsG ΔptsM Δglk strain which suggests that MalX also functions, albeit inefficiently, in vectorial phosphorylation of glucose possibly in conjunction with CRR-MONOMER "Crr" (Enzyme IIAglc) . MalX may also transport maltose by facilitated diffusion . The physiological function of MalX is not clear . MalX/Crr is a member of the PTS Glucose-Glucoside family of transporters . malX forms an operon with CPLX0-8092 "malY"...

## Biological Role

Catalyzes protein-N(pi)-phosphohistidine:maltose 6'-phosphotransferase (reaction.R04111), TRANS-RXN0-574 (reaction.ecocyc.TRANS-RXN0-574), TRANS-RXN0-575 (reaction.ecocyc.TRANS-RXN0-575).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in maltose transport. MalX can also recognize and transport glucose even though this sugar may not represent the natural substrate of the system. {ECO:0000269|PubMed:1856179}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R04111|reaction.R04111]] `KEGG` `database` - via EC:2.7.1.208
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-574|reaction.ecocyc.TRANS-RXN0-574]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-575|reaction.ecocyc.TRANS-RXN0-575]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1621|gene.b1621]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P19642`
- `KEGG:ecj:JW1613;eco:b1621;ecoc:C3026_09320;`
- `GeneID:946009;`
- `GO:GO:0005363; GO:0005886; GO:0008982; GO:0009401; GO:0009758; GO:0015768; GO:0016301; GO:0046323; GO:0055056; GO:0090564; GO:1904659`
- `EC:2.7.1.208`

## Notes

PTS system maltose-specific EIICB component [Includes: Maltose permease IIC component (PTS system maltose-specific EIIC component); Maltose-specific phosphotransferase enzyme IIB component (EC 2.7.1.208) (PTS system maltose-specific EIIB component)]

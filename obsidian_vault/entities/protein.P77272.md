---
entity_id: "protein.P77272"
entity_type: "protein"
name: "murP"
source_database: "UniProt"
source_id: "P77272"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00426}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00426}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "murP yfeV b2429 JW2422"
---

# murP

`protein.P77272`

## Static

- Type: `protein`
- Source: `UniProt:P77272`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00426}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00426}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in N-acetylmuramic acid (MurNAc) transport, yielding cytoplasmic MurNAc-6-P. Is responsible for growth on MurNAc as the sole source of carbon and energy. Is also able to take up anhydro-N-acetylmuramic acid (anhMurNAc), but cannot phosphorylate the carbon 6, probably because of the 1,6-anhydro ring. {ECO:0000269|PubMed:15060041, ECO:0000269|PubMed:16452451}. murP encodes the permease component of the N-acetylmuramic acid PTS transport system. MurP contains PTS Enzyme IIB and IIC domains . MurP is required for the uptake of anhydrous N-acetylmuramic (anhMurNAc) acid from the medium. MurP transports but does not phosphorylate anhMurNAc. The anmK encoded G6880-MONOMER "anhydro-N-acetylmuramic acid kinase" is required to convert imported anhMurNAc to MurNAc-P. E. coli K-12 cannot use anhMurNAc as the sole source of carbon .

## Biological Role

Catalyzes TRANS-RXN0-587 (reaction.ecocyc.TRANS-RXN0-587). Component of N-acetylmuramic acid-specific PTS enzyme II (complex.ecocyc.CPLX0-7).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in N-acetylmuramic acid (MurNAc) transport, yielding cytoplasmic MurNAc-6-P. Is responsible for growth on MurNAc as the sole source of carbon and energy. Is also able to take up anhydro-N-acetylmuramic acid (anhMurNAc), but cannot phosphorylate the carbon 6, probably because of the 1,6-anhydro ring. {ECO:0000269|PubMed:15060041, ECO:0000269|PubMed:16452451}.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-587|reaction.ecocyc.TRANS-RXN0-587]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-7|complex.ecocyc.CPLX0-7]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2429|gene.b2429]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77272`
- `KEGG:ecj:JW2422;eco:b2429;ecoc:C3026_13495;`
- `GeneID:946894;`
- `GO:GO:0005886; GO:0008982; GO:0009401; GO:0016020; GO:0016301; GO:0034219; GO:0090588`
- `EC:2.7.1.192`

## Notes

PTS system N-acetylmuramic acid-specific EIIBC component (EIIBC-MurNAc) [Includes: N-acetylmuramic acid-specific phosphotransferase enzyme IIB component (EC 2.7.1.192) (PTS system N-acetylmuramic acid-specific EIIB component); N-acetylmuramic acid permease IIC component (PTS system N-acetylmuramic acid-specific EIIC component)]

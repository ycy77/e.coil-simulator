---
entity_id: "protein.P09323"
entity_type: "protein"
name: "nagE"
source_database: "UniProt"
source_id: "P09323"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nagE pstN b0679 JW0665"
---

# nagE

`protein.P09323`

## Static

- Type: `protein`
- Source: `UniProt:P09323`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane (PubMed:4919472). This system is involved in N-acetylglucosamine transport (PubMed:4919472). It can also transport and phosphorylate the antibiotic streptozotocin (PubMed:161156). Could play a significant role in the recycling of peptidoglycan (PubMed:19617367). {ECO:0000269|PubMed:161156, ECO:0000269|PubMed:19617367, ECO:0000269|PubMed:4919472, ECO:0000305|PubMed:3056518}.

## Biological Role

Component of N-acetylglucosamine-specific PTS enzyme II (complex.ecocyc.CPLX-167).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane (PubMed:4919472). This system is involved in N-acetylglucosamine transport (PubMed:4919472). It can also transport and phosphorylate the antibiotic streptozotocin (PubMed:161156). Could play a significant role in the recycling of peptidoglycan (PubMed:19617367). {ECO:0000269|PubMed:161156, ECO:0000269|PubMed:19617367, ECO:0000269|PubMed:4919472, ECO:0000305|PubMed:3056518}.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-167|complex.ecocyc.CPLX-167]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0679|gene.b0679]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09323`
- `KEGG:ecj:JW0665;eco:b0679;ecoc:C3026_03375;`
- `GeneID:945292;`
- `GO:GO:0005886; GO:0006974; GO:0008982; GO:0009254; GO:0009401; GO:0015572; GO:0015764; GO:0016301; GO:0019866; GO:0046872; GO:0090563; GO:0090586; GO:0090587; GO:0103111`
- `EC:2.7.1.193`

## Notes

PTS system N-acetylglucosamine-specific EIICBA component (EIICBA-Nag) (EII-Nag) [Includes: N-acetylglucosamine permease IIC component (PTS system N-acetylglucosamine-specific EIIC component); N-acetylglucosamine-specific phosphotransferase enzyme IIB component (EC 2.7.1.193) (PTS system N-acetylglucosamine-specific EIIB component); N-acetylglucosamine-specific phosphotransferase enzyme IIA component (PTS system N-acetylglucosamine-specific EIIA component)]

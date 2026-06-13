---
entity_id: "protein.P17446"
entity_type: "protein"
name: "betI"
source_database: "UniProt"
source_id: "P17446"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "betI b0313 JW0305"
---

# betI

`protein.P17446`

## Static

- Type: `protein`
- Source: `UniProt:P17446`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Repressor involved in the biosynthesis of the osmoprotectant glycine betaine. It represses transcription of the choline transporter BetT and the genes of BetAB involved in the synthesis of glycine betaine. {ECO:0000269|PubMed:8626294, ECO:0000269|PubMed:8626295}. "Betaine inhibitor," BetI, acts as a repressor of glycine betaine synthesis from choline . It is negatively autoregulated and coordinately represses transcription of the choline transporter and the operon related to the synthesis of glycine betaine. These divergent operons are expressed only under aerobic conditions and are induced by osmotic stress . BetI is an unusual repressor because it remains bound to DNA during induction. BetI forms a complex with DNA in the presence of choline, binding to a 20-bp-long sequence with dyad symmetry that overlaps betTp and betIp simultaneously . The position of the repressor gene within the operon is unusual too, as regulatory genes tend to be positioned at the end of operons and this gene is located at the beginning of the operon. BetI is still able to repress transcription at positions as far as -61 from the TSS, but in a weak manner . BetI belongs to the TetR/AcrR family of transcriptional regulators...

## Biological Role

Component of BetI-choline (complex.ecocyc.MONOMER0-49).

## Annotation

FUNCTION: Repressor involved in the biosynthesis of the osmoprotectant glycine betaine. It represses transcription of the choline transporter BetT and the genes of BetAB involved in the synthesis of glycine betaine. {ECO:0000269|PubMed:8626294, ECO:0000269|PubMed:8626295}.

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-49|complex.ecocyc.MONOMER0-49]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0311|gene.b0311]] `RegulonDB` `C` - regulator=BetI; target=betA; function=-
- `represses` --> [[gene.b0312|gene.b0312]] `RegulonDB` `C` - regulator=BetI; target=betB; function=-
- `represses` --> [[gene.b0313|gene.b0313]] `RegulonDB` `C` - regulator=BetI; target=betI; function=-
- `represses` --> [[gene.b0314|gene.b0314]] `RegulonDB` `C` - regulator=BetI; target=betT; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0313|gene.b0313]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17446`
- `KEGG:ecj:JW0305;eco:b0313;ecoc:C3026_01530;ecoc:C3026_24705;`
- `GeneID:944981;`
- `GO:GO:0000976; GO:0003677; GO:0003700; GO:0006355; GO:0006970; GO:0019285; GO:0045892`

## Notes

HTH-type transcriptional regulator BetI

---
entity_id: "protein.P23857"
entity_type: "protein"
name: "pspE"
source_database: "UniProt"
source_id: "P23857"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:1712397}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pspE b1308 JW1301"
---

# pspE

`protein.P23857`

## Static

- Type: `protein`
- Source: `UniProt:P23857`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:1712397}.

## Enriched Summary

FUNCTION: The phage shock protein (psp) operon (pspABCDE) may play a significant role in the competition for survival under nutrient- or energy-limited conditions. PspE catalyzes the sulfur-transfer reaction from thiosulfate to cyanide, to form sulfite and thiocyanate. Also able to use dithiol (dithiothreitol) as an alternate sulfur acceptor. Also possesses a very low mercaptopyruvate sulfurtransferase activity. PspE is a periplasmic sulfurtransferase of the rhodanese family that catalyzes the transfer of sulfur from S2O3 to a recipient thiol compound . Based on analysis of deletion mutants, PspE appears to carry out about 85% of the thiosulfate sulfurtransferase activity, with CPLX0-242 "GlpE" accounting for approximately 10% . The main receipient of the sulfur is GLUTATHIONE (GSH), the dominant cellular thiol in E. coli . The product, CPD-11281 (GSSH), was shown to be the dominant species of cellular sulfane sulfur. It should be noted that the reaction is strongly inhibited by GSSH, and thus the reaction normally favors the reverse direction. The forward reaction is enhanced by the removal of GSSH via translocation from the periplasm to the cytoplasm. In the yeast Saccharomyces cerevisiae GSSH was shown to react with a second GSH molecule, forming OXIDIZED-GLUTATHIONE and HS . However, rapid reduction of GSSH to H2S was not observed in E. coli...

## Biological Role

Catalyzes RXN-19033 (reaction.ecocyc.RXN-19033), THIOSULFATE-SULFURTRANSFERASE-RXN (reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: The phage shock protein (psp) operon (pspABCDE) may play a significant role in the competition for survival under nutrient- or energy-limited conditions. PspE catalyzes the sulfur-transfer reaction from thiosulfate to cyanide, to form sulfite and thiocyanate. Also able to use dithiol (dithiothreitol) as an alternate sulfur acceptor. Also possesses a very low mercaptopyruvate sulfurtransferase activity.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-19033|reaction.ecocyc.RXN-19033]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN|reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1308|gene.b1308]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23857`
- `KEGG:ecj:JW1301;eco:b1308;ecoc:C3026_07670;`
- `GeneID:93775434;945652;`
- `GO:GO:0004792; GO:0030288; GO:0042597`
- `EC:2.8.1.1`

## Notes

Thiosulfate sulfurtransferase PspE (TST) (EC 2.8.1.1) (Phage shock protein E)

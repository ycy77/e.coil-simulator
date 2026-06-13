---
entity_id: "protein.P62395"
entity_type: "protein"
name: "secM"
source_database: "UniProt"
source_id: "P62395"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm, cytosol {ECO:0000269|PubMed:1834634}. Periplasm {ECO:0000269|PubMed:1834634}. Note=The active form is cytosolic, while the periplasmic form is rapidly degraded, mainly by the tail-specific protease (PubMed:11172723). {ECO:0000269|PubMed:11172723}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "secM srrA yacA b0097 JW5007"
---

# secM

`protein.P62395`

## Static

- Type: `protein`
- Source: `UniProt:P62395`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm, cytosol {ECO:0000269|PubMed:1834634}. Periplasm {ECO:0000269|PubMed:1834634}. Note=The active form is cytosolic, while the periplasmic form is rapidly degraded, mainly by the tail-specific protease (PubMed:11172723). {ECO:0000269|PubMed:11172723}.

## Enriched Summary

FUNCTION: Regulates secA expression by translational coupling of the secM secA operon. Ribosomes translating the C-terminal region of secM can disrupt an RNA repressor helix that normally blocks secA translation initiation, derepressing the expression of secA. Translational pausing of secM at Pro-166 under secretion-limiting conditions increases the duration of the disruption and thus increases secA expression. This is controlled by interaction of the secM signal peptide with secA and the translocon, possibly by secA pulling the paused secM out of the ribosome. The arrest sequence (150-FXXXXWIXXXXGIRAGP-166) is sufficient to cause arrest of unrelated proteins (PubMed:11893334). Elongation arrest can be alleviated by mutations in the 23S rRNA or in ribosomal protein L22. Elongation arrest can be alleviated by YheS in vitro (PubMed:38661232). {ECO:0000269|PubMed:11893334, ECO:0000269|PubMed:38661232}. secM encodes a presecretory protein that regulates production of the protein translocation ATPase CPLX0-8089 SecA via translation arrest. SecM functions in the nascent ribsome-associated state to induce translational pausing which affects mRNA folding and regulates secA translation (see ). Early work observing that production of SecA is coordinated with the protein secretion status of the cell and implicating 'gene X' (later secM) in SecA regulation includes...

## Enriched Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Regulates secA expression by translational coupling of the secM secA operon. Ribosomes translating the C-terminal region of secM can disrupt an RNA repressor helix that normally blocks secA translation initiation, derepressing the expression of secA. Translational pausing of secM at Pro-166 under secretion-limiting conditions increases the duration of the disruption and thus increases secA expression. This is controlled by interaction of the secM signal peptide with secA and the translocon, possibly by secA pulling the paused secM out of the ribosome. The arrest sequence (150-FXXXXWIXXXXGIRAGP-166) is sufficient to cause arrest of unrelated proteins (PubMed:11893334). Elongation arrest can be alleviated by mutations in the 23S rRNA or in ribosomal protein L22. Elongation arrest can be alleviated by YheS in vitro (PubMed:38661232). {ECO:0000269|PubMed:11893334, ECO:0000269|PubMed:38661232}.

## Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0097|gene.b0097]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P62395`
- `KEGG:ecj:JW5007;eco:b0097;ecoc:C3026_00390;`
- `GeneID:93777337;944831;`
- `GO:GO:0005829; GO:0006417; GO:0042597; GO:0045182`

## Notes

Secretion monitor (Gene X)

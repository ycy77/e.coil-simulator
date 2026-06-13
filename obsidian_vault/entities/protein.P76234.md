---
entity_id: "protein.P76234"
entity_type: "protein"
name: "yeaE"
source_database: "UniProt"
source_id: "P76234"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yeaE b1781 JW1770"
---

# yeaE

`protein.P76234`

## Static

- Type: `protein`
- Source: `UniProt:P76234`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Aldo-keto reductase that contributes to cellular methylglyoxal detoxification by catalyzing the NADPH-dependent conversion of methylglyoxal to acetol (PubMed:16077126). It also exhibits activity with glyoxal and probably plays a significant role in detoxification of glyoxal in vivo (PubMed:23990306). Can also use aromatic aldehydes such as 4-nitrobenzaldehyde, 3-nitrobenzaldehyde and benzaldehyde, and phenylglyoxal (PubMed:16077126). {ECO:0000269|PubMed:16077126, ECO:0000269|PubMed:23990306}. YeaE has been shown to have methylglyoxal reductase activity . The subunit structure of YeaE has not been determined, but its amino acid sequence similarity to the aldo-keto reductases DkgA (YqhE) and DkgB (YafB) suggests that it may be monomeric . Growth of a yeaE gloA double mutant is inhibited by 0.3 mM methylglyoxal . A yeaE mutant is more sensitive to glyoxal than wild type in plate assays, although the IC50 in a liquid assay is quite similar to that of wild type . Expression of yeaE is not increased in response to methylglyoxal or glyoxal . Review:

## Biological Role

Catalyzes RXN0-4281 (reaction.ecocyc.RXN0-4281).

## Annotation

FUNCTION: Aldo-keto reductase that contributes to cellular methylglyoxal detoxification by catalyzing the NADPH-dependent conversion of methylglyoxal to acetol (PubMed:16077126). It also exhibits activity with glyoxal and probably plays a significant role in detoxification of glyoxal in vivo (PubMed:23990306). Can also use aromatic aldehydes such as 4-nitrobenzaldehyde, 3-nitrobenzaldehyde and benzaldehyde, and phenylglyoxal (PubMed:16077126). {ECO:0000269|PubMed:16077126, ECO:0000269|PubMed:23990306}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4281|reaction.ecocyc.RXN0-4281]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1781|gene.b1781]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76234`
- `KEGG:ecj:JW1770;eco:b1781;ecoc:C3026_10160;`
- `GeneID:946302;`
- `GO:GO:0008106; GO:0016491; GO:0051596`
- `EC:1.1.1.-; 1.1.1.2`

## Notes

Methylglyoxal reductase YeaE (EC 1.1.1.-) (Aldo-keto reductase YeaE) (EC 1.1.1.2)

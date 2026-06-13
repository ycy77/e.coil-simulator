---
entity_id: "protein.P64638"
entity_type: "protein"
name: "feoC"
source_database: "UniProt"
source_id: "P64638"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "feoC yhgG b3410 JW3373"
---

# feoC

`protein.P64638`

## Static

- Type: `protein`
- Source: `UniProt:P64638`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: May function as a transcriptional regulator that controls feoABC expression. {ECO:0000255|HAMAP-Rule:MF_01586, ECO:0000269|PubMed:16718600}. FeoC is part of a conserved ferrous iron transport system. Early studies in Escherichia coli K-12 strains characterized feo mutants which were defective in the import of ferrous iron . The feo operon consists of three co-regulated genes feoABC . FeoC may function as an [Fe-S] dependent transcriptional regulator of feo expression; the protein contains a predicted [Fe-S] cluster binding site and a LysR-like winged helix motif at its N-terminus . FeoC is required for full function of FeoB (Taudte, N., Diplomarbeit, cited in ). Anaerobically reconstituted FeoC contains a redox-active, ferredoxin-like [4Fe-4S]2+/+ cluster which is rapidly oxygen sensitive, degrading to a [2Fe-2S] cluster upon exposure to air . Cluster binding to FeoC leads to slight changes in protein conformation (although the protein remains monomeric) and FeoC may function as an oxygen-sensitive iron sensor . feo is a member of the Fur regulon; expression is repressed by Fur-Fe2+; feo expression is activated by FNR under anaerobic conditions...

## Annotation

FUNCTION: May function as a transcriptional regulator that controls feoABC expression. {ECO:0000255|HAMAP-Rule:MF_01586, ECO:0000269|PubMed:16718600}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3410|gene.b3410]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P64638`
- `KEGG:ecj:JW3373;eco:b3410;ecoc:C3026_18500;`
- `GeneID:86948257;947918;`
- `GO:GO:0003677; GO:0005506; GO:0033212; GO:0051539`

## Notes

Probable [Fe-S]-dependent transcriptional repressor FeoC (Fe(2+) iron transport protein C)

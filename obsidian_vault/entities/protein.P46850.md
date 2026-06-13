---
entity_id: "protein.P46850"
entity_type: "protein"
name: "rtcB"
source_database: "UniProt"
source_id: "P46850"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rtcB yhgL b3421 JW3384"
---

# rtcB

`protein.P46850`

## Static

- Type: `protein`
- Source: `UniProt:P46850`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: GTP-dependent RNA ligase that is involved in RNA repair (PubMed:21224389, PubMed:21757685, PubMed:22045815, PubMed:22474365, PubMed:22730297, PubMed:26858100). Joins RNA with 2',3'-cyclic-phosphate or 3'-phosphate ends to RNA with 5'-hydroxy ends (PubMed:21224389, PubMed:21757685, PubMed:22045815, PubMed:22474365, PubMed:22730297, PubMed:26858100). Also acts as a DNA ligase in case of DNA damage by splicing 'dirty' DNA breaks, characterized by 3'-phosphate (or cyclic-phosphate) and 5'-hydroxy ends that cannot be sealed by classical DNA ligases (PubMed:24218597). Repairs tRNA cleaved by colicins D or E5, does not repair damaged 16S rRNA (By similarity). {ECO:0000250|UniProtKB:P0DX92, ECO:0000269|PubMed:21224389, ECO:0000269|PubMed:21757685, ECO:0000269|PubMed:22045815, ECO:0000269|PubMed:22474365, ECO:0000269|PubMed:22730297, ECO:0000269|PubMed:24218597, ECO:0000269|PubMed:26858100}.; FUNCTION: Able to catalyze tRNA splicing in vivo in yeast, but bacteria are not known to splice tRNA. {ECO:0000269|PubMed:21757685}. RtcB is a GTP-dependent 3'-5' RNA ligase with the ability to join RNA 2',3'-cyclic-PO4 or 3'-PO4 ends to RNA 5'-OH ends . RtcB can perform RNA repair and tRNA splicing functions when expressed in yeast host cells...

## Biological Role

Catalyzes RXN-17905 (reaction.ecocyc.RXN-17905), RXN0-6566 (reaction.ecocyc.RXN0-6566). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

FUNCTION: GTP-dependent RNA ligase that is involved in RNA repair (PubMed:21224389, PubMed:21757685, PubMed:22045815, PubMed:22474365, PubMed:22730297, PubMed:26858100). Joins RNA with 2',3'-cyclic-phosphate or 3'-phosphate ends to RNA with 5'-hydroxy ends (PubMed:21224389, PubMed:21757685, PubMed:22045815, PubMed:22474365, PubMed:22730297, PubMed:26858100). Also acts as a DNA ligase in case of DNA damage by splicing 'dirty' DNA breaks, characterized by 3'-phosphate (or cyclic-phosphate) and 5'-hydroxy ends that cannot be sealed by classical DNA ligases (PubMed:24218597). Repairs tRNA cleaved by colicins D or E5, does not repair damaged 16S rRNA (By similarity). {ECO:0000250|UniProtKB:P0DX92, ECO:0000269|PubMed:21224389, ECO:0000269|PubMed:21757685, ECO:0000269|PubMed:22045815, ECO:0000269|PubMed:22474365, ECO:0000269|PubMed:22730297, ECO:0000269|PubMed:24218597, ECO:0000269|PubMed:26858100}.; FUNCTION: Able to catalyze tRNA splicing in vivo in yeast, but bacteria are not known to splice tRNA. {ECO:0000269|PubMed:21757685}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-17905|reaction.ecocyc.RXN-17905]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6566|reaction.ecocyc.RXN0-6566]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3421|gene.b3421]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46850`
- `KEGG:ecj:JW3384;eco:b3421;ecoc:C3026_18550;`
- `GeneID:947929;`
- `GO:GO:0003909; GO:0005525; GO:0006281; GO:0006396; GO:0006974; GO:0030145; GO:0042245; GO:0170057`
- `EC:6.5.1.8`

## Notes

RNA-splicing ligase RtcB (EC 6.5.1.8) (3'-phosphate/5'-hydroxy nucleic acid ligase)

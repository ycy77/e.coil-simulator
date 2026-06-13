---
entity_id: "protein.P37749"
entity_type: "protein"
name: "wbbI"
source_database: "UniProt"
source_id: "P37749"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wbbI yefG b2034 JW2019"
---

# wbbI

`protein.P37749`

## Static

- Type: `protein`
- Source: `UniProt:P37749`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in the transfer of galactofuranose (Galf) onto an alpha-D-gluco-configured acceptor substrate to form a beta-1,6-linkage. It uses n-octyl alpha-D-glucopyranoside as an acceptor substrate for the addition of galactofuranose from the donor substrate UDP-galactofuranose. It is not able to use beta-D-glucopyranoside isomers. {ECO:0000269|PubMed:17047874}. WbbI is a β-1,6-galactofuranosyltransferase that uses UDP-galactofuranose as the donor and has a modest preference for pyranoside acceptor substrates of the α-D-gluco configuration . When the rfb-50 mutation, an IS5 insertion in the gene encoding rhamnosyl transferase, wbbL, is complemented with a wild type wbbL gene, E. coli K-12 produces the O16 variant of O antigen, with a β-D-galactofuranosyl moiety in the repeating unit . For information on bacterial polysaccharide gene nomenclature see .

## Biological Role

Catalyzes RXN0-5210 (reaction.ecocyc.RXN0-5210).

## Enriched Pathways

- `eco00542` O-Antigen repeat unit biosynthesis (KEGG)

## Annotation

FUNCTION: Involved in the transfer of galactofuranose (Galf) onto an alpha-D-gluco-configured acceptor substrate to form a beta-1,6-linkage. It uses n-octyl alpha-D-glucopyranoside as an acceptor substrate for the addition of galactofuranose from the donor substrate UDP-galactofuranose. It is not able to use beta-D-glucopyranoside isomers. {ECO:0000269|PubMed:17047874}.

## Pathways

- `eco00542` O-Antigen repeat unit biosynthesis (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5210|reaction.ecocyc.RXN0-5210]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2034|gene.b2034]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37749`
- `KEGG:ecj:JW2019;eco:b2034;ecoc:C3026_11460;`
- `GeneID:947041;`
- `GO:GO:0005737; GO:0008921; GO:0009103`
- `EC:2.4.1.-`

## Notes

Beta-1,6-galactofuranosyltransferase WbbI (EC 2.4.1.-) (D-Galf:alpha-D-Glc beta-1,6-galactofuranosyltransferase) (GalF transferase)

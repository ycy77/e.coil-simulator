---
entity_id: "protein.P15043"
entity_type: "protein"
name: "recQ"
source_database: "UniProt"
source_id: "P15043"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "recQ b3822 JW5855"
---

# recQ

`protein.P15043`

## Static

- Type: `protein`
- Source: `UniProt:P15043`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: An ATP-dependent DNA helicase which unwinds DNA in a 3'-5' direction (PubMed:12771204, PubMed:16084389, PubMed:2164680, PubMed:9553043). ATPase activity is stimulated by single-stranded (ss)DNA but only very poorly by double-stranded (ds)DNA (PubMed:2164680). Binds to and unwinds a wide variety of substrates including 3- and 4-way junctions (including Holliday junctions, HJ), flayed duplexes, 5'- and 3'-overhangs and blunt end duplexes (PubMed:19151156, PubMed:9553043, PubMed:22722926). HJ DNA unwinding is stimulated by single-stranded binding protein (SSB) (PubMed:22722926). Unwinds G-quadruplex DNA (PubMed:11292849, PubMed:23657261). Unlike yeast SGS1 or human BLM, is equally active on dsDNA versus G-quadruplex substrates (PubMed:11292849). Can act as an initiator during homologous recombination; unwinds a linear dsDNA substrate which can be used by RecA to initiate homologous DNA pairing as well as dissociation (PubMed:9553043). The identity of a few residues in the C-terminal HRDC domain influences the type of DNA substrate bound (PubMed:16084389). Involved in the RecF recombination pathway (PubMed:2993821). {ECO:0000269|PubMed:11292849, ECO:0000269|PubMed:12771204, ECO:0000269|PubMed:16084389, ECO:0000269|PubMed:19151156, ECO:0000269|PubMed:2164680, ECO:0000269|PubMed:22722926, ECO:0000269|PubMed:23657261, ECO:0000269|PubMed:2993821, ECO:0000269|PubMed:9553043}...

## Biological Role

Catalyzes RXN-11135 (reaction.ecocyc.RXN-11135). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

FUNCTION: An ATP-dependent DNA helicase which unwinds DNA in a 3'-5' direction (PubMed:12771204, PubMed:16084389, PubMed:2164680, PubMed:9553043). ATPase activity is stimulated by single-stranded (ss)DNA but only very poorly by double-stranded (ds)DNA (PubMed:2164680). Binds to and unwinds a wide variety of substrates including 3- and 4-way junctions (including Holliday junctions, HJ), flayed duplexes, 5'- and 3'-overhangs and blunt end duplexes (PubMed:19151156, PubMed:9553043, PubMed:22722926). HJ DNA unwinding is stimulated by single-stranded binding protein (SSB) (PubMed:22722926). Unwinds G-quadruplex DNA (PubMed:11292849, PubMed:23657261). Unlike yeast SGS1 or human BLM, is equally active on dsDNA versus G-quadruplex substrates (PubMed:11292849). Can act as an initiator during homologous recombination; unwinds a linear dsDNA substrate which can be used by RecA to initiate homologous DNA pairing as well as dissociation (PubMed:9553043). The identity of a few residues in the C-terminal HRDC domain influences the type of DNA substrate bound (PubMed:16084389). Involved in the RecF recombination pathway (PubMed:2993821). {ECO:0000269|PubMed:11292849, ECO:0000269|PubMed:12771204, ECO:0000269|PubMed:16084389, ECO:0000269|PubMed:19151156, ECO:0000269|PubMed:2164680, ECO:0000269|PubMed:22722926, ECO:0000269|PubMed:23657261, ECO:0000269|PubMed:2993821, ECO:0000269|PubMed:9553043}.

## Pathways

- `eco03018` RNA degradation (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11135|reaction.ecocyc.RXN-11135]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3822|gene.b3822]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15043`
- `KEGG:ecj:JW5855;eco:b3822;ecoc:C3026_20685;`
- `GeneID:93778115;948318;`
- `GO:GO:0003677; GO:0003678; GO:0005524; GO:0005694; GO:0005737; GO:0006260; GO:0006281; GO:0006310; GO:0006974; GO:0008094; GO:0008270; GO:0009378; GO:0009432; GO:0016887; GO:0017116; GO:0017117; GO:0030894; GO:0043138; GO:0043590; GO:0046914; GO:0140640`
- `EC:5.6.2.4`

## Notes

ATP-dependent DNA helicase RecQ (EC 5.6.2.4) (DNA 3'-5' helicase RecQ)

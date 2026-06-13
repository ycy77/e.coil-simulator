---
entity_id: "protein.P46849"
entity_type: "protein"
name: "rtcA"
source_database: "UniProt"
source_id: "P46849"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rtcA yhgJ yhgK b4475 JW5688"
---

# rtcA

`protein.P46849`

## Static

- Type: `protein`
- Source: `UniProt:P46849`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the conversion of 3'-phosphate to a 2',3'-cyclic phosphodiester at the end of RNA. The mechanism of action of the enzyme occurs in 3 steps: (A) adenylation of the enzyme by ATP; (B) transfer of adenylate to an RNA-N3'P to produce RNA-N3'PP5'A; (C) and attack of the adjacent 2'-hydroxyl on the 3'-phosphorus in the diester linkage to produce the cyclic end product. Likely functions in some aspects of cellular RNA processing. {ECO:0000269|PubMed:9738023}. RNA 3'-terminal phosphate cyclase (RtcA) converts the 3'-terminal phosphate of various RNA substrates into the 2',3'-cyclic phosphodiester in an ATP-dependent reaction . The physiological role of the enzyme is unknown. Recently, it was shown that the enzyme also has a novel polynucleotide 5' adenylylation activity , which raises additional possibilities for its physiological function. RtcA can also act on RNA substrates with 2'-terminal phosphate ends, albeit at a dramatically lower rate. RtcA is proposed to be part of an RNA repair pathway, converting RNA 2'-phosphates, which are not substrates of RtcB, to 2',3'-cyclic phosphates that can be sealed . The reaction mechanism of RtcA has been studied . Cyclization occurs by a three-step mechanism involving formation of a covalent protein-nucleoside monophosphate intermediate . In E. coli, the site of adenylation was shown to be the His308 residue...

## Biological Role

Catalyzes RNA-3-PHOSPHATE-CYCLASE-RXN (reaction.ecocyc.RNA-3-PHOSPHATE-CYCLASE-RXN), RXN-17916 (reaction.ecocyc.RXN-17916), RXN0-6556 (reaction.ecocyc.RXN0-6556). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

FUNCTION: Catalyzes the conversion of 3'-phosphate to a 2',3'-cyclic phosphodiester at the end of RNA. The mechanism of action of the enzyme occurs in 3 steps: (A) adenylation of the enzyme by ATP; (B) transfer of adenylate to an RNA-N3'P to produce RNA-N3'PP5'A; (C) and attack of the adjacent 2'-hydroxyl on the 3'-phosphorus in the diester linkage to produce the cyclic end product. Likely functions in some aspects of cellular RNA processing. {ECO:0000269|PubMed:9738023}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RNA-3-PHOSPHATE-CYCLASE-RXN|reaction.ecocyc.RNA-3-PHOSPHATE-CYCLASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17916|reaction.ecocyc.RXN-17916]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6556|reaction.ecocyc.RXN0-6556]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4475|gene.b4475]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46849`
- `KEGG:ecj:JW5688;eco:b4475;ecoc:C3026_18545;`
- `GeneID:2847707;`
- `GO:GO:0003963; GO:0005524; GO:0005737; GO:0006396`
- `EC:6.5.1.4`

## Notes

RNA 3'-terminal phosphate cyclase (RNA cyclase) (RNA-3'-phosphate cyclase) (EC 6.5.1.4)

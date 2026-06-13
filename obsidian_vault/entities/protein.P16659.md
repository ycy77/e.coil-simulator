---
entity_id: "protein.P16659"
entity_type: "protein"
name: "proS"
source_database: "UniProt"
source_id: "P16659"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "proS drpA b0194 JW0190"
---

# proS

`protein.P16659`

## Static

- Type: `protein`
- Source: `UniProt:P16659`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the attachment of proline to tRNA(Pro) in a two-step reaction: proline is first activated by ATP to form Pro-AMP and then transferred to the acceptor end of tRNA(Pro). As ProRS can inadvertently accommodate and process non-cognate amino acids such as alanine and cysteine, to avoid such errors it has two additional distinct editing activities against alanine. One activity is designated as 'pretransfer' editing and involves the tRNA(Pro)-independent hydrolysis of activated Ala-AMP. The other activity is designated 'posttransfer' editing and involves deacylation of mischarged Ala-tRNA(Pro). Misacylated Cys-tRNA(Pro) is not edited by ProRS, but instead may be edited in trans by YbaK. Proline-tRNA ligase (ProRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. ProRS belongs to the Class IIA aminoacyl-tRNA synthetases . ProRS of E. coli B is a dimer in solution . Specificity determinants within tRNAPro that are important for recognition by ProRS have been identified . The R144 residue within the active site makes a key contact with G72 in the acceptor stem of tRNAPro . Specificity determinants and residues within ProRS that are important for catalytic activity have been investigated...

## Biological Role

Catalyzes L-proline:tRNA(Pro) ligase (AMP-forming) (reaction.R03661). Component of proline—tRNA ligase (complex.ecocyc.PROS-CPLX).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the attachment of proline to tRNA(Pro) in a two-step reaction: proline is first activated by ATP to form Pro-AMP and then transferred to the acceptor end of tRNA(Pro). As ProRS can inadvertently accommodate and process non-cognate amino acids such as alanine and cysteine, to avoid such errors it has two additional distinct editing activities against alanine. One activity is designated as 'pretransfer' editing and involves the tRNA(Pro)-independent hydrolysis of activated Ala-AMP. The other activity is designated 'posttransfer' editing and involves deacylation of mischarged Ala-tRNA(Pro). Misacylated Cys-tRNA(Pro) is not edited by ProRS, but instead may be edited in trans by YbaK.

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03661|reaction.R03661]] `KEGG` `database` - via EC:6.1.1.15
- `is_component_of` --> [[complex.ecocyc.PROS-CPLX|complex.ecocyc.PROS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0194|gene.b0194]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16659`
- `KEGG:ecj:JW0190;eco:b0194;ecoc:C3026_00900;`
- `GeneID:949116;`
- `GO:GO:0004827; GO:0005524; GO:0005829; GO:0006433; GO:0043906; GO:0106074`
- `EC:6.1.1.15`

## Notes

Proline--tRNA ligase (EC 6.1.1.15) (Global RNA synthesis factor) (Prolyl-tRNA synthetase) (ProRS)

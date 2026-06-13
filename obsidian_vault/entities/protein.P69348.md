---
entity_id: "protein.P69348"
entity_type: "protein"
name: "yoeB"
source_database: "UniProt"
source_id: "P69348"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yoeB b4539 JW5331"
---

# yoeB

`protein.P69348`

## Static

- Type: `protein`
- Source: `UniProt:P69348`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. Its mode of function is controversial; it has been proposed to be an mRNA interferase but also an inhibitor of translation initiation. When overproduced in wild-type cells, inhibits bacterial growth and translation by cleavage of mRNA molecules while it has a weak effect on colony forming ability. Overproduction of Lon protease specifically activates YoeB-dependent mRNA cleavage, leading to lethality. YefM binds to the promoter region of the yefM-yeoB operon to repress transcription, YeoB acts as a corepressor.; FUNCTION: Shown in vitro to be an mRNA interferase that requires translation for substrate cleavage; if the mRNA is mutated so as to not be translatable it is no longer cleaved. Cleavage only occurs within translated regions. Has RNase activity and preferentially cleaves at the 3'-end of purine ribonucleotides. {ECO:0000269|PubMed:16109374}.; FUNCTION: Also shown in vitro to be a translation initiation blocker. Binds to the 70S ribosome and 50S ribosomal subunit; binding is inhibited by hygromycin A and tetracycline, both of which bind to the 30S subunit in the A site. Thus YoeB is located at the interface between 50S and 30S ribosomes and interacts with the A site where it cleaves mRNA, blocking translation initiation.

## Biological Role

Component of YefM-YoeB antitoxin/toxin complex / DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-3781), ribosome-dependent mRNA interferase toxin YoeB (complex.ecocyc.CPLX0-8311).

## Annotation

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. Its mode of function is controversial; it has been proposed to be an mRNA interferase but also an inhibitor of translation initiation. When overproduced in wild-type cells, inhibits bacterial growth and translation by cleavage of mRNA molecules while it has a weak effect on colony forming ability. Overproduction of Lon protease specifically activates YoeB-dependent mRNA cleavage, leading to lethality. YefM binds to the promoter region of the yefM-yeoB operon to repress transcription, YeoB acts as a corepressor.; FUNCTION: Shown in vitro to be an mRNA interferase that requires translation for substrate cleavage; if the mRNA is mutated so as to not be translatable it is no longer cleaved. Cleavage only occurs within translated regions. Has RNase activity and preferentially cleaves at the 3'-end of purine ribonucleotides. {ECO:0000269|PubMed:16109374}.; FUNCTION: Also shown in vitro to be a translation initiation blocker. Binds to the 70S ribosome and 50S ribosomal subunit; binding is inhibited by hygromycin A and tetracycline, both of which bind to the 30S subunit in the A site. Thus YoeB is located at the interface between 50S and 30S ribosomes and interacts with the A site where it cleaves mRNA, blocking translation initiation.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3781|complex.ecocyc.CPLX0-3781]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8311|complex.ecocyc.CPLX0-8311]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4539|gene.b4539]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69348`
- `KEGG:ecj:JW5331;eco:b4539;ecoc:C3026_11375;`
- `GeneID:1450274;86946970;93775157;`
- `GO:GO:0003723; GO:0004519; GO:0004521; GO:0006355; GO:0006402; GO:0009408; GO:0016892; GO:0040008; GO:0042803; GO:0043024; GO:0044010; GO:0045947; GO:0098795; GO:0110001`
- `EC:3.1.-.-`

## Notes

Toxin YoeB (EC 3.1.-.-) (Putative endoribonuclease YoeB) (Putative mRNA interferase Yoeb)

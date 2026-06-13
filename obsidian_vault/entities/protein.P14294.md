---
entity_id: "protein.P14294"
entity_type: "protein"
name: "topB"
source_database: "UniProt"
source_id: "P14294"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "topB b1763 JW1752"
---

# topB

`protein.P14294`

## Static

- Type: `protein`
- Source: `UniProt:P14294`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Releases the supercoiling and torsional tension of DNA, which is introduced during the DNA replication and transcription, by transiently cleaving and rejoining one strand of the DNA duplex. Introduces a single-strand break via transesterification at a target site in duplex DNA. The scissile phosphodiester is attacked by the catalytic tyrosine of the enzyme, resulting in the formation of a DNA-(5'-phosphotyrosyl)-enzyme intermediate and the expulsion of a 3'-OH DNA strand. The free DNA strand then undergoes passage around the unbroken strand, thus removing DNA supercoils. Finally, in the religation step, the DNA 3'-OH attacks the covalent intermediate to expel the active-site tyrosine and restore the DNA phosphodiester backbone. TOP3 is a potent decatenase. {ECO:0000255|HAMAP-Rule:MF_00953, ECO:0000269|PubMed:2553698, ECO:0000269|PubMed:6326814}. E. coli possess multiple DNA topoisomerases which coordinate, as well as compete, in order to maintain chromosomes in the appropriate topological state commensurate with their need for replication and transcription. They comprise the type IA enzymes DNA topoisomerase I and DNA topoisomerase III, which are encoded by the EG11013 and EG11014 genes, respectively, and the type II enzymes CPLX0-2424 and CPLX0-2425...

## Biological Role

Catalyzes 5.99.1.2-RXN (reaction.ecocyc.5.99.1.2-RXN). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Releases the supercoiling and torsional tension of DNA, which is introduced during the DNA replication and transcription, by transiently cleaving and rejoining one strand of the DNA duplex. Introduces a single-strand break via transesterification at a target site in duplex DNA. The scissile phosphodiester is attacked by the catalytic tyrosine of the enzyme, resulting in the formation of a DNA-(5'-phosphotyrosyl)-enzyme intermediate and the expulsion of a 3'-OH DNA strand. The free DNA strand then undergoes passage around the unbroken strand, thus removing DNA supercoils. Finally, in the religation step, the DNA 3'-OH attacks the covalent intermediate to expel the active-site tyrosine and restore the DNA phosphodiester backbone. TOP3 is a potent decatenase. {ECO:0000255|HAMAP-Rule:MF_00953, ECO:0000269|PubMed:2553698, ECO:0000269|PubMed:6326814}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.5.99.1.2-RXN|reaction.ecocyc.5.99.1.2-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1763|gene.b1763]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P14294`
- `KEGG:ecj:JW1752;eco:b1763;ecoc:C3026_10060;`
- `GeneID:946141;`
- `GO:GO:0000287; GO:0003917; GO:0006261; GO:0006265; GO:0006281; GO:0006310; GO:0043597; GO:0051304; GO:0098847`
- `EC:5.6.2.1`

## Notes

DNA topoisomerase 3 (EC 5.6.2.1) (DNA topoisomerase III)

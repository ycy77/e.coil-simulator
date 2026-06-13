---
entity_id: "protein.P06612"
entity_type: "protein"
name: "topA"
source_database: "UniProt"
source_id: "P06612"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "topA supX b1274 JW1266"
---

# topA

`protein.P06612`

## Static

- Type: `protein`
- Source: `UniProt:P06612`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Releases the supercoiling and torsional tension of DNA, which is introduced during the DNA replication and transcription, by transiently cleaving and rejoining one strand of the DNA duplex. Introduces a single-strand break via transesterification at a target site in duplex DNA. The scissile phosphodiester is attacked by the catalytic tyrosine of the enzyme, resulting in the formation of a DNA-(5'-phosphotyrosyl)-enzyme intermediate and the expulsion of a 3'-OH DNA strand. The free DNA strand then undergoes passage around the unbroken strand, thus removing DNA supercoils. Finally, in the religation step, the DNA 3'-OH attacks the covalent intermediate to expel the active-site tyrosine and restore the DNA phosphodiester backbone. {ECO:0000255|HAMAP-Rule:MF_00952, ECO:0000269|PubMed:10681504, ECO:0000269|PubMed:21482796, ECO:0000269|PubMed:9497321}. E. coli possess multiple DNA topoisomerases which coordinate, as well as compete, in order to maintain chromosomes in the appropriate topological state commensurate with their need for replication and transcription. They comprise the type IA enzymes DNA topoisomerase I (Topo I) and DNA topoisomerase III, which are encoded by the EG11013 and EG11014 genes, respectively, and the type II enzymes CPLX0-2424 and CPLX0-2425...

## Biological Role

Catalyzes 5.99.1.2-RXN (reaction.ecocyc.5.99.1.2-RXN).

## Annotation

FUNCTION: Releases the supercoiling and torsional tension of DNA, which is introduced during the DNA replication and transcription, by transiently cleaving and rejoining one strand of the DNA duplex. Introduces a single-strand break via transesterification at a target site in duplex DNA. The scissile phosphodiester is attacked by the catalytic tyrosine of the enzyme, resulting in the formation of a DNA-(5'-phosphotyrosyl)-enzyme intermediate and the expulsion of a 3'-OH DNA strand. The free DNA strand then undergoes passage around the unbroken strand, thus removing DNA supercoils. Finally, in the religation step, the DNA 3'-OH attacks the covalent intermediate to expel the active-site tyrosine and restore the DNA phosphodiester backbone. {ECO:0000255|HAMAP-Rule:MF_00952, ECO:0000269|PubMed:10681504, ECO:0000269|PubMed:21482796, ECO:0000269|PubMed:9497321}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.5.99.1.2-RXN|reaction.ecocyc.5.99.1.2-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1274|gene.b1274]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06612`
- `KEGG:ecj:JW1266;eco:b1274;ecoc:C3026_07470;`
- `GeneID:945862;`
- `GO:GO:0003677; GO:0003916; GO:0003917; GO:0005694; GO:0005829; GO:0006265; GO:0007059; GO:0008270; GO:0140226`
- `EC:5.6.2.1`

## Notes

DNA topoisomerase 1 (EC 5.6.2.1) (DNA topoisomerase I) (Omega-protein) (Relaxing enzyme) (Swivelase) (Untwisting enzyme)

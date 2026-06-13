---
entity_id: "protein.P0A7Y4"
entity_type: "protein"
name: "rnhA"
source_database: "UniProt"
source_id: "P0A7Y4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rnhA dasF herA rnh sdrA b0214 JW0204"
---

# rnhA

`protein.P0A7Y4`

## Static

- Type: `protein`
- Source: `UniProt:P0A7Y4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Endonuclease that specifically degrades the RNA of RNA-DNA hybrids. RNase H participates in DNA replication; it helps to specify the origin of genomic replication by suppressing initiation at origins other than the oriC locus; along with the 5'-3' exonuclease of pol1, it removes RNA primers from the Okazaki fragments of lagging strand synthesis; and it defines the origin of replication for ColE1-type plasmids by specific cleavage of an RNA preprimer. Involved in production of retron derived msDNA (a branched RNA linked by a 2',5'-phosphodiester bond to a single-stranded DNA). Strain K12 / MG1655 does not have retrons, however they can be expressed in this strain which requires this enzyme (tested with retron Ec86) (PubMed:7568472). {ECO:0000269|PubMed:7568472}. RNase H carries out the endonucleolytic cleavage of RNA in RNA-DNA hybrids, cleaving near the 3' terminus of the RNA and then digesting the remainder of the RNA . Although its physiological functions are not fully understood, it is involved in DNA replication and repair. Note that gene rnhA is also referred to by its synonym rnh and its product RNase HI (type I RNase H) often is referred to simply as RNase H. A second RNase with a similar structure and catalytic mechanism is encoded by gene EG10861 which produces RNase HII (type 2 RNase H)...

## Biological Role

Catalyzes 3.1.26.4-RXN (reaction.ecocyc.3.1.26.4-RXN). Bound by Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)

## Annotation

FUNCTION: Endonuclease that specifically degrades the RNA of RNA-DNA hybrids. RNase H participates in DNA replication; it helps to specify the origin of genomic replication by suppressing initiation at origins other than the oriC locus; along with the 5'-3' exonuclease of pol1, it removes RNA primers from the Okazaki fragments of lagging strand synthesis; and it defines the origin of replication for ColE1-type plasmids by specific cleavage of an RNA preprimer. Involved in production of retron derived msDNA (a branched RNA linked by a 2',5'-phosphodiester bond to a single-stranded DNA). Strain K12 / MG1655 does not have retrons, however they can be expressed in this strain which requires this enzyme (tested with retron Ec86) (PubMed:7568472). {ECO:0000269|PubMed:7568472}.

## Pathways

- `eco03030` DNA replication (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.1.26.4-RXN|reaction.ecocyc.3.1.26.4-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0214|gene.b0214]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7Y4`
- `KEGG:ecj:JW0204;eco:b0214;ecoc:C3026_01000;`
- `GeneID:86862725;93777209;946955;`
- `GO:GO:0000287; GO:0003676; GO:0004519; GO:0004523; GO:0005737; GO:0043137`
- `EC:3.1.26.4`

## Notes

Ribonuclease HI (RNase HI) (EC 3.1.26.4) (Ribonuclease H) (RNase H)

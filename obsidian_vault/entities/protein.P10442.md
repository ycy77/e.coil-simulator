---
entity_id: "protein.P10442"
entity_type: "protein"
name: "rnhB"
source_database: "UniProt"
source_id: "P10442"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rnhB b0183 JW0178"
---

# rnhB

`protein.P10442`

## Static

- Type: `protein`
- Source: `UniProt:P10442`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Endonuclease that specifically degrades the RNA of RNA-DNA hybrids. {ECO:0000250, ECO:0000269|PubMed:2172991}. RNase HII (type 2 RNase H) cleaves RNA in RNA-DNA hybrids by nicking DNA 5' to the incorporated ribonucleotide . RNase HII is required for removal of misincorporated ribose from DNA . A second RNase with a similar structure and catalytic mechanism is encoded by gene EG10860 which produces RNase HI (type 1 RNase H). RNase HII has also been reported to have junction RNase activity, cleaving RNA-DNADNA and RNA-DNARNA duplexes at the 5' side of the last ribonulceotide at the RNA-DNA junction . In vivo studies show that RNase HII targets isolated mispaired ribonucleoside monophosphates within chromosomal DNA in competition with the mismatch repair system, whereas RNase HI targets a mismatch within an RNA-DNA heteroduplex. RNase HII efficiently targets a single mispaired ribonucleoside monophosphate, whereas RNase HI targets a tract of five ribonucleoside monophosphates with a mispair . Genetic and biochemical evidence suggest that RNase HII initiates the ribonucleotide excision repair process, followed by DNA polymerase I . In an E. coli ΔrnhB strain expressing umuC_Y11A (an active site steric gate mutant of pol V), repair of a significant number of misincorporated ribonucleotides in DNA is dependent on RNase HI...

## Biological Role

Catalyzes 3.1.26.4-RXN (reaction.ecocyc.3.1.26.4-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)

## Annotation

FUNCTION: Endonuclease that specifically degrades the RNA of RNA-DNA hybrids. {ECO:0000250, ECO:0000269|PubMed:2172991}.

## Pathways

- `eco03030` DNA replication (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.1.26.4-RXN|reaction.ecocyc.3.1.26.4-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0183|gene.b0183]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10442`
- `KEGG:ecj:JW0178;eco:b0183;ecoc:C3026_00840;`
- `GeneID:93777242;944852;`
- `GO:GO:0003723; GO:0004523; GO:0005737; GO:0006298; GO:0030145; GO:0032299; GO:0043137; GO:1990516`
- `EC:3.1.26.4`

## Notes

Ribonuclease HII (RNase HII) (EC 3.1.26.4)

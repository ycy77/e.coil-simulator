---
entity_id: "protein.P0AAR3"
entity_type: "protein"
name: "ybaK"
source_database: "UniProt"
source_id: "P0AAR3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybaK b0481 JW0470"
---

# ybaK

`protein.P0AAR3`

## Static

- Type: `protein`
- Source: `UniProt:P0AAR3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Functions in trans to edit the amino acid from incorrectly charged Cys-tRNA(Pro) via a Cys-tRNA(Pro) deacylase activity. May compensate for the lack of Cys-tRNA(Pro) editing by ProRS. Is also able to deacylate Cys-tRNA(Cys), and displays weak deacylase activity in vitro against Gly-tRNA(Gly), as well as, at higher concentrations, some other correctly charged tRNAs. Unlike some of its orthologs it is not able to remove the amino acid moiety from incorrectly charged Ala-tRNA(Pro). {ECO:0000269|PubMed:15886196, ECO:0000269|PubMed:23185990}. YbaK hydrolyzes both incorrectly charged Cys-tRNAPro and correctly charged Cys-tRNACys in vitro . YbaK does not appear to recognize specific tRNAs . However, YbaK interacts with PROS-CPLX ProRS in vivo, and this interaction enhances YbaK's Cys-tRNAPro deacylation activity. The interaction with ProRS appears to provide specificity for hydrolysis of mischarged Cys-tRNAPro . YbaK has similarity to the editing active site (INS domain) of ProRS, which is able to edit mischarged Ala-tRNAPro . A computational model of YbaK bound to the substrate analog 5'-CCA-Cys and application of hybrid quantum mechanical/molecular mechanics (QM/MM) methods provided further insight into catalysis. The reaction mechanism is proposed to involve cyclization of the substrate Cys and subsequent cleavage of the Cys-tRNA ester bond...

## Biological Role

Catalyzes RXN-21077 (reaction.ecocyc.RXN-21077).

## Annotation

FUNCTION: Functions in trans to edit the amino acid from incorrectly charged Cys-tRNA(Pro) via a Cys-tRNA(Pro) deacylase activity. May compensate for the lack of Cys-tRNA(Pro) editing by ProRS. Is also able to deacylate Cys-tRNA(Cys), and displays weak deacylase activity in vitro against Gly-tRNA(Gly), as well as, at higher concentrations, some other correctly charged tRNAs. Unlike some of its orthologs it is not able to remove the amino acid moiety from incorrectly charged Ala-tRNA(Pro). {ECO:0000269|PubMed:15886196, ECO:0000269|PubMed:23185990}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-21077|reaction.ecocyc.RXN-21077]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0481|gene.b0481]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAR3`
- `KEGG:ecj:JW0470;eco:b0481;ecoc:C3026_02365;`
- `GeneID:75203147;947083;`
- `GO:GO:0002161; GO:0005829; GO:0006412; GO:0010165; GO:0016829; GO:0043907; GO:0106074`
- `EC:4.2.-.-`

## Notes

Cys-tRNA(Pro)/Cys-tRNA(Cys) deacylase YbaK (EC 4.2.-.-)

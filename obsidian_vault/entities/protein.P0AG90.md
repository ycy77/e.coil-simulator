---
entity_id: "protein.P0AG90"
entity_type: "protein"
name: "secD"
source_database: "UniProt"
source_id: "P0AG90"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "secD b0408 JW0398"
---

# secD

`protein.P0AG90`

## Static

- Type: `protein`
- Source: `UniProt:P0AG90`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Part of the Sec protein translocase complex. Interacts with the SecYEG preprotein conducting channel. SecDF uses the proton motive force (PMF) to complete protein translocation after the ATP-dependent function of SecA. The large periplasmic domain is thought to have a base and head domain joined by a hinge; movement of the hinge may be coupled to both proton transport and protein export, with the head domain capturing substrate, and a conformational change preventing backward movement and driving forward movement. Expression of V.alginolyticus SecD and SecF in E.coli confers Na(+)-dependent protein export, strongly suggesting SecDF functions via cation-coupled protein translocation. {ECO:0000269|PubMed:21562494}. SecD is an inner membrane protein that is part of the heterotrimeric Sec translocon accessory complex. Early studies characterized the secD locus, composed of yajC-secD-secF, and implicated the products of secD and secF in protein export . SecD and SecF are not absolutely essential but are required for efficient protein transport; secDF double null mutants have a severe protein export defect at 37°C which is exacerbated at 23 °C; overexpressing SecD and SecF improves the export of proteins with a defective signal sequence . SecD and SecF are implicated in SecA membrane cycling at SecYEG in vitro (see further )...

## Biological Role

Component of Sec Holo-Translocon (complex.ecocyc.SEC-SECRETION-CPLX), Sec translocon accessory complex (complex.ecocyc.SECD-SECF-YAJC-YIDC-CPLX).

## Enriched Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Part of the Sec protein translocase complex. Interacts with the SecYEG preprotein conducting channel. SecDF uses the proton motive force (PMF) to complete protein translocation after the ATP-dependent function of SecA. The large periplasmic domain is thought to have a base and head domain joined by a hinge; movement of the hinge may be coupled to both proton transport and protein export, with the head domain capturing substrate, and a conformational change preventing backward movement and driving forward movement. Expression of V.alginolyticus SecD and SecF in E.coli confers Na(+)-dependent protein export, strongly suggesting SecDF functions via cation-coupled protein translocation. {ECO:0000269|PubMed:21562494}.

## Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.SEC-SECRETION-CPLX|complex.ecocyc.SEC-SECRETION-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.SECD-SECF-YAJC-YIDC-CPLX|complex.ecocyc.SECD-SECF-YAJC-YIDC-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0408|gene.b0408]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG90`
- `KEGG:ecj:JW0398;eco:b0408;ecoc:C3026_01985;`
- `GeneID:93777052;949133;`
- `GO:GO:0005886; GO:0006605; GO:0015031; GO:0015450; GO:0016020; GO:0031522; GO:0043952; GO:0065002`

## Notes

Protein translocase subunit SecD (Sec translocon accessory complex subunit SecD)

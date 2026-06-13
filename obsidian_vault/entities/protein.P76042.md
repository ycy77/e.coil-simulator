---
entity_id: "protein.P76042"
entity_type: "protein"
name: "ycjN"
source_database: "UniProt"
source_id: "P76042"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}; Periplasmic side {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycjN b1310 JW1303"
---

# ycjN

`protein.P76042`

## Static

- Type: `protein`
- Source: `UniProt:P76042`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}; Periplasmic side {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex YcjNOPV primarily involved in maltose uptake (PubMed:40721696). The transporter may also be involved in the uptake of glucosides (PubMed:40721696). In vitro, it actively transports ethidium bromide (EB) (PubMed:40721696). This subunit is the solute binding protein of the YcjNOPV transporter (Probable). {ECO:0000269|PubMed:40721696, ECO:0000305}. YcjN is the predicted periplasmic binding protein of a putative ATP-binding cassette transporter (YcjNOPV) . YcjN is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). Over-expressed, purified YcjN is a lipoprotein that is predominantly diacylated at Cys-21; structural analysis indicates that the YcjN resembles sugar-binding proteins .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-55-CPLX).

## Annotation

FUNCTION: Part of the ABC transporter complex YcjNOPV primarily involved in maltose uptake (PubMed:40721696). The transporter may also be involved in the uptake of glucosides (PubMed:40721696). In vitro, it actively transports ethidium bromide (EB) (PubMed:40721696). This subunit is the solute binding protein of the YcjNOPV transporter (Probable). {ECO:0000269|PubMed:40721696, ECO:0000305}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-55-CPLX|complex.ecocyc.ABC-55-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1310|gene.b1310]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76042`
- `KEGG:ecj:JW1303;eco:b1310;ecoc:C3026_07680;`
- `GeneID:945696;`
- `GO:GO:0005886; GO:0015574; GO:0016020; GO:0030288; GO:0055052; GO:0055085`

## Notes

Probable maltose-binding protein YcjN

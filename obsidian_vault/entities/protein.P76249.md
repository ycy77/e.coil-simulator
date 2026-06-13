---
entity_id: "protein.P76249"
entity_type: "protein"
name: "leuE"
source_database: "UniProt"
source_id: "P76249"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "leuE yeaS b1798 JW1787"
---

# leuE

`protein.P76249`

## Static

- Type: `protein`
- Source: `UniProt:P76249`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Exporter of leucine. Can also transport its natural analog L-alpha-amino-n-butyric acid and some other structurally unrelated amino acids. Leucine excretion is probably driven by proton motive force. {ECO:0000269|PubMed:16098526}. The leucine exporter LeuE belongs to the RhtB family of transporters. Overexpression of LeuE resulted in resistance of cells to leucine analogues, glycyl-L-leucine, and several other amino acids and their analogues. Expression of leuE was shown to be induced by leucine, L-α-amino-N-butyric acid, and several other amino acids . Leucine accumulation in a leucine-producing, leuE-overexpressing strain dropped upon addition of CCCP, revealing the dependence of transport upon the proton-motive-force . The global regulator Lrp regulates leuE expression . LeuE: "leucine export"

## Biological Role

Catalyzes L-methionine:proton antiport (reaction.ecocyc.RXN0-7050), L-leucine:proton antiport (reaction.ecocyc.TRANS-RXN0-270).

## Annotation

FUNCTION: Exporter of leucine. Can also transport its natural analog L-alpha-amino-n-butyric acid and some other structurally unrelated amino acids. Leucine excretion is probably driven by proton motive force. {ECO:0000269|PubMed:16098526}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7050|reaction.ecocyc.RXN0-7050]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-270|reaction.ecocyc.TRANS-RXN0-270]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1798|gene.b1798]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76249`
- `KEGG:ecj:JW1787;eco:b1798;ecoc:C3026_10250;`
- `GeneID:946157;`
- `GO:GO:0005886; GO:0015190; GO:0015297; GO:0015820`

## Notes

Leucine efflux protein
